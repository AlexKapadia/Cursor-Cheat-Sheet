# TAO: Facebook's Distributed Data Store for the Social Graph

**Authors:** Nathan Bronson, Zach Amsden, George Cabrera, Prasad Chakka, Peter Dimov, Hui Ding, Jack Ferris, Anthony Giardullo, Sachin Kulkarni, Harry Li, Mark Marchukov, Dmitri Petrov, Lovro Puzar, Yee Jiun Song, Venkat Venkataramani  
**Year:** 2013

---

## What is This?

This folder contains an MDC (Markdown Cursor) cheat sheet derived from the scientific paper: **TAO: Facebook's Distributed Data Store for the Social Graph**.

An MDC file is a comprehensive reference document that Cursor AI can use to understand and implement the techniques, patterns, and methodologies described in the original paper. Think of it as a condensed, actionable version of the paper optimized for code generation and implementation.

This MDC covers Facebook's TAO system, a geographically distributed data store designed specifically for serving social graph data at massive scale. TAO processes over a billion reads per second and handles petabytes of data across thousands of machines.

## Contents

- **`tao-distributed-data-store.mdc`** - The main MDC cheat sheet containing:
  - Paper metadata and abstract
  - Problem statement and motivation
  - Key concepts and techniques (objects, associations, graph-aware caching)
  - Related work and background
  - Complete methodology and architecture
  - Detailed algorithms (object reads, association operations, cache invalidation)
  - Implementation patterns (layered architecture, sharding, replication)
  - Code examples and snippets
  - Mathematical foundations (key formulas, cache hit rate calculations)
  - Experimental setup and scale characteristics
  - Results and evaluation (performance metrics, comparisons)
  - Best practices and recommendations
  - Limitations and assumptions
  - Related techniques and references
  - Practical applications and use cases
  - Implementation checklist

- **`README.md`** - This file, explaining how to use the MDC

## How It Works

The MDC file was automatically generated from the scientific paper using a comprehensive extraction process that:

1. **Reads the entire paper** - Performs multiple passes to ensure complete coverage
2. **Extracts all technical content** - Code examples, algorithms, formulas, and patterns
3. **Organizes information** - Structures content into logical sections
4. **Preserves technical details** - Maintains accuracy of code, formulas, and implementation details
5. **Creates actionable reference** - Formats content for easy use in development

The extraction process follows strict protocols to ensure nothing is missed, making the MDC a reliable "Source of Truth" for the paper's content.

## How to Use This When Building

### Method 1: Reference in Cursor Chat

Explicitly mention the MDC file in your Cursor conversation:

```
"Use the techniques from tao-distributed-data-store/tao-distributed-data-store.mdc to implement a graph data store"
"Follow the patterns in tao-distributed-data-store/tao-distributed-data-store.mdc for caching graph data"
"Apply the TAO architecture from tao-distributed-data-store/tao-distributed-data-store.mdc"
"Use the association list algorithms from the TAO MDC"
"Implement graph-aware caching as described in the TAO paper MDC"
```

### Method 2: Open in Cursor

1. **Open the MDC file** in Cursor's editor
2. Cursor will automatically include it in the context for that conversation
3. The AI will reference the file's patterns and rules when generating code

### Method 3: Add to Cursor Rules

1. **Copy the file path** (e.g., `backend/tao-distributed-data-store/tao-distributed-data-store.mdc`)
2. **Add to `.cursorrules`** file in your project:

```
@backend/tao-distributed-data-store/tao-distributed-data-store.mdc
```

### Method 4: Use Specific Sections

You can reference specific sections of the MDC:

- **Architecture Patterns** - "Use the layered architecture pattern from the TAO MDC"
- **Algorithms** - "Implement the association list query algorithm from the TAO MDC"
- **Implementation Patterns** - "Follow the sharding pattern from the TAO MDC"
- **Best Practices** - "Apply the caching best practices from the TAO MDC"
- **Code Examples** - "Use the association query code example from the TAO MDC"

## Key Concepts

- **Objects and Associations Model:** Typed nodes (objects) and typed edges (associations) representing graph data
- **Graph-Aware Caching:** Cache designed specifically for graph data structures, not just key-value pairs
- **Geographic Distribution:** Single system instance distributed across multiple regions
- **Read-Optimized Architecture:** Heavily optimized for read operations (billions per second)
- **Eventual Consistency:** Favors availability and efficiency over strong consistency
- **Fixed Query API:** Limited set of queries optimized for the workload
- **Association Lists:** Efficient storage and retrieval of edge lists with incremental updates
- **Cache Invalidation:** Graph-aware invalidation using graph semantics
- **Master-Slave Architecture:** Write to master MySQL, read from replicas
- **Sharding:** Distribution of data across multiple machines using consistent hashing
- **Read-After-Write Consistency:** Ensures reads see recent writes for clients sharing a cache
- **Remote Markers:** Tracking stale keys across regions for cache coherence

## Quick Start

1. **Read the MDC file** to understand the TAO architecture and data model
2. **Review the algorithms section** to understand how object and association operations work
3. **Check the implementation patterns** to see how to structure your system
4. **Review the code examples** to see practical usage patterns
5. **Reference the MDC** in Cursor when building graph data stores or distributed caching systems
6. **Follow the best practices** section before starting implementation
7. **Use the implementation checklist** to guide your development

## Use Cases

This MDC is particularly useful when building:

- **Social Graph Systems:** User relationships, connections, and interactions
- **Graph Data Stores:** Systems that need to store and query graph-structured data
- **Distributed Caching Systems:** Graph-aware caching layers
- **High-Scale Read Systems:** Systems optimized for read-heavy workloads
- **Geographically Distributed Systems:** Multi-region data stores
- **Association-Based Data Models:** Systems using typed edges and relationships
- **Content Recommendation Systems:** User-item associations and similarity graphs
- **Knowledge Graphs:** Entity relationships and semantic networks

## Related Resources

- **Original Paper:** "TAO: Facebook's Distributed Data Store for the Social Graph" (USENIX ATC 2013)
- **Related MDCs:**
  - Consider checking `backend/supabase-backend-architecture/` for database architecture patterns
  - Consider checking `backend/mongodb-backend-architecture/` for NoSQL patterns
  - Consider checking `backend/aws-serverless-backend/` for distributed system patterns

## Notes

- This MDC is automatically generated and should be verified against the original paper for critical implementations
- The MDC focuses on practical implementation details and may not include all theoretical background
- TAO is designed for very large scale (billions of objects, petabytes of data) - may be overkill for smaller systems
- The system favors availability over consistency - applications must handle eventual consistency
- TAO uses a fixed API optimized for graph workloads - not a general-purpose database
- Always review best practices and limitations before implementation
- The system is read-optimized - write-heavy workloads may need different approaches

## Implementation Tips

When implementing TAO-like systems:

1. **Start with the Data Model:** Define your object types and association types clearly
2. **Design the Cache Layer:** Build graph-aware caching, not just key-value caching
3. **Implement Incremental Updates:** Association lists should be updated incrementally, not reloaded
4. **Plan for Scale:** Use sharding and replication from the start
5. **Handle Consistency:** Design for eventual consistency and handle staleness gracefully
6. **Monitor Performance:** Track cache hit rates, latency, and throughput
7. **Test Failure Scenarios:** Ensure graceful degradation and proper failover

---

**Remember:** This MDC serves as a comprehensive reference for implementing TAO-like graph data stores. Use it as a guide, but adapt it to your specific requirements and scale.






