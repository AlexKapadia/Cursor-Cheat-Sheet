# Modern Tech Gradient Dark - Design System

## What It Is

This is a comprehensive design system reference document extracted from the **n8n.io** website. It captures the complete visual design language, including colors, typography, components, animations, and responsive patterns used throughout the site.

**Source Website:** https://n8n.io/  
**Design Style:** Modern Tech Gradient Dark  
**Primary Framework:** Nuxt.js  
**CSS Framework:** Tailwind CSS

## Design Style Characteristics

### Key Visual Characteristics

- **Dark Theme Aesthetic**: Deep navy backgrounds (#0e0918, #0c081c) create a premium, technical feel
- **Vibrant Gradients**: Extensive use of purple, violet, and orange gradients for accents and effects
- **Glassmorphism Effects**: Backdrop blur effects create depth and modern visual appeal
- **Custom Typography**: Geomanist font family with tight letter spacing for a unique brand identity
- **Sophisticated Animations**: Multi-layered animations including gradient glows, card hover effects, and parallax scrolling
- **High Contrast**: White and light lavender text on dark backgrounds for excellent readability

### Color Palette Overview

- **Primary Accent**: #ea4b71 (brand pink/magenta)
- **Gradient Colors**: Purple (#6b21ef), Orange (#ff9b26), Violet (#e768e6)
- **Backgrounds**: Deep navy tones with various opacity levels
- **Text**: White primary, lavender gray secondary (#c4bbd3)

### Typography Approach

- **Primary Font**: Geomanist (custom font family)
- **Weights**: Light (300), Regular (400), Medium (500)
- **Style**: Modern sans-serif with tight letter spacing (-0.02em)
- **Scale**: Responsive typography that adapts across breakpoints

### Layout Patterns

- **Grid System**: 12-column responsive grid
- **Spacing**: Consistent spacing scale using Tailwind utilities
- **Containers**: Max-width containers with responsive padding
- **Sections**: Full-width sections with internal container constraints

### Animation Style

- **Subtle but Present**: Animations enhance UX without being distracting
- **Gradient Glows**: Animated gradient effects on buttons and cards
- **Hover States**: Smooth transitions on interactive elements
- **Scroll Effects**: Parallax and fade-in animations on scroll
- **Performance-Focused**: Uses transform and opacity for GPU acceleration

## How to Use When Building

### Method 1: Reference in Cursor Chat

Simply mention the design system in your Cursor chat:

```
"Use the modern-tech-gradient-dark design system for this component"
```

Or be more specific:

```
"Create a button using the primary button styles from modern-tech-gradient-dark"
"Build a card component with the gradient card pattern from modern-tech-gradient-dark"
```

### Method 2: Open in Cursor

1. Open the MDC file: `web-design/modern-tech-gradient-dark/modern-tech-gradient-dark.mdc`
2. Reference specific sections as needed
3. Copy CSS code blocks directly into your project

### Method 3: Add to Cursor Rules

1. Copy the entire MDC file content
2. Add it to your `.cursorrules` file or Cursor Rules configuration
3. The design system will be automatically available in all chat sessions

### Method 4: Use Specific Sections

Reference specific sections from the MDC:

- **Colors**: "Use the color palette from modern-tech-gradient-dark"
- **Typography**: "Apply the typography system from modern-tech-gradient-dark"
- **Components**: "Build this using the card component pattern from modern-tech-gradient-dark"
- **Animations**: "Add the gradient glow animation from modern-tech-gradient-dark"

## Key Design Elements

### Components

1. **Buttons**
   - Primary button with gradient hover effects
   - Secondary button with transparent background
   - Consistent padding and min-height
   - Smooth transitions

2. **Cards**
   - Gradient background variants (default, blue, dark)
   - Animated glow effects on hover
   - Rounded corners (19-20px)
   - Inner shadow effects

3. **Badges**
   - Pill-shaped (44px border-radius)
   - Gradient or flat variants
   - Subtle shadow effects
   - Icon + text layout

4. **Tabs**
   - Gradient layer background
   - Smooth content transitions
   - Active state highlighting
   - Rounded container

5. **Gradient Tiles**
   - Glassmorphism effect (backdrop blur)
   - Purple and orange gradient variants
   - Hover lift effect
   - Social proof layout

6. **Navigation**
   - Fixed header with backdrop blur
   - Dropdown menus with sub-navigation
   - Mobile hamburger menu
   - Smooth transitions

### Visual Effects

1. **Gradient Glows**
   - Animated gradient backgrounds
   - Blur effects (60px)
   - Position-based animations
   - Hover-triggered

2. **Backdrop Blur**
   - Glassmorphism on headers and cards
   - 22px-50px blur radius
   - Semi-transparent backgrounds

3. **Shadow System**
   - Multi-layered shadows
   - Inset shadows for depth
   - Color-matched shadows

4. **Parallax Effects**
   - Scroll-triggered animations
   - Perspective transforms
   - Smooth motion

## Quick Start

### 1. Set Up Design Tokens

```css
:root {
  --color-primary: #ea4b71;
  --color-background-deep: #0e0918;
  --color-text-primary: #ffffff;
  /* ... see MDC for complete token list */
}
```

### 2. Configure Typography

```css
@font-face {
  font-family: geomanist;
  src: url('/fonts/geomanist-regular.woff2') format('woff2');
  /* ... additional font weights */
}
```

### 3. Implement Base Components

Start with buttons and cards, then expand to more complex components:

```css
.btn-primary {
  /* Copy from MDC Component Library section */
}
```

### 4. Add Animations

Implement the gradient glow and hover effects:

```css
@keyframes gradient-glow {
  /* Copy from MDC Animations section */
}
```

### 5. Test Responsive Design

Ensure all components work across breakpoints:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## Contents

The MDC file includes:

- **Website Metadata**: Source URL, frameworks, analysis date
- **Design Overview**: High-level description of the design style
- **Design System Fundamentals**: Colors, typography, spacing, borders, shadows
- **Layout Systems**: Grid system and breakpoints
- **Component Library**: Buttons, cards, forms, navigation, modals, badges, tabs, gradient tiles
- **Animations and Transitions**: CSS transitions, animations, scroll effects, page transitions
- **Page Layouts**: Homepage structure and layout patterns
- **User Flows and Navigation**: Primary user journeys and navigation patterns
- **Responsive Design Patterns**: Mobile, tablet, and desktop adaptations
- **Loading States**: Page load and content loading indicators
- **Interactive Behaviors**: Hover effects, click interactions, scroll behaviors, form interactions
- **Implementation Guidelines**: CSS architecture, component structure, animation performance, accessibility
- **Design Tokens**: Complete CSS variable system
- **Page-Specific Designs**: Homepage layout and components
- **Motion Graphics**: Advanced animations and effects
- **Design Patterns**: Layout, component, and animation patterns
- **Implementation Checklist**: Step-by-step implementation guide

## Related Resources

- **Original Website**: https://n8n.io/
- **n8n Documentation**: https://docs.n8n.io/
- **n8n GitHub**: https://github.com/n8n-io/n8n

## Design System Philosophy

This design system emphasizes:

1. **Depth Through Layers**: Multiple gradient layers and blur effects create visual depth
2. **Motion as Enhancement**: Animations enhance UX without overwhelming
3. **Consistency**: Unified design language across all components
4. **Performance**: Optimized animations using GPU-accelerated properties
5. **Accessibility**: High contrast, keyboard navigation, semantic HTML

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS custom properties (@property) may need fallbacks for older browsers
- Backdrop filter requires -webkit- prefix for Safari
- Test gradient rendering across all target browsers

## Notes

- The design uses Nuxt.js for SSR, consider hydration when implementing
- Backdrop filter effects may impact performance on lower-end devices
- Gradient animations use CSS custom properties which may need polyfills
- All measurements are in rem/px as specified in the MDC
- Color values are exact hex/rgb as extracted from the source

---

**Last Updated**: 2025-11-29  
**Version**: 1.0.0  
**Status**: Complete

For questions or updates to this design system, refer to the source website or update the MDC file accordingly.

