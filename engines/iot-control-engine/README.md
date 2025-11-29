# IoT Control Engine - Source of Truth Documentation

## What It Is

> **CRITICAL ARCHITECTURE PRINCIPLE: THE "ALWAYS ON" RULE**

### Key Architecture Principles

- >
- **Protocol:** HTTP is too heavy for small devices. Use **MQTT** (Message Queuing Telemetry Transport) over WebSockets.
- **The "Shadow" State:** Devices go offline. You cannot query a device directly. You query its "Device Shadow" (last known state) in your database.
- **TimeSeries Data:** Do not store sensor readings in standard Postgres tables. Use **TimescaleDB** or ClickHouse.

## How to Use It

1. Review the `iot-control-engine.mdc` file for detailed architecture and implementation guidelines
2. Follow the architectural principles and patterns outlined in the document
3. Implement the database schemas, API contracts, and frontend components as specified
4. Refer to the code examples and best practices for integration

## Where Information Is From

- **Primary Source:** This MDC file (`iot-control-engine.mdc`)
- The content is based on industry best practices, architectural patterns, and implementation guidelines
- Code examples and schemas are production-ready and follow modern development standards

## How to Build

### Prerequisites

- **Technologies:** AWS, Node.js, REST, Redis, SQL, TypeScript, WebSocket

### Setup Steps

1. Review the database schema and create the necessary tables
2. Set up the required services and APIs (as specified in the MDC)
3. Install dependencies and configure environment variables
4. Follow the implementation phases outlined in the MDC
5. Test each component according to the testing guidelines

## What to Build With It

### Technologies & Tools

- AWS, Node.js, REST, Redis, SQL, TypeScript, WebSocket

### Recommended Stack

The MDC provides guidance for building production-ready systems using:
- Modern web frameworks and libraries
- Database systems with proper schema design
- API integrations and third-party services
- Frontend components and UI patterns
- Security and authentication mechanisms

---

*For detailed implementation instructions, refer to the `iot-control-engine.mdc` file in this directory.*
