from typing import Dict, Any
import random

# Import all variants
from .variant_developer_spotlight import render as render_developer_spotlight
from .variant_creative_agency import render as render_creative_agency
from .variant_minimal_elegance import render as render_minimal_elegance
from .variant_gradient_mesh import render as render_gradient_mesh
from .variant_3d_perspective import render as render_3d_perspective
from .variant_split_showcase import render as render_split_showcase


class PortfolioHeroTemplates:
    """Portfolio-specific hero sections with 6 premium variants"""
    
    VARIANTS = [
        "developer-spotlight",
        "creative-agency",
        "minimal-elegance",
        "gradient-mesh",
        "3d-perspective",
        "split-showcase"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        """Render a hero section using the specified or random variant"""
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "developer-spotlight": render_developer_spotlight,
            "creative-agency": render_creative_agency,
            "minimal-elegance": render_minimal_elegance,
            "gradient-mesh": render_gradient_mesh,
            "3d-perspective": render_3d_perspective,
            "split-showcase": render_split_showcase
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        # Fallback to first variant
        return render_developer_spotlight(props, colors)
