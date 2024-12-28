import numpy as np

def calculate_variance(data):
    mean = np.mean(data)
    variance = np.mean((data - mean) ** 2)
    return variance

def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    standard_deviation = np.sqrt(variance)
    return standard_deviation

# Example usage
data = [10, 12, 23, 23, 16, 23, 21, 16]
variance = calculate_variance(data)
standard_deviation = calculate_standard_deviation(data)

print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")