# Split Stitch

Split the thread. Fill with line.

## What It Is

Split stitch creates a **raised, textured line** by splitting the previous stitch with the needle, creating a braided, cord-like appearance. It's excellent for outlines and filling.

## Construction

- **Split previous**: Needle emerges splitting the thread of previous stitch
- **Short stitches**: Usually 2–3 mm long
- **Braided look**: Thread splits create interwoven texture
- **Raised line**: Sits slightly proud of fabric

## Visual DNA

- **Braided texture**: Like a tiny rope or cord
- **Raised line**: Slight dimensionality
- **Soft edge**: Slightly fuzzy from split fibers
- **Dense coverage**: Can fill areas with parallel lines
- **Common uses**: Outlines, filling, stems, lettering, medieval embroidery

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_length` | 0.003–0.01 | Short splits |
| `raise_height` | 0.0–0.005 | Slight bump |
| `thread_plies` | 2–6 | Number of strands affects split |
| `braid_visibility` | 0.3–0.8 | How obvious the split texture |

## GLSL Snippet

```glsl
float split_stitch(vec2 uv, float len) {
    float segment = floor(uv.x / len);
    float local = fract(uv.x / len);
    float split = mod(segment, 2.0) * 0.5 + 0.25;
    float stitch = smoothstep(split - 0.1, split, local) * smoothstep(split + 0.1, split, local);
    return stitch * braid_visibility;
}
```

## Prompt Template

> "Split-stitched outline in [COLOR] floss, raised braided line from splitting previous stitches, soft fuzzy edge, medieval embroidery style on [FABRIC]"

## Anti-Drift

- **Not stem stitch**: Split is flat braided; stem is twisted rope
- **Not back stitch**: Split is textured and raised; back is flat and solid
- **Thread splitting**: The physical splitting of previous stitch is the technique

---

*Split the thread, pull through. The braid is the fill.*
