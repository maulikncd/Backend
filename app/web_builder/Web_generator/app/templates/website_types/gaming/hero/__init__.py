from typing import Dict, Any
import random

from .variant_neon_cyber import render as render_neon
from .variant_glitch_effect import render as render_glitch
from .variant_particle_storm import render as render_particles
from .variant_game_showcase import render as render_showcase
from .variant_streamer_intro import render as render_streamer
from .variant_dark_tournament import render as render_tournament
from .variant_epic_cinematic import render as render_cinematic
from .variant_retro_arcade import render as render_retro
from .variant_esports_tournament import render as render_esports
from .variant_split_showcase import render as render_split
from .variant_parallax_layers import render as render_parallax
from .variant_card_showcase import render as render_cards

class GamingHeroTemplates:
    """Gaming-specific hero sections - 10 Premium Variants"""
    
    VARIANTS = [
        "neon-cyber",
        "glitch-effect",
        "particle-storm",
        "game-showcase",
        "streamer-intro",
        "dark-tournament",
        "epic-cinematic",
        "retro-arcade",
        "esports-tournament",
        "split-showcase"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
            
        dispatch = {
            "neon-cyber": render_neon,
            "glitch-effect": render_glitch,
            "particle-storm": render_particles,
            "game-showcase": render_showcase,
            "streamer-intro": render_streamer,
            "dark-tournament": render_tournament,
            "epic-cinematic": render_cinematic,
            "retro-arcade": render_retro,
            "esports-tournament": render_esports,
            "split-showcase": render_split
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
            
        return render_neon(props, colors)
