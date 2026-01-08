from typing import Dict, Any
import random

from .variant_cyber_link import render as render_cyber
from .variant_mega_links import render as render_mega
from .variant_newsletter import render as render_newsletter
from .variant_glass_footer import render as render_glass
from .variant_minimal_dark import render as render_minimal
from .variant_mega_footer import render as render_mega_full
from .variant_neon_grid import render as render_neon
from .variant_split_footer import render as render_split
from .variant_animated import render as render_animated
from .variant_stats_footer import render as render_stats

class GamingFooterTemplates:
    VARIANTS = [
        "cyber-link", "mega-links", "newsletter",
        "glass-footer", "minimal-dark", "mega-footer", 
        "neon-grid", "split-footer", "animated", "stats-footer"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "cyber-link": render_cyber,
            "mega-links": render_mega,
            "newsletter": render_newsletter,
            "glass-footer": render_glass,
            "minimal-dark": render_minimal,
            "mega-footer": render_mega_full,
            "neon-grid": render_neon,
            "split-footer": render_split,
            "animated": render_animated,
            "stats-footer": render_stats
        }
        return dispatch.get(variant, render_cyber)(props, colors)
