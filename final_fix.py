#!/usr/bin/env python3
"""Apply all mobile optimizations ASAP"""
import re, json

with open('index.html') as f:
    content = f.read()

# Parse template
m = re.search(r'<script type="__bundler/template">([\s\S]*?)</script>', content)
raw_json = m.group(1).strip()
html = json.loads(raw_json)

# 1. Add overflow-x: hidden
html = html.replace('<html><head>', '<html><head><style>html, body { overflow-x: hidden; }</style>')

# 2. Replace responsive CSS
old_css = re.search(r'<style id="__responsive">[\s\S]*?</style>', html).group()
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
  section{padding-left:28px !important; padding-right:28px !important;}
  section[style*="padding:72px"], section[style*="padding:90px"], section[style*="padding:40px"]{padding-top:28px !important; padding-bottom:28px !important;}
  [style*="repeat(2,1fr)"], [style*="repeat(3,1fr)"], [style*="grid-template-columns:1fr 1fr"]{grid-template-columns:1fr !important;}
  [style*="repeat(4,1fr)"]{grid-template-columns:repeat(2,1fr) !important; gap:28px 16px !important;}
  [style*="grid-template-columns:200px 1fr"]{grid-template-columns:1fr !important; gap:6px !important;}
  h1[style*="font:500 74px"]{font-size:clamp(42px,9vw,56px) !important; line-height:1.1 !important;}
  [style*="font:500 56px"], [style*="font:500 54px"], [style*="font:500 52px"]{font-size:clamp(32px,8.5vw,44px) !important; line-height:1.12 !important;}
  [style*="font:600 52px"]{font-size:42px !important;}
  [style*="font:500 38px"]{font-size:32px !important;}
  [style*="max-width:300px"]{max-width:120px !important;}
  .hero-buttons > div{display: inline-flex !important; gap: 12px; white-space: nowrap !important;}
  .hero-buttons .btn{padding: 14px 24px !important; min-width: auto !important;}
  .hero-strip{margin-top: 8px !important; font-size: 12px !important; letter-spacing: 0.05em !important; color: #666 !important; text-transform: uppercase !important;}
}
@media (max-width:480px){
  section{padding-left:16px !important; padding-right:16px !important;}
  [style*="repeat(4,1fr)"]:not([style*="grid-template-columns"]){grid-template-columns:repeat(2,1fr) !important; gap:16px !important;}
  [style*="repeat(2,1fr)"], [style*="repeat(3,1fr)"], [style*="grid-template-columns:1fr 1fr"]{grid-template-columns:1fr !important;}
  [style*="repeat(4,1fr)"]{grid-template-columns:1fr !important; gap:20px !important;}
  [style*="grid-template-columns:200px 1fr"]{grid-template-columns:1fr !important; gap:6px !important;}
  h1[style*="font:500 74px"]{font-size:clamp(30px,7vw,38px) !important; line-height:1.08 !important;}
  [style*="font:500 56px"], [style*="font:500 54px"], [style*="font:500 52px"]{font-size:clamp(26px,7vw,32px) !important; line-height:1.1 !important;}
  [style*="font:600 52px"]{font-size:32px !important;}
  [style*="font:500 38px"]{font-size:24px !important;}
  .card h3{font-size:19px !important; padding:20px 16px 16px 16px !important; word-break:break-word !important; overflow-wrap:break-word !important;}
  .work-item > div:nth-child(1), .work-item > div:nth-child(2){text-align:left !important; margin-bottom:4px !important;}
  .work-item > div:nth-child(2){font-size:16px !important; font-weight:400 !important;}
  header{padding:20px 20px 32px !important;}
}
@media (max-width:400px){[style*="repeat(4,1fr)"]{grid-template-columns:1fr !important; nav a[style*="font:600 22px"]{font-size:19px !important;}}}
</style>'''
html = html.replace(old_css, new_css)

# 3. Add credibility strip
if '<div class="hero-strip">' not in html:
    html = html.replace('</body>', '<div class="hero-strip">Forbes India Top 200 · 13K+ community · 50+ media features</div></body>')

# Write back
with open('index.html', 'w') as f:
    f.write(content.replace(raw_json, json.dumps(html)))

print("✓ Mobile optimizations applied!")