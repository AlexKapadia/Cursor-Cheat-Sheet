# Communication Engine

## What It Is

> **CRITICAL ARCHITECTURE PRINCIPLE: THE "ROUTER" PATTERN**

### Key Architecture Principles

- >
- >
- **The Notification Center:** Always call `notifyUser(userId, 'welcome')` instead of directly calling email/SMS functions
- **The Router Logic:** Checks user preferences (`email_enabled`, `sms_enabled`) and message urgency
- **Urgent Messages (Security Codes):** Always sent via SMS + Email regardless of preferences

## How to Use It

1. Review the `communication-engine.mdc` file for detailed architecture and implementation guidelines
2. Follow the architectural principles and patterns outlined in the document
3. Implement the database schemas, API contracts, and frontend components as specified
4. Refer to the code examples and best practices for integration

## Where Information Is From

- **Primary Source:** This MDC file (`communication-engine.mdc`)
- The content is based on industry best practices, architectural patterns, and implementation guidelines
- Code examples and schemas are production-ready and follow modern development standards

## How to Build

### Prerequisites

- **Technologies:** CSS, Git, HTML, React, Redis, SQL, Supabase, Tailwind, TypeScript

### Setup Steps

1. Review the database schema and create the necessary tables
2. Set up the required services and APIs (as specified in the MDC)
3. Install dependencies and configure environment variables
4. Follow the implementation phases outlined in the MDC
5. Test each component according to the testing guidelines

## What to Build With It

### Technologies & Tools

- CSS, Git, HTML, React, Redis, SQL, Supabase, Tailwind, TypeScript

### Recommended Stack

The MDC provides guidance for building production-ready systems using:
- Modern web frameworks and libraries
- Database systems with proper schema design
- API integrations and third-party services
- Frontend components and UI patterns
- Security and authentication mechanisms

---

*For detailed implementation instructions, refer to the `communication-engine.mdc` file in this directory.*
