# Cursor Rules & Architecture Guides

> **A comprehensive collection of architecture guides, design systems, integration rules, and best practices for building modern applications with Cursor AI.**

This repository contains curated documentation, rules, and reference guides organised by category. When you want to build something, point Cursor to the relevant files in this repository to get expert-level guidance and architectural patterns.

---

## 🚀 How to Use This Repository

### With Cursor AI

1. **Open the relevant category folder** for your project
2. **Reference specific files** in your Cursor chat:
   - "Use the patterns from `engines/decision-logic-engine.mdc`"
   - "Follow the architecture in `backend/supabase-backend-architecture.mdc`"
   - "Apply the design system from `web-design/apple-adaptive-system.mdc`"

3. **Point Cursor to multiple files** for comprehensive guidance:
   - "Read all files in `ai/` and `backend/` to understand the full stack architecture"
   - "Use `apis-integration/stripe-integration-rules.md` and `engines/fintech-ledger-engine.mdc` for payment processing"

### Quick Start

```bash
# Example: Building a diagnostic app
# Reference: engines/decision-logic-engine.mdc

# Example: Building a payment system
# Reference: apis-integration/stripe-integration-rules.md + engines/fintech-ledger-engine.mdc

# Example: Building a modern web app
# Reference: web-design/apple-adaptive-system.mdc + backend/supabase-backend-architecture.mdc
```

---

## 📁 Repository Structure

### 🤖 [AI](./ai/)
AI and machine learning guides, integration rules, and engine architectures.

- `agentic-ai-guide.md` - Agentic AI system design patterns
- `ai-transcription-engine.mdc` - Speech-to-text transcription architecture
- `ai-writing-rules.md` - Writing guidelines for AI-generated content
- `chatbot-creation-guide.mdc` - Conversational AI chatbot architecture
- `gemini-ai-integration-guide.md` - Google Gemini API integration
- `machine-learning-models-guide.md` - ML model development and deployment
- `openai-integration-rules.md` - OpenAI API integration patterns
- `rag-ai-engine.mdc` - Retrieval-Augmented Generation (RAG) architecture

### 🔌 [APIs & Integration](./apis-integration/)
Third-party API integration guides and reference documentation.

- `api-integration-guide.mdc` - General API integration patterns
- `mapbox-reference.md` - Mapbox mapping service integration
- `stripe-integration-rules.md` - Stripe payment processing integration

### ⚙️ [Backend](./backend/)
Backend architecture patterns, serverless configurations, and database architectures.

- `aws-serverless-backend.mdc` - AWS Lambda, API Gateway, and serverless patterns
- `mongodb-backend-architecture.mdc` - MongoDB database architecture and patterns
- `supabase-backend-architecture.mdc` - Supabase backend architecture and best practices

### 🗄️ [Databases](./databases/)
Database-specific rules, schemas, and optimisation patterns.

*(Currently empty - database-specific guides are in `backend/`)*

### 🛠️ [Development Tools](./development-tools/)
Code quality, version control, and development workflow guides.

- `code-review-rules.md` - Code review best practices and checklists
- `codebase-hygiene.mdc` - Code organisation and maintenance patterns
- `git-connection-rules.md` - Git workflow and branching strategies
- `github-research-rules.md` - GitHub research and discovery workflows
- `report-data-extraction-rules.md` - Data extraction from reports and documents

### 🏗️ [Engines](./engines/)
Application engines and business logic systems for common use cases.

- `booking-reservation-engine.mdc` - Booking and reservation system architecture
- `decision-logic-engine.mdc` - Graph-based decision logic and diagnostic systems
- `fintech-ledger-engine.mdc` - Financial transaction ledger architecture
- `freelance-bidding-engine.mdc` - Freelance marketplace bidding system
- `marketplace-engine.mdc` - Multi-vendor marketplace architecture
- `security-encryption-engine.mdc` - Security and encryption patterns
- `social-event-engine.mdc` - Social event management system
- `social-media-engine.mdc` - Social media platform architecture

### 🔬 [Science & Maths](./science-maths/)
Scientific computing, mathematical analysis, and data processing guides.

