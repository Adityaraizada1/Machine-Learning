import numpy as np

def calculate_percentiles(data, percentiles):
    """
    Calculate the specified percentiles for the given data.

    Parameters:
    data (list or numpy array): The input data.
    percentiles (list): A list of percentiles to calculate (0-100).

    Returns:
    dict: A dictionary with percentiles as keys and the corresponding values.
    """
    data = np.array(data)
    results = {}
    for percentile in percentiles:
        results[percentile] = np.percentile(data, percentile)
    return results

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
percentiles = [25, 50, 75]
percentile_values = calculate_percentiles(data, percentiles)
print(percentile_values)