# Importing libraries
import pandas as pd 
import numpy as np
from sklearn import metrics
import pickle
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC



# Reading data
df = pd.read_csv("heart.csv")
print(df.head(10))


# Selecting feature columns and the predicted class column
feature_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

predicted_class = ['target']


# Splitting the data into training and testing sets
X = df[feature_columns]
y = df[predicted_class]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=10)

print("Training Data")
print(X_train.shape)
print(y_train.shape)
print("\n")
print("Testing Data")
print(X_test.shape)
print(y_test.shape)

# Handling missing values
fill_values = SimpleImputer(missing_values=0, strategy="mean")

X_train = fill_values.fit_transform(X_train)
X_test = fill_values.fit_transform(X_test)

# Creating an SVM model and training it on the training data
svm_model = SVC(random_state=10)

model = svm_model.fit(X_train, y_train.values.ravel())

# Saving the trained model to a file
pickle.dump(model, open("SVMmodel111.pkl", 'wb'))


# Making predictions on the testing data
Y_pred = model.predict(X_test)


# Calculating accuracy
acc_score = metrics.accuracy_score(y_test, Y_pred)
print("SVM Accuracy =", acc_score)


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# Calculate precision, recall, and F1-score
precision = precision_score(y_test, Y_pred)
recall = recall_score(y_test, Y_pred)
f1 = f1_score(y_test, Y_pred)

print("SVM Precision =", precision)
print("SVM Recall =", recall)
print("SVM F1-Score =", f1)

# Plot confusion matrix
cm = confusion_matrix(y_test, Y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix of SVM')
plt.savefig('RESULT/svm_cm.png')
plt.show()
