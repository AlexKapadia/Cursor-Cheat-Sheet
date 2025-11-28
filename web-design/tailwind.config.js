/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    './pages/**/*.{js,jsx,ts,tsx}',
    './components/**/*.{js,jsx,ts,tsx}',
    './app/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      // Enforce "Razor" Geometry - No rounded corners by default
      borderRadius: {
        none: '0',
        sm: '2px', // Minimal exception for micro-interactions (use sparingly)
        DEFAULT: '0', // Override default to enforce sharp edges
        md: '0',
        lg: '0',
        xl: '0',
        '2xl': '0',
        '3xl': '0',
        full: '0', // Even "full" is sharp (for specific use cases)
      },
      // Color System: "The Deep Forest"
      colors: {
        'bg-void': '#050805',
        'accent-primary': '#8FA38F',
        'accent-glow': '#2D4A3E',
        'text-light': '#EAECE8',
      },
      // Typography: "Sharp & Editorial"
      fontFamily: {
        headline: ['Söhne', 'Helvetica Now', 'Inter', 'sans-serif'],
        label: ['Courier New', 'Monaco', 'Menlo', 'Consolas', 'monospace'],
      },
      letterSpacing: {
        tight: '-0.02em', // For headlines
        widest: '0.25em', // For labels/meta
      },
      // Motion Physics: "Liquid Time"
      transitionTimingFunction: {
        liquid: 'cubic-bezier(0.2, 0.8, 0.2, 1)',
      },
      transitionDuration: {
        1200: '1.2s', // Default "Liquid Time" duration
        2400: '2.4s', // Slow animations
      },
    },
  },
  plugins: [],
};

