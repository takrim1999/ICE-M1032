import math

## Dataset

data = [
['Mid', 'Fair', 'Employee', 'Average', 'Yes'],
['Mid', 'Fair', 'Employee', 'Max', 'No'],
['Young', 'Low', 'Student', 'Min', 'Yes'],
['Old', 'High', 'Employee', 'Max', 'No'],
['Old', 'Fair', 'Retire', 'Average', 'No'],
['Young', 'Low', 'Student', 'Min', 'Yes'],
['Young', 'Fair', 'Employee', 'Average', 'Yes'],
['Mid', 'Low', 'Employee', 'Max', 'No'],
['Young', 'Fair', 'Student', 'Average', 'Yes'],
['Old', 'High', 'Retire', 'Min', 'No'],
['Young', 'Fair', 'Employee', 'Average', 'Yes'],
['Mid', 'Low', 'Employee', 'Max', 'Yes']
]

features = ['Age', 'Income', 'Status', 'Credit']

## Core logics

def calculate_entropy(p):
    return -p * math.log2(p) if p != 0 else 0

def get_entropy(dataset):
    total = len(dataset)
    yes_count = sum(1 for row in dataset if row[-1]=="Yes")
    no_count = total - yes_count

    return calculate_entropy(yes_count/total) + calculate_entropy(no_count/total)

def information_gain(dataset, index):
    total_entropy = get_entropy(dataset)
    values = set(row[index] for row in dataset)
    weighted_entropy = 0
    print(f"Feature: {features[index]}")

    for v in values:
        subset = [row for row in dataset if row[index] == v]
        weight = len(subset)/len(dataset)
        subset_entropy = get_entropy(subset)
        weighted_entropy += weight * subset_entropy
        gain = total_entropy - weighted_entropy
        print(f"Information Gain: {round(gain,3)}")
        return gain

print("Entropy of Dataset: ", round(get_entropy(data)),3)
gains = []
print("Information Gains")
for i in range(len(features)):
    g = information_gain(data,i)
    gains.append(g)

best_index = gains.index(max(gains))
print("Best Attribute:", features[best_index])

