## Equations
citation: Thanks to a StackExchange Post that shows the induction of Shell's Law in Vector Form.

Components with respect to **n**

```math
\mathbf{r} = \mathbf{r}_{\parallel} + \mathbf{r}_{\perp}
```

One parallel and the other normal to axis **n** respectively:

```math
\mathbf{r}_{\parallel} = (\mathbf{n} \cdot \mathbf{r}) \mathbf{n}
```

```math
\mathbf{r}_{\perp} = (\mathbf{n} \times \mathbf{r}) \times \mathbf{n} = \mathbf{r} - (\mathbf{n} \cdot \mathbf{r}) \mathbf{n}
```

That is:

```math
\mathbf{r} = (\mathbf{n} \cdot \mathbf{r}) \mathbf{n} + (\mathbf{n} \times \mathbf{r}) \times \mathbf{n}
```

The vectors **t**, **i** are decomposed as follows:

```math
\mathbf{t} = (\mathbf{n} \cdot \mathbf{t}) \mathbf{n} + (\mathbf{n} \times \mathbf{t}) \times \mathbf{n}
```

```math
\mathbf{i} = (\mathbf{n} \cdot \mathbf{i}) \mathbf{n} + (\mathbf{n} \times \mathbf{i}) \times \mathbf{n}
```

Now, Snell's Law is expressed as:

```math
(\mathbf{n} \times \mathbf{t}) = \mu (\mathbf{n} \times \mathbf{i})
```

See Figure-02 in the bottom.

Equation (4) combined with (5) and (6) yields:

```math
\mathbf{t} = (\mathbf{n} \cdot \mathbf{t}) \mathbf{n} + \mu [\mathbf{i} - (\mathbf{n} \cdot \mathbf{i}) \mathbf{n}]
```

Taking norms in (7), and since the vector $ (\mathbf{n} \cdot \mathbf{t}) \mathbf{n} $ is normal to the vector $[\mathbf{i} - (\mathbf{n} \cdot \mathbf{i}) \mathbf{n}]$:

```math
\|\mathbf{t}\|^2 = (\mathbf{n} \cdot \mathbf{t})^2 + \mu^2 \|\mathbf{i} - (\mathbf{n} \cdot \mathbf{i}) \mathbf{n}\|^2
```

or:

```math
1 = (\mathbf{n} \cdot \mathbf{t})^2 + \mu^2 \left[ 1 - (\mathbf{n} \cdot \mathbf{i})^2 \right]
```

So:

```math
(\mathbf{n} \cdot \mathbf{t}) = \pm \sqrt{1 - \mu^2 \left[ 1 - (\mathbf{n} \cdot \mathbf{i})^2 \right]}
```

Since the angle between **n**, **t** is less than \(\pi/2\), we keep the plus sign in (10), and (7) yields finally:

```math
\mathbf{t} = \sqrt{1 - \mu^2 \left[ 1 - (\mathbf{n} \cdot \mathbf{i})^2 \right]} \mathbf{n} + \mu \left[ \mathbf{i} - (\mathbf{n} \cdot \mathbf{i}) \mathbf{n} \right]
```
