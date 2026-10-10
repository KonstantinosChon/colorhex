"""
colorhex.colors — hex/rgb color conversion utilities
"""

def hex_to_rgb(hex_color: str) -> tuple:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def lighten(hex_color: str, factor: float = 0.2) -> str:
    r, g, b = hex_to_rgb(hex_color)
    r = min(255, int(r + (255 - r) * factor))
    g = min(255, int(g + (255 - g) * factor))
    b = min(255, int(b + (255 - b) * factor))
    return rgb_to_hex(r, g, b)

def darken(hex_color: str, factor: float = 0.2) -> str:
    r, g, b = hex_to_rgb(hex_color)
    r = max(0, int(r * (1 - factor)))
    g = max(0, int(g * (1 - factor)))
    b = max(0, int(b * (1 - factor)))
    return rgb_to_hex(r, g, b)

def complementary(hex_color: str) -> str:
    r, g, b = hex_to_rgb(hex_color)
    return rgb_to_hex(255 - r, 255 - g, 255 - b)

def to_ansi(hex_color: str) -> str:
    r, g, b = hex_to_rgb(hex_color)
    return f"\033[38;2;{r};{g};{b}m"

def generate_palette(base: str, steps: int = 5) -> list:
    palette = []
    for i in range(steps):
        factor = i / (steps - 1)
        r, g, b = hex_to_rgb(base)
        r = int(r * (1 - factor) + 255 * factor)
        g = int(g * (1 - factor) + 255 * factor)
        b = int(b * (1 - factor) + 255 * factor)
        palette.append(rgb_to_hex(r, g, b))
    return palette
