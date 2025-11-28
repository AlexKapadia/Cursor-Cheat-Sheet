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
   - "Use `apis-integration/stripe-integration-rules.mdc` and `engines/fintech-ledger-engine.mdc` for payment processing"

### Quick Start

```bash
# Example: Building a diagnostic app
# Reference: engines/decision-logic-engine.mdc

# Example: Building a payment system
# Reference: apis-integration/stripe-integration-rules.mdc + engines/fintech-ledger-engine.mdc

# Example: Building a modern web app
# Reference: web-design/apple-adaptive-system.mdc + backend/supabase-backend-architecture.mdc
```

---

## 📁 Repository Structure

### 🤖 [AI](./ai/)
AI and machine learning guides, integration rules, and engine architectures.

- `agentic-ai-guide.mdc` - Agentic AI system design patterns
- `ai-transcription-engine.mdc` - Speech-to-text transcription architecture
- `ai-writing-rules.mdc` - Writing guidelines for AI-generated content
- `chatbot-creation-guide.mdc` - Conversational AI chatbot architecture
- `gemini-ai-integration-guide.mdc` - Google Gemini API integration
- `machine-learning-models-guide.mdc` - ML model development and deployment
- `openai-integration-rules.mdc` - OpenAI API integration patterns
- `rag-ai-engine.mdc` - Retrieval-Augmented Generation (RAG) architecture

### 🔌 [APIs & Integration](./apis-integration/)
Third-party API integration guides and reference documentation.

- `api-integration-guide.mdc` - General API integration patterns
- `google-maps-engine.mdc` - Google Maps Platform integration with Advanced Markers and cost optimization
- `mapbox-reference.mdc` - Mapbox mapping service integration
- `posthog-analytics-engine.mdc` - PostHog analytics integration and event tracking
- `stripe-integration-rules.mdc` - Stripe payment processing integration

### ⚙️ [Backend](./backend/)
Backend architecture patterns, serverless configurations, and database architectures.

- `aws-serverless-backend.mdc` - AWS Lambda, API Gateway, and serverless patterns
- `clerk-auth-engine.mdc` - Clerk authentication, user sync, and RBAC architecture
- `etl-pipeline-engine.mdc` - ETL (Extract, Transform, Load) pipeline architecture
- `headless-cms-engine.mdc` - Headless CMS architecture with Sanity, GROQ, and visual editing
- `mongodb-backend-architecture.mdc` - MongoDB database architecture and patterns
- `supabase-backend-architecture.mdc` - Supabase backend architecture and best practices
- `workflow-automation-engine.mdc` - Workflow automation and orchestration patterns

### 🗄️ [Databases](./databases/)
Database-specific rules, schemas, and optimisation patterns.

*(Currently empty - database-specific guides are in `backend/`)*

### 🛠️ [Development Tools](./development-tools/)
Code quality, version control, and development workflow guides.

- `code-review-rules.mdc` - Code review best practices and checklists
- `codebase-hygiene.mdc` - Code organisation and maintenance patterns
- `git-connection-rules.mdc` - Git workflow and branching strategies
- `github-research-rules.mdc` - GitHub research and discovery workflows
- `report-data-extraction-rules.mdc` - Data extraction from reports and documents

### 🏗️ [Engines](./engines/)
Application engines and business logic systems for common use cases.

- `booking-reservation-engine.mdc` - Booking and reservation system architecture
- `cal-scheduling-engine.mdc` - Calendar scheduling and appointment management
- `communication-engine.mdc` - Communication systems (email, SMS, notifications)
- `decision-logic-engine.mdc` - Graph-based decision logic and diagnostic systems
- `fintech-ledger-engine.mdc` - Financial transaction ledger architecture
- `freelance-bidding-engine.mdc` - Freelance marketplace bidding system
- `iot-control-engine.mdc` - IoT device control and management systems
- `liveblocks-multiplayer-engine.mdc` - Real-time multiplayer collaboration with Liveblocks
- `marketplace-engine.mdc` - Multi-vendor marketplace architecture
- `mux-video-engine.mdc` - Video streaming and processing with Mux
- `security-encryption-engine.mdc` - Security and encryption patterns
- `social-event-engine.mdc` - Social event management system
- `social-media-engine.mdc` - Social media platform architecture

### 🔬 [Science & Maths](./science-maths/)
Scientific computing, mathematical analysis, and data processing guides.

- `data-analysis-rules.mdc` - Data analysis workflows and patterns
- `dem-data-rules.mdc` - Digital Elevation Model (DEM) data processing
- `excel-data-extraction-rules.mdc` - Excel data extraction and parsing
- `gis-rules.mdc` - Geographic Information Systems (GIS) patterns
- `graph_generator.py` - Graph generation utilities
- `mathematical-equation-extraction-rules.mdc` - Mathematical equation parsing
- `mathematical-functions-analysis-rules.mdc` - Function analysis patterns
- `phreeqc-geochemistry-engine.mdc` - PHREEQC geochemical modelling
- `statistical-analysis-engine.mdc` - Statistical analysis architecture
- `vector-math-visual-engine.mdc` - Vector mathematics visualisation

### 💰 [Quantitative Finance](./)
Financial engineering, risk modeling, and quantitative analysis.

