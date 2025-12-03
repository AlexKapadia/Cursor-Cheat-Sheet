#!/usr/bin/env python3
"""
Lusano Website Extractor
Extracts HTML, CSS, and design elements for MDC conversion
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin, urlparse


class LusanoExtractor:
    def __init__(self, base_url="https://www.lusano.com/"):
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
        """Detect technology stack from HTML"""
        self.technology_stack = {}
        
        # Check for React
        if soup.find('script', string=re.compile(r'React|react')):
            self.technology_stack['framework'] = 'React'
        elif soup.find('script', src=re.compile(r'react')):
            self.technology_stack['framework'] = 'React'
        
        # Check for Vue
        if soup.find('script', string=re.compile(r'Vue|vue')):
            self.technology_stack['framework'] = 'Vue'
        elif soup.find('script', src=re.compile(r'vue')):
            self.technology_stack['framework'] = 'Vue'
        
        # Check for Next.js
        if soup.find('script', src=re.compile(r'next')):
            self.technology_stack['framework'] = 'Next.js'
        
        # Check for CSS frameworks
        css_links = soup.find_all('link', rel='stylesheet')
        for link in css_links:
            href = link.get('href', '')
            if 'tailwind' in href.lower():
                self.technology_stack['css_framework'] = 'Tailwind CSS'
            elif 'bootstrap' in href.lower():
                self.technology_stack['css_framework'] = 'Bootstrap'
            elif 'material' in href.lower():
                self.technology_stack['css_framework'] = 'Material UI'
        
        # Check for JavaScript libraries
        scripts = soup.find_all('script', src=True)
        libraries = []
        for script in scripts:
            src = script.get('src', '')
            if 'jquery' in src.lower():
                libraries.append('jQuery')
            elif 'gsap' in src.lower():
                libraries.append('GSAP')
            elif 'framer' in src.lower():
                libraries.append('Framer Motion')
        
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
        
        # From link tags (Google Fonts, etc.)
        font_links = soup.find_all('link', href=re.compile(r'fonts\.(googleapis|gstatic)'))
        for link in font_links:
            href = link.get('href', '')
            if 'family=' in href:
                fonts = re.findall(r'family=([^&]+)', href)
                for font in fonts:
                    font = font.replace('+', ' ')
                    self.design_elements['fonts'].add(font)
    
    def extract_breakpoints(self, css_content):
        """Extract media query breakpoints"""
        # Find media queries
        media_pattern = r'@media\s+[^{]*\([^)]*(\d+)px[^)]*\)'
        breakpoints = re.findall(media_pattern, css_content)
        for bp in breakpoints:
            self.design_elements['breakpoints'].add(int(bp))
    
    def discover_pages(self, soup):
        """Discover pages from navigation and links"""
        # Find navigation links
        nav_links = soup.find_all('a', href=True)
        for link in nav_links:
            href = link.get('href', '')
            if href:
                full_url = urljoin(self.base_url, href)
                parsed = urlparse(full_url)
                if parsed.netloc == urlparse(self.base_url).netloc:
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
    extractor = LusanoExtractor()
    results = extractor.analyze_homepage()
    
    if results:
        print("\n=== Technology Stack ===")
        print(json.dumps(results['technology_stack'], indent=2))
        
        print("\n=== Design Elements ===")
        print(json.dumps(results['design_elements'], indent=2))
        
        print("\n=== Discovered Pages ===")
        for page in results['pages']:
            print(page)
        
        # Save HTML
        with open('lusano-homepage.html', 'w', encoding='utf-8') as f:
            f.write(str(results['soup']))
        
        # Save CSS
        with open('lusano-styles.css', 'w', encoding='utf-8') as f:
            f.write(results['css'])






