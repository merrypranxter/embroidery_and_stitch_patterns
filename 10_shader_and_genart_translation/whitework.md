# Whitework

White on white. Shadow and texture.

## What It Is

Whitework is **embroidery worked in white thread on white fabric**, creating patterns through texture, stitch density, and shadow rather than color contrast. It includes many techniques like pulled thread, Hardanger, and shadow work.

## Construction

- **White thread**: Usually white cotton, linen, or silk
- **White ground**: White fabric base
- **Texture contrast**: Pattern created by stitch density variation
- **Shadow play**: Open areas create shadow against dense stitches

## Visual DNA

- **Monochrome subtlety**: No color, only tone and texture
- **Shadow depth**: Open areas appear darker due to shadow
- **Delicate and refined**: Elegant, understated appearance
- **Variety of techniques**: Includes pulled thread, Hardanger, drawn thread
- **Common uses**: Bridal, christening, table linens, ecclesiastical, heirloom

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `tone_range` | 0.0–0.3 | Subtle shadow variation |
| `texture_contrast` | 0.2–0.8 | Dense vs. open areas |
| `thread_fineness` | 0.001–0.005 | Fine white thread |
| `technique` | pulled/hardanger/drawn | Whitework sub-type |

## GLSL Snippet

```glsl
float whitework(vec2 uv, float density) {
    float solid = solid_stitch_area(uv, scale);
    float open = open_mesh_area(uv, scale);
    float shadow = (1.0 - open) * shadow_depth;
    return solid + shadow;
}
```

## Prompt Template

> "Whitework embroidery in white thread on white linen, [TECHNIQUE] pattern with tonal texture and shadow contrast, subtle monochrome elegance, heirloom bridal textile"

## Anti-Drift

- **Not color work**: Whitework has no color; tonal only
- **Shadow is key**: The contrast comes from light/shadow, not hue
- **Includes many techniques**: Whitework is a category, not a single stitch

---

*White on white, shadow is the color. The absence is the pattern.*
