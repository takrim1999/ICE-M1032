def nominal_dissimilarity(x, y):
    """
    Calculates dissimilarity for nominal attributes.
    d(i, j) = (p - m) / p
    """
    if len(x) != len(y):
        raise ValueError("Vectors must be same length")
    
    p = len(x)
    m = 0 # matches
    
    for i in range(p):
        if x[i] == y[i]:
            m += 1
            
    return (p - m) / p

# Example Data
x = ["Circle", "Red", "Small"]
y = ["Circle", "Blue", "Small"]

dist = nominal_dissimilarity(x, y)
print(f"Object x: {x}")
print(f"Object y: {y}")
print(f"Nominal Dissimilarity: {dist:.4f}")
print(f"Nominal Similarity: {1 - dist:.4f}")