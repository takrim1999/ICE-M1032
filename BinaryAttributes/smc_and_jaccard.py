def binary_measures(x, y):
    q = r = s = t = 0
    for i in range(len(x)):
        if x[i] == 1 and y[i] == 1: q += 1
        elif x[i] == 1 and y[i] == 0: r += 1
        elif x[i] == 0 and y[i] == 1: s += 1
        elif x[i] == 0 and y[i] == 0: t += 1
    
    # Simple Matching Coefficient (Symmetric)
    smc_dist = (r + s) / (q + r + s + t)
    
    # Jaccard (Asymmetric)
    # Handle division by zero if vectors are all zeros
    denom_jac = q + r + s
    jac_dist = (r + s) / denom_jac if denom_jac != 0 else 0.0
    
    return smc_dist, jac_dist

# Example Data
x = [1, 0, 0, 1]
y = [1, 0, 1, 0]

smc, jaccard = binary_measures(x, y)
print(f"x: {x}")
print(f"y: {y}")
print(f"Symmetric (SMC) Distance: {smc:.4f}")
print(f"Asymmetric (Jaccard) Distance: {jaccard:.4f}")