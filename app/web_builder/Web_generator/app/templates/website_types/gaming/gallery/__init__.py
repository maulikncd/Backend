from typing import Dict, Any
import random

from .variant_media_wall import render as render_media
from .variant_screenshot_grid import render as render_grid
from .variant_trailers import render as render_trailers
from .variant_masonry_grid import render as render_masonry
from .variant_lightbox import render as render_lightbox
from .variant_horizontal_scroll import render as render_scroll
from .variant_3d_cards import render as render_3d
from .variant_fullscreen_slider import render as render_fullscreen
from .variant_video_reel import render as render_video
from .variant_bento_layout import render as render_bento

class GamingGalleryTemplates:
    VARIANTS = [
        "media-wall", "screenshot-grid", "trailers",
        "masonry-grid", "lightbox", "horizontal-scroll", 
        "3d-cards", "fullscreen-slider", "video-reel", "bento-layout"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None: variant = random.choice(cls.VARIANTS)
        dispatch = {
            "media-wall": render_media,
            "screenshot-grid": render_grid,
            "trailers": render_trailers,
            "masonry-grid": render_masonry,
            "lightbox": render_lightbox,
            "horizontal-scroll": render_scroll,
            "3d-cards": render_3d,
            "fullscreen-slider": render_fullscreen,
            "video-reel": render_video,
            "bento-layout": render_bento
        }
        return dispatch.get(variant, render_media)(props, colors)
