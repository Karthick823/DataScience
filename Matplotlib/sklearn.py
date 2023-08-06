from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import numpy as np

iris = load_iris()
features = iris.data.T

print(features)