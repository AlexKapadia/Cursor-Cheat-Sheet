# Website to MDC Conversion Project

## Overview
This project provides a comprehensive framework for analyzing websites and converting them into structured MDC (Markdown Cursor) format. The analysis covers visual design, interactive elements, responsive patterns, code structure, and accessibility.

## Target Website
- **URL**: `https://xx.wearemotto.com/`
- **Status**: Protected by Cloudflare (requires JavaScript-enabled browser)
- **Access Method**: Browser automation (Puppeteer/Playwright)

## Project Structure

```
@website-to-mdc/
├── README.md                          # This file
├── website-to-mdc-rules.mdc           # Comprehensive analysis framework
├── analysis/                          # Detailed analysis files
│   ├── 01-discovery.md               # Phase 1: Discovery results
│   ├── 02-visual-structure.md        # Phase 2: Visual analysis
│   ├── 03-interactive-elements.md    # Phase 2: Interactive analysis
│   ├── 04-responsive-design.md       # Phase 2: Responsive analysis
│   ├── 05-design-patterns.md         # Phase 3: Design patterns
│   ├── 06-code-structure.md          # Phase 4: Code analysis
│   ├── 07-content-analysis.md        # Phase 5: Content analysis
│   └── 08-performance-accessibility.md # Phase 6-7: Performance & A11y
└── assets/                            # Supporting assets
    ├── screenshots/                   # Visual references
    ├── color-palette.json            # Extracted color system
    └── typography-system.json        # Typography tokens
```

## Methodology

The analysis follows an 8-phase approach:

1. **Phase 1: Website Access and Discovery**
   - URL validation and accessibility
   - Technology stack detection
   - Sitemap and navigation discovery
   - Page inventory creation

2. **Phase 2: Multi-Pass Design Analysis**
   - Pass 1: Visual structure mapping
   - Pass 2: Interactive elements and behaviors
   - Pass 3: Responsive design analysis
   - Pass 4: Page flow and navigation mapping

3. **Phase 3: Design Element Extraction**
   - Visual patterns (icons, images, shadows, borders)
   - Interactive patterns (hover effects, loading states)
   - Animation patterns
   - Responsive patterns

4. **Phase 4: Code Structure Analysis**
   - HTML structure and semantics
   - CSS architecture
   - JavaScript patterns

5. **Phase 5: Content Analysis**
   - Content structure
   - SEO elements

6. **Phase 6: Performance Analysis**
   - Core Web Vitals
   - Optimization patterns

7. **Phase 7: Accessibility Analysis**
   - WCAG compliance
   - Inclusive design patterns

8. **Phase 8: MDC File Generation**
   - Structured documentation
   - Design token extraction
   - Code examples

## Setup

### Prerequisites
- Node.js (v18+)
- npm or yarn

### Installation

```bash
# Install browser automation tools
npm install puppeteer playwright

# Or install globally
npm install -g puppeteer playwright
```

## Usage

### Browser Automation Script

For Cloudflare-protected sites, use the provided browser automation script:

```bash
node scripts/analyze-website.js
```

### Manual Analysis

Follow the framework outlined in `website-to-mdc-rules.mdc` to conduct a manual analysis.

## Tools

- **Puppeteer/Playwright**: Browser automation for JavaScript-heavy sites
- **Chrome DevTools**: Performance and accessibility analysis
- **Lighthouse**: Automated audits
- **WAVE**: Accessibility evaluation

## Current Status

- ✅ Framework defined in `website-to-mdc-rules.mdc`
- ✅ Directory structure created
- ⏳ Browser automation setup (in progress)
- ⏳ Phase 1: Discovery (pending site access)
- ⏳ Phase 2-7: Analysis (pending)

## Notes

- The target website is protected by Cloudflare, requiring browser automation
- All analysis should respect rate limits and terms of service
- Screenshots and extracted data should be used for documentation purposes only

## Contributing

When adding new analysis:
1. Follow the phase structure outlined in the rules file
2. Update the corresponding analysis markdown file
3. Add screenshots to the assets folder
4. Update this README with findings

---

*Last Updated: 2025-11-29*

