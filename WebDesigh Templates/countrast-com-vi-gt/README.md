# Countrast - Data-Driven Minimalist Design System

## What It Is

This MDC (Markdown Design Conversion) file documents the complete design system of **Countrast** (https://countrast.com/vi/gt), a country comparison website that presents statistical data in a clean, minimal interface. The design system represents a **Data-Driven Minimalist** aesthetic, prioritizing clarity and readability over decorative elements.

**Purpose:** This MDC serves as a complete reference for developers to recreate the Countrast design without needing to see the original website. It includes all design tokens, component styles, responsive patterns, and implementation guidelines.

## Design Style Characteristics

### Visual Approach
- **Minimalist Philosophy:** Clean, uncluttered interface with no shadows, gradients, or complex animations
- **Data-First Design:** Every design decision supports the primary goal of comparing country statistics clearly
- **Warm Neutral Palette:** Stone and zinc color families create an approachable, professional feel
- **Typography Contrast:** Monospace font (Reddit Mono) for data values, sans-serif (Rubik) for UI elements

### Key Characteristics
- **Color Palette:** Warm stone tones (#f4f3ec background) with neutral grays for text and borders
- **Typography:** Dual-font system emphasizing data readability
- **Layout:** Grid-based responsive system (2-column mobile, 12-column tablet+)
- **Animation Style:** Minimal - only subtle CSS transitions (0.15s) for hover states
- **Component Style:** Flat design with transparent backgrounds and minimal borders

## How to Use When Building

### Method 1: Reference in Cursor Chat
Simply mention the MDC file in your conversation:
```
"Use the design system from countrast-com-vi-gt.mdc to style the country comparison interface"
```

### Method 2: Open in Cursor
Open the MDC file directly in Cursor to reference specific sections:
- Press `Ctrl+P` (or `Cmd+P` on Mac)
- Type `countrast-com-vi-gt.mdc`
- Navigate to the section you need (e.g., "Color Palette", "Typography System")

### Method 3: Add to Cursor Rules
Add the MDC to your `.cursorrules` file or reference it in project-specific rules:
```
When building the country comparison feature, follow the design system in countrast-com-vi-gt.mdc
```

### Method 4: Use Specific Sections
Reference specific sections for targeted implementation:
- **Colors:** Use the "Color Palette" section for all color values
- **Typography:** Use the "Typography System" section for font sizes, weights, and line heights
- **Components:** Use the "Component Library" section for button, card, and form styles
- **Responsive:** Use the "Responsive Design Patterns" section for breakpoint-specific styles

**Example:**
```
"Create a button component using the 'Country Selection Button' styles from the Component Library section"
```

## Key Design Elements

### 1. Dual Typography System
- **Reddit Mono (Monospace):** Used for all data values and numbers
- **Rubik (Sans-serif):** Used for UI labels, buttons, and interface text
- **Purpose:** Creates clear visual distinction between data and interface

### 2. Warm Stone Color Palette
- **Background:** `#f4f3ec` (stone-100) - Warm, off-white background
- **Text:** `#050505` (zinc-950) - High contrast for readability
- **Borders:** `#d1d1d1` (neutral-300) - Subtle dividers
- **Hover States:** `rgba(41, 37, 36, 0.05)` - Subtle background on interaction

### 3. Responsive Grid System
- **Mobile:** 2-column grid for metrics
- **Tablet+:** 12-column grid for flexible layouts
- **Breakpoints:** 768px (tablet), 1280px (desktop)

### 4. Minimal Interactive Elements
- **Buttons:** Transparent backgrounds with subtle hover states
- **Data Buttons:** Dashed underline decoration for interactive data points
- **Radio Buttons:** Custom-styled unit toggle (metric/imperial)
- **Transitions:** 0.15s duration with smooth easing

### 5. Data Visualization Containers
- **Metric Cards:** Icon + value + label pattern
- **Comparison Sections:** Side-by-side country data (responsive stacking)
- **Loading States:** 600x600px placeholder for data visualizations

## Quick Start

### Step 1: Set Up Design Tokens
Copy the CSS variables from the "Design Tokens" section into your project:
```css
:root {
  --color-stone-100: rgb(244 243 236);
  --color-zinc-950: rgb(5 5 5);
  /* ... all tokens from MDC */
}
```

### Step 2: Configure Typography
Set up the dual-font system:
```css
body {
  font-family: var(--font-family-mono); /* Reddit Mono for data */
}

.ui-text {
  font-family: var(--font-family-primary); /* Rubik for UI */
}
```

### Step 3: Implement Core Components
Start with the most essential components:
1. **Header** - Logo and unit toggle
2. **Country Buttons** - Selection interface
3. **Comparison Cards** - Data display containers
4. **Metric Cards** - Icon + value + label pattern

### Step 4: Add Responsive Behavior
Implement breakpoints:
- Mobile: 2-column grid, stacked layout
- Tablet: 12-column grid, side-by-side comparison
- Desktop: Enhanced spacing and typography

### Step 5: Add Interactions
Implement hover states and transitions:
- Country button hover: Subtle background change
- Data button hover: Underline decoration
- Smooth transitions (0.15s duration)

## Contents

The MDC file includes comprehensive documentation of:

### Design System Fundamentals
- **Color Palette:** Complete color system with hex codes and usage
- **Typography System:** Font families, sizes, weights, line heights, letter spacing
- **Spacing System:** Complete spacing scale (0.125rem to 3rem)
- **Border Radius System:** Minimal radius values
- **Shadow System:** No shadows (flat design)

### Layout Systems
- **Grid System:** 2-column mobile, 12-column tablet+ layouts
- **Breakpoints:** Mobile, tablet, desktop breakpoint values
- **Container Patterns:** Max-width constraints and responsive padding

### Component Library
- **Buttons:** Country selection, data value, unit toggle buttons
- **Cards:** Comparison cards, metric cards
- **Forms:** Radio button groups, unit toggle
- **Navigation:** Header navigation, country list
- **Loading Indicators:** Placeholder states

### Animations and Transitions
- **CSS Transitions:** Standard and extended duration transitions
- **Hover Effects:** Button and link hover states
- **Click Interactions:** Button feedback patterns

### Responsive Design Patterns
- **Mobile (< 768px):** Stacked layout, compact spacing
- **Tablet (768px - 1279px):** Side-by-side comparison, 12-column grid
- **Desktop (> 1280px):** Enhanced spacing, larger typography

### Page Layouts
- **Country Comparison Page:** Complete layout structure with ASCII diagram
- **Component Usage:** Detailed breakdown of components per page
- **Responsive Behavior:** How layouts adapt per breakpoint

### Implementation Guidelines
- **CSS Architecture:** Tailwind CSS utility-first approach
- **Component Structure:** React functional components
- **Animation Performance:** Best practices for transitions
- **Accessibility:** Focus states, ARIA patterns, semantic HTML

### Design Tokens
Complete CSS variable system for:
- Colors (stone, zinc, neutral palettes)
- Typography (fonts, sizes, weights, line heights)
- Spacing (0.125rem to 3rem scale)
- Borders (width, radius, colors)
- Transitions (duration, timing functions)
- Breakpoints (tablet, desktop values)

## Related Resources

- **Original Website:** https://countrast.com/vi/gt
- **Source URL:** https://countrast.com/vi/gt
- **Technology Stack:** React (Vite), Tailwind CSS
- **Analysis Date:** 2025-01-29

## Design Philosophy Notes

This design system emphasizes:

1. **Clarity Over Decoration:** No unnecessary visual elements
2. **Data Readability:** Typography choices prioritize number readability
3. **Warm Professionalism:** Stone color palette feels approachable yet professional
4. **Responsive Flexibility:** Grid system adapts seamlessly across devices
5. **Subtle Interactions:** Hover states provide feedback without distraction
6. **Performance:** Minimal CSS and simple transitions ensure fast loads
7. **Accessibility:** Semantic HTML and proper labeling support all users

## Implementation Checklist

The MDC includes a complete implementation checklist covering:
- ✅ Design token setup
- ✅ Typography configuration
- ✅ Color palette implementation
- ✅ Spacing system setup
- ✅ Component implementation
- ✅ Responsive design
- ✅ Animation implementation

Use this checklist to track your implementation progress and ensure nothing is missed.

---

**Note:** This design system is optimized for data visualization and comparison interfaces. The minimalist approach ensures users can focus on the data without visual distractions.

