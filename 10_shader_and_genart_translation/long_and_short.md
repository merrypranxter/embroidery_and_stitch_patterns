# Long and Short Stitch

Gradated fill. Silk painting in thread.

## What It Is

Long and short stitch is a **filling technique** using alternating long and short stitches to create smooth color gradations and shading. It's the primary stitch for thread painting.

## Construction

- **First row**: Alternating long and short stitches
- **Subsequent rows**: Stitches split the gaps of previous row
- **Color blending**: Different colors in adjacent rows create gradation
- **Directional**: All stitches follow light/shade direction

## Visual DNA

- **Smooth gradation**: No visible rows; seamless color transition
- **Directional sheen**: Light reflects along stitch direction
- **Painterly**: Resembles brush strokes
- **Thread painting**: The technique for realistic imagery in thread
- **Common uses**: Realistic florals, portraits, animals, landscapes, silk shading

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_direction` | 0°–180° | Light direction |
| `color_gradation` | 0.0–1.0 | How smooth the blend |
| `row_visibility` | 0.0–0.2 | How obvious the rows |
| `sheen_intensity` | 0.3–0.8 | Silk reflection |

## GLSL Snippet

```glsl
float long_and_short(vec2 uv, float direction) {
    vec2 rotated = rotate(uv, direction);
    float row = floor(rotated.y / row_height);
    float offset = mod(row, 2.0) * 0.5;
    float long = smoothstep(0.0, 0.1, fract(rotated.x + offset));
    float short = smoothstep(0.0, 0.05, fract(rotated.x + offset + 0.5));
    return mix(long, short, 0.5);
}
```

## Prompt Template

> "Long and short stitch [SUBJECT] in silk floss, smooth color gradation with directional sheen, thread painting technique, realistic shading, silk embroidery art"

## Anti-Drift

- **Not satin stitch**: Long and short has varied lengths; satin is uniform
- **Not seed stitch**: Long and short is directional fill; seed is scattered
- **Thread painting**: The technique for realistic imagery

---

*Long, short, split the gap. The gradation is the painting.*
