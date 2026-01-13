def tanimoto_coefficient(x, y):
    dot_xy = sum(a*b for a,b in zip(x,y))
    dot_xx = sum(a*a for a in x)
    dot_yy = sum(b*b for b in y)
    
    denom = dot_xx + dot_yy - dot_xy
    
    if denom == 0: return 0.0
    return dot_xy / denom

x = [1, 1]
y = [1, 0]

sim = tanimoto_coefficient(x, y)
print(f"Vector x: {x}")
print(f"Vector y: {y}")
print(f"Tanimoto Coefficient: {sim:.4f}")