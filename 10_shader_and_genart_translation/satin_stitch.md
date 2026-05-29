# Satin Stitch

Flat silk fields. Dense coverage.

## What It Is

Satin stitch is a **series of flat straight stitches worked closely together** to completely cover an area with thread, creating a smooth, shiny, satin-like surface. It's the primary filling stitch.

## Construction

- **Parallel stitches**: Straight stitches laid side by side
- **Full coverage**: No fabric visible between stitches
- **Directional**: All stitches in same direction
- **Edge containment**: Stitches stay within shape boundary

## Visual DNA

- **Smooth flat surface**: Thread completely covers fabric
- **Satin sheen**: Light reflects off parallel threads
- **Directional light**: Sheen changes with viewing angle
- **Crisp edges**: Clean boundaries of filled shape
- **Common uses**: Filling shapes, petals, leaves, monograms, motifs

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_direction` | 0°–180° | Angle of parallel stitches |
| `stitch_density` | 0.8–1.0 | Coverage percentage |
| `sheen_intensity` | 0.3–0.8 | Light reflection |
| `edge_crispness` | 0.9–1.0 | Clean boundaries |

## GLSL Snippet

```glsl
float satin_stitch(vec2 uv, float direction) {
    vec2 rotated = rotate(uv, direction);
    float stitch = abs(fract(rotated.x / stitch_width) - 0.5) * 2.0;
    float coverage = smoothstep(1.0, 0.0, stitch);
    float sheen = pow(dot(normal, light), 4.0) * coverage;
    return sheen;
}
```

## Prompt Template

> "Satin-stitched [SHAPE] in [COLOR] silk floss, dense flat coverage with directional sheen, smooth satin-like surface, crisp edges, traditional embroidery filling"

## Anti-Drift

- **Not long and short**: Satin is all same length; long and short varies
- **Not seed stitch**: Satin covers fully; seed is scattered dots
- **Direction matters**: Sheen changes with stitch angle

---

*Parallel, dense, flat. The sheen is the direction.*
