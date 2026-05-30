# Blackwork

Geometric monochrome. Spanish tradition.

## What It Is

Blackwork is **counted-thread embroidery** worked in black silk on white linen, creating intricate geometric patterns. It was popular in Tudor England and has Spanish origins.

## Construction

- **Counted thread**: Worked on even-weave linen grid
- **Holbein stitch**: Double running stitch creates reversible pattern
- **Geometric patterns**: Symmetrical, often based on diaper patterns
- **Monochrome**: Black thread on white ground

## Visual DNA

- **Black on white**: Stark monochrome contrast
- **Geometric precision**: Counted, symmetrical patterns
- **Reversible**: Often identical front and back
- **Dense fills**: Intricate diaper and geometric fills
- **Common uses**: Cuffs, collars, samplers, borders, historical reenactment

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `grid_size` | 0.005–0.02 | Even-weave count |
| `pattern_density` | 0.3–0.9 | How dense the blackwork |
| `reversible` | 0–1 | Same front and back |
| `geometric_type` | 0–5 | Diaper, lattice, etc. |

## GLSL Snippet

```glsl
float blackwork(vec2 uv, float grid) {
    vec2 cell = floor(uv / grid);
    float pattern = geometric_fill(cell, pattern_id);
    float stitch = smoothstep(0.0, 0.1, pattern);
    return stitch;
}
```

## Prompt Template

> "Blackwork embroidery in black silk on white linen, counted-thread geometric [PATTERN], reversible Holbein stitch, Tudor monochrome tradition"

## Anti-Drift

- **Not cross stitch**: Blackwork is running stitch; cross is X-shaped
- **Monochrome**: Black on white is the tradition
- **Counted thread**: Must align to fabric grid

---

*Black on white, counted and precise. The geometry is the discipline.*
