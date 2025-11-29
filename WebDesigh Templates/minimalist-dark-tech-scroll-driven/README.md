# Minimalist Dark Tech Scroll-Driven Design System

## What It Is

This is a comprehensive design system extracted from [Citix.me](https://www.citix.me/), a website showcasing innovative urban technology products. The design system represents a sophisticated minimalist aesthetic with a dark, high-contrast color palette, bold typography, and scroll-driven animations.

**Source Website:** https://www.citix.me/  
**Design Style:** Minimalist Dark Tech Scroll-Driven  
**Purpose:** Complete design system reference for recreating the Citix website design

## Design Style Characteristics

### Visual Identity
- **Dark Background:** Deep black (#101010) creates a high-contrast foundation
- **Bold Red Accent:** Vibrant red (#FB0733) used for highlights, CTAs, and active states
- **Minimalist Aesthetic:** Clean, spacious layouts with generous white space
- **Typography-Focused:** Massive display typography with tight letter spacing creates dramatic impact

### Key Visual Elements
- **Large Display Typography:** Hero headings scale from 248sp down to 16sp responsively
- **Scroll-Driven Animations:** GSAP-powered scroll-triggered reveals and 3D transforms
- **Progress Indicators:** Animated progress lines that fill based on scroll position
- **3D Product Cards:** Parallax effects and 3D transforms on product showcases
- **Smooth Transitions:** Custom easing functions for fluid animations

### Color Palette
- **Primary:** Black (#101010) - Background and primary text
- **Accent:** Red (#FB0733) - Highlights, CTAs, progress indicators
- **Neutral:** White (#FFFFFF) - Text on dark, light mode background
- **Secondary Text:** Reduced opacity (65%) for hierarchy

### Typography Approach
- **Display Fonts:** Custom fonts for large headings
- **Body Fonts:** Custom fonts for readable body text
- **Scale:** Fluid typography system that adapts from 248sp to 13sp
- **Letter Spacing:** Tight spacing (-0.04em) for large headings

### Layout Patterns
- **Full-Viewport Sections:** Hero sections use entire viewport height
- **Grid Systems:** 6-column and 10-column responsive grids
- **Spacious Design:** Generous spacing allows content to breathe
- **Scroll-Driven:** Layout adapts and animates based on scroll position

### Animation Style
- **Scroll-Triggered:** GSAP ScrollTrigger powers most animations
- **Character Reveals:** Text reveals character by character
- **3D Transforms:** Product cards transform in 3D space
- **Smooth Easing:** Custom cubic-bezier functions for natural motion
- **Micro-interactions:** Subtle hover effects and state transitions

## How to Use When Building

### Method 1: Reference in Cursor Chat

Simply reference the design system in your conversation:

```
"Use the design system from minimalist-dark-tech-scroll-driven.mdc to create a landing page with scroll-triggered animations"
```

```
"Build a hero section using the typography scale and color palette from minimalist-dark-tech-scroll-driven.mdc"
```

```
"Create a product showcase component with 3D transforms following the patterns in minimalist-dark-tech-scroll-driven.mdc"
```

### Method 2: Open in Cursor

1. Open the MDC file in Cursor: `web-design/minimalist-dark-tech-scroll-driven/minimalist-dark-tech-scroll-driven.mdc`
2. Reference specific sections as needed
3. Copy design tokens, component CSS, or animation patterns
4. Adapt to your project requirements

### Method 3: Add to Cursor Rules

1. Add the MDC file to your Cursor Rules directory
2. The design system will be available for all projects
3. Reference components and patterns in any conversation
4. Build consistently across projects

### Method 4: Use Specific Sections

**For Typography:**
- Reference the "Typography System" section
- Use the type scale and font weights
- Apply letter spacing values
- Adapt responsive breakpoints

**For Colors:**
- Use the color palette from "Color Palette" section
- Apply CSS custom properties
- Use gradient definitions
- Reference RGB values for rgba

**For Components:**
- Copy component CSS from "Component Library"
- Adapt to your framework (React, Vue, etc.)
- Use state management patterns
- Apply responsive variations

**For Animations:**
- Reference "Animations and Transitions" section
- Use easing functions
- Implement scroll-triggered animations
- Apply micro-interactions

## Key Design Elements

### 1. Navigation System
- **Burger Menu:** Full-screen overlay with slide animations
- **Side Navigation:** Scroll progress indicator with section links
- **Footer Navigation:** Product links and social media
- **Smooth Scroll:** GSAP-powered smooth scrolling

### 2. Hero Sections
- **Scroll-Driven Reveals:** Character-by-character text animation
- **Multiple Hero Headings:** Each with unique styling and animations
- **Product Showcase:** 3D transformed product cards
- **Scroll Indicator:** Animated line that guides users

### 3. Product Components
- **3D Product Cards:** Parallax effects and depth transforms
- **Tabbed Navigation:** Smooth width animations
- **Product Galleries:** Progress indicators and number navigation
- **Hover Effects:** Arrow reveals and color transitions

### 4. Timeline Component
- **Vertical Timeline:** Progress line with scroll tracking
- **Video Content:** Masked gradients for smooth transitions
- **Text Reveals:** Opacity and visibility animations
- **Responsive Adaptations:** Mobile and tablet layouts

### 5. Animation System
- **GSAP Integration:** ScrollTrigger for scroll animations
- **CSS Transitions:** Custom easing functions
- **3D Transforms:** GPU-accelerated animations
- **Progress Tracking:** CSS custom properties updated by JavaScript

### 6. Responsive Design
- **Fluid Spacing:** Viewport-based spacing system
- **Responsive Typography:** Scales from 248sp to 13sp
- **Breakpoint System:** 479px (mobile), 1023px (tablet), 1024px+ (desktop)
- **Component Adaptations:** Layout changes per breakpoint

## Quick Start

### 1. Set Up CSS Variables

```css
:root {
  --black: #101010;
  --white: #FFFFFF;
  --red: #FB0733;
  --spacing: clamp(...);
  --smooth: cubic-bezier(0.76, 0, 0.24, 1);
  /* ... more variables */
}
```

### 2. Implement Typography Scale

```css
.hero-heading {
  font-size: calc(var(--spacing) * 248);
  letter-spacing: -0.04em;
  line-height: 1;
  font-weight: 300;
}
```

### 3. Create Component Structure

```html
<div class="component">
  <div class="component_element">
    <!-- Content -->
  </div>
</div>
```

### 4. Add Animations

```css
.element {
  opacity: 0;
  transition: opacity 0.4s var(--smooth);
}

.element.active {
  opacity: 1;
}
```

### 5. Implement Responsive Breakpoints

```css
@media screen and (max-width: 1023px) {
  /* Tablet styles */
}

@media screen and (max-width: 479px) {
  /* Mobile styles */
}
```

## Contents

The MDC file includes:

### Design Fundamentals
- Complete color palette with usage patterns
- Typography system with responsive scales
- Spacing system with fluid calculations
- Border and shadow systems
- Gradient definitions

### Component Library
- Navigation (burger menu, side nav, footer)
- Hero sections with scroll animations
- Product cards with 3D transforms
- Tabs component with width animations
- Timeline component with progress tracking
- Gallery component with progress indicators
- Buttons with hover effects
- Progress indicators
- Scroll indicators

### Animation System
- CSS transitions with custom easing
- CSS animations for reveals
- Scroll-triggered animations (GSAP)
- Page transitions
- Micro-interactions

### Layout Systems
- Grid systems (6-column, 10-column)
- Container patterns
- Breakpoint system
- Responsive utilities

### Responsive Patterns
- Mobile layouts (< 479px)
- Tablet layouts (479px - 1023px)
- Desktop layouts (> 1023px)
- Component variations per breakpoint

### Implementation Guidelines
- CSS architecture
- Component structure
- Animation performance
- Accessibility considerations

### Design Tokens
- Complete CSS custom properties
- Reusable values
- Consistent naming

## Related Resources

- **Original Website:** [Citix.me](https://www.citix.me/)
- **Technologies Used:**
  - [Astro](https://astro.build/) - Static site generator
  - [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
  - [GSAP](https://greensock.com/gsap/) - Animation library
  - [ScrollTrigger](https://greensock.com/scrolltrigger/) - Scroll animation plugin

## Design Philosophy

This design system embodies:

1. **Minimalism:** Clean, uncluttered layouts with focus on content
2. **Typography First:** Large, impactful typography creates hierarchy
3. **Motion as Narrative:** Scroll animations guide user attention
4. **High Contrast:** Dark background with bright accents for clarity
5. **Performance:** GPU-accelerated animations for smooth experience

## Best Practices

1. **Use CSS Variables:** Leverage the design tokens for consistency
2. **Respect Spacing System:** Use the fluid spacing system for responsive design
3. **Optimize Animations:** Use `transform` and `opacity` for performance
4. **Test Responsively:** Verify designs at all breakpoints
5. **Maintain Contrast:** Ensure text remains readable with opacity variations

## Notes

- The design uses modern CSS features (`color-mix()`, custom properties)
- GSAP is required for scroll-triggered animations
- Custom fonts are loaded from the original site
- Some animations require JavaScript (GSAP ScrollTrigger)
- The spacing system is viewport-based for true fluidity

---

**Ready to Build:** This design system provides everything needed to recreate the Citix website design. All components, animations, and responsive patterns are documented with code examples and implementation guidelines.

