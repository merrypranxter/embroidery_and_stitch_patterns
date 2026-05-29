# Couching

Lay and tack. Gold thread held.

## What It Is

Couching lays **thick or expensive threads on fabric surface** and tacks them down with small stitches. It's used for goldwork, thick yarns, and threads too heavy to pass through fabric.

## Construction

- **Lay thread**: Thick thread placed on fabric surface
- **Tack down**: Small stitches (couching stitches) hold it in place
- **Directional laying**: Thread follows design path
- **Decorative tacks**: Tacking stitches can be decorative

## Visual DNA

- **Thick laid thread**: Heavy cord or metal thread on surface
- **Visible tacks**: Small stitches crossing the laid thread
- **Dimensional**: Thick thread sits proud of fabric
- **Rich material**: Often gold, silver, silk, or wool
- **Common uses**: Goldwork, ecclesiastical, crewel, heavy decorative lines

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `laid_thickness` | 0.005–0.02 | Heavy thread diameter |
| `tack_size` | 0.001–0.003 | Small holding stitch |
| `tack_spacing` | 0.01–0.03 | Distance between tacks |
| `material` | gold/silver/wool/silk | Thread type |

## GLSL Snippet

```glsl
float couching(vec2 uv, float thickness) {
    float laid = line_sdf(uv, path) < thickness ? 1.0 : 0.0;
    float tack = mod(path_distance(uv, path), tack_spacing) < tack_size ? 1.0 : 0.0;
    return max(laid, tack * 0.5);
}
```

## Prompt Template

> "Couched gold thread in [PATTERN] on dark velvet, thick metallic cord laid on surface and tacked with small stitches, dimensional rich ecclesiastical embroidery"

## Anti-Drift

- **Not laid work**: Couching specifically has tacking stitches; laid work may not
- **Not stem stitch**: Couching uses separate thick thread; stem is twisted floss
- **Thread too thick**: Couching is for threads that can't pass through fabric

---

*Lay, tack, lay, tack. The thread is too precious to pull through.*
