# Crewel Work

Wool on linen. Jacobean florals.

## What It Is

Crewel work is **surface embroidery using wool thread** on a sturdy fabric ground (usually linen twill). It's characterized by bold, flowing Jacobean-style floral designs and textured stitches.

## Construction

- **Wool thread**: 2-ply crewel wool, soft and thick
- **Linen twill ground**: Sturdy fabric that supports heavy stitching
- **Free-form**: Not counted; worked from printed or drawn design
- **Varied stitches**: Many stitch types in one piece

## Visual DNA

- **Bold wool texture**: Thick, soft, matte wool stitches
- **Flowing florals**: Elaborate Jacobean-style flowers and vines
- **Rich colors**: Deep, saturated wool colors
- **Textured surface**: Dimensional from thick wool
- **Common uses**: Wall hangings, cushions, curtains, traditional English embroidery

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `thread_thickness` | 0.003–0.01 | Wool diameter |
| `texture_matte` | 0.8–1.0 | Wool has no sheen |
| `color_depth` | 0.7–1.0 | Rich saturated wool |
| `floral_scale` | 0.1–0.5 | Jacobean motif size |

## GLSL Snippet

```glsl
float crewel_work(vec2 uv, float thickness) {
    float wool = wool_texture(uv, scale) * thickness;
    float floral = jacobean_pattern(uv, motif_scale);
    return wool * floral;
}
```

## Prompt Template

> "Crewel work embroidery in rich wool on linen twill, bold Jacobean floral design with flowing vines, thick matte wool texture, traditional English embroidery"

## Anti-Drift

- **Not cross stitch**: Crewel is free-form surface; cross is counted grid
- **Not needlepoint**: Crewel is surface; needlepoint covers canvas
- **Wool specific**: Crewel uses wool; other embroidery uses cotton or silk

---

*Wool on linen, free-form florals. The Jacobean is the style.*
