# Hardanger

Norwegian counted. Cut and withdrawn.

## What It Is

Hardanger is a **Norwegian counted-thread embroidery** combining satin stitch blocks, cutwork, and needle weaving. It creates geometric patterns with open, lacy areas and solid, dense areas.

## Construction

- **Satin stitch kloster blocks**: Solid rectangular blocks of satin stitches
- **Cutting**: Threads cut between blocks to create open areas
- **Needle weaving**: Threads woven over open areas to create patterns
- **Withdrawn threads**: Some threads removed, others remain

## Visual DNA

- **Solid blocks**: Dense satin-stitched rectangles
- **Open spaces**: Cut and withdrawn thread areas
- **Woven bars**: Threads woven across open areas
- **Geometric precision**: Counted, symmetrical patterns
- **Common uses**: Table linens, doilies, samplers, Christmas ornaments

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `block_size` | 0.02–0.05 | Kloster block dimensions |
| `open_ratio` | 0.2–0.6 | Percentage of open space |
| `weave_pattern` | 0–3 | Needle weave style over openings |
| `geometric_type` | 0–5 | Star, diamond, square motifs |

## GLSL Snippet

```glsl
float hardanger(vec2 uv, float block) {
    float solid = kloster_block(uv, block);
    float open = cut_area(uv, block);
    float woven = needle_weave(uv, open, pattern);
    return max(solid, woven);
}
```

## Prompt Template

> "Hardanger embroidery in white cotton, satin-stitch kloster blocks with cutwork open spaces and woven bars, geometric Norwegian counted-thread lace"

## Anti-Drift

- **Not pulled thread**: Hardanger cuts threads; pulled thread distorts without cutting
- **Counted thread**: Must align to even-weave grid
- **Norwegian origin**: Specifically from Hardanger region

---

*Satin, cut, weave. The block is the foundation.*
