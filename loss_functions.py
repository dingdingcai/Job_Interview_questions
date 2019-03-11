import numpy as np
def cross_entropy(predictions, targets, epsilon=1e-12):
    """
    predictions: (N, K)
    targets:(N, k)
    return scalar
    """
    prob = np.exp(predictions) / np.sum(np.exp(predictions))
    predictions = np.clip(prob, epsilon, 1. - epsilon)
    CE = -np.mean(targets * (np.log(prob + 1e-9)))
    return CE


def Onehot(labels, classes):
    """
    convert label to onehot matrix
    target: N x 1 
    classes: the number of class
    """
    hot_matrix = np.zeros((len(labels), classes))
    for i, v in enumerate(labels):
        hot_matrix[i, v] = 1
    return hot_matrix


predictions = np.array([[0.5, 25, 35, 1],[0.01, 11, 0.21, 6]])
labels = np.array([3, 3])
classes = 4
targets = Onehot(labels, classes)
print(targets)
x = cross_entropy(predictions, targets)
print(x)
