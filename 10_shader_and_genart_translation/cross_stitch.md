# Cross Stitch

The X. Pixel art in thread.

## What It Is

Cross stitch creates **X-shaped stitches** on a regular grid (usually Aida cloth), forming pixelated patterns. It's one of the most popular counted-thread embroidery techniques.

## Construction

- **Counted thread**: Worked on even-weave fabric with regular holes
- **X shape**: Two diagonal stitches crossing
- **Regular grid**: Stitches align to fabric grid
- **Full and half**: Full crosses and fractional stitches for detail

## Visual DNA

- **Visible grid**: Fabric grid apparent between stitches
- **Pixelated**: Image formed from discrete X units
- **Color blocking**: Solid areas of single color
- **Slight texture**: Thread sits on fabric surface
- **Common uses**: Samplers, portraits, patterns, bookmarks, ornaments

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `grid_size` | 0.01–0.05 | Distance between stitches |
| `thread_count` | 1–6 | Strands per stitch |
| `coverage` | 0.6–0.9 | How much grid is covered |
| `pattern` | — | Chart-based design |

## GLSL Snippet

```glsl
float cross_stitch(vec2 uv, float grid) {
    vec2 cell = floor(uv / grid);
    vec2 local = fract(uv / grid) - 0.5;
    float diagonal1 = smoothstep(0.0, 0.1, abs(local.x - local.y));
    float diagonal2 = smoothstep(0.0, 0.1, abs(local.x + local.y));
    float cross = max(diagonal1, diagonal2);
    return cross;
}
```

## Prompt Template

> "Cross-stitched [PATTERN] on Aida cloth, regular grid of X-shaped stitches, pixelated color-block image, counted-thread embroidery sampler"

## Anti-Drift

- **Not needlepoint**: Cross stitch is diagonal X; needlepoint is vertical/horizontal
- **Counted thread**: Must align to fabric grid
- **Grid visible**: The cloth grid is part of the aesthetic

---

*Two diagonals, one X. The grid is the pixel.*
