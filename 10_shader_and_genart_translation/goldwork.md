# Goldwork

Metal thread. Regal shine.

## What It Is

Goldwork is **embroidery using metal threads** — real gold, silver, or metal-wrapped threads — on fabric, often combined with silk and other materials. It's associated with royalty, religion, and military.

## Construction

- **Metal threads**: Real gold, silver, or copper-wrapped threads
- **Couching**: Thick metal threads laid and tacked
- **Purl threads**: Coiled metal springs cut and applied
- **Padding**: Felt or thread padding raises elements

## Visual DNA

- **Metallic shine**: Real metal reflects light
- **Dimensional**: Padded and raised elements
- **Rich and regal**: Luxurious, opulent appearance
- **Textured metal**: Smooth threads, coiled purl, checkered plate
- **Common uses**: Royal garments, military insignia, ecclesiastical, ceremonial

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `metallic_type` | gold/silver/copper | Metal color |
| `shine_intensity` | 0.8–1.0 | Real metal reflectivity |
| `padding_height` | 0.0–0.05 | Raised elements |
| `thread_variety` | 0–5 | Different metal thread types |

## GLSL Snippet

```glsl
float goldwork(vec2 uv, float shine) {
    float laid = couching_path(uv, thickness);
    float purl = coiled_metal(uv, scale);
    float plate = checkered_plate(uv, pattern);
    float metal = max(laid, max(purl, plate));
    return metal * shine * fresnel(normal, view);
}
```

## Prompt Template

> "Goldwork embroidery with [MOTIF] in real gold thread, couching and purl metal techniques, raised padded elements, regal ecclesiastical shine, ceremonial textile"

## Anti-Drift

- **Not metallic thread**: Goldwork uses real metal; metallic thread is synthetic
- **Not regular embroidery**: Goldwork is specifically metal thread techniques
- **Historical luxury**: Associated with royalty and religion

---

*Real metal, laid and tacked. The shine is the status.*
