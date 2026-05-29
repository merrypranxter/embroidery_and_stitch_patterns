# Chain Stitch

Linked loops. The chain of thread.

## What It Is

Chain stitch creates **interlocking loops of thread** that form a chain-like line. Each loop is anchored by the next stitch, creating a decorative, slightly raised line.

## Construction

- **Loop formation**: Needle emerges, thread looped under, needle re-enters inside loop
- **Interlocking**: Each new loop passes through previous loop
- **Anchor**: Final loop secured with small tack stitch
- **Direction**: Can work in any direction

## Visual DNA

- **Visible loops**: Oval or round links clearly visible
- **Slight raise**: Loop sits proud of fabric surface
- **Decorative line**: More ornamental than functional
- **Hand-drawn chain**: Like a tiny thread chain
- **Common uses**: Outlines, filling, decorative borders, lazy daisy (detached chain)

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `loop_size` | 0.01–0.03 | Diameter of each link |
| `link_spacing` | 0.005–0.02 | Distance between loop centers |
| `raise_height` | 0.0–0.01 | Loop dimensionality |
| `line_path` | — | Straight or curved |

## GLSL Snippet

```glsl
float chain_stitch(vec2 uv, float size) {
    float segment = floor(uv.x / size);
    float local = fract(uv.x / size) - 0.5;
    float loop = smoothstep(0.0, 0.1, abs(local) - size * 0.3);
    return loop;
}
```

## Prompt Template

> "Chain-stitched border in [COLOR] floss, interlocking loop chain with slight raise, decorative ornamental line, traditional embroidery on [FABRIC]"

## Anti-Drift

- **Not stem stitch**: Chain is linked loops; stem is twisted rope
- **Not lazy daisy**: Chain is continuous; lazy daisy is detached single loop
- **Decorative**: More ornamental than structural

---

*Loop through loop. The chain is the line.*
