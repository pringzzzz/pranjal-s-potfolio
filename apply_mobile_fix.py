#!/usr/bin/env python3
import re
import json

# Read the current HTML file
with open('/Users/pranjalbharti/Documents/GitHub/pranjal-s-potfolio/index.html', 'r') as f:
    content = f.read()

# Find the template script tag
template_match = re.search(r'<script type="__bundler/template">([\s\S]*?)</script>', content)
if not template_match:
    print("ERROR: Could not find template script")
    exit(1)

# Get the raw JSON string from the script tag
raw_json = template_match.group(1).strip()

# Parse the JSON to get the HTML string
html = json.loads(raw_json)
print(f"Loaded template HTML: {len(html)} chars")

# ============================================
# Apply optimizations
# ============================================

# 1. Replace the responsive CSS block with enhanced version
old_css = re.search(r'<style id="__responsive">[\s\S]*?</style>', html)
if not old_css:
    print("ERROR: Could not find responsive CSS")
    exit(1)

new_css = '''<style id="__responsive">
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

  /* Hero photo size */
  [style*="max-width:300px"]{max-width:120px !important;}
  /* Hero buttons - side by side */
  .hero-buttons > div{display: inline-flex !important; gap: 12px; white-space: nowrap !important;}
  .hero-buttons .btn{padding: 14px 24px !important; min-width: auto !important;}

  /* Credibility strip */
  .hero-strip{margin-top: 8px !important; font-size: 12px !important; letter-spacing: 0.05em !important; color: #666 !important; text-transform: uppercase !important;}
}
@media (max-width:480px){
  /* Small mobile - impact grid to 2 columns */
  section{padding-left:16px !important; padding-right:16px !important;}
  [style*="repeat(4,1fr)"]:not([style*="grid-template-columns"]){grid-template-columns:repeat(2,1fr) !important; gap:16px !important;}

  /* Single-column grids */
  [style*="repeat(2,1fr)"], [style*="repeat(3,1fr)"], [style*="grid-template-columns:1fr 1fr"]{grid-template-columns:1fr !important;}
  [style*="repeat(4,1fr)"]{grid-template-columns:1fr !important; gap:20px !important;}
  [style*="grid-template-columns:200px 1fr"]{grid-template-columns:1fr !important; gap:6px !important;}

  h1[style*="font:500 74px"]{font-size:clamp(30px,7vw,38px) !important; line-height:1.08 !important;}
  [style*="font:500 56px"], [style*="font:500 54px"], [style*="font:500 52px"]{font-size:clamp(26px,7vw,32px) !important; line-height:1.1 !important;}
  [style*="font:600 52px"]{font-size:32px !important;}
  [style*="font:500 38px"]{font-size:24px !important;}

  /* Card heading fixes */
  .card h3{font-size:19px !important; padding:20px 16px 16px 16px !important; word-break:break-word !important; overflow-wrap:break-word !important;}

  /* Work section - stack dates above roles */
  .work-item > div:nth-child(1), .work-item > div:nth-child(2){text-align:left !important; margin-bottom:4px !important;}
  .work-item > div:nth-child(2){font-size:16px !important; font-weight:400 !important;}

  /* Hero spacing */
  header{padding:20px 20px 32px !important;}
}
@media (max-width:400px){
  [style*="repeat(4,1fr)"]{grid-template-columns:1fr !important;}
  nav a[style*="font:600 22px"]{font-size:19px !important;}
}
</style>'''

html = html[:old_css.start()] + new_css + html[old_css.end():]
print("✓ Updated responsive CSS")

# 2. Add credibility strip after "Say hello" button
# Find buttons in the HTML
buttons = re.findall(r'<button[^>]*>([^<]+)</button>', html)
print(f"Found {len(buttons)} buttons: {[b.strip() for b in buttons]}")

say_hello = re.search(r'<button[^>]*>\s*Say hello\s*</button>', html)
if say_hello:
    strip = '<div class="hero-strip">Forbes India Top 200 · 13K+ community · 50+ media features</div>'
    html = html[:say_hello.end()] + strip + html[say_hello.end():]
    print("✓ Added credibility strip")
else:
    print("✗ Could not find Say hello button")

# 3. Wrap hero section
# Find sections with gradient backgrounds
sections_with_gradient = re.findall(r'<section[^>]*>[^<]*<h1[^>]*>[^<]+</h1>', html, re.DOTALL)
if sections_with_gradient:
    print(f"✓ Found {len(sections_with_gradient)} section(s) with h1")

# Serialize back to JSON
new_json = json.dumps(html)
new_content = content.replace(raw_json, new_json)

# Write back
with open('/Users/pranjalbharti/Documents/GitHub/pranjal-s-potfolio/index.html', 'w') as f:
    f.write(new_content)

print(f"\n✓ File updated: {len(new_content)} bytes")

# Verify the JSON is still valid
with open('/Users/pranjalbharti/Documents/GitHub/pranjal-s-potfolio/index.html', 'r') as f:
    verify_content = f.read()

m2 = re.search(r'<script type="__bundler/template">([\s\S]*?)</script>', verify_content)
if m2:
    try:
        verify_html = json.loads(m2.group(1).strip())
        print("✓ Verification: Template JSON is valid")

        checks = [
            ("@media (max-width:768px)", "Tablet breakpoint at 768px"),
            ("@media (max-width:480px)", "Small mobile breakpoint at 480px"),
            ("overflow-x: hidden", "Overflow hidden on body"),
            ("Forbes India Top 200", "Credibility strip text"),
        ]
        for check, desc in checks:
            if check in verify_html:
                print(f"  ✓ {desc}")
            else:
                print(f"  ✗ MISSING: {desc}")
    except Exception as e:
        print(f"✗ ERROR: Template JSON invalid after update: {e}")
        exit(1)
