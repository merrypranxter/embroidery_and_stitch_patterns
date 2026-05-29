# Bullion Knot

The coil. Spring of thread.

## What It Is

Bullion knot is a **long coiled knot** created by wrapping thread many times around the needle and pulling through, forming a spring-like coil. It's used for dimensional details like stamens, horns, and textured dots.

## Construction

- **Many wraps**: Thread wrapped 5–20 times around needle
- **Pull through**: Needle drawn through all wraps
- **Coil forms**: Wraps spring into a tight coil
- **Anchor**: Coil secured at both ends

## Visual DNA

- **Spring coil**: Like a tiny metal spring made of thread
- **Dimensional**: Sits significantly proud of fabric
- **Textured surface**: Visible coil ridges
- **Varied length**: Short coils for dots, long for lines
- **Common uses**: Flower stamens, insect bodies, horns, textured dots

## Shader Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| `coil_length` | 0.01–0.05 | Length of coil |
| `wrap_count` | 5–20 | Number of thread wraps |
| `coil_diameter` | 0.002–0.005 | Thickness of coil |
| `height` | 0.0–0.02 | Dimensional relief |

## GLSL Snippet

```glsl
float bullion_knot(vec2 uv, vec2 pos, float len) {
    float along = dot(uv - pos, direction);
    float across = length(uv - pos - direction * along);
    float coil = smoothstep(0.0, 0.01, across) * smoothstep(0.0, len, along) * smoothstep(len, len - 0.01, along);
    float ridges = sin(along * wrap_count * PI / len) * 0.3 + 0.7;
    return coil * ridges * height;
}
```

## Prompt Template

> "Bullion knot [DETAIL] in [COLOR] floss, long coiled spring-like knot with visible ridges, dimensional thread coil, traditional embroidery detail"

## Anti-Drift

- **Not French knot**: Bullion is long coil; French is small round bead
- **Not cast-on stitch**: Bullion is wrapped and pulled; cast-on is knitted on
- **Coil texture**: The spring-like ridges are the signature

---

*Wrap many, pull once. The coil is the spring.*
