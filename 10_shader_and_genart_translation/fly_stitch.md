# Fly Stitch

V-shaped scatter. Insect wing.

## What It Is

Fly stitch creates **V-shaped stitches** anchored with a small horizontal tack, resembling insect wings or scattered leaves. It's used for fillers, foliage, and organic scatter.

## Construction

- **V shape**: Two diagonal stitches meeting at bottom
- **Tack stitch**: Small horizontal stitch anchors the V point
- **Scatter or row**: Can be scattered randomly or in rows
- **Varied size**: Large and small Vs for texture

## Visual DNA

- **V scatter**: Wing-like shapes scattered across area
- **Anchor visible**: Small horizontal stitch at V point
- **Organic feel**: Natural, leaf-like appearance
- **Fill texture**: Covers areas with directional scatter
- **Common uses**: Foliage, fillers, grass, scattered leaves

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `v_size` | 0.01–0.04 | Height of V |
| `v_width` | 0.01–0.03 | Width at top |
| `scatter_density` | 0–50 | Vs per unit area |
| `tack_visibility` | 0.0–0.01 | Anchor stitch |

## GLSL Snippet

```glsl
float fly_stitch(vec2 uv, float size) {
    float v = abs(fract(uv.x / size) - 0.5) * 2.0;
    float shape = smoothstep(v * size, 0.0, uv.y);
    float tack = smoothstep(0.0, 0.002, abs(uv.y));
    return max(shape, tack);
}
```

## Prompt Template

> "Fly stitch foliage in [COLOR] floss, V-shaped scattered stitches with anchor tacks, organic leaf-like texture, embroidery filler on [FABRIC]"

## Anti-Drift

- **Not leaf stitch**: Fly is detached V; leaf stitch is filled shape
- **Anchor defines it**: The tack stitch is part of the structure
- **Scatter or row**: Can be either arrangement

---

*Two diagonals, one tack. The V is the wing.*
