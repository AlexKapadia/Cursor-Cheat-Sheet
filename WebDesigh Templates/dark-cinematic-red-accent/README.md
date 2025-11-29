# Dark Cinematic Red Accent - Design System

A comprehensive design system extracted from the Netflix UK homepage, featuring a dark cinematic aesthetic with bold red accents, custom typography, and smooth animations optimized for video content consumption.

## What It Is

This MDC (Markdown Cursor) file contains the complete design system from Netflix UK's homepage. It includes all design tokens, components, layouts, animations, and responsive patterns needed to recreate the Netflix homepage design. The design system emphasizes:

- **Dark Theme**: Pure black backgrounds with high contrast
- **Bold Red Accent**: Netflix's signature red (#E50914) for primary actions
- **Cinematic Layout**: Full-viewport hero sections with gradient overlays
- **Custom Typography**: Netflix Sans Variable font family
- **Smooth Animations**: Subtle transitions and micro-interactions
- **Responsive Design**: Carefully crafted breakpoints from mobile to ultra-wide desktop

## Design Style Characteristics

### Visual Identity

**Color Palette:**
- Primary: Netflix Red (#E50914) - Used for buttons, CTAs, and brand elements
- Background: Pure Black (#000000) - Creates high contrast and cinematic feel
- Text: White with opacity variations for hierarchy
- Gradients: Complex multi-color gradients on hero sections

**Typography:**
- Primary Font: Netflix Sans Variable (custom font)
- Fallbacks: Helvetica Neue, Segoe UI, Roboto, Ubuntu
- Weights: Regular (400), Medium (500)
- Sizes: Responsive scaling from mobile to desktop

**Layout Patterns:**
- Full-width hero sections with gradient backgrounds
- Centered containers with responsive padding
- Maximum width: 1920px (120rem)
- Dramatic padding scaling at larger breakpoints

**Animation Style:**
- Smooth, subtle transitions
- Cubic-bezier timing functions for natural motion
- Respects `prefers-reduced-motion` for accessibility
- Focus on content, not flashy effects

### Key Design Elements

1. **Hero Section**
   - Full viewport height
   - Complex gradient backgrounds (red to black, purple to blue)
   - Centered content with large CTAs
   - Responsive typography scaling

2. **Primary Buttons**
   - Netflix red background (#E50914)
   - Smooth hover transitions (darker red)
   - Immediate active feedback
   - Disabled states with reduced opacity

3. **Navigation Header**
   - Fixed positioning
   - Minimal design (logo + sign in button)
   - Responsive height (5rem mobile, 5.5rem desktop)
   - Clean, unobtrusive

4. **Content Sections**
   - Horizontal scrolling patterns (for content rows)
   - Smooth fade-in animations
   - Responsive padding
   - Dark backgrounds with content overlays

5. **Gradient Overlays**
   - Multiple gradient layers
   - 77.82deg angle
   - Color stops from red/purple to dark blue/black
   - Creates depth without shadows

## How to Use When Building

### Method 1: Reference in Cursor Chat

Simply reference the design system in your Cursor chat:

```
"Use the design system from dark-cinematic-red-accent.mdc to create a landing page with a hero section, primary red buttons, and dark theme"
```

```
"Build a Netflix-style homepage using the dark-cinematic-red-accent design system - include the hero section with gradients and the primary button styles"
```

```
"Create a dark-themed video streaming interface using the color palette and typography from dark-cinematic-red-accent.mdc"
```

### Method 2: Open in Cursor

1. Open `dark-cinematic-red-accent.mdc` in Cursor
2. Reference specific sections as needed:
   - Color tokens for theming
   - Component styles for buttons, cards, forms
   - Layout patterns for hero sections
   - Animation code for transitions
3. Copy relevant CSS code blocks
4. Adapt to your project structure

### Method 3: Add to Cursor Rules

1. Add `dark-cinematic-red-accent.mdc` to your Cursor Rules folder
2. The design system will be available for all projects
3. Reference components and patterns in any project
4. Use design tokens across multiple files

**Example Usage:**
```
"Use the Netflix red (#E50914) from the dark-cinematic-red-accent design system for all primary buttons"
```

### Method 4: Use Specific Sections

**For Color Palette:**
```
"Use the color tokens from the Design Tokens section - specifically --color-primary for buttons"
```

**For Components:**
```
"Implement the primary button component from dark-cinematic-red-accent.mdc with all states (hover, active, disabled)"
```

**For Typography:**
```
"Apply the Netflix Sans typography system from dark-cinematic-red-accent.mdc - use the font-family-primary token"
```

**For Layouts:**
```
"Create a hero section using the Homepage Layout structure from dark-cinematic-red-accent.mdc"
```

**For Animations:**
```
"Add the fade-in animation from dark-cinematic-red-accent.mdc to content sections"
```

## Key Design Elements

### Color System

- **Primary Red**: `#E50914` (rgb(229,9,20)) - Brand color, buttons, CTAs
- **Hover Red**: `#C11119` (rgb(193,17,25)) - Button hover state
- **Active Red**: `#99161D` (rgb(153,22,29)) - Button active state
- **Background**: `#000000` - Pure black for maximum contrast
- **Text Primary**: `#FFFFFF` - White for main text
- **Text Secondary**: `rgba(255,255,255,0.7)` - Secondary text
- **Gradients**: Complex multi-color gradients for hero sections

### Typography System

- **Font Family**: Netflix Sans Variable (with system fallbacks)
- **Font Weights**: 400 (regular), 500 (medium)
- **Font Sizes**: Responsive scaling (1rem base, 1.125rem for headings)
- **Line Heights**: 1.2 (tight), 1.5 (normal), 1.75 (relaxed)

### Component Library

- **Primary Button**: Red background, white text, smooth transitions
- **Secondary Button**: Gray background, white text
- **Hero Section**: Full viewport, gradient backgrounds, centered content
- **Navigation Header**: Fixed, minimal, logo + sign in
- **Content Cards**: Transparent backgrounds, hover overlays
- **Forms**: Dark inputs with red focus states
- **Modals**: Dark overlays with scale animations

### Spacing System

- **Mobile Padding**: 1.5rem (24px)
- **Tablet Padding**: 2rem (32px)
- **Desktop Padding**: 5rem (80px)
- **Large Desktop Padding**: 9.25rem (148px)
- **Extra Large Padding**: 22.125rem (354px)

### Breakpoints

- **Mobile**: < 600px
- **Tablet**: 600px - 959px
- **Desktop**: 960px - 1279px
- **Large Desktop**: 1280px - 1919px
- **Extra Large**: 1920px+

### Animation System

- **Standard Transition**: 0.2s cubic-bezier(0.32, 0.94, 0.6, 1)
- **Smooth Transition**: 0.5s cubic-bezier(0.33, 0, 0, 1)
- **Transform Transition**: 533ms cubic-bezier(0.32, 0.94, 0.6, 1)
- **Reduced Motion**: Respects `prefers-reduced-motion` media query

## Quick Start

### 1. Set Up Design Tokens

Copy the CSS variables from the "Design Tokens" section into your CSS:

```css
:root {
  --color-primary: rgb(229, 9, 20);
  --color-background: rgb(0, 0, 0);
  /* ... all other tokens */
}
```

### 2. Load Typography

Add the Netflix Sans Variable font (or use fallbacks):

```css
@font-face {
  font-family: "Netflix Sans Variable";
  src: url("path-to-font.woff2") format("woff2");
}
```

### 3. Implement Core Components

Start with the primary button:

```css
.btn-primary {
  background-color: var(--color-primary);
  color: var(--color-text-primary);
  /* ... see MDC for full styles */
}
```

### 4. Create Hero Section

Use the hero section layout from the "Page Layouts" section:

```html
<section class="hero-section">
  <div class="hero-background"></div>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <!-- Content -->
  </div>
</section>
```

### 5. Add Responsive Behavior

Implement breakpoints from the "Responsive Design Patterns" section:

```css
@media all and (min-width: 600px) {
  /* Tablet styles */
}

@media all and (min-width: 960px) {
  /* Desktop styles */
}
```

## Contents

The MDC file includes:

### Design System Fundamentals
- Complete color palette (primary, neutral, semantic, gradients)
- Typography system (fonts, sizes, weights, line heights)
- Spacing system (responsive padding, component spacing)
- Border radius system
- Shadow system

### Layout Systems
- Grid system
- Flexbox layout patterns
- Complete breakpoint system
- Container patterns

### Component Library
- Buttons (primary, secondary, all states)
- Cards (hero, content)
- Forms (inputs, validation states)
- Navigation (header, mobile menu)
- Modals/Dialogs
- Loading indicators

### Animations and Transitions
- CSS transitions
- CSS animations (fade, slide, scale)
- Scroll animations
- Page transitions

### Page Layouts
- Homepage layout structure
- Component usage patterns
- Responsive behavior

### User Flows and Navigation
- Primary user flows
- Navigation structure
- Link patterns

### Responsive Design Patterns
- Mobile patterns (< 600px)
- Tablet patterns (600px - 959px)
- Desktop patterns (960px+)
- Large desktop patterns (1280px+)
- Extra large patterns (1920px+)

### Interactive Behaviors
- Hover effects
- Click interactions
- Scroll behaviors
- Form interactions

### Implementation Guidelines
- CSS architecture
- Component structure
- Animation performance
- Accessibility considerations

### Design Tokens
- Complete CSS variable system
- All color, typography, spacing, and layout tokens

## Related Resources

- **Original Website**: [Netflix UK](https://www.netflix.com/gb/)
- **Font Source**: Netflix Sans Variable (custom font, use fallbacks if unavailable)
- **Design System Type**: Dark theme, cinematic, video-focused

## Design Philosophy

This design system is optimized for:

1. **Video Content**: Dark backgrounds reduce eye strain during extended viewing
2. **High Contrast**: Pure black and white create maximum readability
3. **Brand Recognition**: Netflix red is instantly recognizable
4. **Content Focus**: Minimal navigation keeps focus on content
5. **Smooth Experience**: Subtle animations enhance without distracting
6. **Accessibility**: High contrast, reduced motion support, keyboard navigation

## Best Practices

1. **Maintain Color Accuracy**: Use exact hex values for Netflix red (#E50914)
2. **Respect Typography**: Use Netflix Sans or appropriate fallbacks
3. **Follow Spacing Scale**: Use the responsive padding system
4. **Implement All States**: Include hover, active, disabled, focus states
5. **Test Responsiveness**: Verify at all breakpoints
6. **Respect Motion Preferences**: Always include reduced motion support
7. **Maintain Contrast**: Ensure text meets WCAG contrast requirements

## Notes

- This design system is extracted from the Netflix UK homepage
- Some components may vary on other Netflix pages
- Font loading may require external resources
- Gradients may need fine-tuning for exact visual match
- Consider performance when implementing animations

---

**Remember**: This design system enables you to recreate the Netflix homepage design. Use it as a reference for dark themes, cinematic layouts, and video-focused interfaces.

