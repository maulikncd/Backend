from typing import Dict, Any
import random

from .variant_minimal_cards import render as render_minimal
from .variant_bento_grid import render as render_bento
from .variant_case_studies import render as render_case
from .variant_featured_hero import render as render_featured
from .variant_horizontal_scroll import render as render_scroll
from .variant_list_style import render as render_list
from .variant_masonry import render as render_masonry
from .variant_alternating import render as render_alt
from .variant_filter_tabs import render as render_filter
from .variant_numbered import render as render_numbered

class PortfolioProjectsTemplates:
    VARIANTS = [
        "minimal-cards", "bento-grid", "case-studies", "featured-hero",
        "horizontal-scroll", "list-style", "masonry", "alternating",
        "filter-tabs", "numbered"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "minimal-cards": render_minimal,
            "bento-grid": render_bento,
            "case-studies": render_case,
            "featured-hero": render_featured,
            "horizontal-scroll": render_scroll,
            "list-style": render_list,
            "masonry": render_masonry,
            "alternating": render_alt,
            "filter-tabs": render_filter,
            "numbered": render_numbered
        }
        return dispatch.get(variant, render_minimal)(props, colors)
