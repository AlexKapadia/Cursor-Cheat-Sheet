/**
 * Website Analysis Script using Puppeteer
 * Analyzes websites protected by Cloudflare or requiring JavaScript execution
 */

const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');

const TARGET_URL = 'https://xx.wearemotto.com/';
const OUTPUT_DIR = path.join(__dirname, '..');
const SCREENSHOTS_DIR = path.join(OUTPUT_DIR, 'assets', 'screenshots');

// Breakpoints for responsive analysis
const BREAKPOINTS = [
  { name: 'mobile-small', width: 320, height: 568 },
  { name: 'mobile-medium', width: 375, height: 667 },
  { name: 'mobile-large', width: 414, height: 896 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'tablet-large', width: 1024, height: 1366 },
  { name: 'desktop', width: 1280, height: 720 },
  { name: 'desktop-large', width: 1440, height: 900 },
  { name: 'desktop-xl', width: 1920, height: 1080 },
];

async function ensureDirectory(dir) {
  try {
    await fs.mkdir(dir, { recursive: true });
  } catch (error) {
    console.error(`Error creating directory ${dir}:`, error);
  }
}

async function analyzeWebsite() {
  console.log('Starting website analysis...');
  console.log(`Target URL: ${TARGET_URL}`);

  // Ensure output directories exist
  await ensureDirectory(SCREENSHOTS_DIR);

  const browser = await puppeteer.launch({
    headless: false, // Set to true for headless mode
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-blink-features=AutomationControlled',
    ],
  });

  try {
    const page = await browser.newPage();

    // Set a realistic user agent
    await page.setUserAgent(
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    );

    // Navigate to the site
    console.log('Navigating to website...');
    await page.goto(TARGET_URL, {
      waitUntil: 'networkidle2',
      timeout: 60000,
    });

    // Wait for Cloudflare challenge if present
    console.log('Waiting for page to load...');
    await page.waitForTimeout(5000); // Wait for any JavaScript execution

    // Check if we're on a challenge page
    const challengeText = await page.evaluate(() => {
      const challenge = document.querySelector('#challenge-error-text');
      return challenge ? challenge.textContent : null;
    });

    if (challengeText) {
      console.log('Cloudflare challenge detected. Waiting for resolution...');
      // Wait up to 30 seconds for challenge to resolve
      await page.waitForFunction(
        () => !document.querySelector('#challenge-error-text'),
        { timeout: 30000 }
      );
    }

    // Phase 1: Discovery
    console.log('\n=== Phase 1: Discovery ===');
    const discovery = await performDiscovery(page);
    await saveDiscovery(discovery);

    // Phase 2: Visual Analysis
    console.log('\n=== Phase 2: Visual Analysis ===');
    await captureScreenshots(page);

    // Phase 3: Technology Detection
    console.log('\n=== Phase 3: Technology Detection ===');
    const techStack = await detectTechnology(page);
    console.log('Technology Stack:', JSON.stringify(techStack, null, 2));

    // Phase 4: Content Extraction
    console.log('\n=== Phase 4: Content Extraction ===');
    const content = await extractContent(page);
    await saveContent(content);

    console.log('\nAnalysis complete!');
    console.log(`Results saved to: ${OUTPUT_DIR}`);

  } catch (error) {
    console.error('Error during analysis:', error);
  } finally {
    await browser.close();
  }
}

async function performDiscovery(page) {
  const discovery = {
    url: TARGET_URL,
    title: await page.title(),
    timestamp: new Date().toISOString(),
    pages: [],
    navigation: {},
    sitemap: null,
  };

  // Extract navigation
  discovery.navigation = await page.evaluate(() => {
    const nav = {};
    const headerNav = document.querySelector('nav, header nav, .navigation, .nav');
    if (headerNav) {
      nav.header = Array.from(headerNav.querySelectorAll('a')).map(a => ({
        text: a.textContent.trim(),
        href: a.href,
      }));
    }
    const footerNav = document.querySelector('footer nav, footer .nav');
    if (footerNav) {
      nav.footer = Array.from(footerNav.querySelectorAll('a')).map(a => ({
        text: a.textContent.trim(),
        href: a.href,
      }));
    }
    return nav;
  });

  // Try to find sitemap
  try {
    const sitemapUrl = new URL('/sitemap.xml', TARGET_URL).href;
    const response = await page.goto(sitemapUrl, { waitUntil: 'networkidle0' });
    if (response && response.status() === 200) {
      discovery.sitemap = sitemapUrl;
    }
  } catch (error) {
    console.log('No sitemap.xml found');
  }

  return discovery;
}

