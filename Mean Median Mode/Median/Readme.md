# 📊 Median in Machine Learning

## 🤔 What is Median?

The median is a measure of central tendency that represents the middle value in a dataset when it is ordered in ascending or descending order. If the dataset has an odd number of observations, the median is the middle value. If the dataset has an even number of observations, the median is the average of the two middle values.

## 🧮 How to Calculate Median

1. **Order the Data**: Arrange the data points in ascending or descending order.
2. **Find the Middle**:
    - If the number of observations (n) is odd, the median is the value at position (n + 1) / 2.
    - If the number of observations (n) is even, the median is the average of the values at positions n / 2 and (n / 2) + 1.

## 📈 Example

For an odd number of observations:
```
Data: 3, 1, 4, 2, 5
Ordered Data: 1, 2, 3, 4, 5
Median: 3
```

For an even number of observations:
```
Data: 3, 1, 4, 2
Ordered Data: 1, 2, 3, 4
Median: (2 + 3) / 2 = 2.5
```

## 🤖 Use of Median in Machine Learning

1. **Handling Outliers**: The median is less affected by outliers and skewed data compared to the mean. This makes it a robust measure of central tendency in datasets with extreme values.
2. **Feature Engineering**: Median can be used to impute missing values in a dataset, especially when the data contains outliers.
3. **Model Evaluation**: In some machine learning models, the median can be used to evaluate the central tendency of prediction errors.

## 🏁 Conclusion

The median is a simple yet powerful statistical measure that is widely used in machine learning to handle outliers and skewed data. Understanding and utilizing the median can improve the robustness and accuracy of machine learning models.
