from typing import Dict, Any
import random

from .variant_grid import render as render_grid
from .variant_featured import render as render_featured
from .variant_card_grid import render as render_cards
from .variant_carousel import render as render_carousel
from .variant_pricing import render as render_pricing
from .variant_bundles import render as render_bundles
from .variant_flash_sale import render as render_flash
from .variant_coins import render as render_coins
from .variant_season_pass import render as render_pass
from .variant_skins import render as render_skins

class GamingStoreTemplates:
    VARIANTS = [
        "grid", "featured", "card-grid", "carousel", "pricing",
        "bundles", "flash-sale", "coins", "season-pass", "skins"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "grid": render_grid,
            "featured": render_featured,
            "card-grid": render_cards,
            "carousel": render_carousel,
            "pricing": render_pricing,
            "bundles": render_bundles,
            "flash-sale": render_flash,
            "coins": render_coins,
            "season-pass": render_pass,
            "skins": render_skins
        }
        return dispatch.get(variant, render_grid)(props, colors)
