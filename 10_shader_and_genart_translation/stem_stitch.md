# Stem Stitch

The twisted rope. Botanical line.

## What It Is

Stem stitch creates a **slightly raised, twisted rope-like line** by working stitches along a path with each stitch emerging from the midpoint of the previous one. It's the classic stitch for stems, vines, and organic lines.

## Construction

- **Midpoint emergence**: Each new stitch emerges from middle of previous stitch
- **Slight overlap**: Creates twisted, corded appearance
- **Directional**: Best worked left-to-right or along curve
- **Consistent length**: Even stitches create smooth rope

## Visual DNA

- **Rope texture**: Twisted, corded appearance
- **Slight raise**: Thread sits slightly proud of fabric
- **Organic flow**: Natural curves and botanical lines
- **Hand-spun look**: Like a tiny hand-twisted cord
- **Common uses**: Stems, vines, lettering, outlines, organic shapes

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_length` | 0.005–0.02 | Length of each stitch |
| `twist_factor` | 0.3–0.7 | How much overlap creates rope |
| `raise_height` | 0.0–0.01 | Slight dimensional quality |
| `curve_smoothness` | 0.8–1.0 | How well it follows curves |

## GLSL Snippet

```glsl
float stem_stitch(vec2 uv, float len) {
    float segment = floor(uv.x / len);
    float local = fract(uv.x / len);
    float twist = sin(local * PI) * 0.1;
    float stitch = smoothstep(0.0, 0.2, local) * smoothstep(1.0, 0.8, local);
    return stitch * (1.0 + twist);
}
```

## Prompt Template

> "Stem-stitched vine in [COLOR] floss, twisted rope-like texture with slight raise, botanical organic line following natural curves, traditional embroidery"

## Anti-Drift

- **Not back stitch**: Stem is twisted and raised; back is flat and solid
- **Not chain stitch**: Stem is twisted line; chain is linked loops
- **Botanical classic**: The stem stitch is named for its use on plant stems

---

*Midpoint to midpoint. The twist is the rope.*
