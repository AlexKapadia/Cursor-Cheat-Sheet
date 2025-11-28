# Stripe Integration Rules and Guidelines

## Setup and Configuration

### API Keys and Environment Variables

- **Never commit API keys to version control.** Always use environment variables.
- **Use test keys during development.** Stripe provides separate test and live API keys.
- **Store keys securely:**
  - Use `.env` files (and ensure they're in `.gitignore`)
  - Use secret management services in production (AWS Secrets Manager, Azure Key Vault, etc.)
  - Never log or expose keys in error messages or client-side code
- **Use different keys for different environments:**
  - Test mode keys: `sk_test_...` and `pk_test_...`
  - Live mode keys: `sk_live_...` and `pk_live_...`
- **Initialise the Stripe client once and reuse it.** Don't create new instances for each request.
- **Set API version explicitly** to avoid breaking changes when Stripe updates their API:
  ```javascript
  const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY, {
    apiVersion: '2024-11-20.acacia', // Use latest stable version
  });
  ```

### Webhook Configuration

- **Always verify webhook signatures** before processing webhook events.
- **Use webhook signing secrets** from the Stripe Dashboard, not API keys.
- **Store webhook signing secrets as environment variables** separate from API keys.
- **Handle idempotency** - webhooks can be delivered multiple times; use idempotency keys.
- **Respond quickly to webhooks** (within 20 seconds) to avoid retries.
- **Log webhook events** for debugging, but don't log sensitive payment data.

## Payment Processing

### Payment Methods

- **Support multiple payment methods** when possible (cards, bank transfers, digital wallets).
- **Use Payment Intents API** for all card payments (not the deprecated Charges API).
- **Use Setup Intents** for saving payment methods without charging immediately.
- **Handle 3D Secure (3DS) authentication** - some payments require additional authentication.
- **Implement proper payment method validation** on the client side before submission.

### Payment Intent Flow

- **Create Payment Intents on the server side** - never create them client-side with secret keys.
- **Use client secrets** to confirm payments on the client side.
- **Handle payment status properly:**
  - `requires_payment_method` - Payment failed, needs new payment method
  - `requires_confirmation` - Payment needs confirmation
  - `requires_action` - 3DS or other authentication required
  - `processing` - Payment is being processed
  - `requires_capture` - Payment authorised, needs capture
  - `succeeded` - Payment completed
  - `canceled` - Payment cancelled
- **Implement proper error handling** for each status.
- **Use idempotency keys** when creating Payment Intents to prevent duplicate charges.

### Subscription Management

- **Use Subscriptions API** for recurring payments.
- **Handle subscription lifecycle events:**
  - `customer.subscription.created`
  - `customer.subscription.updated`
  - `customer.subscription.deleted`
  - `invoice.payment_succeeded`
  - `invoice.payment_failed`
- **Implement dunning management** for failed subscription payments.
- **Handle prorations correctly** when changing subscription plans.
- **Support subscription upgrades and downgrades** with proper proration logic.
- **Set up trial periods** when applicable.
- **Handle subscription cancellations** - immediate vs. end of period.

### Refunds and Disputes

- **Process refunds through Stripe** - don't manually adjust charges.
- **Handle partial refunds** when needed.
- **Monitor disputes (chargebacks)** and respond within deadlines.
- **Implement dispute webhook handlers** to track and respond to disputes.
- **Keep evidence ready** for dispute responses (receipts, shipping confirmations, etc.).

## Security Best Practices

### PCI Compliance

- **Never store full card numbers** - Stripe handles PCI compliance for you.
- **Never send card data to your server** - use Stripe.js or mobile SDKs.
- **Use Stripe Elements or Stripe Checkout** for card input to avoid PCI scope.
- **If you must handle card data directly**, you need PCI Level 1 certification (avoid this if possible).

### Data Handling

- **Don't log sensitive payment data** (card numbers, CVV, full account numbers).
- **Sanitise error messages** - don't expose internal details to users.
- **Validate all input** before sending to Stripe.
- **Use HTTPS everywhere** - Stripe requires encrypted connections.
- **Implement rate limiting** on payment endpoints to prevent abuse.

### Authentication and Authorisation

- **Verify user identity** before allowing payment operations.
- **Implement proper access controls** - users should only access their own payment data.
- **Use Stripe Connect** for marketplace scenarios with proper security.
- **Validate webhook signatures** to ensure events are from Stripe.

## Error Handling

### API Errors

- **Handle all Stripe error types:**
  - `StripeCardError` - Card was declined
  - `StripeRateLimitError` - Too many requests
  - `StripeInvalidRequestError` - Invalid parameters
  - `StripeAPIError` - Stripe API error
  - `StripeConnectionError` - Network error
  - `StripeAuthenticationError` - Authentication failed
- **Provide user-friendly error messages** based on error codes:
  - `card_declined` - Card was declined
  - `insufficient_funds` - Insufficient funds
  - `expired_card` - Card expired
  - `incorrect_cvc` - Incorrect CVC
  - `processing_error` - Processing error
- **Log detailed errors server-side** for debugging, but show generic messages to users.
- **Implement retry logic** for transient errors (rate limits, network issues).
- **Use exponential backoff** for retries.

### Payment Failures

- **Handle payment failures gracefully** with clear user messaging.
- **Provide actionable next steps** when payments fail.
- **Allow users to retry** with different payment methods.
- **Track payment failure reasons** for analytics and improvement.

## Webhooks

### Webhook Implementation

- **Verify webhook signatures** using the webhook signing secret:
  ```javascript
  const sig = request.headers['stripe-signature'];
  const event = stripe.webhooks.constructEvent(payload, sig, webhookSecret);
  ```
- **Handle webhook idempotency** - use event IDs to prevent duplicate processing.
- **Process webhooks asynchronously** when possible to respond quickly.
- **Return 200 status** quickly, then process the event.
- **Handle webhook retries** - Stripe will retry failed webhooks.

### Critical Webhook Events

- **Payment events:**
  - `payment_intent.succeeded`
  - `payment_intent.payment_failed`
  - `payment_intent.requires_action`
- **Subscription events:**
  - `customer.subscription.created`
  - `customer.subscription.updated`
  - `customer.subscription.deleted`
  - `invoice.payment_succeeded`
  - `invoice.payment_failed`
- **Dispute events:**
  - `charge.dispute.created`
  - `charge.dispute.updated`
- **Customer events:**
  - `customer.created`
  - `customer.updated`
  - `customer.deleted`

### Webhook Testing

- **Use Stripe CLI** for local webhook testing: `stripe listen --forward-to localhost:3000/webhooks`
- **Test webhook failure scenarios** - what happens if processing fails?
- **Test webhook retries** to ensure idempotency works correctly.

## Testing

### Test Mode

- **Always test in test mode first** before using live mode.
- **Use test card numbers** provided by Stripe:
  - Success: `4242 4242 4242 4242`
  - Decline: `4000 0000 0000 0002`
  - 3DS required: `4000 0025 0000 3155`
- **Use test mode webhooks** for local development.
- **Test all payment scenarios:**
  - Successful payments
  - Failed payments
  - 3DS authentication
  - Refunds
  - Subscriptions
  - Payment method updates

### Test Data Management

- **Create test customers** for development.
- **Use test mode API keys** in development environments.
- **Clean up test data** periodically to avoid clutter.
- **Use separate test accounts** for different developers if needed.

### Integration Testing

- **Test the full payment flow** end-to-end.
- **Test error scenarios** - network failures, API errors, declined cards.
- **Test webhook processing** with mock events.
- **Test subscription lifecycle** - creation, updates, cancellations.

## Common Patterns

### Customer Management

- **Create Stripe customers** when users sign up or make their first purchase.
- **Store Stripe customer IDs** in your database, not full customer objects.
- **Update customer metadata** to sync with your user data.
- **Handle customer deletion** - decide if you want to delete from Stripe or just mark as inactive.

### Payment Method Storage

- **Use Payment Methods API** to save payment methods.
- **Attach payment methods to customers** for reuse.
- **Set default payment methods** for subscriptions.
- **Handle payment method updates** when cards expire or are replaced.

### Idempotency

- **Always use idempotency keys** for:
  - Creating Payment Intents
  - Creating Subscriptions
  - Processing Refunds
  - Any operation that could be retried
- **Generate idempotency keys** client-side or use request IDs.
- **Store idempotency keys** to handle retries correctly.

### Metadata

- **Use metadata** to store additional information:
  - Order IDs
  - User IDs
  - Internal references
  - Custom tracking data
- **Keep metadata under 500 characters** per key.
- **Use structured metadata** for complex data (JSON strings).

## Performance and Scalability

### API Usage

- **Batch operations when possible** - use Stripe's batch APIs.
- **Implement proper pagination** for listing operations.
- **Cache customer data** when appropriate (but keep it fresh).
- **Use webhooks instead of polling** for status updates.

### Rate Limiting

- **Respect Stripe's rate limits:**
  - 100 requests per second per API key
  - Burst up to 100 requests
- **Implement exponential backoff** for rate limit errors.
- **Use idempotency keys** to safely retry requests.
- **Monitor API usage** to stay within limits.

### Database Considerations

- **Store minimal Stripe data** in your database:
  - Customer IDs
  - Payment Intent IDs
  - Subscription IDs
  - Status flags
- **Fetch full objects from Stripe** when needed, don't duplicate all data.
- **Sync critical status changes** via webhooks to your database.

## International Considerations

### Currency Handling

- **Support multiple currencies** when applicable.
- **Handle currency conversion** if needed (Stripe handles this automatically).
- **Display amounts in user's currency** with proper formatting.
- **Handle currency-specific formatting** (decimal places, symbols).

### Local Payment Methods

- **Support local payment methods** in relevant markets:
  - SEPA (Europe)
  - BACS (UK)
  - ACH (US)
  - iDEAL (Netherlands)
  - etc.
- **Handle different payment flows** for different payment methods.
- **Provide appropriate messaging** for each payment method type.

### Tax Handling

- **Use Stripe Tax** for automatic tax calculation when available.
- **Handle tax-inclusive vs tax-exclusive** pricing correctly.
- **Support tax exemptions** when applicable.
- **Store tax information** for compliance and reporting.

## Reporting and Analytics

### Financial Reporting

- **Use Stripe Dashboard** for high-level reporting.
- **Export data via API** for custom reporting needs.
- **Track key metrics:**
  - Revenue
  - Payment success rates
  - Refund rates
  - Chargeback rates
  - Subscription churn

### Event Tracking

- **Log important payment events** in your system.
- **Track conversion funnels** - from intent to completion.
- **Monitor payment failures** to identify issues.
- **Analyse subscription metrics** - MRR, churn, lifetime value.

## Edge Cases and Considerations

### Partial Captures

- **Handle partial captures** for Payment Intents when needed.
- **Set `capture_method: 'manual'`** if you need to capture later.
- **Capture within 7 days** for most payment methods (or they'll be automatically cancelled).

### Payment Expiration

- **Handle expired Payment Intents** - they expire after 24 hours if not confirmed.
- **Create new Payment Intents** if the user returns after expiration.
- **Don't reuse expired Payment Intents.**

### Subscription Prorations

- **Understand proration behaviour** when changing subscriptions:
  - Immediate proration charges/credits
  - End-of-period changes
  - Trial period handling
- **Calculate prorations correctly** or let Stripe handle it automatically.
- **Communicate proration changes** clearly to users.

### Failed Payments

- **Handle failed subscription payments:**
  - Retry logic (Stripe handles this automatically)
  - Dunning emails (configure in Stripe)
  - Grace periods
  - Subscription cancellation after max retries
- **Notify users** about failed payments and next steps.
- **Provide easy payment method updates** for failed subscriptions.

### Disputes and Chargebacks

- **Monitor disputes** via webhooks.
- **Respond to disputes** within deadlines (typically 7-21 days).
- **Provide evidence** for dispute responses:
  - Proof of delivery
  - Customer communication
  - Terms of service acceptance
  - Product/service description
- **Track dispute rates** and work to reduce them.

## Code Examples and Patterns

### Payment Intent Creation (Server-Side)

```javascript
// Good: Server-side Payment Intent creation
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000, // $20.00 in cents
  currency: 'usd',
  customer: customerId,
  payment_method_types: ['card'],
  metadata: {
    order_id: 'order_123',
    user_id: 'user_456',
  },
}, {
  idempotencyKey: requestId, // Always use idempotency keys
});
```

### Payment Confirmation (Client-Side)

```javascript
// Good: Client-side confirmation with Stripe.js
const { error, paymentIntent } = await stripe.confirmCardPayment(
  clientSecret,
  {
    payment_method: {
      card: cardElement,
      billing_details: {
        name: 'Customer Name',
      },
    },
  }
);
```

### Webhook Handling

```javascript
// Good: Webhook signature verification and idempotency
app.post('/webhooks/stripe', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
  } catch (err) {
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Check if we've already processed this event
  const existingEvent = await db.events.findOne({ stripeEventId: event.id });
  if (existingEvent) {
    return res.status(200).json({ received: true, duplicate: true });
  }

  // Process the event
  await handleStripeEvent(event);

  // Mark event as processed
  await db.events.create({ stripeEventId: event.id, type: event.type });

  res.status(200).json({ received: true });
});
```

### Error Handling

```javascript
// Good: Comprehensive error handling
try {
  const paymentIntent = await stripe.paymentIntents.create({...});
} catch (error) {
  if (error.type === 'StripeCardError') {
    // Card was declined
    switch (error.code) {
      case 'card_declined':
        return { error: 'Your card was declined. Please try a different payment method.' };
      case 'insufficient_funds':
        return { error: 'Insufficient funds. Please try a different card.' };
      case 'expired_card':
        return { error: 'Your card has expired. Please update your payment method.' };
      default:
        return { error: 'Payment failed. Please try again.' };
    }
  } else if (error.type === 'StripeRateLimitError') {
    // Retry with exponential backoff
    return { error: 'Too many requests. Please try again in a moment.' };
  } else {
    // Log full error server-side, return generic message
    console.error('Stripe error:', error);
    return { error: 'An error occurred. Please try again later.' };
  }
}
```

## Documentation and Maintenance

### Code Documentation

- **Document Stripe integration points** in your codebase.
- **Explain why certain patterns are used** (not just what).
- **Document webhook handlers** and what they do.
- **Keep API version notes** when upgrading.

### Monitoring and Alerts

- **Set up alerts for:**
  - High payment failure rates
  - Webhook delivery failures
  - API errors
  - Dispute creation
  - Subscription cancellations
- **Monitor Stripe Dashboard** regularly for issues.
- **Track key metrics** over time to identify trends.

### Version Management

- **Pin Stripe API version** in your code.
- **Test API version upgrades** in staging before production.
- **Review Stripe changelog** regularly for breaking changes.
- **Plan migration paths** for deprecated features.

---

**Remember:** Stripe handles the complex parts of payment processing, but you're responsible for integrating it correctly, handling errors gracefully, and providing a good user experience. Always test thoroughly in test mode before going live, and monitor your integration continuously.

