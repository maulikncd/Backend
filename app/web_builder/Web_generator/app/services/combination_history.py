"""
Combination History Service

Tracks which template variants have been used to prevent repetition.
Ensures each generation gets unique layouts for premium feel.
"""

import json
import random
from typing import Dict, List, Any, Optional
from pathlib import Path


class CombinationHistory:
    """
    Tracks template combination usage to avoid repetition.
    Each category (hero, features, nav, etc.) maintains its own history.
    """
    
    def __init__(self, history_file: str = None):
        """Initialize with optional persistence file."""
        if history_file:
            self.history_file = Path(history_file)
        else:
            # Default to same directory as this file
            self.history_file = Path(__file__).parent / ".template_history.json"
        
        self._history: Dict[str, List[str]] = {}
        self._max_history = 10  # Keep last 10 choices per category
        self._load_history()
    
    def _load_history(self):
        """Load history from file if exists."""
        try:
            if self.history_file.exists():
                with open(self.history_file, "r") as f:
                    self._history = json.load(f)
        except (json.JSONDecodeError, IOError):
            self._history = {}
    
    def _save_history(self):
        """Save history to file."""
        try:
            with open(self.history_file, "w") as f:
                json.dump(self._history, f, indent=2)
        except IOError:
            pass  # Fail silently if can't write
    
    def get_unused_choice(self, category: str, options: List[str], prefer_new: bool = True) -> str:
        """
        Get a choice from options that hasn't been used recently.
        
        Args:
            category: Category name (e.g., "hero_layouts", "nav_styles")
            options: List of available options
            prefer_new: If True, prefer unused options over recently used
            
        Returns:
            Selected option string
        """
        if not options:
            return "default"
        
        # Get history for this category
        used = self._history.get(category, [])
        
        # Find unused options
        unused = [opt for opt in options if opt not in used]
        
        if unused and prefer_new:
            # Pick random from unused
            choice = random.choice(unused)
        else:
            # All have been used, reset and pick from all
            # But prefer ones used longest ago (at start of list)
            if used:
                # Get least recently used that's still valid
                valid_old = [opt for opt in used if opt in options]
                if valid_old:
                    choice = valid_old[0]  # Oldest used
                else:
                    choice = random.choice(options)
            else:
                choice = random.choice(options)
        
        # Record this choice
        self._record_choice(category, choice)
        
        return choice
    
    def _record_choice(self, category: str, choice: str):
        """Record a choice in history."""
        if category not in self._history:
            self._history[category] = []
        
        # Remove if already exists (to move to end)
        if choice in self._history[category]:
            self._history[category].remove(choice)
        
        # Add to end (most recent)
        self._history[category].append(choice)
        
        # Trim to max history
        if len(self._history[category]) > self._max_history:
            self._history[category] = self._history[category][-self._max_history:]
        
        # Save to file
        self._save_history()
    
    def record_generation(self, project_id: str, combination: Dict[str, str]):
        """
        Record a complete generation's combination for a project.
        
        Args:
            project_id: Unique project identifier
            combination: Dict mapping category to chosen variant
        """
        # Record each choice in its category
        for category, choice in combination.items():
            self._record_choice(category, choice)
    
    def get_history(self, category: str) -> List[str]:
        """Get history for a category."""
        return self._history.get(category, [])
    
    def clear_category(self, category: str):
        """Clear history for a specific category."""
        if category in self._history:
            del self._history[category]
            self._save_history()
    
    def clear_all(self):
        """Clear all history."""
        self._history = {}
        self._save_history()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get usage statistics."""
        return {
            "categories": list(self._history.keys()),
            "total_tracked": sum(len(v) for v in self._history.values()),
            "per_category": {k: len(v) for k, v in self._history.items()}
        }


# Singleton instance
combination_history = CombinationHistory()
