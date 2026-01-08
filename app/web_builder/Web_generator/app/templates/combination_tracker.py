"""
Combination Tracker - Ensures unique template combinations
Prevents repetition across generations
"""

import os
import json
from typing import Dict, List, Set, Optional, Any
from datetime import datetime
import random


class CombinationTracker:
    """
    Tracks used template combinations to ensure variety.
    
    Features:
    - Stores last N generations per website type
    - Weighted selection (recently used = lower weight)
    - Auto-cleanup of old history
    """
    
    HISTORY_FILE = os.path.join(os.path.dirname(__file__), ".combination_history.json")
    MAX_HISTORY_PER_TYPE = 10  # Keep last 10 generations for uniqueness check
    
    _current_session_variants = {} # Temporary buffer for current generation
    
    @classmethod
    def start_session(cls):
        """Start a new generation session"""
        cls._current_session_variants = {}
    
    @classmethod
    def get_session_variants(cls) -> Dict[str, str]:
        """Get variants picked in current session"""
        return cls._current_session_variants
    
    @classmethod
    def load_history(cls) -> Dict[str, List[Dict]]:
        """Load combination history from file"""
        try:
            if os.path.exists(cls.HISTORY_FILE):
                with open(cls.HISTORY_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"[CombinationTracker] Load error: {e}")
        return {}
    
    @classmethod
    def save_history(cls, history: Dict[str, List[Dict]]) -> None:
        """Save combination history to file"""
        try:
            with open(cls.HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2)
        except Exception as e:
            print(f"[CombinationTracker] Save error: {e}")
    
    @classmethod
    def record_generation(cls, website_type: str, used_variants: Dict[str, str]) -> None:
        """
        Record a generation's template choices.
        
        Args:
            website_type: Type of website (cafe, gaming, etc.)
            used_variants: Dict of component_type -> variant_name
        """
        history = cls.load_history()
        
        if website_type not in history:
            history[website_type] = []
        
        # Add new record
        history[website_type].append({
            "timestamp": datetime.now().isoformat(),
            "variants": used_variants
        })
        
        # Keep only last N records
        history[website_type] = history[website_type][-cls.MAX_HISTORY_PER_TYPE:]
        
        cls.save_history(history)
        print(f"[CombinationTracker] Recorded: {website_type} -> {list(used_variants.values())[:3]}...")
    
    @classmethod
    def get_recently_used(cls, website_type: str, component_type: str, lookback: int = 5) -> Set[str]:
        """
        Get variants used in recent generations.
        
        Args:
            website_type: Type of website
            component_type: Component type (hero, navbar, etc.)
            lookback: How many generations to look back
            
        Returns:
            Set of recently used variant names
        """
        history = cls.load_history()
        records = history.get(website_type, [])
        
        recent_variants = set()
        for record in records[-lookback:]:
            variant = record.get("variants", {}).get(component_type)
            if variant:
                recent_variants.add(variant)
        
        return recent_variants
    
    @classmethod
    def select_fresh_variant(
        cls,
        website_type: str,
        component_type: str,
        available_variants: List[str],
        lookback: int = 5
    ) -> str:
        """
        Select a variant that wasn't used recently.
        
        Args:
            website_type: Type of website
            component_type: Component type
            available_variants: List of all available variants
            lookback: How many generations to avoid
            
        Returns:
            Selected variant name
        """
        if not available_variants:
            return "default"
        
        # Get recently used
        recent = cls.get_recently_used(website_type, component_type, lookback)
        
        # Filter out recently used
        fresh = [v for v in available_variants if v not in recent]
        
        # If all variants were used recently, use any
        if not fresh:
            print(f"[CombinationTracker] All {component_type} variants used recently, selecting random")
            fresh = available_variants
        
        selected = random.choice(fresh)
        
        # Track in current session
        cls._current_session_variants[component_type] = selected
        
        print(f"[CombinationTracker] Selected {component_type}: '{selected}' (avoided: {recent})")
        return selected
    
    @classmethod
    def get_unique_combination(
        cls,
        website_type: str,
        component_variants: Dict[str, List[str]],
        lookback: int = 3
    ) -> Dict[str, str]:
        """
        Get a complete unique combination for all components.
        
        Args:
            website_type: Type of website
            component_variants: Dict of component_type -> list of variants
            lookback: How many generations to avoid
            
        Returns:
            Dict of component_type -> selected variant
        """
        combination = {}
        
        for component_type, variants in component_variants.items():
            combination[component_type] = cls.select_fresh_variant(
                website_type=website_type,
                component_type=component_type,
                available_variants=variants,
                lookback=lookback
            )
        
        return combination
    
    @classmethod
    def clear_history(cls, website_type: str = None) -> None:
        """Clear history for a type or all"""
        if website_type:
            history = cls.load_history()
            if website_type in history:
                del history[website_type]
                cls.save_history(history)
        else:
            if os.path.exists(cls.HISTORY_FILE):
                os.remove(cls.HISTORY_FILE)
    
    # ============================================================
    # WEBSITE UNIQUENESS VERIFICATION
    # ============================================================
    
    @classmethod
    def generate_combination_hash(cls, used_variants: Dict[str, str]) -> str:
        """
        Generate a hash representing the website's template combination.
        
        Args:
            used_variants: Dict of component_type -> variant_name
            
        Returns:
            String hash representing this unique combination
        """
        import hashlib
        
        # Sort keys for consistent hashing
        sorted_items = sorted(used_variants.items())
        combination_str = "|".join([f"{k}:{v}" for k, v in sorted_items])
        
        # Create a short hash
        hash_obj = hashlib.md5(combination_str.encode())
        return hash_obj.hexdigest()[:12]
    
    @classmethod
    def is_duplicate_combination(cls, website_type: str, used_variants: Dict[str, str], lookback: int = 10) -> bool:
        """
        Check if this exact combination was used in recent generations.
        
        Args:
            website_type: Type of website
            used_variants: Dict of component_type -> variant_name
            lookback: How many generations to check (default: 10)
            
        Returns:
            True if this is a duplicate, False if unique
        """
        history = cls.load_history()
        records = history.get(website_type, [])
        
        # Generate hash for current combination
        current_hash = cls.generate_combination_hash(used_variants)
        
        # Check against last N generations
        for record in records[-lookback:]:
            stored_variants = record.get("variants", {})
            stored_hash = cls.generate_combination_hash(stored_variants)
            
            if current_hash == stored_hash:
                print(f"[CombinationTracker] ⚠️ DUPLICATE detected! Hash: {current_hash}")
                return True
        
        print(f"[CombinationTracker] ✅ Unique combination. Hash: {current_hash}")
        return False
    
    @classmethod
    def get_unique_variants_avoiding_duplicates(
        cls,
        website_type: str,
        component_variants: Dict[str, List[str]],
        max_attempts: int = 5
    ) -> Dict[str, str]:
        """
        Get a complete unique combination that doesn't match any in last 10 generations.
        
        Args:
            website_type: Type of website
            component_variants: Dict of component_type -> list of variants
            max_attempts: How many times to try before giving up
            
        Returns:
            Dict of component_type -> selected variant (guaranteed unique if possible)
        """
        for attempt in range(max_attempts):
            # Use different lookback values to get more variety
            lookback = 3 + (attempt * 2)  # 3, 5, 7, 9, 11
            
            combination = cls.get_unique_combination(
                website_type=website_type,
                component_variants=component_variants,
                lookback=min(lookback, cls.MAX_HISTORY_PER_TYPE)
            )
            
            # Check if this exact combination exists
            if not cls.is_duplicate_combination(website_type, combination):
                print(f"[CombinationTracker] 🎯 Found unique combination on attempt {attempt + 1}")
                return combination
            
            print(f"[CombinationTracker] 🔄 Attempt {attempt + 1} produced duplicate, retrying...")
        
        # If all attempts failed, still return the last combination (with warning)
        print(f"[CombinationTracker] ⚠️ Could not find unique combination after {max_attempts} attempts")
        return combination
    
    @classmethod
    def get_generation_stats(cls, website_type: str = None) -> Dict[str, Any]:
        """
        Get statistics about generation history.
        
        Args:
            website_type: Optional - get stats for specific type, or all if None
            
        Returns:
            Dict with statistics
        """
        history = cls.load_history()
        
        if website_type:
            records = history.get(website_type, [])
            unique_hashes = set()
            for record in records:
                hash_val = cls.generate_combination_hash(record.get("variants", {}))
                unique_hashes.add(hash_val)
            
            return {
                "website_type": website_type,
                "total_generations": len(records),
                "unique_combinations": len(unique_hashes),
                "duplicate_rate": 1 - (len(unique_hashes) / max(len(records), 1))
            }
        else:
            stats = {}
            for wtype, records in history.items():
                unique_hashes = set()
                for record in records:
                    hash_val = cls.generate_combination_hash(record.get("variants", {}))
                    unique_hashes.add(hash_val)
                
                stats[wtype] = {
                    "total_generations": len(records),
                    "unique_combinations": len(unique_hashes),
                    "duplicate_rate": 1 - (len(unique_hashes) / max(len(records), 1))
                }
            
            return stats


# Export
__all__ = ["CombinationTracker"]
