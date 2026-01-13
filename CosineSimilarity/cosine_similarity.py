import math

def cosine_similarity(x, y):
    dot_product = sum(a*b for a,b in zip(x,y))
    norm_x = math.sqrt(sum(a*a for a in x))
    norm_y = math.sqrt(sum(b*b for b in y))
    
    if norm_x == 0 or norm_y == 0:
        return 0.0
        
    return dot_product / (norm_x * norm_y)

x = [1, 1]
y = [1, 0]

sim = cosine_similarity(x, y)
print(f"Vector x: {x}")
print(f"Vector y: {y}")
print(f"Cosine Similarity: {sim:.4f}")