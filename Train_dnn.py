#import libraries
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2
import joblib


# Reading data
df = pd.read_csv("heart.csv")

# Display the first 10 rows of the dataset
print(df.head(10))

# Define the feature columns and the predicted class column
feature_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

predicted_class = ['target']

# Split the dataset into training and testing sets
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

# Impute missing values
fill_values = SimpleImputer(missing_values=0, strategy="mean")


X_train = fill_values.fit_transform(X_train)
X_test = fill_values.transform(X_test)

print("------------Before Scaling----------")
print(X_train)
# Normalize the data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("------------After Scaling----------")
print(X_train)


# Create a DNN model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],), kernel_regularizer=l2(0.001)))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))



# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print(model.summary())

# Train the model
model.fit(X_train, y_train, epochs=500, batch_size=32)

# Save the model
model.save("DNN_model11.h5")


# Evaluate the model
_, accuracy = model.evaluate(X_test, y_test)
print("DNN Accuracy =", accuracy)

from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, plot_confusion_matrix
import matplotlib.pyplot as plt

# Make predictions
y_pred = model.predict(X_test)
y_pred_binary = (y_pred > 0.5).astype(int)

# Calculate metrics
precision = precision_score(y_test, y_pred_binary)
recall = recall_score(y_test, y_pred_binary)
f1 = f1_score(y_test, y_pred_binary)

print("DNN Precision =", precision)
print("DNN Recall =", recall)
print("DNN F1-Score =", f1)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred_binary)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix of DNN")
plt.colorbar()

tick_marks = np.arange(2)
plt.xticks(tick_marks, ['Class 0', 'Class 1'])
plt.yticks(tick_marks, ['Class 0', 'Class 1'])

plt.xlabel('Predicted')
plt.ylabel('True')

for i in range(2):
    for j in range(2):
        plt.text(j, i, format(conf_matrix[i, j], 'd'), horizontalalignment="center", color="white" if conf_matrix[i, j] > conf_matrix.max() / 2 else "black")

plt.savefig('RESULT/dnn_cm.png')
plt.show()