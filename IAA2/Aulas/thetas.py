import numpy as np


def slr(feature1, feature2):
    n = len(feature1)
    
    mean_feature1 = np.mean(feature1)
    mean_feature2 = np.mean(feature2)
    
    numerator = np.sum((feature1 - mean_feature1) * (feature2 - mean_feature2))
    denominator = np.sum((feature1 - mean_feature1) ** 2)
    theta1 = round(numerator / denominator, 4)
    
    theta2 = round(mean_feature2 - theta1 * mean_feature1, 4)
    
    return theta1, theta2
feature1 = np.array([1, 2, 4, 5, 6, 7, 8])
feature2 = np.array([2, 4, 6, 8, 10, 12, 14])
theta1, theta2 = slr(feature1, feature2)
print(theta1, theta2)