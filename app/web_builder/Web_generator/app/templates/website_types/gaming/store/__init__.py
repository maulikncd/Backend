from typing import Dict, Any
import random

from .variant_grid import render as render_grid

class GamingStoreTemplates:
    VARIANTS = ["grid"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        return render_grid(props, colors)
