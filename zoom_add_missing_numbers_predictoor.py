import re

INPUT_FILE = "existing.txt"
OUTPUT_FILE = "expanded.txt"

# Explicit Unicode-aware regex (Python 3 is Unicode by default,
# but re.UNICODE makes intent crystal clear)
digit_pattern = re.compile(r"\d{2}", re.UNICODE)

bases = set()

# Read input as UTF-8, tolerate BOM, normalize newlines
with open(INPUT_FILE, "r", encoding="utf-8-sig", errors="replace") as f:
    for line in f:
        domain = line.strip()
        if not domain:
            continue

        match = digit_pattern.search(domain)
        if not match:
            continue

        base = domain[:match.start()] + "{}" + domain[match.end():]
        bases.add(base)

expanded = []

# Generate 00–09
for base in sorted(bases):
    for i in range(10):
        expanded.append(base.replace("{}", f"{i:02d}", 1))

# Write output as UTF-8
with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(expanded))

print(f"Generated {len(expanded)} domains -> {OUTPUT_FILE}")
