#!/usr/bin/env python3
"""Tiny SVG cross-stitch exporter for repo experiments."""
from pathlib import Path

def export_svg(grid, palette, cell=16, path='cross_stitch.svg'):
    rows, cols = len(grid), len(grid[0])
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{cols*cell}" height="{rows*cell}" viewBox="0 0 {cols*cell} {rows*cell}">']
    parts.append('<rect width="100%" height="100%" fill="#f3ead8"/>')
    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            if val is None: continue
            color = palette[val % len(palette)]
            x0,y0=x*cell,y*cell
            pad=cell*0.22
            parts.append(f'<path d="M{x0+pad},{y0+pad} L{x0+cell-pad},{y0+cell-pad} M{x0+cell-pad},{y0+pad} L{x0+pad},{y0+cell-pad}" stroke="{color}" stroke-width="3" stroke-linecap="round"/>')
    parts.append('</svg>')
    Path(path).write_text('\n'.join(parts), encoding='utf-8')

if __name__ == '__main__':
    grid = [[(x+y)%5 if (x-10)**2+(y-10)**2 < 80 else None for x in range(21)] for y in range(21)]
    export_svg(grid, ['#ff3fa4','#23f7dd','#fff261','#7038ff','#ffffff'])
