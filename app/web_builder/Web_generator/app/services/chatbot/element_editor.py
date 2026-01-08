"""
Element Editor - Direct HTML element modifications
Handles text, style, color, and structural edits on specific elements
"""

import re
import json
from typing import Dict, Any, Optional, Tuple, List
from bs4 import BeautifulSoup
import copy


class ElementEditor:
    """
    Handles direct HTML element modifications.
    Works with the actual HTML content to edit specific elements.
    """
    
    # Supported CSS properties for style editing
    STYLE_PROPERTIES = [
        'color', 'background-color', 'background', 'font-size', 'font-weight',
        'padding', 'margin', 'border', 'border-radius', 'width', 'height',
        'display', 'opacity', 'text-align', 'font-family', 'line-height',
        'box-shadow', 'text-shadow', 'transform', 'transition',
        'flex', 'grid', 'gap', 'justify-content', 'align-items'
    ]
    
    # Color names to hex mapping
    COLOR_MAP = {
        'red': '#ef4444',
        'blue': '#3b82f6',
        'green': '#22c55e',
        'yellow': '#eab308',
        'purple': '#a855f7',
        'pink': '#ec4899',
        'orange': '#f97316',
        'white': '#ffffff',
        'black': '#000000',
        'gray': '#6b7280',
        'grey': '#6b7280',
        'cyan': '#06b6d4',
        'teal': '#14b8a6',
        'indigo': '#6366f1',
        'violet': '#8b5cf6',
        'gold': '#fbbf24',
        'silver': '#9ca3af',
        'brown': '#a16207',
        'navy': '#1e3a5a',
        'maroon': '#991b1b',
        'olive': '#65a30d',
        'lime': '#84cc16',
        'aqua': '#22d3ee',
        'coral': '#f97171',
        'salmon': '#fca5a5',
        'tan': '#c2a886',
    }
    
    def __init__(self):
        self.modification_log = []
    
    def parse_color(self, color_input: str) -> str:
        """
        Parse color input (name, hex, rgb) and return hex.
        """
        color_input = color_input.lower().strip()
        
        # Already a hex color
        if color_input.startswith('#'):
            return color_input
        
        # Named color
        if color_input in self.COLOR_MAP:
            return self.COLOR_MAP[color_input]
        
        # RGB format
        rgb_match = re.match(r'rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', color_input)
        if rgb_match:
            r, g, b = int(rgb_match.group(1)), int(rgb_match.group(2)), int(rgb_match.group(3))
            return f'#{r:02x}{g:02x}{b:02x}'
        
        # HSL format - approximate conversion
        hsl_match = re.match(r'hsl\s*\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)', color_input)
        if hsl_match:
            # Return as-is, CSS supports HSL
            return color_input
        
        # Return as-is if nothing matches (might be a valid CSS color)
        return color_input
    
    def find_element_by_selector(self, html: str, selector: Dict[str, Any]) -> Tuple[BeautifulSoup, Any]:
        """
        Find an element in HTML by various selectors.
        
        Args:
            html: HTML string
            selector: Dict with id, classes, tagName, text hints
            
        Returns:
            Tuple of (soup, element)
        """
        soup = BeautifulSoup(html, 'html.parser')
        element = None
        
        # 1. Try by ID first (most specific)
        if selector.get('id'):
            element = soup.find(id=selector['id'])
            if element:
                return soup, element
        
        # 2. Try by Tag + Text Content (High Specificity)
        # Prioritize this over class-only match to avoid hitting wrong element with same styles
        if selector.get('text'):
            search_text = selector['text'].strip()
            tag = selector.get('tagName', '').lower()
            
            # Find candidates with matching tag
            candidates = soup.find_all(tag) if tag else soup.find_all()
            
            for el in candidates:
                # Check Text Match (fuzzy inclusion)
                el_text = el.get_text().strip()
                if not el_text:
                    continue
                    
                # Match if search text is part of element text or vice versa (for short texts)
                if search_text in el_text or (len(el_text) < len(search_text) and el_text in search_text):
                    
                    # Verify Classes if provided (to be sure it's similar style)
                    if selector.get('classes'):
                        req_classes = selector['classes'].split() if isinstance(selector['classes'], str) else selector['classes']
                        el_classes = el.get('class', [])
                        # We allow partial class match but at least some should match
                        if req_classes and not any(c in el_classes for c in req_classes):
                            continue 
                            
                    return soup, el

        # 3. Try by Tag + Class combination (Fallback if text changed/not found)
        if selector.get('classes'):
            classes = selector['classes'].split() if isinstance(selector['classes'], str) else selector['classes']
            if classes:
                # Search for element containing these classes
                # Use a more robust check than the previous slice logic
                if selector.get('tagName'):
                    candidates = soup.find_all(selector['tagName'].lower())
                else:
                    candidates = soup.find_all()
                    
                for el in candidates:
                    el_classes = el.get('class', [])
                    # Match if it has the primary classes
                    if all(c in el_classes for c in classes[:2]): # Match first 2 classes at least
                        return soup, el
        
        # 4. Fallback to just tag (Least specific)
        if selector.get('tagName'):
            tag = selector['tagName'].lower()
            elements = soup.find_all(tag)
            if elements:
                return soup, elements[0]
        
        return soup, None
    
    def edit_text(
        self, 
        html: str, 
        selector: Dict[str, Any], 
        new_text: str
    ) -> Tuple[str, bool, str]:
        """
        Edit the text content of an element.
        
        Args:
            html: Full HTML string
            selector: Element selector info
            new_text: New text content
            
        Returns:
            Tuple of (modified_html, success, message)
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return html, False, "Could not find the element to edit"
            
            old_text = element.string or element.get_text()
            
            # For elements with only text content
            if element.string:
                element.string = new_text
            else:
                # For elements with mixed content, replace all text
                element.clear()
                element.string = new_text
            
            self.modification_log.append({
                'action': 'edit_text',
                'selector': selector,
                'old_value': old_text[:100],
                'new_value': new_text[:100]
            })
            
            return str(soup), True, f"Changed text from '{old_text[:30]}...' to '{new_text[:30]}...'"
            
        except Exception as e:
            return html, False, f"Error editing text: {str(e)}"
    
    def edit_color(
        self,
        html: str,
        selector: Dict[str, Any],
        color_type: str,  # 'text', 'background', 'border'
        new_color: str
    ) -> Tuple[str, bool, str]:
        """
        Edit the color of an element.
        
        Args:
            html: Full HTML string
            selector: Element selector info
            color_type: Type of color to change
            new_color: New color value
            
        Returns:
            Tuple of (modified_html, success, message)
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return html, False, "Could not find the element to edit"
            
            # Parse the color
            parsed_color = self.parse_color(new_color)
            
            # Get existing styles
            existing_style = element.get('style', '')
            style_dict = {}
            
            if existing_style:
                for item in existing_style.split(';'):
                    if ':' in item:
                        key, value = item.split(':', 1)
                        style_dict[key.strip()] = value.strip()
            
            # Determine CSS property
            if color_type == 'text':
                style_dict['color'] = parsed_color
            elif color_type == 'background':
                style_dict['background-color'] = parsed_color
            elif color_type == 'border':
                if 'border' in style_dict:
                    # Try to preserve border width/style
                    style_dict['border-color'] = parsed_color
                else:
                    style_dict['border'] = f'1px solid {parsed_color}'
            
            # Rebuild style string
            new_style = '; '.join(f'{k}: {v}' for k, v in style_dict.items())
            element['style'] = new_style
            
            self.modification_log.append({
                'action': 'edit_color',
                'selector': selector,
                'color_type': color_type,
                'new_color': parsed_color
            })
            
            return str(soup), True, f"Changed {color_type} color to {parsed_color}"
            
        except Exception as e:
            return html, False, f"Error editing color: {str(e)}"
    
    def edit_class(
        self,
        html: str,
        selector: Dict[str, Any],
        action: str,  # 'add', 'remove', 'replace'
        classes: str,
        replace_with: str = None
    ) -> Tuple[str, bool, str]:
        """
        Edit classes of an element.
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return html, False, "Could not find the element to edit"
            
            existing_classes = element.get('class', [])
            if isinstance(existing_classes, str):
                existing_classes = existing_classes.split()
            
            new_classes = classes.split()
            
            if action == 'add':
                existing_classes.extend([c for c in new_classes if c not in existing_classes])
            elif action == 'remove':
                existing_classes = [c for c in existing_classes if c not in new_classes]
            elif action == 'replace' and replace_with:
                replace_classes = replace_with.split()
                existing_classes = [replace_classes[0] if c == new_classes[0] else c for c in existing_classes]
            
            element['class'] = existing_classes
            
            return str(soup), True, f"Updated classes: {action} {classes}"
            
        except Exception as e:
            return html, False, f"Error editing classes: {str(e)}"
    
    def edit_style(
        self,
        html: str,
        selector: Dict[str, Any],
        property_name: str,
        value: str
    ) -> Tuple[str, bool, str]:
        """
        Edit a specific CSS style property.
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return html, False, "Could not find the element to edit"
            
            # Get existing styles
            existing_style = element.get('style', '')
            style_dict = {}
            
            if existing_style:
                for item in existing_style.split(';'):
                    if ':' in item:
                        key, val = item.split(':', 1)
                        style_dict[key.strip()] = val.strip()
            
            # Set new property
            style_dict[property_name] = value
            
            # Rebuild style string
            new_style = '; '.join(f'{k}: {v}' for k, v in style_dict.items())
            element['style'] = new_style
            
            return str(soup), True, f"Set {property_name} to {value}"
            
        except Exception as e:
            return html, False, f"Error editing style: {str(e)}"
    
    def remove_element(
        self,
        html: str,
        selector: Dict[str, Any]
    ) -> Tuple[str, bool, str]:
        """
        Remove an element from the HTML.
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return html, False, "Could not find the element to remove"
            
            tag_name = element.name
            element.decompose()
            
            return str(soup), True, f"Removed {tag_name} element"
            
        except Exception as e:
            return html, False, f"Error removing element: {str(e)}"
    
    def add_element(
        self,
        html: str,
        parent_selector: Dict[str, Any],
        new_element_html: str,
        position: str = 'end'  # 'start', 'end', 'before', 'after'
    ) -> Tuple[str, bool, str]:
        """
        Add a new element to the HTML.
        """
        try:
            soup, parent = self.find_element_by_selector(html, parent_selector)
            
            if not parent:
                return html, False, "Could not find the parent element"
            
            new_soup = BeautifulSoup(new_element_html, 'html.parser')
            new_element = new_soup.find()
            
            if not new_element:
                return html, False, "Invalid HTML for new element"
            
            if position == 'start':
                parent.insert(0, copy.copy(new_element))
            elif position == 'end':
                parent.append(copy.copy(new_element))
            elif position == 'before':
                parent.insert_before(copy.copy(new_element))
            elif position == 'after':
                parent.insert_after(copy.copy(new_element))
            
            return str(soup), True, f"Added new {new_element.name} element"
            
        except Exception as e:
            return html, False, f"Error adding element: {str(e)}"
    
    def replace_element(
        self,
        html: str,
        selector: Dict[str, Any],
        new_element_html: str
    ) -> Tuple[str, bool, str]:
        """
        Replace an element with new HTML.
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return html, False, "Could not find the element to replace"
            
            new_soup = BeautifulSoup(new_element_html, 'html.parser')
            new_element = new_soup.find()
            
            if not new_element:
                return html, False, "Invalid HTML for replacement"
            
            element.replace_with(copy.copy(new_element))
            
            return str(soup), True, f"Replaced element with new {new_element.name}"
            
        except Exception as e:
            return html, False, f"Error replacing element: {str(e)}"
    
    def get_element_info(
        self,
        html: str,
        selector: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Get detailed information about an element.
        """
        try:
            soup, element = self.find_element_by_selector(html, selector)
            
            if not element:
                return {'error': 'Element not found'}
            
            return {
                'tagName': element.name,
                'id': element.get('id'),
                'classes': element.get('class', []),
                'style': element.get('style', ''),
                'text': element.get_text()[:200] if element.get_text() else '',
                'attributes': dict(element.attrs),
                'children': len(element.find_all(recursive=False))
            }
            
        except Exception as e:
            return {'error': str(e)}


# Singleton instance
_element_editor_instance = None


def get_element_editor() -> ElementEditor:
    """Get or create element editor singleton instance."""
    global _element_editor_instance
    if _element_editor_instance is None:
        _element_editor_instance = ElementEditor()
    return _element_editor_instance
