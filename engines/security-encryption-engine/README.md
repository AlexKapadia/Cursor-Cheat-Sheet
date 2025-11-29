# Security & Encryption Engine

**Version:** 1.0.0

## What It Is

> **⚠️ CRITICAL ARCHITECTURE PRINCIPLE: "ZERO TRUST"**

### Key Architecture Principles

- >
- **Assume Breach:** Design the system assuming the database *will* be leaked. If it is, sensitive columns must be unreadable ciphertext.
- **Sanitize Everything:** Never trust input from the client. Validate strict schemas (Zod) before processing.
- **Least Privilege:** The API database user should not have `DROP TABLE` permissions.

## How to Use It

1. Review the `security-encryption-engine.mdc` file for detailed architecture and implementation guidelines
2. Follow the architectural principles and patterns outlined in the document
3. Implement the database schemas, API contracts, and frontend components as specified
4. Refer to the code examples and best practices for integration

## Where Information Is From

- **Primary Source:** This MDC file (`security-encryption-engine.mdc`)
- The content is based on industry best practices, architectural patterns, and implementation guidelines
- Code examples and schemas are production-ready and follow modern development standards

## How to Build

### Prerequisites

- **Technologies:** AWS, CSS, Git, GitHub, HTML, Next.js, PostgreSQL, REST, React, SQL, Supabase, TypeScript

### Setup Steps

1. Review the database schema and create the necessary tables
2. Set up the required services and APIs (as specified in the MDC)
3. Install dependencies and configure environment variables
4. Follow the implementation phases outlined in the MDC
5. Test each component according to the testing guidelines

## What to Build With It

### Technologies & Tools

- AWS, CSS, Git, GitHub, HTML, Next.js, PostgreSQL, REST, React, SQL, Supabase, TypeScript

### Recommended Stack

The MDC provides guidance for building production-ready systems using:
- Modern web frameworks and libraries
- Database systems with proper schema design
- API integrations and third-party services
- Frontend components and UI patterns
- Security and authentication mechanisms

---

*For detailed implementation instructions, refer to the `security-encryption-engine.mdc` file in this directory.*
