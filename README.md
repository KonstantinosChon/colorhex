# colorhex

Lightweight Python utility for hex/RGB color conversion, palette generation, and CSS theme formatting.

## Installation

```bash
pip install colorhex
```

## Usage

```python
from colorhex import hex_to_rgb, rgb_to_hex, lighten, darken, generate_theme, print_theme

# Convert hex to RGB
print(hex_to_rgb("#ff5733"))   # (255, 87, 51)

# Lighten / darken
print(lighten("#ff5733", 0.3)) # "#ff9475"
print(darken("#ff5733", 0.2))  # "#cc4629"

# Generate a full CSS theme
print_theme("#3a86ff")
# :root {
#   --color-primary: #3a86ff;
#   --color-primary-light: #6ba4ff;
#   ...
# }
```

## API

| Function | Description |
|---|---|
| `hex_to_rgb(hex)` | Convert hex string to (r, g, b) tuple |
| `rgb_to_hex(r, g, b)` | Convert RGB values to hex string |
| `lighten(hex, factor)` | Lighten a color by factor (0.0–1.0) |
| `darken(hex, factor)` | Darken a color by factor (0.0–1.0) |
| `complementary(hex)` | Get the complementary color |
| `generate_palette(base, steps)` | Generate a gradient palette |
| `generate_theme(primary)` | Generate a full theme dict |
| `to_css_vars(palette, prefix)` | Format palette as CSS variables |

## License

MIT
