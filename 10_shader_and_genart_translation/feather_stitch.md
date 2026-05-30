# Feather Stitch

The branching line. Coral branch.

## What It Is

Feather stitch creates a **branching, feather-like line** with stitches that alternate left and right of a central spine. It resembles coral, ferns, or feathers.

## Construction

- **Central spine**: Imaginary line down center
- **Alternating sides**: Stitches alternate left and right
- **Anchor points**: Each stitch anchored at spine, extends outward
- **Branching**: Can split into multiple directions

## Visual DNA

- **Branching line**: Like a coral or fern frond
- **Alternating arms**: Left-right-left-right rhythm
- **Organic growth**: Natural, spreading pattern
- **Textural line**: More than a simple outline
- **Common uses**: Seams, foliage, decorative borders, crazy quilting

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `branch_angle` | 30°–60° | Arm angle from spine |
| `arm_length` | 0.01–0.04 | How far arms extend |
| `spacing` | 0.01–0.03 | Distance along spine |
| `branching` | 0–1 | Simple vs. complex branching |

## GLSL Snippet

```glsl
float feather_stitch(vec2 uv, float angle) {
    float segment = floor(uv.x / spacing);
    float side = mod(segment, 2.0) * 2.0 - 1.0;
    vec2 arm = vec2(cos(angle), sin(angle) * side);
    float along = dot(uv, normalize(arm));
    float stitch = smoothstep(0.0, 0.1, along) * smoothstep(arm_length, arm_length - 0.01, along);
    return stitch;
}
```

## Prompt Template

> "Feather-stitched [MOTIF] in [COLOR] floss, branching coral-like line with alternating arms, organic fern texture, decorative embroidery border"

## Anti-Drift

- **Not fern stitch**: Feather is more open and alternating; fern is denser
- **Not fly stitch**: Feather is connected branches; fly is scattered Vs
- **Spine-based**: Always has a central line

---

*Left, right, branch. The spine is the tree.*
