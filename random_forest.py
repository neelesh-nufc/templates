import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris # A built-in dataset

# 1. Load a dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Create a Random Forest Classifier
# n_estimators: Number of trees in the forest (e.g., 100)
# random_state: For reproducibility
# max_features: Controls feature randomness (sqrt for classification is common)
#               'sqrt' means sqrt(n_features) features are considered at each split
#               'log2' means log2(n_features) features are considered
#               an integer for a fixed number of features
#               a float for a percentage of features
clf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42, n_jobs=-1) 
# n_jobs=-1 uses all available CPU cores for faster training

# 3. Train the model
print("Training the Random Forest Classifier...")
clf.fit(X_train, y_train)
print("Training complete.")

# 4. Make predictions
y_pred = clf.predict(X_test)

# 5. Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 6. Feature Importance (a nice byproduct of Random Forests)
feature_importances = pd.Series(clf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nFeature Importances:")
print(feature_importances)

# Example prediction
sample_flower = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=iris.feature_names) # A Setosa-like flower
predicted_class_encoded = clf.predict(sample_flower)
predicted_flower_name = iris.target_names[predicted_class_encoded[0]]
print(f"\nPredicted class for sample flower: {predicted_flower_name}")