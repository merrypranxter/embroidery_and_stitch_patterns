# Back Stitch

The continuous line. Strong and steady.

## What It Is

Back stitch creates a **solid, unbroken line** by stitching backward one step for every two steps forward. It's the strongest basic stitch for outlines and lettering.

## Construction

- **Two forward, one back**: Needle emerges, goes forward two stitch lengths, then back one
- **Overlap**: Each stitch overlaps the previous by half its length
- **Continuous coverage**: No gaps between stitches
- **Any direction**: Works in curves and straight lines

## Visual DNA

- **Solid line**: No gaps, continuous thread coverage
- **Slight thickness**: Double thread at overlap points
- **Strong edge**: Clean, bold boundary line
- **Hand character**: Slight variation in stitch length
- **Common uses**: Outlines, lettering, stems, borders, strong lines

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_length` | 0.005–0.02 | Length of visible segment |
| `overlap` | 0.5 | Always half overlap |
| `thickness` | 0.001–0.004 | Thread diameter |
| `line_path` | — | Can be curved or straight |

## GLSL Snippet

```glsl
float back_stitch(vec2 uv, float len, float thickness) {
    float segment = floor(uv.x / len);
    float local = fract(uv.x / len);
    float stitch = smoothstep(0.0, 0.1, local) * smoothstep(1.0, 0.9, local);
    return stitch * thickness_line(uv.y, thickness);
}
```

## Prompt Template

> "Back-stitched outline in [COLOR] floss, solid continuous line with slight overlap thickening, strong bold edge, hand embroidery on [FABRIC]"

## Anti-Drift

- **Not running stitch**: Back stitch has no gaps; running stitch does
- **Not stem stitch**: Back stitch is flat; stem stitch is twisted
- **Strongest basic**: Best for outlines that need durability

---

*Forward two, back one. The overlap is the strength.*
