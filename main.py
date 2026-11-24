import os

LINE = "Her knuckles split on the last bolt, the gasket seats on the second try, and after three days the engine catches and holds."

# Assert single line of 1-240 characters
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert 1 <= len(LINE) <= 240, f"entry length {len(LINE)} out of range 1-240"

# Create /output if needed
os.makedirs("/output", exist_ok=True)

# Deliberately no trailing newline: /output/entry.txt is the raw entry text, so a
# final '\n' would be a phantom character that is not part of the line. newline=""
# keeps write() byte-identical to LINE (UTF-8).
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Print the line
print(LINE)