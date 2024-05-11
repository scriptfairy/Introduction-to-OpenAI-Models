import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# Load embeddings and labels


def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        X = [item['embedding'] for item in data]
        # Convert scores to boolean: True for positive, False for negative
        y = [item['score'] == 'True' for item in data]
    return X, y


X, y = load_data('embeddings.json')
# print("-------- X = \n ", X[1])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
# model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Testing realy amazing\n")
# "really amazing" victor
e1 = [0.343048632144928, -0.3309374749660492, -0.5637745261192322, 0.04711998626589775, 0.11376921832561493, -
      0.31761518120765686, -0.28869980573654175, 0.44205737113952637, -0.1346609741449356, 0.20498140156269073]
preds = model.predict([e1])

print(preds)
