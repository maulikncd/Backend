from typing import Dict, Any
import random

from .variant_carousel import render as render_carousel
from .variant_grid_showcase import render as render_grid
from .variant_featured_hero import render as render_featured
from .variant_card_stack import render as render_stack
from .variant_horizontal_rows import render as render_rows
from .variant_masonry import render as render_masonry
from .variant_list_view import render as render_list
from .variant_bento_games import render as render_bento
from .variant_3d_cards import render as render_3d
from .variant_spotlight import render as render_spotlight

class GamingGamesTemplates:
    VARIANTS = [
        "carousel", "grid-showcase", "featured-hero", "card-stack",
        "horizontal-rows", "masonry", "list-view", "bento-games",
        "3d-cards", "spotlight"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "carousel": render_carousel,
            "grid-showcase": render_grid,
            "featured-hero": render_featured,
            "card-stack": render_stack,
            "horizontal-rows": render_rows,
            "masonry": render_masonry,
            "list-view": render_list,
            "bento-games": render_bento,
            "3d-cards": render_3d,
            "spotlight": render_spotlight
        }
        return dispatch.get(variant, render_carousel)(props, colors)
