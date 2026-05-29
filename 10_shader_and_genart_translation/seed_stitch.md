# Seed Stitch

Scattered dots. Random fill.

## What It Is

Seed stitch creates a **scattered field of tiny straight stitches** of varying lengths and directions, resembling seeds scattered on soil. It's a simple filling stitch with organic texture.

## Construction

- **Random placement**: Stitches scattered without pattern
- **Varied length**: Short and tiny stitches mixed
- **Any direction**: Stitches point in random directions
- **Dense coverage**: Fills area with texture, not solid color

## Visual DNA

- **Scattered dots**: Tiny dashes randomly oriented
- **Organic texture**: Like seeds or grains
- **Subtle color**: Usually monochrome or limited palette
- **Visual interest**: Breaks up large solid areas
- **Common uses**: Fillers, ground texture, skies, soil, abstract fills

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `stitch_length` | 0.003–0.01 | Tiny dashes |
| `density` | 50–500 | Stitches per unit area |
| `direction_randomness` | 0.0–1.0 | How random orientations |
| `color_variation` | 0.0–0.2 | Slight tone differences |

## GLSL Snippet

```glsl
float seed_stitch(vec2 uv, float seed) {
    vec2 grid = floor(uv * density);
    float rnd = random(grid + seed);
    vec2 pos = (grid + vec2(rnd, fract(rnd * 1.618))) / density;
    float dir = rnd * PI;
    float len = stitch_length * (0.5 + rnd);
    vec2 stitch = vec2(cos(dir), sin(dir)) * len;
    float dist = line_distance(uv, pos, pos + stitch);
    return smoothstep(0.0, 0.001, dist);
}
```

## Prompt Template

> "Seed-stitched fill in [COLOR] floss, scattered tiny straight stitches of random length and direction, organic grain-like texture, embroidery filler"

## Anti-Drift

- **Not French knot**: Seed is flat stitch; French knot is dimensional bump
- **Not satin**: Seed is scattered; satin is parallel and dense
- **Random is key**: The randomness defines seed stitch

---

*Scatter, don't arrange. The randomness is the field.*
