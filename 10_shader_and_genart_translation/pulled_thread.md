# Pulled Thread

Tension magic. Fabric becomes lace.

## What It Is

Pulled thread work creates **open patterns by pulling threads tight** in specific arrangements, distorting the fabric weave to create lacy, geometric designs without cutting or removing threads.

## Construction

- **Ground fabric**: Even-weave linen or cotton
- **Pulling stitches**: Specific stitches pull threads together
- **Tension creates gaps**: Pulled threads open spaces in weave
- **No cutting**: Threads are pulled, not removed

## Visual DNA

- **Openwork without cutting**: Gaps from tension, not removal
- **Geometric patterns**: Diamonds, squares, stars from pulled arrangements
- **Fabric distortion**: Weave visibly distorted by tension
- **Lacy appearance**: Resembles lace but is woven fabric
- **Common uses**: Table linens, samplers, whitework, decorative pieces

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `pull_tension` | 0.5–1.0 | How tight the stitches |
| `gap_size` | 0.0–0.1 | Open areas from pulling |
| `pattern_type` | 0–5 | Diamond, square, star, etc. |
| `weave_distortion` | 0.0–0.2 | Visible fabric warp |

## GLSL Snippet

```glsl
float pulled_thread(vec2 uv, float tension) {
    float stitch = stitch_pattern(uv, scale);
    float pull = stitch * tension;
    float gap = warp_opening(uv, pull);
    return gap;
}
```

## Prompt Template

> "Pulled thread work in white linen, geometric [PATTERN] created by tension stitches distorting weave, openwork without cutting, traditional whitework technique"

## Anti-Drift

- **Not drawn thread**: Pulled thread distorts; drawn thread removes threads
- **Not lace**: Pulled thread is woven fabric manipulated; lace is constructed openwork
- **Tension is key**: The pulling force creates the gaps

---

*Pull tight, the weave opens. The tension is the lace.*
