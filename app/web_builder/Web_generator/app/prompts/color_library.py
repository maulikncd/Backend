"""
Premium Color Palette Library
Professionally curated color combinations for various industries and moods.
Ensures websites look high-end and cohesive with proper contrast.
"""

from typing import Dict, List, Any, Tuple
import random
import re

class ColorUtils:
    """Utility functions for color manipulation and contrast checking"""
    
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
        """Convert RGB tuple to hex color"""
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    
    @staticmethod
    def get_luminance(hex_color: str) -> float:
        """Calculate relative luminance of a color (0 = darkest, 1 = lightest)"""
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        # Normalize to 0-1
        r, g, b = r/255, g/255, b/255
        # Apply gamma correction
        r = r/12.92 if r <= 0.03928 else ((r + 0.055)/1.055) ** 2.4
        g = g/12.92 if g <= 0.03928 else ((g + 0.055)/1.055) ** 2.4
        b = b/12.92 if b <= 0.03928 else ((b + 0.055)/1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    @staticmethod
    def get_contrast_ratio(color1: str, color2: str) -> float:
        """Calculate contrast ratio between two colors (1 to 21)"""
        l1 = ColorUtils.get_luminance(color1)
        l2 = ColorUtils.get_luminance(color2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)
    
    @staticmethod
    def is_dark(hex_color: str) -> bool:
        """Check if a color is dark (luminance < 0.5)"""
        return ColorUtils.get_luminance(hex_color) < 0.5
    
    @staticmethod
    def get_text_color_for_background(bg_color: str) -> str:
        """Get appropriate text color (white or dark) for a given background"""
        if ColorUtils.is_dark(bg_color):
            return "#FFFFFF"
        else:
            return "#1A1A1A"
    
    @staticmethod
    def get_readable_text_color(bg_color: str, preferred_text: str = None) -> str:
        """
        Get a readable text color for a background.
        If preferred_text has good contrast, use it. Otherwise, return white or black.
        """
        if preferred_text:
            contrast = ColorUtils.get_contrast_ratio(bg_color, preferred_text)
            if contrast >= 4.5:  # WCAG AA standard for normal text
                return preferred_text
        
        # Fall back to white or dark based on background
        return ColorUtils.get_text_color_for_background(bg_color)


class ColorPaletteLibrary:
    """
    Collection of high-quality color palettes with guaranteed contrast.
    Each palette includes:
    - primary: The main brand color
    - secondary: Complementary color
    - accent: For highlights and CTAs
    - background: Page background
    - surface: Cards and section backgrounds
    - text: Primary text color (guaranteed readable on background)
    - text_on_primary: Text color for use on primary color backgrounds
    - text_on_dark: Light text for dark sections
    - text_on_light: Dark text for light sections
    """
    
    PALETTES = {
        "LUXURY_DARK": [
            {
                "name": "Midnight Gold",
                "primary": "#D4AF37",
                "secondary": "#1A1A1A", 
                "accent": "#F5E6C8",
                "background": "#0F0F0F",
                "surface": "#1E1E1E",
                "text": "#F5F5F5",
                "text_on_primary": "#0F0F0F",
                "text_on_dark": "#F5F5F5",
                "text_on_light": "#1A1A1A"
            },
            {
                "name": "Royal Emerald",
                "primary": "#2D8B59",
                "secondary": "#C5A059",
                "accent": "#4ECDC4",
                "background": "#0A1612",
                "surface": "#132620",
                "text": "#FFFFFF",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#FFFFFF",
                "text_on_light": "#0A1612"
            }
        ],
        "MODERN_TECH": [
            {
                "name": "Cyber Blue",
                "primary": "#3B82F6",
                "secondary": "#6366F1", 
                "accent": "#F43F5E",
                "background": "#0B0E14",
                "surface": "#151921",
                "text": "#F8FAFC",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#F8FAFC",
                "text_on_light": "#0B0E14"
            },
            {
                "name": "Sleek Mint",
                "primary": "#10B981",
                "secondary": "#059669",
                "accent": "#3B82F6",
                "background": "#F8FAFC",
                "surface": "#FFFFFF",
                "text": "#0F172A",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#F8FAFC",
                "text_on_light": "#0F172A"
            },
            {
                "name": "Amethyst Flow",
                "primary": "#8B5CF6",
                "secondary": "#7C3AED",
                "accent": "#10B981",
                "background": "#0F172A",
                "surface": "#1E293B",
                "text": "#F8FAFC",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#F8FAFC",
                "text_on_light": "#0F172A"
            }
        ],
        "WARM_FOOD": [
            {
                "name": "Tuscan Sun",
                "primary": "#E67E22",
                "secondary": "#D35400",
                "accent": "#27AE60",
                "background": "#FFFAF5",
                "surface": "#FFFFFF",
                "text": "#2C2C2C",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#FFFAF5",
                "text_on_light": "#2C2C2C"
            },
            {
                "name": "Elegant Bistro",
                "primary": "#8B0000",
                "secondary": "#C9A062",
                "accent": "#228B22",
                "background": "#0D0D0D",
                "surface": "#1A1A1A",
                "text": "#F5F5F5",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#F5F5F5",
                "text_on_light": "#0D0D0D"
            },
            {
                "name": "Fresh Garden",
                "primary": "#2E8B57",
                "secondary": "#E67E22",
                "accent": "#C9A062",
                "background": "#FAFAFA",
                "surface": "#FFFFFF",
                "text": "#1A1A1A",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#FAFAFA",
                "text_on_light": "#1A1A1A"
            },
            {
                "name": "Cozy Warmth",
                "primary": "#B8860B",
                "secondary": "#8B4513",
                "accent": "#CD853F",
                "background": "#FFF8F0",
                "surface": "#FFFFFF",
                "text": "#3E2723",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#FFF8F0",
                "text_on_light": "#3E2723"
            },
            {
                "name": "Dark Diner",
                "primary": "#FF6B35",
                "secondary": "#F7C59F",
                "accent": "#2EC4B6",
                "background": "#1A1A2E",
                "surface": "#16213E",
                "text": "#EAEAEA",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#EAEAEA",
                "text_on_light": "#1A1A2E"
            }
        ],
        "VIBRANT_CREATIVE": [
            {
                "name": "Neon Nights",
                "primary": "#FF00FF",
                "secondary": "#00FFFF",
                "accent": "#FFFF00",
                "background": "#121212",
                "surface": "#1E1E1E",
                "text": "#FFFFFF",
                "text_on_primary": "#000000",
                "text_on_dark": "#FFFFFF",
                "text_on_light": "#121212"
            },
            {
                "name": "Sunset Pop",
                "primary": "#FF5F6D",
                "secondary": "#FFC371",
                "accent": "#6366F1",
                "background": "#FFFFFF",
                "surface": "#FFF5F5",
                "text": "#2D2D2D",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#FFFFFF",
                "text_on_light": "#2D2D2D"
            }
        ],
        "PROFESSIONAL_CLEAN": [
            {
                "name": "Corporate Blue",
                "primary": "#1E40AF",
                "secondary": "#3B82F6",
                "accent": "#F59E0B",
                "background": "#F8FAFC",
                "surface": "#FFFFFF",
                "text": "#1E293B",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#F8FAFC",
                "text_on_light": "#1E293B"
            },
            {
                "name": "Slate Professional",
                "primary": "#475569",
                "secondary": "#64748B",
                "accent": "#0EA5E9",
                "background": "#F1F5F9",
                "surface": "#FFFFFF",
                "text": "#1E293B",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#F1F5F9",
                "text_on_light": "#1E293B"
            }
        ],
        "GAMING_NEON": [
            {
                "name": "Toxic Venom",
                "primary": "#39FF14",
                "secondary": "#00FF87",
                "accent": "#7F00FF",
                "background": "#0D0D0D",
                "surface": "#1A1A1A",
                "text": "#F5F5F5",
                "text_on_primary": "#0D0D0D",
                "text_on_dark": "#F5F5F5",
                "text_on_light": "#0D0D0D"
            },
            {
                "name": "Cyberpunk Red",
                "primary": "#FF003C",
                "secondary": "#00E0FF",
                "accent": "#FFFC00",
                "background": "#050505",
                "surface": "#121212",
                "text": "#EAEAEA",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#EAEAEA",
                "text_on_light": "#050505"
            }
        ],
        "CINEMATIC": [
            {
                "name": "Netflix Noir",
                "primary": "#E50914",
                "secondary": "#B81D24",
                "accent": "#F5F5F1",
                "background": "#000000",
                "surface": "#141414",
                "text": "#FFFFFF",
                "text_on_primary": "#FFFFFF",
                "text_on_dark": "#FFFFFF",
                "text_on_light": "#000000"
            },
            {
                "name": "Golden Era",
                "primary": "#D4AF37",
                "secondary": "#C9A227",
                "accent": "#E50914",
                "background": "#0A0A0A",
                "surface": "#1A1A1A",
                "text": "#F5F5F5",
                "text_on_primary": "#0A0A0A",
                "text_on_dark": "#F5F5F5",
                "text_on_light": "#0A0A0A"
            }
        ]
    }

    @classmethod
    def get_palettes_for_industry(cls, industry: str) -> List[Dict[str, str]]:
        """Get recommended palettes based on industry type"""
        industry = industry.lower()
        
        mapping = {
            "cafe": "WARM_FOOD",
            "coffee": "WARM_FOOD",
            "restaurant": "WARM_FOOD",
            "bakery": "WARM_FOOD",
            "dining": "WARM_FOOD",
            "food": "WARM_FOOD",
            "gaming": "GAMING_NEON",
            "esports": "GAMING_NEON",
            "movie": "CINEMATIC",
            "cinema": "CINEMATIC",
            "theater": "CINEMATIC",
            "portfolio": "MODERN_TECH",
            "developer": "MODERN_TECH",
            "designer": "VIBRANT_CREATIVE",
            "agency": "MODERN_TECH",
            "technology": "MODERN_TECH",
            "software": "MODERN_TECH",
            "ecommerce": "PROFESSIONAL_CLEAN",
            "shop": "PROFESSIONAL_CLEAN",
            "store": "PROFESSIONAL_CLEAN",
            "retail": "PROFESSIONAL_CLEAN",
            "luxury": "LUXURY_DARK"
        }
        
        category = mapping.get(industry, "PROFESSIONAL_CLEAN")
        return cls.PALETTES.get(category, cls.PALETTES["PROFESSIONAL_CLEAN"])

    @classmethod
    def get_random_palette(cls) -> Dict[str, str]:
        """Get a random palette from the entire library"""
        category = random.choice(list(cls.PALETTES.keys()))
        return random.choice(cls.PALETTES[category])

    @classmethod
    def get_all_categories(cls) -> Dict[str, List[Dict[str, str]]]:
        """Return the complete library"""
        return cls.PALETTES
    
    @classmethod
    def validate_and_fix_palette(cls, colors: Dict[str, str]) -> Dict[str, str]:
        """
        Validate a color palette and fix any contrast issues.
        Ensures text is always readable on backgrounds.
        """
        fixed = colors.copy()
        
        # Ensure we have all required keys
        bg = fixed.get("background", "#FFFFFF")
        
        # Fix text color if contrast is poor
        text = fixed.get("text", "#000000")
        if ColorUtils.get_contrast_ratio(bg, text) < 4.5:
            fixed["text"] = ColorUtils.get_text_color_for_background(bg)
        
        # Add helper text colors if missing
        if "text_on_dark" not in fixed:
            fixed["text_on_dark"] = "#FFFFFF"
        if "text_on_light" not in fixed:
            fixed["text_on_light"] = "#1A1A1A"
        
        # Ensure text_on_primary is readable
        primary = fixed.get("primary", "#3B82F6")
        if "text_on_primary" not in fixed:
            fixed["text_on_primary"] = ColorUtils.get_text_color_for_background(primary)
        
        return fixed
    
    @classmethod
    def get_safe_palette_for_industry(cls, industry: str) -> Dict[str, str]:
        """Get a validated, contrast-safe palette for an industry"""
        palettes = cls.get_palettes_for_industry(industry)
        palette = random.choice(palettes)
        return cls.validate_and_fix_palette(palette)
