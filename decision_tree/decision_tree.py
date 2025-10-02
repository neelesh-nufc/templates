import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 1. Load Data (using Iris dataset as an example)
iris = load_iris()
X = iris.data  # Features
y = iris.target # Target variable
feature_names = iris.feature_names
target_names = iris.target_names

# 2. Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Create and Train the Decision Tree Classifier
# You can adjust parameters like 'criterion' (gini or entropy) and 'max_depth'
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 4. Make Predictions (Optional)
y_pred = clf.predict(X_test)

# 5. Evaluate the Model (Optional)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# 6. Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(clf, 
          feature_names=feature_names, 
          class_names=target_names,
          filled=True, 
          rounded=True)
plt.title("Decision Tree Classifier for Iris Dataset")
plt.show()