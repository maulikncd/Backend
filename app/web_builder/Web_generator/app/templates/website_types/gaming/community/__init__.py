from typing import Dict, Any
import random

from .variant_discord_hub import render as render_discord

class GamingCommunityTemplates:
    VARIANTS = ["discord-hub"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        return render_discord(props, colors)
