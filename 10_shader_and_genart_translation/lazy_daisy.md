# Lazy Daisy

The detached petal. Single chain loop.

## What It Is

Lazy daisy is a **single detached chain stitch** forming a teardrop or petal shape, anchored at the pointed end. It's used for flower petals, leaves, and decorative accents.

## Construction

- **Loop up**: Thread emerges, forms loop
- **Tack down**: Needle re-enters near exit, securing loop
- **Anchor stitch**: Small stitch across loop point holds it
- **Single unit**: One loop = one petal

## Visual DNA

- **Teardrop shape**: Round end, pointed anchored end
- **Single loop**: One chain link, detached
- **Petal arrangement**: Multiple lazy daisies radiate from center
- **Slight raise**: Loop sits above fabric
- **Common uses**: Flower petals, leaves, simple florals, decorative accents

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `petal_length` | 0.02–0.05 | From anchor to round end |
| `petal_width` | 0.01–0.03 | Round end diameter |
| `anchor_size` | 0.001–0.003 | Tack stitch |
| `arrangement` | radial/scattered | How petals placed |

## GLSL Snippet

```glsl
float lazy_daisy(vec2 uv, vec2 anchor, float len) {
    vec2 to_petal = normalize(vec2(0.0, 1.0));
    float along = dot(uv - anchor, to_petal);
    float across = length(uv - anchor - to_petal * along);
    float width = len * 0.3 * sin(along / len * PI);
    float petal = smoothstep(width, 0.0, across) * smoothstep(0.0, len, along);
    return petal;
}
```

## Prompt Template

> "Lazy daisy [FLOWER] in [COLOR] floss, single detached chain loop petals radiating from center, teardrop shapes anchored at point, simple floral embroidery"

## Anti-Drift

- **Not chain stitch**: Lazy daisy is single detached loop; chain is continuous
- **Not satin stitch**: Lazy daisy is loop; satin is flat fill
- **Anchor is key**: The tack stitch at point defines the shape

---

*Loop up, tack down. The petal is the loop.*
