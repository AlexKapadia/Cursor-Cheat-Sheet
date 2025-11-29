# Design Style Naming Convention

## Overview

The MDC filename should be based on the dominant design style characteristics. This makes it easy for users to identify and choose designs at a glance.

## Naming Format

**Format:** `[design-style]-[key-characteristic]-[additional-feature].mdc`

- Use lowercase
- Separate words with hyphens
- Keep under 60 characters
- Make it instantly recognizable

## Naming Process

### Step 1: Analyze Design Style

Identify the following characteristics:

1. **Primary Aesthetic**
   - Modern
   - Classic
   - Playful
   - Elegant
   - Bold
   - Minimalist
   - Brutalist
   - Retro
   - Futuristic

2. **Color Approach**
   - Vibrant
   - Muted
   - Monochrome
   - Gradient-heavy
   - Dark-mode
   - Light-mode

3. **Typography Focus**
   - Typography-focused
   - Mixed
   - Sans-serif dominant
   - Serif dominant
   - Display fonts

4. **Layout Style**
   - Grid-heavy
   - Asymmetric
   - Centered
   - Full-width
   - Card-based
   - Magazine-style

5. **Animation Level**
   - Static
   - Subtle
   - Animated
   - Motion-heavy
   - Micro-interactions

6. **Special Effects**
   - Glassmorphism
   - Neumorphism
   - 3D
   - Parallax
   - Particle effects
   - Video backgrounds

### Step 2: Select Key Characteristics

Choose 2-4 most prominent characteristics that best describe the design.

### Step 3: Create Descriptive Name

Combine the characteristics into a clear, recognizable name.

## Examples

### Good Examples

- `modern-minimalist-clean-lines.mdc`
  - Modern aesthetic
  - Minimalist approach
  - Clean lines characteristic

- `bold-corporate-gradient-hero.mdc`
  - Bold aesthetic
  - Corporate style
  - Gradient-heavy
  - Hero section focus

- `playful-creative-animated.mdc`
  - Playful aesthetic
  - Creative approach
  - Heavy animation

- `elegant-typography-focused.mdc`
  - Elegant aesthetic
  - Typography-focused
  - Clean, refined

- `dark-mode-glassmorphism.mdc`
  - Dark mode
  - Glassmorphism effect
  - Modern, sleek

- `brutalist-bold-typography.mdc`
  - Brutalist aesthetic
  - Bold approach
  - Typography-focused

- `vibrant-gradient-animated.mdc`
  - Vibrant colors
  - Gradient-heavy
  - Animated interactions

- `minimalist-typography-centered.mdc`
  - Minimalist approach
  - Typography-focused
  - Centered layout

- `corporate-blue-professional.mdc`
  - Corporate style
  - Blue color scheme
  - Professional aesthetic

- `creative-illustration-playful.mdc`
  - Creative approach
  - Illustration-heavy
  - Playful aesthetic

### Bad Examples (Avoid)

- `website-design.mdc` - Too generic
- `design-system.mdc` - Not descriptive
- `modern-website.mdc` - Too vague
- `cool-design.mdc` - Subjective, not descriptive
- `new-design.mdc` - Meaningless

## Style Categories Reference

### Aesthetic Categories
- Modern
- Classic
- Playful
- Elegant
- Bold
- Minimalist
- Brutalist
- Retro
- Futuristic
- Corporate
- Creative
- Professional

### Color Categories
- Vibrant
- Muted
- Monochrome
- Gradient-heavy
- Dark-mode
- Light-mode
- Colorful
- Pastel
- High-contrast

### Typography Categories
- Typography-focused
- Mixed
- Sans-serif dominant
- Serif dominant
- Display fonts
- Handwritten
- Geometric

### Layout Categories
- Grid-heavy
- Asymmetric
- Centered
- Full-width
- Card-based
- Magazine-style
- Split-screen
- Sidebar

### Animation Categories
- Static
- Subtle
- Animated
- Motion-heavy
- Micro-interactions
- Scroll-heavy
- Parallax

### Special Effects Categories
- Glassmorphism
- Neumorphism
- 3D
- Parallax
- Particle effects
- Video backgrounds
- Blur effects
- Gradient overlays

## Naming Guidelines

1. **Be Specific**: Use specific terms that accurately describe the design
2. **Be Concise**: Keep it under 60 characters
3. **Be Descriptive**: The name should give a clear picture of the design
4. **Be Consistent**: Use consistent terminology across all MDCs
5. **Be Recognizable**: The name should be instantly understandable

## Validation

Before finalizing a name, ask:
- Can someone identify the design style from the name?
- Is it specific enough?
- Is it descriptive enough?
- Is it under 60 characters?
- Does it use consistent terminology?

## Examples by Design Type

### Minimalist Designs
- `minimalist-typography-centered.mdc`
- `minimalist-white-space-clean.mdc`
- `minimalist-monochrome-simple.mdc`

### Bold Designs
- `bold-corporate-gradient.mdc`
- `bold-typography-high-contrast.mdc`
- `bold-colorful-vibrant.mdc`

### Playful Designs
- `playful-creative-animated.mdc`
- `playful-illustration-colorful.mdc`
- `playful-rounded-soft.mdc`

### Elegant Designs
- `elegant-typography-refined.mdc`
- `elegant-serif-classic.mdc`
- `elegant-spacing-luxury.mdc`

### Modern Designs
- `modern-minimalist-clean.mdc`
- `modern-gradient-glassmorphism.mdc`
- `modern-grid-structured.mdc`

### Dark Mode Designs
- `dark-mode-glassmorphism.mdc`
- `dark-mode-neon-accent.mdc`
- `dark-mode-minimalist.mdc`

## Folder Structure

The folder name should match the MDC filename (without .mdc):

```
web-design/
  └── modern-minimalist-clean-lines/
      ├── modern-minimalist-clean-lines.mdc
      └── README.md
```

## Best Practices

1. **Analyze thoroughly** before naming
2. **Use 2-4 key characteristics** for balance
3. **Prioritize most prominent** characteristics
4. **Test the name** - does it make sense?
5. **Be consistent** with terminology

---

**Remember:** The filename is the first thing users see. Make it count. It should instantly communicate what design style the MDC contains.