- `data-analysis-rules.md` - Data analysis workflows and patterns
- `dem-data-rules.md` - Digital Elevation Model (DEM) data processing
- `excel-data-extraction-rules.md` - Excel data extraction and parsing
- `gis-rules.md` - Geographic Information Systems (GIS) patterns
- `graph_generator.py` - Graph generation utilities
- `mathematical-equation-extraction-rules.md` - Mathematical equation parsing
- `mathematical-functions-analysis-rules.md` - Function analysis patterns
- `phreeqc-geochemistry-engine.mdc` - PHREEQC geochemical modelling
- `statistical-analysis-engine.mdc` - Statistical analysis architecture
- `vector-math-visual-engine.mdc` - Vector mathematics visualisation

### 🎨 [Web Design](./web-design/)
UI/UX design systems, component libraries, and visual design patterns.

- `apple-adaptive-system.mdc` - Apple-inspired adaptive design system
- `apple-saas-suite.mdc` - SaaS application design patterns
- `AtmosphericBackground.tsx` - React component for atmospheric backgrounds
- `brutalist-archival-index.mdc` - Brutalist design system
- `cinematic-angular-smoke.mdc` - Cinematic smoke effects
- `code-website-publishing-guide.mdc` - Code documentation website patterns
- `data-driven-cyber-ui.mdc` - Cyberpunk data visualisation UI
- `interactive-motion.mdc` - Interactive motion design patterns
- `japanese-corporate-playful.mdc` - Japanese-inspired corporate design
- `kinetic-minimalist-portfolio.mdc` - Minimalist portfolio design
- `motion-graphics-library.mdc` - Motion graphics component library
- `RazorCard.tsx` - React card component
- `sculptural-luxury-minimal.mdc` - Luxury minimalist design system
- `structural-swiss-grid.mdc` - Swiss grid system architecture
- `tailwind.config.js` - Tailwind CSS configuration
- `TimelineConnector.tsx` - React timeline component
- `tokyo-techno-minimal.mdc` - Tokyo-inspired techno design

---

## 💡 Usage Examples

### Example 1: Building a Diagnostic Application

```markdown
Reference these files in Cursor:
- engines/decision-logic-engine.mdc (graph-based decision logic)
- web-design/apple-adaptive-system.mdc (UI design system)
- backend/supabase-backend-architecture.mdc (backend architecture)
```

### Example 2: Creating a Payment System

```markdown
Reference these files in Cursor:
- apis-integration/stripe-integration-rules.md (payment integration)
- engines/fintech-ledger-engine.mdc (transaction ledger)
- security-encryption-engine.mdc (security patterns)
```

### Example 3: Building a Social Platform

```markdown
Reference these files in Cursor:
- engines/social-media-engine.mdc (core architecture)
- engines/social-event-engine.mdc (event features)
- web-design/tokyo-techno-minimal.mdc (design system)
- backend/mongodb-backend-architecture.mdc (database)
```

### Example 4: Data Analysis Application

```markdown
Reference these files in Cursor:
- science-maths/data-analysis-rules.md (analysis patterns)
- science-maths/statistical-analysis-engine.mdc (statistics engine)
- science-maths/vector-math-visual-engine.mdc (visualisation)
- web-design/data-driven-cyber-ui.mdc (data UI)
```

---

## 📝 File Format Guide

- **`.md`** - Markdown documentation files (rules, guides, reference)
- **`.mdc`** - Markdown Cursor files (architecture guides, system designs)
- **`.tsx`** - React TypeScript components
- **`.js`** - JavaScript configuration files
- **`.py`** - Python utilities and scripts

---

## 🎯 Best Practices

1. **Start with the engine/architecture file** relevant to your use case
2. **Add design system files** for UI/UX guidance
3. **Include backend/API files** for infrastructure patterns
4. **Reference development tools** for code quality and workflow
5. **Combine multiple files** for comprehensive guidance

---

## 🔄 Contributing

When adding new guides:

1. Place files in the appropriate category folder
2. Use descriptive, kebab-case filenames
3. Update this README with the new file
4. Follow the existing file format conventions

---

## 📚 Additional Resources

- [Cursor AI Documentation](https://cursor.sh/docs)
- [Cursor Rules Format](https://cursor.sh/docs/context/rules)

---

## 📄 License

This repository contains architectural patterns, guides, and reference materials. Use them as templates and starting points for your projects.

---

**Last Updated:** November 2025

**Total Files:** 50+ architecture guides, rules, and components

**Categories:** 8 organised folders covering AI, Backend, Engines, Web Design, Science & Maths, APIs, Development Tools, and Databases

