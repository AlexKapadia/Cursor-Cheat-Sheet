# Cal.com Scheduling Engine

## What It Is

> **CRITICAL ARCHITECTURE PRINCIPLE: THE "HEADLESS" RULE**

### Key Architecture Principles

- >
- **Not an Iframe:** Do not embed the Cal.com iframe. Use the **Atom Components** (`@calcom/atoms`) or the Platform API to build a custom booking flow that matches your app design (`apple-saas-suite.mdc`).
- **The "Managed User" Model:** Your users are "Managed Users" inside your Cal.com Platform instance. Generate an Access Token for them so they can connect their Google Calendars.
- **Design System Integration:** All UI components must follow the Apple Design System (`apple-saas-suite.mdc`) - white cards, rounded corners, glass effects, and SF Pro typography.

## How to Use It

1. Review the `cal-scheduling-engine.mdc` file for detailed architecture and implementation guidelines
2. Follow the architectural principles and patterns outlined in the document
3. Implement the database schemas, API contracts, and frontend components as specified
4. Refer to the code examples and best practices for integration

## Where Information Is From

- **Primary Source:** This MDC file (`cal-scheduling-engine.mdc`)
- The content is based on industry best practices, architectural patterns, and implementation guidelines
- Code examples and schemas are production-ready and follow modern development standards

## How to Build

### Prerequisites

- **Technologies:** Git, React, SQL, TypeScript

### Setup Steps

1. Review the database schema and create the necessary tables
2. Set up the required services and APIs (as specified in the MDC)
3. Install dependencies and configure environment variables
4. Follow the implementation phases outlined in the MDC
5. Test each component according to the testing guidelines

## What to Build With It

### Technologies & Tools

- Git, React, SQL, TypeScript

### Recommended Stack

The MDC provides guidance for building production-ready systems using:
- Modern web frameworks and libraries
- Database systems with proper schema design
- API integrations and third-party services
- Frontend components and UI patterns
- Security and authentication mechanisms

---

*For detailed implementation instructions, refer to the `cal-scheduling-engine.mdc` file in this directory.*
