#!/usr/bin/env python3
"""Build a quick JSON manifest of markdown files in this repo."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[2]
files = sorted(str(p.relative_to(root)) for p in root.rglob('*.md'))
Path(root/'16_structured_data/generated_manifest.json').write_text(json.dumps({'markdown_files': files}, indent=2), encoding='utf-8')
print(f'wrote {len(files)} markdown file entries')
