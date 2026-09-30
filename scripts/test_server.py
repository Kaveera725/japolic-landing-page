import urllib.request
import re

urls = [
    'http://localhost:3000/index.html',
    'http://localhost:3000/direction.html',
    'http://localhost:3000/components.html',
    'http://localhost:3000/landing.css',
    'http://localhost:3000/tokens.css',
    'http://localhost:3000/components.css'
]

all_ok = True
for url in urls:
    try:
        resp = urllib.request.urlopen(url)
        content_len = len(resp.read())
        print(f"PASS: {url} -> Status {resp.status} ({content_len} bytes)")
    except Exception as e:
        print(f"FAIL: {url} -> {e}")
        all_ok = False

print("\n--- Cross-file Link Audit ---")
for filename in ['direction.html', 'components.html']:
    with open(filename, 'r', encoding='utf-8') as fp:
        html = fp.read()
    links = re.findall(r'href="([^"]+)"', html)
    print(f"{filename} links: {sorted(list(set(links)))}")

if all_ok:
    print("\nALL URLS SERVING PERFECTLY (200 OK).")
else:
    print("\nSOME URLS FAILED.")
