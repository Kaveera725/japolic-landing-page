import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

all_ids = set(re.findall(r'id="([^"]+)"', html))
print("All defined IDs on page (count = %d):" % len(all_ids))
print(sorted(list(all_ids)))

all_hash_links = set(re.findall(r'href="#([^"]+)"', html))
print("\nAll hash links on page:")
print(sorted(list(all_hash_links)))

unmatched_hash_links = all_hash_links - all_ids
print("\nHash links without matching target ID:")
print(sorted(list(unmatched_hash_links)))
