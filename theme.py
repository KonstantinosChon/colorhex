"""
colorhex.theme — CSS variable and theme generation
"""
from .colors import lighten, darken, complementary

def to_css_vars(palette: dict, prefix: str = "color") -> str:
    lines = [":root {"]
    for name, value in palette.items():
        lines.append(f"  --{prefix}-{name}: {value};")
    lines.append("}")
    return "\n".join(lines)

def generate_theme(primary: str) -> dict:
    return {
        "primary":          primary,
        "primary-light":    lighten(primary, 0.2),
        "primary-dark":     darken(primary, 0.2),
        "primary-lighter":  lighten(primary, 0.4),
        "primary-darker":   darken(primary, 0.4),
        "accent":           complementary(primary),
    }

def print_theme(primary: str) -> None:
    theme = generate_theme(primary)
    print(to_css_vars(theme))
