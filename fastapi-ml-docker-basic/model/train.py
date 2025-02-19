import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Train a simple logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model/model.pkl")
