# Template Management System Architecture
# =========================================

## Folder Structure (Scalable for 100+ Templates)

```
app/templates/
├── __init__.py                    # Main exports
├── registry.py                    # Central template registry
├── combination_tracker.py         # Tracks used combinations
│
├── website_types/                 # Type-Specific Templates
│   ├── __init__.py
│   │
│   ├── cafe/                      # ☕ Cafe Templates
│   │   ├── __init__.py            # CafeTemplates class
│   │   ├── hero/                  # Hero variants (split into files)
│   │   │   ├── __init__.py        
│   │   │   ├── morning_fresh.py   # Variant 1
│   │   │   ├── coffee_steam.py    # Variant 2
│   │   │   ├── warm_welcome.py    # Variant 3
│   │   │   └── ...
│   │   ├── navbar/
│   │   │   ├── transparent.py
│   │   │   ├── sticky_warm.py
│   │   │   └── ...
│   │   ├── menu/
│   │   ├── about/
│   │   ├── gallery/
│   │   ├── footer/
│   │   └── cta/
│   │
│   ├── gaming/                    # 🎮 Gaming Templates
│   ├── portfolio/                 # 💼 Portfolio Templates
│   ├── ecommerce/                 # 🛒 E-commerce Templates
│   ├── restaurant/                # 🍽️ Restaurant Templates
│   └── agency/                    # 🏢 Agency Templates
│
├── shared/                        # Cross-Type Components
│   ├── navbar/
│   ├── footer/
│   ├── contact/
│   └── cta/
│
└── assets/                        # Template metadata
    └── template_manifest.json     # All templates registry
```

## Key Principles:

1. **Variant Isolation**: Each variant in separate file (easy to add/edit)
2. **Combination Tracking**: JSON file tracks last N generations
3. **Auto-Discovery**: System scans folders for new templates
4. **Weighted Selection**: Popular templates less likely to repeat

## Files to Create:

1. `combination_tracker.py` - Tracks history
2. Separate variant files for each component
3. `template_manifest.json` - Central registry
