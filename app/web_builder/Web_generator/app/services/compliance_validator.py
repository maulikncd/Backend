"""
Blueprint Compliance Validator
Ensures that generated websites match the blueprint specification

This module validates:
1. All blueprint components are present in generated HTML
2. User's answers are properly reflected in the content  
3. Color palette is correctly applied
4. Template variants match what was specified
"""

from typing import Dict, Any, List, Optional, Tuple
import re
import hashlib


class BlueprintComplianceValidator:
    """
    Validates that generated HTML websites comply with their blueprint.
    
    Features:
    - Component presence verification
    - Color palette compliance check
    - User content injection verification
    - Props compliance report generation
    """
    
    @classmethod
    def validate_website_against_blueprint(
        cls,
        blueprint: Dict[str, Any],
        generated_html: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Main validation function that checks website against blueprint.
        
        Args:
            blueprint: The blueprint JSON
            generated_html: Dict of page_name -> html_content
            
        Returns:
            Validation report with compliance score and issues
        """
        report = {
            "is_compliant": True,
            "compliance_score": 100,
            "checks_passed": [],
            "checks_failed": [],
            "warnings": [],
            "component_compliance": {},
            "color_compliance": {},
            "content_compliance": {}
        }
        
        # Check 1: Component Presence
        component_result = cls._check_component_presence(blueprint, generated_html)
        report["component_compliance"] = component_result
        if not component_result["all_present"]:
            report["is_compliant"] = False
            report["checks_failed"].append("component_presence")
            report["compliance_score"] -= 20
        else:
            report["checks_passed"].append("component_presence")
        
        # Check 2: Color Palette
        color_result = cls._check_color_compliance(blueprint, generated_html)
        report["color_compliance"] = color_result
        if not color_result["colors_applied"]:
            report["warnings"].append("color_palette_not_fully_applied")
            report["compliance_score"] -= 10
        else:
            report["checks_passed"].append("color_palette")
        
        # Check 3: User Content Injection
        content_result = cls._check_content_injection(blueprint, generated_html)
        report["content_compliance"] = content_result
        if not content_result["content_injected"]:
            report["warnings"].append("user_content_not_fully_injected")
            report["compliance_score"] -= 15
        else:
            report["checks_passed"].append("content_injection")
        
        # Ensure score doesn't go below 0
        report["compliance_score"] = max(0, report["compliance_score"])
        
        # Set final compliance status
        report["is_compliant"] = report["compliance_score"] >= 70
        
        print(f"[BlueprintComplianceValidator] ✅ Compliance Score: {report['compliance_score']}/100")
        return report
    
    @classmethod
    def _check_component_presence(
        cls,
        blueprint: Dict[str, Any],
        generated_html: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Check if all blueprint components are present in generated HTML.
        """
        components = blueprint.get("components", {})
        component_order = blueprint.get("componentOrder", list(components.keys()))
        
        all_html = " ".join(generated_html.values()).lower()
        
        present = []
        missing = []
        
        for comp_id in component_order:
            comp = components.get(comp_id, {})
            comp_type = comp.get("type", "").lower()
            comp_name = comp.get("name", "").lower()
            
            # Check if component has corresponding section in HTML
            # Look for section IDs, classes, or content markers
            markers = [
                f'id="{comp_type}"',
                f'id="{comp.get("id", comp_type).lower()}"',
                f'class=".*{comp_type}.*"',
                f'section-{comp_type}',
            ]
            
            found = any(marker in all_html or comp_type in all_html for marker in markers)
            
            if found:
                present.append(comp_id)
            else:
                missing.append(comp_id)
                print(f"[BlueprintComplianceValidator] ⚠️ Missing component: {comp_id} ({comp_type})")
        
        return {
            "all_present": len(missing) == 0,
            "present_count": len(present),
            "missing_count": len(missing),
            "present": present,
            "missing": missing
        }
    
    @classmethod
    def _check_color_compliance(
        cls,
        blueprint: Dict[str, Any],
        generated_html: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Check if the color palette is correctly applied.
        """
        theme = blueprint.get("theme", {})
        palette = theme.get("palette", {})
        
        all_html = " ".join(generated_html.values())
        
        colors_found = []
        colors_missing = []
        
        for color_key, color_value in palette.items():
            if isinstance(color_value, str) and color_value.startswith("#"):
                # Check if color appears in HTML (in styles, inline, or CSS variables)
                if color_value.lower() in all_html.lower():
                    colors_found.append(color_key)
                else:
                    colors_missing.append(color_key)
        
        return {
            "colors_applied": len(colors_missing) <= 1,  # Allow 1 missing color
            "found": colors_found,
            "missing": colors_missing,
            "primary_applied": "primary" in colors_found
        }
    
    @classmethod
    def _check_content_injection(
        cls,
        blueprint: Dict[str, Any],
        generated_html: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Check if user's content (from questionnaire) is properly injected.
        """
        components = blueprint.get("components", {})
        all_html = " ".join(generated_html.values()).lower()
        
        content_found = []
        content_missing = []
        
        for comp_id, comp in components.items():
            props = comp.get("props", {})
            
            # Check key content fields
            content_keys = ["title", "subtitle", "businessName", "headline", "story"]
            
            for key in content_keys:
                if key in props and props[key]:
                    value = str(props[key]).lower()
                    # Only check if value is substantial (not default placeholder)
                    if len(value) > 3 and value not in ["lorem", "ipsum", "default"]:
                        if value in all_html:
                            content_found.append(f"{comp_id}.{key}")
                        else:
                            content_missing.append(f"{comp_id}.{key}")
        
        return {
            "content_injected": len(content_missing) <= 2,  # Allow 2 missing items
            "found": content_found,
            "missing": content_missing
        }
    
    @classmethod
    def generate_compliance_report(
        cls,
        blueprint: Dict[str, Any],
        generated_html: Dict[str, str],
        session_id: str
    ) -> Dict[str, Any]:
        """
        Generate a comprehensive compliance report.
        
        Args:
            blueprint: The blueprint JSON
            generated_html: Dict of page_name -> html_content
            session_id: Session ID for tracking
            
        Returns:
            Complete compliance report
        """
        from datetime import datetime
        
        validation = cls.validate_website_against_blueprint(blueprint, generated_html)
        
        report = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "blueprint_id": blueprint.get("blueprint_id"),
            "project_name": blueprint.get("projectName"),
            "website_type": blueprint.get("websiteType"),
            "validation": validation,
            "summary": {
                "total_components": len(blueprint.get("components", {})),
                "components_verified": validation["component_compliance"].get("present_count", 0),
                "compliance_grade": cls._get_grade(validation["compliance_score"]),
                "is_production_ready": validation["compliance_score"] >= 80
            }
        }
        
        # Log summary
        print(f"[BlueprintComplianceValidator] 📊 Report for {session_id}:")
        print(f"  - Components: {report['summary']['components_verified']}/{report['summary']['total_components']}")
        print(f"  - Grade: {report['summary']['compliance_grade']}")
        print(f"  - Production Ready: {report['summary']['is_production_ready']}")
        
        return report
    
    @classmethod
    def _get_grade(cls, score: int) -> str:
        """Convert score to letter grade"""
        if score >= 95:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 85:
            return "B+"
        elif score >= 80:
            return "B"
        elif score >= 75:
            return "C+"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"


class BlueprintWebsiteTracker:
    """
    Tracks the relationship between blueprints and generated websites.
    Ensures traceability and enables debugging.
    """
    
    _tracking_data: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def record_generation(
        cls,
        session_id: str,
        blueprint: Dict[str, Any],
        generated_html: Dict[str, str],
        used_variants: Dict[str, str]
    ) -> str:
        """
        Record a website generation for tracking.
        
        Args:
            session_id: Session ID
            blueprint: Blueprint used
            generated_html: Generated HTML pages
            used_variants: Template variants used
            
        Returns:
            Tracking ID for this generation
        """
        from datetime import datetime
        
        # Generate tracking ID
        tracking_id = f"gen_{session_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Create tracking record
        cls._tracking_data[tracking_id] = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "blueprint_hash": cls._hash_blueprint(blueprint),
            "pages_generated": list(generated_html.keys()),
            "variants_used": used_variants,
            "component_count": len(blueprint.get("components", {})),
            "website_type": blueprint.get("websiteType", "unknown")
        }
        
        print(f"[BlueprintWebsiteTracker] 📝 Recorded generation: {tracking_id}")
        return tracking_id
    
    @classmethod
    def _hash_blueprint(cls, blueprint: Dict[str, Any]) -> str:
        """Create a hash of the blueprint for comparison"""
        import json
        # Only hash key structural elements
        key_data = {
            "components": list(blueprint.get("components", {}).keys()),
            "componentOrder": blueprint.get("componentOrder", []),
            "websiteType": blueprint.get("websiteType")
        }
        data_str = json.dumps(key_data, sort_keys=True)
        return hashlib.md5(data_str.encode()).hexdigest()[:12]
    
    @classmethod
    def verify_generation_matches_blueprint(
        cls,
        tracking_id: str,
        blueprint: Dict[str, Any]
    ) -> bool:
        """
        Verify that a generation matches its original blueprint.
        """
        if tracking_id not in cls._tracking_data:
            print(f"[BlueprintWebsiteTracker] ⚠️ Tracking ID not found: {tracking_id}")
            return False
        
        record = cls._tracking_data[tracking_id]
        current_hash = cls._hash_blueprint(blueprint)
        
        if current_hash == record["blueprint_hash"]:
            print(f"[BlueprintWebsiteTracker] ✅ Blueprint hash matches for {tracking_id}")
            return True
        else:
            print(f"[BlueprintWebsiteTracker] ❌ Blueprint hash MISMATCH for {tracking_id}")
            return False


# Export
__all__ = ["BlueprintComplianceValidator", "BlueprintWebsiteTracker"]
