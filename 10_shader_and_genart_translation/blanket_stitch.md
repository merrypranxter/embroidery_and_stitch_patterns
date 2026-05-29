# Blanket Stitch

The edge guard. Loop and anchor.

## What It Is

Blanket stitch is an **edge-finishing stitch** that creates a line of loops along fabric edges, preventing fraying while adding decorative detail. It's functional and ornamental.

## Construction

- **Edge perpendicular**: Needle emerges at edge, goes in perpendicular
- **Loop formation**: Thread loops under needle before pull
- **Even spacing**: Regular intervals along edge
- **Varied depth**: Can be shallow or deep for different effects

## Visual DNA

- **Loop edge**: Visible loops along fabric boundary
- **Right-angle entry**: Stitches enter perpendicular to edge
- **Clean finish**: Neat, professional edge treatment
- **Decorative or functional**: Can be plain or elaborate
- **Common uses**: Blanket edges, applique, felt finishing, buttonholes

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_depth` | 0.01–0.05 | How far into fabric |
| `loop_height` | 0.005–0.02 | Loop size |
| `spacing` | 0.01–0.03 | Distance between stitches |
| `edge_path` | — | Straight or curved |

## GLSL Snippet

```glsl
float blanket_stitch(vec2 uv, float depth, float height) {
    float segment = floor(uv.x / spacing);
    float local = fract(uv.x / spacing) - 0.5;
    float vertical = smoothstep(0.0, 0.1, abs(local));
    float loop = smoothstep(0.0, height, uv.y) * smoothstep(depth, depth - 0.01, uv.y);
    return vertical * loop;
}
```

## Prompt Template

> "Blanket-stitched edge in [COLOR] thread, looped edge finish preventing fray, clean perpendicular stitches, functional and decorative border on [FABRIC]"

## Anti-Drift

- **Not buttonhole**: Blanket is spaced; buttonhole is dense and close
- **Not whip stitch**: Blanket has loops; whip is overcast wrapping
- **Edge stitch**: Always worked on fabric edge

---

*Loop under, pull, repeat. The edge is the finish.*
