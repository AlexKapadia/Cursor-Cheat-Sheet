#!/usr/bin/env python3
"""
Vogue UK Website Extractor
Extracts HTML, CSS, and design elements for MDC conversion
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin, urlparse
import time

class VogueExtractor:
    def __init__(self, base_url="https://www.vogue.co.uk/"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.discovered_pages = set()
        self.technology_stack = {}
        self.design_elements = {
            'colors': set(),
            'fonts': set(),
            'spacing': set(),
            'components': [],
            'animations': [],
            'breakpoints': set()
        }
    
    def fetch_page(self, url):
        """Fetch a page and return BeautifulSoup object"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def detect_technology_stack(self, soup):
        """Detect frontend framework, CSS framework, and libraries"""
        html_str = str(soup)
        
        # Detect React
        if 'react' in html_str.lower() or 'data-reactroot' in html_str:
            self.technology_stack['framework'] = 'React'
        
        # Detect Next.js
        if '__next' in html_str or 'next.js' in html_str.lower():
            self.technology_stack['framework'] = 'Next.js'
        
        # Detect Vue
        if 'vue' in html_str.lower() or 'data-v-' in html_str:
            self.technology_stack['framework'] = 'Vue'
        
        # Detect Angular
        if 'ng-' in html_str or 'angular' in html_str.lower():
            self.technology_stack['framework'] = 'Angular'
        
        # Detect CSS frameworks
        if 'tailwind' in html_str.lower():
            self.technology_stack['css_framework'] = 'Tailwind CSS'
        elif 'bootstrap' in html_str.lower():
            self.technology_stack['css_framework'] = 'Bootstrap'
        elif 'material' in html_str.lower():
            self.technology_stack['css_framework'] = 'Material UI'
        else:
            self.technology_stack['css_framework'] = 'Custom CSS'
        
        # Detect JavaScript libraries
        scripts = soup.find_all('script', src=True)
        libraries = []
        for script in scripts:
            src = script.get('src', '')
            if 'jquery' in src.lower():
                libraries.append('jQuery')
            if 'gsap' in src.lower():
                libraries.append('GSAP')
            if 'framer' in src.lower():
                libraries.append('Framer Motion')
            if 'three' in src.lower():
                libraries.append('Three.js')
        
        if libraries:
            self.technology_stack['libraries'] = libraries
    
    def extract_css(self, soup):
        """Extract CSS from stylesheets and inline styles"""
        css_content = []
        
        # Extract inline styles
        inline_styles = soup.find_all(style=True)
        for element in inline_styles:
            style = element.get('style', '')
            if style:
                css_content.append(f"/* Inline style from {element.name} */\n{style}\n")
        
        # Extract stylesheets
        stylesheets = soup.find_all('link', rel='stylesheet')
        for link in stylesheets:
            href = link.get('href', '')
            if href:
                full_url = urljoin(self.base_url, href)
                try:
                    response = self.session.get(full_url, timeout=5)
                    if response.status_code == 200:
                        css_content.append(f"/* Stylesheet: {href} */\n{response.text}\n")
                except:
                    pass
        
        # Extract style tags
        style_tags = soup.find_all('style')
        for style in style_tags:
            if style.string:
                css_content.append(f"/* Style tag */\n{style.string}\n")
        
        return '\n'.join(css_content)
    
    def extract_colors(self, css_content):
        """Extract color values from CSS"""
        # Hex colors
        hex_pattern = r'#([0-9a-fA-F]{3,6})\b'
        hex_colors = re.findall(hex_pattern, css_content)
        for color in hex_colors:
            self.design_elements['colors'].add(f"#{color}")
        
        # RGB colors
        rgb_pattern = r'rgba?\([^)]+\)'
        rgb_colors = re.findall(rgb_pattern, css_content)
        for color in rgb_colors:
            self.design_elements['colors'].add(color)
        
        # HSL colors
        hsl_pattern = r'hsla?\([^)]+\)'
        hsl_colors = re.findall(hsl_pattern, css_content)
        for color in hsl_colors:
            self.design_elements['colors'].add(color)
    
    def extract_fonts(self, soup, css_content):
        """Extract font families"""
        # From CSS
        font_pattern = r'font-family:\s*([^;]+)'
        fonts = re.findall(font_pattern, css_content)
        for font in fonts:
            # Clean up font string
            font = font.strip().strip('"').strip("'")
            if font:
                self.design_elements['fonts'].add(font)
        
        # From computed styles (would need browser automation for full accuracy)
    
    def extract_breakpoints(self, css_content):
        """Extract media query breakpoints"""
        breakpoint_pattern = r'@media\s+[^{]*\([^)]*(\d+)px[^)]*\)'
        breakpoints = re.findall(breakpoint_pattern, css_content)
        for bp in breakpoints:
            self.design_elements['breakpoints'].add(int(bp))
    
    def discover_pages(self, soup):
        """Discover pages from navigation and links"""
        # Find navigation menus
        nav_elements = soup.find_all(['nav', 'header', 'footer'])
        
        for nav in nav_elements:
            links = nav.find_all('a', href=True)
            for link in links:
                href = link.get('href', '')
                if href:
                    full_url = urljoin(self.base_url, href)
                    # Only include same-domain links
                    if urlparse(full_url).netloc == urlparse(self.base_url).netloc:
                        self.discovered_pages.add(full_url)
        
        # Limit to reasonable number for initial analysis
        return list(self.discovered_pages)[:20]
    
    def analyze_homepage(self):
        """Perform comprehensive analysis of homepage"""
        print("Fetching homepage...")
        soup = self.fetch_page(self.base_url)
        
        if not soup:
            return None
        
        print("Detecting technology stack...")
        self.detect_technology_stack(soup)
        
        print("Extracting CSS...")
        css_content = self.extract_css(soup)
        
        print("Extracting design elements...")
        self.extract_colors(css_content)
        self.extract_fonts(soup, css_content)
        self.extract_breakpoints(css_content)
        
        print("Discovering pages...")
        pages = self.discover_pages(soup)
        
        return {
            'soup': soup,
            'css': css_content,
            'pages': pages,
            'technology_stack': self.technology_stack,
            'design_elements': {
                'colors': list(self.design_elements['colors']),
                'fonts': list(self.design_elements['fonts']),
                'breakpoints': sorted(list(self.design_elements['breakpoints']))
            }
        }
    

