# French Knot

The bead of thread. Tiny sphere.

## What It Is

French knot is a **small dimensional knot** created by wrapping thread around the needle and pulling tight, forming a tiny bead-like bump on the fabric surface. It's used for texture, centers of flowers, and scattered fills.

## Construction

- **Needle up**: Thread emerges at knot location
- **Wrap**: Thread wrapped around needle 1–3 times
- **Re-insert**: Needle goes back down near entry point
- **Pull tight**: Thread drawn through wraps to form knot

## Visual DNA

- **Tiny spheres**: Small round bumps on fabric
- **Dimensional**: Sits proud of surface
- **Scattered or clustered**: Can be dense fill or accent dots
- **Textural contrast**: Bumpy against smooth fabric
- **Common uses**: Flower centers, eyes, texture fills, stamens, scattered accents

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `knot_size` | 0.003–0.01 | Diameter of bump |
| `wrap_count` | 1–3 | Thread wraps around needle |
| `height` | 0.0–0.01 | Dimensional bump |
| `density` | 0–500 | Knots per unit area |

## GLSL Snippet

```glsl
float french_knot(vec2 uv, vec2 pos, float size) {
    float dist = length(uv - pos) / size;
    float knot = smoothstep(1.0, 0.0, dist);
    float height = knot * bump_scale;
    return height;
}
```

## Prompt Template

> "French knot [MOTIF] in [COLOR] floss, tiny thread beads scattered across fabric, dimensional bump texture, flower centers and scattered accents, traditional embroidery"

## Anti-Drift

- **Not seed stitch**: French knot is dimensional bump; seed is flat straight stitch
- **Not bullion**: French knot is small and round; bullion is long and coiled
- **Wrap count matters**: More wraps = bigger knot

---

*Wrap, pull, bead. The bump is the texture.*
