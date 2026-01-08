"""
Blueprint Editor - Handles blueprint modifications
Supports add, edit, and remove operations on website components
"""

import json
import copy
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime


class BlueprintEditor:
    """
    Handles all blueprint modification operations.
    Works with the blueprint JSON structure to add, edit, and remove components.
    """
    
    def __init__(self):
        self.modification_history = []
    
    def get_component(self, blueprint: Dict[str, Any], component_type: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific component from the blueprint.
        
        Args:
            blueprint: The full blueprint dict
            component_type: Type of component (hero, about, menu, etc.)
            
        Returns:
            Component dict if found, None otherwise
        """
        components = blueprint.get("components", {})
        return components.get(component_type)
    
    def get_all_components(self, blueprint: Dict[str, Any]) -> List[str]:
        """Get list of all component types in the blueprint."""
        return list(blueprint.get("components", {}).keys())
    
    def get_component_order(self, blueprint: Dict[str, Any]) -> List[str]:
        """Get the order of components for rendering."""
        return blueprint.get("componentOrder", [])
    
    def edit_root_field(
        self, 
        blueprint: Dict[str, Any], 
        field_path: str, 
        new_value: Any
    ) -> Tuple[Dict[str, Any], bool, str]:
        """
        Edit a root-level field in the blueprint (not inside a component).
        
        Args:
            blueprint: The full blueprint dict
            field_path: Dot-notation path to field (e.g., "projectName" or "theme.colorPalette.primary")
            new_value: New value to set
            
        Returns:
            Tuple of (modified_blueprint, success, message)
        """
        modified = copy.deepcopy(blueprint)
        
        # Parse field path
        path_parts = field_path.split(".")
        
        try:
            # Navigate to parent of target field
            current = modified
            for part in path_parts[:-1]:
                if isinstance(current, dict):
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                else:
                    return blueprint, False, f"Invalid path: {field_path}"
            
            # Get old value for history
            final_key = path_parts[-1]
            old_value = current.get(final_key) if isinstance(current, dict) else None
            
            # Set new value
            if isinstance(current, dict):
                current[final_key] = new_value
            else:
                return blueprint, False, f"Cannot set value at path: {field_path}"
            
            # Record modification
            self.modification_history.append({
                "action": "edit_root",
                "field": field_path,
                "old_value": old_value,
                "new_value": new_value,
                "timestamp": datetime.now().isoformat()
            })
            
            return modified, True, f"Updated {field_path} to '{new_value}'"
            
        except Exception as e:
            return blueprint, False, f"Error editing root field: {str(e)}"

    
    def edit_component(
        self, 
        blueprint: Dict[str, Any], 
        component_type: str, 
        field_path: str, 
        new_value: Any
    ) -> Tuple[Dict[str, Any], bool, str]:
        """
        Edit a specific field within a component.
        
        Args:
            blueprint: The full blueprint dict (will be modified in place)
            component_type: Type of component to edit
            field_path: Dot-notation path to field (e.g., "props.headline")
            new_value: New value to set
            
        Returns:
            Tuple of (modified_blueprint, success, message)
        """
        # Create a deep copy to preserve original
        modified = copy.deepcopy(blueprint)
        
        components = modified.get("components", {})
        target_id = component_type
        
        # Resolve component ID if not found directly
        if component_type not in components:
            found = False
            # 1. Try adding 'comp-' prefix
            if f"comp-{component_type}" in components:
                target_id = f"comp-{component_type}"
                found = True
            # 2. Search for close matches in keys
            else:
                for key in components.keys():
                    if key.lower() == component_type.lower():
                        target_id = key
                        found = True
                        break
                    if key.endswith(f"-{component_type}"):
                        target_id = key
                        found = True
                        break
            
            # 3. 🆕 Search by 'type' field (e.g. comp-home -> type: Home)
            if not found:
                 clean_input = component_type.lower().replace("comp-", "")
                 for key, val in components.items():
                     c_type = val.get("type", "").lower()
                     if c_type == clean_input:
                         target_id = key
                         found = True
                         break
            
            if not found:
                return blueprint, False, f"Component '{component_type}' not found"
        
        component = components[target_id]
        
        # 🆕 Prop Aliasing (Handle common AI mismatches like ctaButton vs cta)
        props = component.get("props", {})
        parts = field_path.split(".")
        if len(parts) == 2 and parts[0] == "props":
             prop_name = parts[1]
             # CTA Aliases: Map to 'cta' if it exists and request is for alias
             if prop_name in ["ctaButton", "buttonText", "btnText", "actionButton"] and "cta" in props and prop_name not in props:
                 field_path = "props.cta"
             # Title Aliases
             elif prop_name in ["heading", "headline", "header"] and "title" in props and prop_name not in props:
                 field_path = "props.title"

        # Parse field path and navigate
        path_parts = field_path.split(".")
        current = component
        
        try:
            # Navigate to parent of target field
            for part in path_parts[:-1]:
                if isinstance(current, dict):
                    current = current.get(part, {})
                elif isinstance(current, list) and part.isdigit():
                    current = current[int(part)]
                else:
                    return blueprint, False, f"Invalid path: {field_path}"
            
            # Get old value for history
            final_key = path_parts[-1]
            old_value = current.get(final_key) if isinstance(current, dict) else None
            
            # Set new value
            if isinstance(current, dict):
                current[final_key] = new_value
            elif isinstance(current, list) and final_key.isdigit():
                current[int(final_key)] = new_value
            else:
                return blueprint, False, f"Cannot set value at path: {field_path}"
            
            # Record modification
            self.modification_history.append({
                "action": "edit",
                "component": target_id,
                "field": field_path,
                "old_value": old_value,
                "new_value": new_value,
                "timestamp": datetime.now().isoformat()
            })
            
            return modified, True, f"Updated {target_id}.{field_path}"
            
        except Exception as e:
            return blueprint, False, f"Error editing: {str(e)}"
    
    def add_component(
        self, 
        blueprint: Dict[str, Any], 
        component_type: str, 
        component_data: Dict[str, Any],
        position: Optional[int] = None
    ) -> Tuple[Dict[str, Any], bool, str]:
        """
        Add a new component to the blueprint.
        
        Args:
            blueprint: The full blueprint dict
            component_type: Type of component to add
            component_data: Component data including type and props
            position: Optional position in componentOrder (defaults to end)
            
        Returns:
            Tuple of (modified_blueprint, success, message)
        """
        modified = copy.deepcopy(blueprint)
        
        # Check if component already exists
        if component_type in modified.get("components", {}):
            return blueprint, False, f"Component '{component_type}' already exists. Use edit instead."
        
        # Ensure components dict exists
        if "components" not in modified:
            modified["components"] = {}
        
        # Add the component
        modified["components"][component_type] = component_data
        
        # Add to componentOrder
        if "componentOrder" not in modified:
            modified["componentOrder"] = []
        
        if position is not None and 0 <= position <= len(modified["componentOrder"]):
            modified["componentOrder"].insert(position, component_type)
        else:
            modified["componentOrder"].append(component_type)
        
        # Record modification
        self.modification_history.append({
            "action": "add",
            "component": component_type,
            "data": component_data,
            "position": position,
            "timestamp": datetime.now().isoformat()
        })
        
        return modified, True, f"Added new {component_type} section"
    
    def remove_component(
        self, 
        blueprint: Dict[str, Any], 
        component_type: str
    ) -> Tuple[Dict[str, Any], bool, str]:
        """
        Remove a component from the blueprint.
        
        Args:
            blueprint: The full blueprint dict
            component_type: Type of component to remove
            
        Returns:
            Tuple of (modified_blueprint, success, message)
        """
        modified = copy.deepcopy(blueprint)
        
        # Check if component exists
        if component_type not in modified.get("components", {}):
            return blueprint, False, f"Component '{component_type}' not found"
        
        # Store for history
        removed_data = modified["components"][component_type]
        
        # Remove from components
        del modified["components"][component_type]
        
        # Remove from componentOrder
        if component_type in modified.get("componentOrder", []):
            modified["componentOrder"].remove(component_type)
        
        # Record modification
        self.modification_history.append({
            "action": "remove",
            "component": component_type,
            "removed_data": removed_data,
            "timestamp": datetime.now().isoformat()
        })
        
        return modified, True, f"Removed {component_type} section"
    
    def get_modification_history(self) -> List[Dict[str, Any]]:
        """Get the history of modifications made in this session."""
        return self.modification_history
    
    def clear_history(self):
        """Clear the modification history."""
        self.modification_history = []
    
    def get_blueprint_summary(self, blueprint: Dict[str, Any]) -> str:
        """
        Generate a human-readable summary of the blueprint for AI context.
        
        Args:
            blueprint: The full blueprint dict
            
        Returns:
            String summary of the blueprint
        """
        summary_parts = []
        
        # Project info
        project_name = blueprint.get("projectName", "Unnamed Project")
        website_type = blueprint.get("websiteType", "unknown")
        summary_parts.append(f"Project: {project_name} ({website_type} website)")
        
        # Theme
        theme = blueprint.get("theme", {})
        colors = theme.get("colorPalette", {})
        if colors:
            summary_parts.append(f"Colors: Primary={colors.get('primary', 'N/A')}, Secondary={colors.get('secondary', 'N/A')}")
        
        # Components
        components = blueprint.get("components", {})
        component_order = blueprint.get("componentOrder", list(components.keys()))
        summary_parts.append(f"\nComponents ({len(components)} sections):")
        
        for comp_name in component_order:
            comp = components.get(comp_name, {})
            props = comp.get("props", {})
            
            # Get key info based on component type
            if comp_name == "hero":
                headline = props.get("headline", "")
                summary_parts.append(f"  - Hero: \"{headline[:50]}...\"" if len(headline) > 50 else f"  - Hero: \"{headline}\"")
            elif comp_name == "about":
                title = props.get("title", "About")
                summary_parts.append(f"  - About: \"{title}\"")
            elif comp_name == "menu":
                categories = props.get("categories", [])
                summary_parts.append(f"  - Menu: {len(categories)} categories")
            elif comp_name == "gallery":
                images = props.get("images", [])
                summary_parts.append(f"  - Gallery: {len(images)} images")
            elif comp_name == "testimonials":
                items = props.get("testimonials", [])
                summary_parts.append(f"  - Testimonials: {len(items)} reviews")
            elif comp_name == "contact":
                summary_parts.append(f"  - Contact section")
            elif comp_name == "footer":
                summary_parts.append(f"  - Footer")
            else:
                summary_parts.append(f"  - {comp_name.title()}")
        
        return "\n".join(summary_parts)
    
    def validate_blueprint(self, blueprint: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate that blueprint has required structure.
        
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []
        
        if not blueprint:
            return False, ["Blueprint is empty"]
        
        if "projectName" not in blueprint:
            issues.append("Missing projectName")
        
        if "components" not in blueprint:
            issues.append("Missing components section")
        elif not isinstance(blueprint["components"], dict):
            issues.append("Components must be a dictionary")
        
        if "componentOrder" not in blueprint:
            issues.append("Missing componentOrder")
        
        return len(issues) == 0, issues