- `quant-finance-engine.mdc` - Monte Carlo stock price projection with Merton Jump Diffusion, Yahoo Finance data pipeline, and risk modeling

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
- apis-integration/stripe-integration-rules.mdc (payment integration)
- engines/fintech-ledger-engine.mdc (transaction ledger)
- engines/security-encryption-engine.mdc (security patterns)
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
- science-maths/data-analysis-rules.mdc (analysis patterns)
- science-maths/statistical-analysis-engine.mdc (statistics engine)
- science-maths/vector-math-visual-engine.mdc (visualisation)
- web-design/data-driven-cyber-ui.mdc (data UI)
```

### Example 5: Financial Analysis Dashboard

```markdown
Reference these files in Cursor:
- quant-finance-engine.mdc (Monte Carlo simulation, risk modeling)
- science-maths/statistical-analysis-engine.mdc (statistical analysis)
- web-design/data-driven-cyber-ui.mdc (financial data visualization)
- backend/supabase-backend-architecture.mdc (data storage)
```

---

## 📝 File Format Guide

- **`.mdc`** - Markdown Cursor files (architecture guides, system designs, rules, and reference documentation)
- **`.md`** - Standard markdown files (README only)
- **`.tsx`** - React TypeScript components
- **`.js`** - JavaScript configuration files
- **`.py`** - Python utilities and scripts

---

## 📘 Understanding .mdc Files (Cursor Rules)

### What are .mdc Files?

`.mdc` files are **Markdown Cursor** files that contain architecture guides, design patterns, and rules that Cursor AI can reference when generating code. They serve as "Source of Truth" documentation for specific domains, technologies, or patterns.

### How .mdc Files Work

Each `.mdc` file contains:

1. **Frontmatter Configuration** (at the top of the file):
   ```yaml
   ---
   alwaysApply: false
   ---
   ```
   - `alwaysApply: false` - The file is **not automatically applied** to every conversation. You must explicitly reference it.
   - `alwaysApply: true` - The file is **automatically included** in all Cursor conversations (use sparingly).

2. **Content Structure**:
   - Architecture principles and critical rules
   - Code examples and implementation patterns
   - Mathematical formulas (using LaTeX)
   - API endpoints and data structures
   - Best practices and anti-patterns

### How to Use .mdc Files

#### Method 1: Reference in Cursor Chat

**Explicitly mention the file** in your Cursor conversation:

```
"Use the patterns from quant-finance-engine.mdc to build a Monte Carlo simulation"
"Follow the architecture in backend/supabase-backend-architecture.mdc"
"Apply the design system from web-design/apple-adaptive-system.mdc"
```

#### Method 2: Open Files in Cursor

1. **Open the file** in Cursor's editor
2. Cursor will automatically include it in the context for that conversation
3. The AI will reference the file's patterns and rules

#### Method 3: Add to Cursor Rules

1. **Copy the file path** (e.g., `quant-finance-engine.mdc`)
2. **Add to `.cursorrules`** file in your project:
   ```
   @quant-finance-engine.mdc
   @backend/supabase-backend-architecture.mdc
   ```
3. These files will be automatically included in all conversations

### Setting Up .mdc Files

#### Option 1: Clone This Repository

```bash
git clone https://github.com/AlexKapadia/Cursor-Cheat-Sheet.git
cd Cursor-Cheat-Sheet
```

Then reference files by their relative path:
- `quant-finance-engine.mdc`
- `backend/supabase-backend-architecture.mdc`
- `engines/decision-logic-engine.mdc`

#### Option 2: Copy Specific Files

1. **Copy the `.mdc` file** you need to your project directory
2. **Reference it directly** in Cursor chat or add to `.cursorrules`

#### Option 3: Use as Remote Reference

If the repository is in a known location, you can reference files by their full path or add the repository to Cursor's workspace.

### Choosing How Files Are Applied

**Default Behavior (`alwaysApply: false`):**
- Files are **opt-in** - you must explicitly reference them
- Recommended for most files to avoid context bloat
- Gives you control over which patterns are active

**Auto-Apply (`alwaysApply: true`):**
- Files are **automatically included** in every conversation
- Use only for critical, universal rules
- Can slow down Cursor if too many files are auto-applied

**To Change Application Mode:**

1. Open the `.mdc` file
2. Edit the frontmatter:
   ```yaml
   ---
   alwaysApply: true  # or false
   ---
   ```
3. Save the file

### Best Practices for Using .mdc Files

1. **Start Specific**: Reference 1-2 relevant files for your current task
2. **Combine Strategically**: Mix architecture files with design system files
3. **Update Regularly**: Keep files updated as patterns evolve
4. **Document Dependencies**: Some files reference others (e.g., backend + API integration)
5. **Avoid Overload**: Don't reference too many files at once (3-5 max recommended)

### Example Workflow

```bash
# 1. You want to build a financial analysis dashboard
# 2. Reference the relevant files in Cursor:

"Use quant-finance-engine.mdc for the Monte Carlo simulation,
 web-design/data-driven-cyber-ui.mdc for the UI,
 and backend/supabase-backend-architecture.mdc for data storage"

# 3. Cursor will read all three files and apply their patterns
```

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

**Last Updated:** January 2025

**Total Files:** 60+ architecture guides, rules, and components

**Categories:** 8 organised folders covering AI, Backend, Engines, Web Design, Science & Maths, APIs, Development Tools, Databases, and Quantitative Finance

