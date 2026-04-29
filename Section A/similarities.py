import math

## Creating some low level logics
def get_dot_product(vector1, vector2):
    sum = 0
    for i,j in zip(vector1, vector2):
        sum += (i*j)
    return sum

def get_magnitude_squared(vector):
    sum = 0
    for i in vector:
        sum += i**2
    return sum

def get_magnitude(vector):
    return math.sqrt(get_magnitude_squared(vector))

def get_binary_frequencies(vector1, vector2):
    f00 = f01 = f10 = f11 = 0
    for i,j in zip(vector1,vector2):
        if i ==0 and j == 0:
            f00 += 1
        elif i ==0 and j == 1:
            f01 += 1
        elif i ==1 and j == 0:
            f10 += 1
        else:
            f11 += 1
    return  f00, f01, f10, f11
   ## This looks more professional
   # return {'f00': f00 , 'f01': f01, 'f10': f10, 'f11': f11}

## Test done
# print(get_binary_frequencies([1,0,1,0,1],[1,1,1,1,1]))
# print(get_magnitude([1,0,1,0,1,0])

## Now building the core logics

def calculate_smc(vector1, vector2):
    """Simple Matching Coefficient: (f11 + f00) / total"""
    if len(vector1) != len(vector2):
        return {'Error' : "Both vector must be equal to find similarities"}
    else:
        f00, f01, f10, f11 = get_binary_frequencies(vector1, vector2)
    return (f00 + f11) / (f00 + f01 + f10 + f11)

def calculate_jaccard(vector1, vector2):
    """Jaccard Coefficient: f11 / (f11 + f10 + f01)"""
    if len(vector1) != len(vector2):
        return {'Error' : "Both vector must be equal to find similarities"}
    else:
        f00, f01, f10, f11 = get_binary_frequencies(vector1, vector2)
        return f11/(f01+f10+f11)

def calculate_cosine(vector1, vector2):
    """Cosine Similarity: (A.B) / (|A| * |B|)"""
    return (get_dot_product(vector1,vector2))/(get_magnitude(vector1)*get_magnitude(vector2))

def calculate_tanimoto(vector1, vector2):
    """Tanimoto Coefficient: (A.B) / (|A|^2 + |B|^2 - A.B)"""
    return get_dot_product(vector1,vector2)/(get_magnitude_squared(vector1)+get_magnitude_squared(vector2)-get_dot_product(vector1,vector2))

print(calculate_smc([1, 0, 1, 1, 0],[1, 1, 0, 1, 0]))
print(calculate_jaccard([1, 0, 1, 1, 0],[1, 1, 0, 1, 0]))
print(calculate_cosine([1.0, 9.0, 7.0],[2.0, 3.0, 8.0]))
print(calculate_tanimoto([1.0, 9.0, 7.0],[2.0, 3.0, 8.0]))