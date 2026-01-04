# ============================================
# 🔺 Triangle Pattern Cheat Sheet (Python)
# ============================================

rows = 5  # You can change this value for larger/smaller triangles

# --------------------------------------------
# 1. Solid Right-Angled Triangle (Left-Aligned)
# --------------------------------------------
for i in range(1, rows + 1):
    print("* " * i)

# --------------------------------------------
# 2. Solid Right-Angled Triangle (Right-Aligned)
# --------------------------------------------
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# --------------------------------------------
# 3. Inverted Right-Angled Triangle (Left-Aligned)
# --------------------------------------------
for i in range(rows, 0, -1):
    print("* " * i)

# --------------------------------------------
# 4. Inverted Right-Angled Triangle (Right-Aligned)
# --------------------------------------------
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

# --------------------------------------------
# 5. Equilateral Triangle
# --------------------------------------------
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# --------------------------------------------
# 6. Inverted Equilateral Triangle
# --------------------------------------------
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)

# --------------------------------------------
# 7. Hollow Right-Angled Triangle
# --------------------------------------------
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# --------------------------------------------
# 8. Hollow Equilateral Triangle
# --------------------------------------------
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# Diamond Pattern in Python

rows = 5  # You can change this value to adjust the size of the diamond

# Top half of the diamond (equilateral triangle)
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Bottom half of the diamond (inverted equilateral triangle)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

# ============================================
# 🔄 Triangle Operations
# ============================================

# --- Vertical Flip ---
# Reverse outer loop direction
# Example: from range(1, rows + 1) to range(rows, 0, -1)

# --- Horizontal Flip ---
# Adjust leading spaces
# Example: " " * (rows - i) ↔ " " * (i - 1)

# --- Rotate 90° Clockwise ---
for i in range(rows):
    for j in range(rows):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# --- Rotate 270° Counterclockwise ---
for i in range(rows):
    for j in range(rows):
        if j < rows - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    # ============================================
# 💎 Diamond Pattern with Operations (Python)
# ============================================

rows = 5  # You can change this value to resize the diamond

# -------------------------------
# 1. Solid Diamond Pattern
# -------------------------------
# Top half
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Bottom half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

# -------------------------------
# 2. Vertically Flipped Diamond
# -------------------------------
top = [(" " * (rows - i) + "* " * i) for i in range(1, rows + 1)]
bottom = [(" " * (rows - i) + "* " * i) for i in range(rows - 1, 0, -1)]

for line in reversed(top + bottom):
    print(line)

# -------------------------------
# 3. Horizontally Flipped Diamond
# -------------------------------
# Flip spacing logic
for i in range(1, rows + 1):
    print(" " * (i - 1) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (i - 1) + "* " * i)

# -------------------------------
# 4. Hollow Diamond Pattern
# -------------------------------
# Top half
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# Bottom half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# -------------------------------
# 5. Rotate Diamond 90° Clockwise (Advanced)
# -------------------------------
# Build diamond into a grid
grid = []
for i in range(1, rows + 1):
    grid.append((" " * (rows - i) + "* " * i).rstrip())
for i in range(rows - 1, 0, -1):
    grid.append((" " * (rows - i) + "* " * i).rstrip())

# Rotate and print
rotated = list(zip(*grid[::-1]))
for row in rotated:
    print("".join(row))

# ============================================
# 🧠 Tips
# ============================================
# - Replace "*" with numbers, emojis, or letters
# - Use input() to make it interactive
# - Combine flips and rotations for cool effects
# - Use time.sleep() for animation

# ============================================
# 🧠 Pro Tips
# ============================================
# - Use end="" to control line breaks
# - Replace "*" with numbers, emojis, or characters
# - Combine patterns for diamonds, pyramids, hourglasses
# - Use input() to make interactive triangle generators