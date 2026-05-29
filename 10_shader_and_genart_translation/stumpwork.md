# Stumpwork

Raised embroidery. Sculptural thread.

## What It Is

Stumpwork is a **three-dimensional embroidery technique** where motifs are worked separately on a wire or padded foundation, then attached to the main fabric, creating sculptural, raised elements.

## Construction

- **Wire foundation**: Thin wire shapes the 3D elements
- **Detached work**: Motifs worked on separate fabric, then cut out
- **Padding**: Felt or thread padding raises elements
- **Attachment**: Sewn onto main fabric at edges

## Visual DNA

- **Dimensional elements**: Flowers, insects, figures standing proud
- **Wire edges**: Thin wire outlines visible at edges
- **Separate pieces**: Each element is an individual component
- **Sculptural depth**: Significant 3D relief
- **Common uses**: Caskets, boxes, mirror frames, ecclesiastical, royal pieces

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `element_height` | 0.0–0.1 | 3D relief |
| `wire_thickness` | 0.0005–0.002 | Thin wire edge |
| `padding_density` | 0.5–1.0 | How padded the elements |
| `motif_complexity` | 0.3–1.0 | Simple vs. elaborate |

## GLSL Snippet

```glsl
float stumpwork(vec2 uv, float height) {
    float motif = detached_element(uv, scale);
    float wire = wire_outline(uv, motif, thickness);
    float padding = padded_base(uv, motif, density);
    return max(motif * height, wire + padding);
}
```

## Prompt Template

> "Stumpwork embroidery with raised [MOTIF] elements, wire-edged dimensional pieces attached to silk ground, sculptural 3D thread art, 17th-century style"

## Anti-Drift

- **Not regular embroidery**: Stumpwork is 3D assembled; regular is flat
- **Not applique**: Stumpwork uses wire and padding; applique is fabric layers
- **Historical technique**: Associated with 17th-century English embroidery

---

*Wire, pad, attach. The dimension is the sculpture.*
