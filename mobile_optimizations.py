#!/usr/bin/env python3
import re
import json

# Read the current HTML file
with open('/Users/pranjalbharti/Documents/GitHub/pranjal-s-potfolio/index.html', 'r') as f:
    html_content = f.read()

# Extract the template JSON
template_match = re.search(r'<script type="__bundler/template">([\s\S]*?)</script>', html_content)
if not template_match:
    print("Error: Could not find template script")
    exit()

json_str = template_match.group(1).strip()
template_data = json.loads(json_str)

# The template data contains the full HTML - we need to modify it
full_html = template_data

# 1. Add overflow-x: hidden to html and body
full_html = re.sub(
    r'<html><head>',
    '<html><head><style>html, body { overflow-x: hidden; }</style>',
    full_html
)

# 2. Update the responsive CSS with tablet breakpoint and new mobile requirements
new_responsive_css = """
<style id="__responsive">
/* ===== Mobile optimization (auto-injected) ===== */
html{-webkit-text-size-adjust:100%;}
body { overflow-x: hidden; }
img,svg,video{max-width:100%; overflow-x: hidden; }
.nav-burger{display:none;}
@media (max-width:860px){
  nav{padding:14px 20px !important;}
  .nav-burger{display:flex !important;}
  .nav-links{display:none !important; position:absolute; top:100%; left:0; right:0;
    flex-direction:column !important; align-items:stretch !important; gap:2px !important;
    background:#f4ecdd; padding:10px 20px 20px !important;
    border-bottom:1px solid rgba(20,35,74,.12); box-shadow:0 22px 34px rgba(20,35,74,.14);}
  nav.nav-open .nav-links{display:flex !important;}
  .nav-links a{padding:13px 8px !important; font-size:17px !important;}
  .nav-links a.btn{margin-top:12px; text-align:center; padding:14px 22px !important;}

  header{padding:44px 20px 60px !important;}
  section{padding-left:20px !important; padding-right:20px !important;}
  section[style*="padding:72px"], section[style*="padding:90px"]{padding-top:56px !important; padding-bottom:56px !important;}
  footer{padding:32px 20px !important; flex-direction:column !important; justify-content:center !important; text-align:center;}

  h1[style*="font:500 74px"]{font-size:clamp(34px,8vw,42px) !important; line-height:1.08 !important; max-width:90vw;}
  [style*="font:500 56px"], [style*="font:500 54px"], [style*="font:500 52px"]{font-size:clamp(28px,8vw,36px) !important; line-height:1.1 !important;}
  [style*="font:600 52px"]{font-size:36px !important;}
  [style*="font:500 38px"]{font-size:26px !important;}
  header p, [style*="font:400 19px"]{font-size:17px !important;}

  [style*="repeat(2,1fr)"], [style*="repeat(3,1fr)"], [style*="grid-template-columns:1fr 1fr"]{grid-template-columns:1fr !important;}
  [style*="repeat(4,1fr)"]{grid-template-columns:repeat(2,1fr) !important; gap:28px 16px !important;}
  [style*="grid-template-columns:200px 1fr"]{grid-template-columns:1fr !important; gap:6px !important;}

  div[style*="gap:16px; margin-top:40px"], div[style*="gap:16px; margin-top:38px"]{flex-wrap:wrap; justify-content:center;}
}
@media (max-width:768px){
  /* Tablet breakpoint */
  section{padding-left:28px !important; padding-right:28px !important;}
  section[style*="padding:72px"], section[style*="padding:90px"], section[style*="padding:40px"]{padding-top:28px !important; padding-bottom:28px !important;}

  [style*="repeat(2,1fr)"], [style*="repeat(3,1fr)"], [style*="grid-template-columns:1fr 1fr"]{grid-template-columns:1fr !important;}
  [style*="repeat(4,1fr)"]{grid-template-columns:repeat(2,1fr) !important; gap:28px 16px !important;}
  [style*="grid-template-columns:200px 1fr"]{grid-template-columns:1fr !important; gap:6px !important;}

  h1[style*="font:500 74px"]{font-size:clamp(42px,9vw,56px) !important; line-height:1.1 !important;}
  [style*="font:500 56px"], [style*="font:500 54px"], [style*="font:500 52px"]{font-size:clamp(32px,8.5vw,44px) !important; line-height:1.12 !important;}
  [style*="font:600 52px"]{font-size:42px !important;}
  [style*="font:500 38px"]{font-size:32px !important;}

  /* Hero photo and CTA button layout */
  [style*="max-width:300px"]{max-width:120px !important;}
  .hero-buttons > div{display: inline-flex !important; gap: 12px; white-space: nowrap !important;}
  .hero-buttons .btn{padding: 14px 24px !important; min-width: auto !important;}

  /* Credibility strip */
  .hero-strip{margin-top: 8px !important; font-size: 12px !important; letter-spacing: 0.05em !important; color: #666 !important; text-transform: uppercase !important;}
}
@media (max-width:480px){
  /* Small mobile breakpoint */
  section{padding-left:16px !important; padding-right:16px !important;}
  section[style*="repeat(4,1fr)"]{grid-template-columns:1fr !important; gap:20px !important;}

  [style*="grid-template-columns:repeat(2,1fr)"]{grid-template-columns:1fr !important; gap:20px !important;}
  [style*="grid-template-columns:repeat(3,1fr)"], [style*="repeat(3,1fr)"]{grid-template-columns:1fr !important; gap:16px !important;}

  h1[style*="font:500 74px"]{font-size:clamp(30px,7vw,38px) !important; line-height:1.08 !important;}
  [style*="font:500 56px"], [style*="font:500 54px"], [style*="font:500 52px"]{font-size:clamp(26px,7vw,32px) !important; line-height:1.1 !important;}
  [style*="font:600 52px"]{font-size:32px !important;}
  [style*="font:500 38px"]{font-size:24px !important;}

  /* Impact stats - 2 columns */
  [style*="repeat(4,1fr)"]:not([style*="grid-template-columns"]){grid-template-columns: repeat(2, 1fr) !important; gap: 16px !important;}

  /* Card heading fixes */
  .card h3{font-size:19px !important; padding: 20px 16px 16px 16px !important; word-break: break-word !important; overflow-wrap: break-word !important;}

  /* Where I've worked - stack dates above roles */
  .work-item > div:nth-child(1), .work-item > div:nth-child(2){text-align: left !important; margin-bottom: 4px !important;}
  .work-item > div:nth-child(2){font-size:16px !important; font-weight:400 !important;}

  /* Hero spacing */
  header{padding:20px 20px 32px !important;}
  .hero-content > div{margin-bottom: 16px !important;}
  .hero-content > div:last-child{margin-bottom: 0 !important;}
}
@media (max-width:400px){
  [style*="repeat(4,1fr)"]{grid-template-columns:1fr !important;}
  nav a[style*="font:600 22px"]{font-size:19px !important;}
}
</style>
"""

