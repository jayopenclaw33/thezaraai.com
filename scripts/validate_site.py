#!/usr/bin/env python3
"""Dependency-light validation for the static TheZaraAI website."""
from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse, unquote
import json, re, sys
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'thezaraai.com'
errors: list[str] = []
warnings: list[str] = []

def target_for(path: str, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme in ('mailto', 'tel', 'javascript', 'data') or href.startswith('#'):
        return None
    if parsed.scheme and parsed.netloc not in (DOMAIN, 'www.' + DOMAIN):
        return None
    target_path = unquote(parsed.path)
    if not target_path:
        return ROOT / 'index.html'
    if target_path.startswith('/'):
        candidate = ROOT / target_path.lstrip('/')
    else:
        candidate = path.parent / target_path
    if candidate.is_dir() or target_path.endswith('/'):
        candidate = candidate / 'index.html'
    return candidate

def value(soup, tag, **attrs):
    node = soup.find(tag, attrs=attrs)
    return node.get('content') if node and node.has_attr('content') else (node.get('href') if node else None)

for page in sorted(ROOT.rglob('*.html')):
    rel = page.relative_to(ROOT)
    text = page.read_text(errors='replace')
    soup = BeautifulSoup(text, 'html.parser')
    noindex = 'noindex' in (value(soup, 'meta', name='robots') or '')
    banner = str(rel) == 'free-agent-course/linkedin-banner.html'
    if not noindex and not banner:
        title = soup.title.get_text(' ', strip=True) if soup.title else ''
        description = value(soup, 'meta', name='description') or ''
        canonical = value(soup, 'link', rel='canonical') or ''
        h1_count = len(soup.find_all('h1'))
        for label, actual in [('title', title), ('description', description), ('canonical', canonical), ('og:title', value(soup, 'meta', property='og:title')), ('twitter:card', value(soup, 'meta', name='twitter:card'))]:
            if not actual:
                errors.append(f'{rel}: missing {label}')
        if h1_count != 1:
            errors.append(f'{rel}: expected one h1, found {h1_count}')
        if title and len(title) > 60:
            warnings.append(f'{rel}: title is {len(title)} characters')
        if description and len(description) > 160:
            warnings.append(f'{rel}: meta description is {len(description)} characters')
        if canonical and not canonical.startswith('https://thezaraai.com/'):
            errors.append(f'{rel}: non-canonical host: {canonical}')
    for img in soup.find_all('img'):
        if not img.has_attr('alt'):
            errors.append(f'{rel}: img without alt: {img.get("src", "unknown")}')
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        if href == '#':
            errors.append(f'{rel}: placeholder link #')
            continue
        target = target_for(page, href)
        if target is not None and not target.exists():
            errors.append(f'{rel}: broken internal link {href} -> {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}')
    for script in soup.find_all('script', attrs={'type':'application/ld+json'}):
        payload = script.get_text(strip=True)
        try:
            data = json.loads(payload)
        except json.JSONDecodeError as exc:
            errors.append(f'{rel}: invalid JSON-LD: {exc.msg}')
            continue
        graph = data.get('@graph', [data]) if isinstance(data, dict) else []
        for node in graph:
            if node.get('@type') == 'FAQPage':
                visible = soup.get_text(' ', strip=True)
                for item in node.get('mainEntity', []):
                    question = item.get('name', '')
                    if question and question not in visible:
                        errors.append(f'{rel}: FAQ schema question not visible: {question}')

# Ensure all URLs in sitemap map to actual static files.
sitemap = ROOT/'sitemap.xml'
if sitemap.exists():
    for loc in re.findall(r'<loc>(.*?)</loc>', sitemap.read_text()):
        target = target_for(ROOT/'index.html', loc)
        if target is not None and not target.exists():
            errors.append(f'sitemap.xml: URL does not map to a file: {loc}')

print(f'Validated {len(list(ROOT.rglob("*.html")))} HTML files.')
if warnings:
    print('\nWarnings:')
    print('\n'.join(f'- {item}' for item in warnings))
if errors:
    print('\nErrors:')
    print('\n'.join(f'- {item}' for item in errors))
    sys.exit(1)
print('Validation passed with no errors.')