async function detectTechnology(page) {
  return await page.evaluate(() => {
    const tech = {
      frameworks: [],
      libraries: [],
      css: [],
      analytics: [],
    };

    // Detect React
    if (window.React || document.querySelector('[data-reactroot]')) {
      tech.frameworks.push('React');
    }

    // Detect Vue
    if (window.Vue || document.querySelector('[data-v-]')) {
      tech.frameworks.push('Vue');
    }

    // Detect Angular
    if (window.ng || document.querySelector('[ng-app]')) {
      tech.frameworks.push('Angular');
    }

    // Detect Next.js
    if (window.__NEXT_DATA__) {
      tech.frameworks.push('Next.js');
    }

    // Detect CSS frameworks
    const stylesheets = Array.from(document.styleSheets);
    stylesheets.forEach(sheet => {
      try {
        const href = sheet.href || '';
        if (href.includes('bootstrap')) tech.css.push('Bootstrap');
        if (href.includes('tailwind')) tech.css.push('Tailwind CSS');
        if (href.includes('material')) tech.css.push('Material UI');
      } catch (e) {
        // Cross-origin stylesheets may throw errors
      }
    });

    // Detect analytics
    if (window.gtag || window.ga) tech.analytics.push('Google Analytics');
    if (window._gaq) tech.analytics.push('Google Analytics (Legacy)');

    return tech;
  });
}

async function extractContent(page) {
  return await page.evaluate(() => {
    return {
      headings: Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(h => ({
        level: h.tagName,
        text: h.textContent.trim(),
      })),
      links: Array.from(document.querySelectorAll('a')).map(a => ({
        text: a.textContent.trim(),
        href: a.href,
      })),
      images: Array.from(document.querySelectorAll('img')).map(img => ({
        src: img.src,
        alt: img.alt,
        width: img.width,
        height: img.height,
      })),
      meta: {
        title: document.title,
        description: document.querySelector('meta[name="description"]')?.content || null,
        viewport: document.querySelector('meta[name="viewport"]')?.content || null,
      },
    };
  });
}

async function captureScreenshots(page) {
  console.log('Capturing screenshots at multiple breakpoints...');

  for (const breakpoint of BREAKPOINTS) {
    console.log(`  - ${breakpoint.name} (${breakpoint.width}x${breakpoint.height})`);
    await page.setViewport({
      width: breakpoint.width,
      height: breakpoint.height,
    });

    // Wait for layout to stabilize
    await page.waitForTimeout(1000);

    const screenshotPath = path.join(
      SCREENSHOTS_DIR,
      `${breakpoint.name}-${breakpoint.width}x${breakpoint.height}.png`
    );

    await page.screenshot({
      path: screenshotPath,
      fullPage: true,
    });
  }
}

async function saveDiscovery(discovery) {
  const filePath = path.join(OUTPUT_DIR, 'analysis', '01-discovery.md');
  await ensureDirectory(path.dirname(filePath));

  const content = `# Phase 1: Discovery Results

**Date**: ${discovery.timestamp}
**URL**: ${discovery.url}
**Title**: ${discovery.title}

## Navigation Structure

### Header Navigation
${discovery.navigation.header ? discovery.navigation.header.map(link => `- [${link.text}](${link.href})`).join('\n') : 'Not found'}

### Footer Navigation
${discovery.navigation.footer ? discovery.navigation.footer.map(link => `- [${link.text}](${link.href})`).join('\n') : 'Not found'}

## Sitemap
${discovery.sitemap ? `Found at: ${discovery.sitemap}` : 'Not found'}

## Notes
- Website is protected by Cloudflare
- Requires JavaScript execution for full content
`;

  await fs.writeFile(filePath, content, 'utf8');
  console.log(`Discovery results saved to: ${filePath}`);
}

async function saveContent(content) {
  const filePath = path.join(OUTPUT_DIR, 'analysis', '07-content-analysis.md');
  await ensureDirectory(path.dirname(filePath));

  const headingsByLevel = {
    h1: content.headings.filter(h => h.level === 'H1'),
    h2: content.headings.filter(h => h.level === 'H2'),
    h3: content.headings.filter(h => h.level === 'H3'),
  };

  const mdContent = `# Phase 5: Content Analysis

## Meta Information
- **Title**: ${content.meta.title}
- **Description**: ${content.meta.description || 'Not set'}
- **Viewport**: ${content.meta.viewport || 'Not set'}

## Heading Structure

### H1 Headings
${headingsByLevel.h1.map(h => `- ${h.text}`).join('\n') || 'None found'}

### H2 Headings
${headingsByLevel.h2.map(h => `- ${h.text}`).join('\n') || 'None found'}

### H3 Headings
${headingsByLevel.h3.map(h => `- ${h.text}`).join('\n') || 'None found'}

## Links
Total links found: ${content.links.length}

## Images
Total images found: ${content.images.length}
${content.images.slice(0, 10).map(img => `- ${img.alt || 'No alt text'} (${img.src})`).join('\n')}
${content.images.length > 10 ? `\n... and ${content.images.length - 10} more` : ''}
`;

  await fs.writeFile(filePath, mdContent, 'utf8');
  console.log(`Content analysis saved to: ${filePath}`);
}

// Run the analysis
if (require.main === module) {
  analyzeWebsite().catch(console.error);
}

module.exports = { analyzeWebsite };