# Find where the old responsive style starts and ends
responsive_start = full_html.find('<style id="__responsive">')
if responsive_start == -1:
    print("Error: Could not find responsive CSS start")
    exit()

responsive_end = full_html.find('</style>', responsive_start + 1)
if responsive_end == -1:
    print("Error: Could not find responsive CSS end")
    exit()

# Replace the responsive CSS
full_html = full_html[:responsive_start] + new_responsive_css + full_html[responsive_end:]

# 3. Clamp font sizes in inline styles - use safe string operations
def replace_font_inline(match):
    style = match.group(1)
    # Find font-size values
    def clamp_size(m):
        size = int(m.group(1))
        if size >= 74:
            return f'font-size: clamp({size-16}px, 8vw, {size-24}px)'
        elif size >= 52:
            return f'font-size: clamp({size-16}px, 8vw, {size-12}px)'
        elif size >= 38:
            return f'font-size: clamp({size-10}px, 8vw, {size-6}px)'
        return m.group(0)
    new_style = re.sub(r'font-size:\s*(\d{2,})px', clamp_size, style)
    return f'style="{new_style}"'

full_html = re.sub(r'style="([^"]*font-size:\s*\d{2,}px[^"]*)"', replace_font_inline, full_html)

# 4. Add credibility strip after hero buttons (find the Say hello button location)
say_hello_pattern = r'(<button[^>]*>Say hello</button>)'
hero_buttons_match = re.search(say_hello_pattern, full_html)
if hero_buttons_match:
    insertion_point = hero_buttons_match.end()
    credibility_html = '''<div class="hero-strip">Forbes India Top 200 · 13K+ community · 50+ media features</div>'''
    full_html = full_html[:insertion_point] + credibility_html + full_html[insertion_point:]

# 5. Add max-width wrapper to hero section to prevent glow overflow
hero_pattern = r'(<section[^>]*>[\s\S]*?<h1[^>]*>[^<]*</h1>[\s\S]*?</section>)'
def wrap_hero(match):
    hero_section = match.group(1)
    # Check if it has the gradient background
    if 'linear-gradient(' in hero_section and 'position: relative' in hero_section:
        return '<div style="max-width: 100vw; overflow: hidden;">' + hero_section + '</div>'
    return match.group()
full_html = re.sub(hero_pattern, wrap_hero, full_html)

# Update the HTML in the template data
template_data = full_html

# Re-encode and update the HTML file
new_html = html_content.replace(json_str, json.dumps(template_data))

# Write the updated file
with open('/Users/pranjalbharti/Documents/GitHub/pranjal-s-potfolio/index.html', 'w') as f:
    f.write(new_html)

print("Mobile optimizations applied successfully!")
print("File size:", len(new_html), "characters")