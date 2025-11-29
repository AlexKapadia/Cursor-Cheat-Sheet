# Booking & Reservation Engine

## What It Is

> **CRITICAL ARCHITECTURE PRINCIPLE: THE "NO DOUBLE-BOOKING" RULE**

### Key Architecture Principles

- >
- **Atomic Transactions:** Never check availability and then book separately. Use Database Transactions (Postgres Isolation Levels) to ensure two concurrent requests cannot book the same slot.
- **Timezones:** All data stored in UTC. All availability logic converts User Local Time → UTC before querying the database.
- **The "Block" System:** A calendar is made of "Slots." A booking consumes slots. Overlapping slots = conflict.

## How to Use It

1. Review the `booking-reservation-engine.mdc` file for detailed architecture and implementation guidelines
2. Follow the architectural principles and patterns outlined in the document
3. Implement the database schemas, API contracts, and frontend components as specified
4. Refer to the code examples and best practices for integration

## Where Information Is From

- **Primary Source:** This MDC file (`booking-reservation-engine.mdc`)
- The content is based on industry best practices, architectural patterns, and implementation guidelines
- Code examples and schemas are production-ready and follow modern development standards

## How to Build

### Prerequisites

- **Technologies:** Git, Node.js, React, SQL, Stripe, Supabase, TypeScript

### Setup Steps

1. Review the database schema and create the necessary tables
2. Set up the required services and APIs (as specified in the MDC)
3. Install dependencies and configure environment variables
4. Follow the implementation phases outlined in the MDC
5. Test each component according to the testing guidelines

## What to Build With It

### Technologies & Tools

- Git, Node.js, React, SQL, Stripe, Supabase, TypeScript

### Recommended Stack

The MDC provides guidance for building production-ready systems using:
- Modern web frameworks and libraries
- Database systems with proper schema design
- API integrations and third-party services
- Frontend components and UI patterns
- Security and authentication mechanisms

---

*For detailed implementation instructions, refer to the `booking-reservation-engine.mdc` file in this directory.*
