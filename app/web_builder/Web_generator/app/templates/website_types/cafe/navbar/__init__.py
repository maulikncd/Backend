from typing import Dict, Any
import random

# Premium Variants (New - Rich & Modern)
from .variant_glassmorphic_premium import render as render_glassmorphic_premium
from .variant_floating_modern import render as render_floating_modern
from .variant_luxury_elegant import render as render_luxury_elegant

# Existing Variants
from .variant_transparent_elegant import render as render_transparent_elegant
from .variant_floating_pill import render as render_floating_pill
from .variant_aura_clean import render as render_aura_clean
from .variant_dark_overlay import render as render_dark_overlay
from .variant_centered_logo import render as render_centered_logo
from .variant_underline_anim import render as render_underline_anim
from .variant_sidebar_toggle import render as render_sidebar_toggle
from .variant_split_bar import render as render_split_bar
from .variant_boxed_pill import render as render_boxed_pill
from .variant_minimal_line import render as render_minimal_line

class CafeNavbarTemplates:
    """Modular Navbar Templates for Cafe - Premium Variants"""
    
    # Premium variants listed first for higher selection priority
    VARIANTS = [
        # ⭐ Premium Variants (New - Use these primarily)
        "glassmorphic-premium",
        "floating-modern",
        "luxury-elegant",
        # Standard Variants
        "transparent-elegant",
        "floating-pill",
        "aura-clean",
        "dark-overlay",
        "centered-logo",
        "underline-anim",
        "sidebar-toggle",
        "split-bar",
        "boxed-pill",
        "minimal-line"
    ]
    
    # Only use premium variants for new generations
    PREMIUM_VARIANTS = [
        "glassmorphic-premium",
        "floating-modern", 
        "luxury-elegant"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            # Prefer premium variants (70% chance)
            if random.random() < 0.7:
                variant = random.choice(cls.PREMIUM_VARIANTS)
            else:
                variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            # Premium
            "glassmorphic-premium": render_glassmorphic_premium,
            "floating-modern": render_floating_modern,
            "luxury-elegant": render_luxury_elegant,
            # Standard
            "transparent-elegant": render_transparent_elegant,
            "floating-pill": render_floating_pill,
            "aura-clean": render_aura_clean,
            "dark-overlay": render_dark_overlay,
            "centered-logo": render_centered_logo,
            "underline-anim": render_underline_anim,
            "sidebar-toggle": render_sidebar_toggle,
            "split-bar": render_split_bar,
            "boxed-pill": render_boxed_pill,
            "minimal-line": render_minimal_line
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        # Default to premium glassmorphic
        return render_glassmorphic_premium(props, colors)
