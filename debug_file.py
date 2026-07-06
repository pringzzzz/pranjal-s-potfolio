#!/usr/bin/env python3
import re
import json

# Read the current HTML file
with open('/Users/pranjalbharti/Documents/GitHub/pranjal-s-potfolio/index.html', 'r') as f:
    content = f.read()

# Find the template script
template_match = re.search(r'<script type="__bundler/template">([\s\S]*?)</script>', content)
if not template_match:
    print("Error: Could not find template script")
    exit()

raw_json = template_match.group(1).strip()

print("=" * 50)
print("RAW JSON STRING ANALYSIS")
print("=" * 50)
print(f"Length: {len(raw_json)}")
print(f"First 200 characters: {repr(raw_json[:200])}")
print(f"Last 200 characters: {repr(raw_json[-200:])}")

print("\n" + "=" * 50)
print("CHECKING FOR UNTERMINATED STRINGS")
print("=" * 50)

# The json string should start with a quote and end with a quote
print(f"Starts with quote: {raw_json[0] == '\"'}")
print(f"Ends with quote: {raw_json[-1] == '\"'}")

# Check for quote count imbalance
quote_count = raw_json.count('"')
escaped_quotes = raw_json.count('\\"')
print(f"Total quotes: {quote_count}")
print(f"Escaped quotes: {escaped_quotes}")
print(f"Unescaped quotes: {quote_count - escaped_quotes}")

# Try to find where the issue is
if not raw_json.startswith('"') or not raw_json.endswith('"'):
    print("ERROR: JSON does not start and end with quotes!")
else:
    print("JSON string is properly quoted")
    # Try to find position where parsing fails
    for i in range(0, len(raw_json), 100):
        try:
            json.loads(raw_json[:i+100])
        except:
            print(f"Parse fails after {i+100} chars, context: {repr(raw_json[max(0,i-50):i+100])}")
            break
