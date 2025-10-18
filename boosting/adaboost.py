from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# Load the Breast Cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target


print('name of the Features \n', data.feature_names)
print('name of the classes \n', data.target_names)
print('name of the classes \n', data.data.shape)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Logistic Regression Model
log_reg = LogisticRegression()
#AdaBoost classifier
adaboost = AdaBoostClassifier(n_estimators=500, random_state=42)

# Train the classifiers
log_reg.fit(X_train, y_train)
adaboost.fit(X_train, y_train)

# Make predictions on the test set
y_pred_1 = adaboost.predict(X_test)
y_pred_2 = log_reg.predict(X_test)

# Calculate the accuracy of the model
accuracy_1 = accuracy_score(y_test, y_pred_2)
accuracy_2 = accuracy_score(y_test, y_pred_1)
print("Accuracy of logistic Regression:", accuracy_1)
print("Accuracy of AdaBoost:", accuracy_2)