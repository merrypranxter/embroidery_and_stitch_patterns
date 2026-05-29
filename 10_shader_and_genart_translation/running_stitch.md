# Running Stitch

The simplest line. In-out, in-out.

## What It Is

Running stitch is the **most basic hand embroidery stitch** — the needle weaves in and out of the fabric in a straight line, creating a dashed-line effect. It's the foundation of all stitch work.

## Construction

- **In-out rhythm**: Needle enters, exits, enters, exits in regular intervals
- **Spacing**: Even or uneven gaps between stitches
- **Direction**: Can travel in any direction
- **Single thread**: Usually one strand of embroidery floss

## Visual DNA

- **Dashed line**: Short straight segments with gaps
- **Hand-drawn quality**: Slight wobble from human hand
- **Simple and honest**: No pretension, just thread marking path
- **Versatile**: Used for outlines, gathers, quilting, basting
- **Common uses**: Basting, gathering, outlines, quilting lines, kantha

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_length` | 0.005–0.02 | Length of each dash |
| `gap_length` | 0.002–0.01 | Space between stitches |
| `thread_thickness` | 0.001–0.003 | Floss diameter |
| `wobble` | 0.0–0.002 | Hand-drawn imperfection |

## GLSL Snippet

```glsl
float running_stitch(vec2 uv, float len, float gap) {
    float pos = fract(uv.x / (len + gap));
    float stitch = smoothstep(0.0, 0.1, pos) * smoothstep(len / (len + gap), len / (len + gap) - 0.1, pos);
    return stitch;
}
```

## Prompt Template

> "Running stitch line in [COLOR] embroidery floss, simple in-out dashed line, hand-sewn quality with slight wobble, traditional basic stitch on [FABRIC]"

## Anti-Drift

- **Not back stitch**: Running stitch has gaps; back stitch is continuous
- **Not stem stitch**: Running is straight dashes; stem is twisted rope
- **Foundation stitch**: Often used underneath other stitches

---

*In, out, in, out. The gap is as important as the stitch.*
