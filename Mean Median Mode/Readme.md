# 📊 Mean, Median, and Mode in Machine Learning

## 📝 Introduction
In statistics and machine learning, mean, median, and mode are fundamental concepts used to describe the central tendency of a dataset. Understanding these measures is crucial for data analysis and interpretation.

## 📈 Mean
The mean, also known as the average, is the sum of all values in a dataset divided by the number of values. It is sensitive to outliers and can be skewed by extremely high or low values.

### 📐 Formula
\[ \text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n} \]

### 💡 Usage in Machine Learning
- **Feature Scaling**: Mean is used in normalization techniques to scale features.
- **Loss Functions**: Mean squared error (MSE) is a common loss function in regression tasks.

## 📉 Median
The median is the middle value of a dataset when it is ordered in ascending or descending order. It is less affected by outliers compared to the mean.

### 🔢 Calculation
- For an odd number of observations: Median is the middle value.
- For an even number of observations: Median is the average of the two middle values.

### 💡 Usage in Machine Learning
- **Robust Statistics**: Median is used in robust statistical methods to reduce the effect of outliers.
- **Imputation**: Median can be used to fill missing values in a dataset.

## 📊 Mode
The mode is the value that appears most frequently in a dataset. A dataset can have one mode, more than one mode, or no mode at all.

### 💡 Usage in Machine Learning
- **Categorical Data**: Mode is often used to summarize categorical data.
- **Imputation**: Mode can be used to fill missing categorical values.

## 🔍 Conclusion
Mean, median, and mode are essential statistical measures that provide insights into the distribution and central tendency of data. Their appropriate use in machine learning can enhance data preprocessing, feature engineering, and model evaluation.
