# Shadow Work

Backlit stitches. Reverse embroidery.

## What It Is

Shadow work (also called shadow embroidery or shadow stitching) creates **patterns visible on the reverse side of sheer fabric** by working herringbone stitches on the back. The stitches cast shadows through the fabric.

## Construction

- **Sheer fabric**: Usually organdy, voile, or fine cotton
- **Back-side stitches**: Herringbone stitch worked on reverse
- **Shadow cast**: Stitches visible through fabric as tone
- **Front side smooth**: Right side shows only shadow, no stitches

## Visual DNA

- **Shadow tone**: Pattern visible as subtle darkening through sheer fabric
- **Front smooth**: No visible stitches on right side
- **Back herringbone**: Clear herringbone pattern on reverse
- **Delicate and subtle**: Extremely refined, elegant effect
- **Common uses**: Baby garments, bridal, fine linens, heirloom pieces

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `fabric_sheerness` | 0.5–0.9 | How transparent |
| `shadow_opacity` | 0.1–0.3 | Tone visible through fabric |
| `stitch_density` | 0.5–1.0 | How dense the back stitches |
| `pattern_type` | 0–3 | Floral, geometric, etc. |

## GLSL Snippet

```glsl
float shadow_work(vec2 uv, float sheerness) {
    float back_stitch = herringbone(uv, scale);
    float shadow = back_stitch * shadow_opacity;
    float front = fabric_texture(uv, sheerness);
    return front + shadow * (1.0 - sheerness);
}
```

## Prompt Template

> "Shadow work embroidery on white organdy, [PATTERN] visible as subtle shadow through sheer fabric, herringbone stitches on reverse side, delicate heirloom whitework"

## Anti-Drift

- **Not regular embroidery**: Shadow work is worked on reverse; regular is front
- **Sheer fabric required**: The shadow needs transparency
- **Herringbone on back**: The specific stitch matters

---

*Stitch the back, show the front. The shadow is the pattern.*