if __name__ == "__main__":
    extractor = VogueExtractor()
    results = extractor.analyze_homepage()
    
    if results:
        print("\n=== Technology Stack ===")
        print(json.dumps(results['technology_stack'], indent=2))
        
        print("\n=== Design Elements ===")
        print(f"Colors found: {len(results['design_elements']['colors'])}")
        print(f"Fonts found: {len(results['design_elements']['fonts'])}")
        print(f"Breakpoints: {results['design_elements']['breakpoints']}")
        
        print(f"\n=== Pages Discovered: {len(results['pages'])} ===")
        for page in results['pages'][:10]:
            print(f"  - {page}")
        
        # Save HTML
        with open('vogue_homepage.html', 'w', encoding='utf-8') as f:
            f.write(str(results['soup']))
        
        # Save CSS
        with open('vogue_styles.css', 'w', encoding='utf-8') as f:
            f.write(results['css'])
        
        # Save analysis
        with open('vogue_analysis.json', 'w', encoding='utf-8') as f:
            json.dump({
                'technology_stack': results['technology_stack'],
                'design_elements': results['design_elements'],
                'pages': results['pages']
            }, f, indent=2)
        
        print("\nFiles saved:")
        print("  - vogue_homepage.html")
        print("  - vogue_styles.css")
        print("  - vogue_analysis.json")

