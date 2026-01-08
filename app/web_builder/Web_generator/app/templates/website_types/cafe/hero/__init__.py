from typing import Dict, Any, List
import random

# Import all variants
from .variant_warm_welcome import render as render_warm_welcome
from .variant_coffee_steam import render as render_coffee_steam
from .variant_split_menu import render as render_split_menu
from .variant_cozy_atmosphere import render as render_cozy_atmosphere
from .variant_morning_fresh import render as render_morning_fresh
from .variant_rustic_charm import render as render_rustic_charm
from .variant_modern_minimal import render as render_modern_minimal
from .variant_full_bleed_food import render as render_full_bleed_food
from .variant_aura_premium import render as render_aura_premium
from .variant_dark_elegance import render as render_dark_elegance

class CafeHeroTemplates:
    """Cafe-specific hero sections in a modular structure"""
    
    VARIANTS = [
        "warm-welcome",
        "coffee-steam",
        "split-menu",
        "cozy-atmosphere",
        "morning-fresh",
        "rustic-charm",
        "modern-minimal",
        "full-bleed-food",
        "aura-premium",
        "dark-elegance"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        """Render a hero section using the specified or random variant"""
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        # Dispatch to the appropriate render function
        dispatch = {
            "warm-welcome": render_warm_welcome,
            "coffee-steam": render_coffee_steam,
            "split-menu": render_split_menu,
            "cozy-atmosphere": render_cozy_atmosphere,
            "morning-fresh": render_morning_fresh,
            "rustic-charm": render_rustic_charm,
            "modern-minimal": render_modern_minimal,
            "full-bleed-food": render_full_bleed_food,
            "aura-premium": render_aura_premium,
            "dark-elegance": render_dark_elegance
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
            
        # Fallback to first variant
        return render_warm_welcome(props, colors)
