# Load libraries required to load dataset and preprocess for modeling
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
# Load libraries required to save model as a pickle
import pickle
import joblib


### Create Perceptron Model with Iris dataset
class Perceptron:
    
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0 
            for xi, target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        # step function (if our net_input is higher than 0, we take our info that it's our 1st class, otherwise -1 class)
        return np.where(self.net_input(X) >= 0, 1, -1)


model = Perceptron()


# Defining X,y that will be input for Perceptron Model
# Load dataset
iris = load_iris()
df = pd.DataFrame(data = np.c_[iris['data'], iris['target']],
                 columns = iris['feature_names']+ ['target']) 

# Defining X,y using iloc since we need array for our computation
# X: using only sepal length, petal length
# y: using Target
X, y = df.iloc[:100, [0,2]].values, df.iloc[:100, 4]

# Preprocessing y for our model
def a(x):
    if x == 0:
        return -1
    else:
        return 1
    
y = y.map(a)
y = y.values


# Train Perceptron model
model.fit(X,y)

# Save the trained model as a pickle string.
saved_model = pickle.dumps(model)

# Save the model as a pickle in a file
joblib.dump(model, 'model.pkl')

