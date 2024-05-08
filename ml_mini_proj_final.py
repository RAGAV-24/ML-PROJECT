# -*- coding: utf-8 -*-
"""ml mini proj .final

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SfBuFga94ls0H8x4YTcD0KlH45mM1Rdb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.metrics import classification_report

df=pd.read_csv("/content/Copy of prediction - Copy of prediction.csv")

df

df.info()

df.isnull().sum()

print(df.columns)

df[df['Unnamed: 2'].isnull()]

# Assuming 'df' is your DataFrame and 'column_name' is the name of the column you want to remove
column_name = 'Unnamed: 2'
df = df.drop(column_name, axis=1)

df.isnull().sum()

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

# Assuming 'df' is your DataFrame and 'target_column' is the name of the target column
target_column = 'Final hardness (HRC) - post tempering'

# Drop rows with missing values
df.dropna(inplace=True)

# Split the data into features (X) and target variable (y)
X = df.drop(target_column, axis=1)
y = df[target_column]

# Identify categorical columns
categorical_cols = X.select_dtypes(include=['object']).columns

# One-hot encode categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'
)

X_encoded = preprocessor.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create the multilinear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train_scaled, y_train)

from sklearn.metrics import r2_score

# Make predictions on the training data
y_train_pred = model.predict(X_train_scaled)

# Compute the R-squared (R2) score
r2_train = r2_score(y_train, y_train_pred)

print(f"Multilinear Regression R-squared (R2) score on training data: {r2_train:.4f}")

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous target variable into class labels for training data
y_train1_classes = np.digitize(y_train, bins=thresholds)

from sklearn.metrics import classification_report

# Convert continuous predictions on the training data into class labels
y_train1_pred_classes = np.digitize(y_train_pred, bins=thresholds)


# Print the classification report for the training data
print("Classification Report (Training Data):")
print(classification_report(y_train_classes, y_train_pred_classes))

from sklearn.metrics import r2_score

# Compute R-squared (R2) score for the test data
r2_test = r2_score(y_test, y_test_pred)

print(f"R-squared (R2) score on test data: {r2_test:.4f}")

import numpy as np

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous target variable into class labels
y_test_classes = np.digitize(y_test, bins=thresholds)

from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(y_test_classes, y_pred_classes))

from sklearn.ensemble import RandomForestRegressor

# Initialize the Random Forest Regressor model
model2 = RandomForestRegressor(n_estimators=600, random_state=55)

# Fit the model to the training data
model2.fit(X_train, y_train)

from sklearn.metrics import r2_score

# Make predictions on the training data
y_train_pred = model2.predict(X_train)

# Compute R-squared (R2) score
r2_train = r2_score(y_train, y_train_pred)

print(f"RandomForestRegressor R-squared (R2) score on training data: {r2_train:.4f}")

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous target variable into class labels for training data
y_train_classes = np.digitize(y_train, bins=thresholds)

from sklearn.metrics import classification_report

# Convert continuous predictions on the training data into class labels
y_train_pred_classes = np.digitize(y_train_pred, bins=thresholds)

# Print the classification report for the training data
print("Classification Report (Training Data):")
print(classification_report(y_train_classes, y_train_pred_classes))

from sklearn.metrics import r2_score

# Make predictions on the test data
y_test_pred = model2.predict(X_test)

# Compute R-squared (R2) score for the test data
r2_test = r2_score(y_test, y_test_pred)

print(f"RandomForestRegressor R-squared (R2) score on test data: {r2_test:.4f}")

import numpy as np

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous predictions into class labels
y_pred_classes = np.digitize(y_test_pred, bins=thresholds)

from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(y_test_classes, y_pred_classes))

from sklearn.tree import DecisionTreeRegressor

# Create the Decision Tree Regressor model
dt_model = DecisionTreeRegressor(random_state=42)

# Fit the model to the training data
dt_model.fit(X_train, y_train)

from sklearn.metrics import r2_score

# Make predictions on the training data
y_train_pred_dt = dt_model.predict(X_train)

# Compute R-squared (R2) score for the training data
r2_train_dt = r2_score(y_train, y_train_pred_dt)

print(f"Decision Tree Regressor R-squared (R2) score on training data: {r2_train_dt:.4f}")

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous target variable into class labels for training data
y_train_classes = np.digitize(y_train, bins=thresholds)

from sklearn.metrics import classification_report

# Convert continuous predictions on the training data into class labels
y_train_pred_classes = np.digitize(y_train_pred, bins=thresholds)

# Print the classification report for the training data
print("Classification Report (Training Data):")
print(classification_report(y_train_classes, y_train_pred_classes))

#Make predictions on the test data
y_test_pred_dt = dt_model.predict(X_test)

# Compute R-squared (R2) score for the test data
r2_test_dt = r2_score(y_test, y_test_pred_dt)

print(f"Decision Tree Regressor R-squared (R2) score on test data: {r2_test_dt:.4f}")

import numpy as np

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous predictions into class labels
y_pred_classes = np.digitize(y_test_pred, bins=thresholds)

from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(y_test_classes, y_pred_classes))

from sklearn.ensemble import GradientBoostingRegressor

# Create the Gradient Boosting Regressor model
gb_model = GradientBoostingRegressor(random_state=42)

# Fit the model to the training data
gb_model.fit(X_train, y_train)

from sklearn.metrics import r2_score

# Make predictions on the training data
y_train_pred_gb = gb_model.predict(X_train)

# Compute R-squared (R2) score for the training data
r2_train_gb = r2_score(y_train, y_train_pred_gb)

print(f"Gradient Boosting Regressor R-squared (R2) score on training data: {r2_train_gb:.4f}")

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous target variable into class labels for training data
y_train_classes = np.digitize(y_train, bins=thresholds)

from sklearn.metrics import classification_report

# Convert continuous predictions on the training data into class labels
y_train_pred_classes = np.digitize(y_train_pred, bins=thresholds)

# Print the classification report for the training data
print("Classification Report (Training Data):")
print(classification_report(y_train_classes, y_train_pred_classes))

# Make predictions on the test data
y_test_pred_gb = gb_model.predict(X_test)

# Compute R-squared (R2) score for the test data
r2_test_gb = r2_score(y_test, y_test_pred_gb)

print(f"Gradient Boosting Regressor R-squared (R2) score on test data: {r2_test_gb:.4f}")

import numpy as np

# Define thresholds to categorize predictions into classes
thresholds = [50, 60, 70]  # Adjust these thresholds as needed

# Convert continuous predictions into class labels
y_pred_classes = np.digitize(y_test_pred, bins=thresholds)

from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(y_test_classes, y_pred_classes))

# Calculate the accuracy of the multilinear regression model
multilinear_accuracy = model.score(X_test_scaled, y_test)

# Print the accuracy
print(f"Multilinear Regression Accuracy: {multilinear_accuracy:.4f}")

# Calculate the accuracy of the Random Forest classifier model
randomforest_accuracy = model2.score(X_test, y_test)

# Print the accuracy
print(f"Random Forest Classifier Accuracy: {randomforest_accuracy:.4f}")

# Calculate the accuracy of the Decision Tree regressor model
decisiontree_accuracy = dt_model.score(X_test, y_test)

# Print the accuracy
print(f"Decision Tree Regressor Accuracy: {decisiontree_accuracy:.4f}")

# Calculate the accuracy of the Gradient Boosting regressor model
gradientboosting_accuracy = gb_model.score(X_test, y_test)

# Print the accuracy
print(f"Gradient Boosting Regressor Accuracy: {gradientboosting_accuracy:.4f}")

# Calculate the training accuracy of the Multilinear Regression model
multilinear_training_accuracy = model.score(X_train_scaled, y_train)

# Print the training accuracy
print(f"Multilinear Regression Training Accuracy: {multilinear_training_accuracy:.4f}")

# Calculate the training accuracy of the Random Forest model
randomforest_training_accuracy = model2.score(X_train, y_train)

# Print the training accuracy
print(f"Random Forest Training Accuracy: {randomforest_training_accuracy:.4f}")

# Calculate the training accuracy of the Decision Tree model
decisiontree_training_accuracy = dt_model.score(X_train, y_train)

# Print the training accuracy
print(f"Decision Tree Training Accuracy: {decisiontree_training_accuracy:.4f}")

# Calculate the training accuracy of the Gradient Boosting model
gradientboosting_training_accuracy = gb_model.score(X_train, y_train)

# Print the training accuracy
print(f"Gradient Boosting Training Accuracy: {gradientboosting_training_accuracy:.4f}")

# Accuracy values
accuracies = [multilinear_training_accuracy, randomforest_training_accuracy, decisiontree_training_accuracy, gradientboosting_training_accuracy]

# Model names
model_names = ['Multilinear Regression', 'Random Forest', 'Decision Tree', 'Gradient Boosting']

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(model_names, accuracies, color='skyblue')

# Adding labels and title
plt.xlabel('Models')
plt.ylabel('Training Accuracy')
plt.title('Trained Model Accuracies')
plt.ylim(0, 1)  # set y-axis limit to make the differences clearer
plt.xticks(rotation=45)  # rotate x-axis labels for better readability
plt.grid(axis='y')  # add gridlines on y-axis for better estimation

# Display the bar chart
plt.show()

import matplotlib.pyplot as plt

# Test accuracy values
test_accuracies = [multilinear_accuracy, randomforest_accuracy, decisiontree_accuracy, gradientboosting_accuracy]

# Model names
model_names = ['Multilinear Regression', 'Random Forest Classifier', 'Decision Tree Regressor', 'Gradient Boosting Regressor']

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(model_names, test_accuracies, color='lightgreen')

# Adding labels and title
plt.xlabel('Models')
plt.ylabel('Test Accuracy')
plt.title('Test Model Accuracies')
plt.ylim(0, 1)  # set y-axis limit to make the differences clearer
plt.xticks(rotation=45)  # rotate x-axis labels for better readability
plt.grid(axis='y')  # add gridlines on y-axis for better estimation

# Display the bar chart
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Training accuracy values
train_accuracies = [multilinear_training_accuracy, randomforest_training_accuracy, decisiontree_training_accuracy, gradientboosting_training_accuracy]

# Test accuracy values
test_accuracies = [multilinear_accuracy, randomforest_accuracy, decisiontree_accuracy, gradientboosting_accuracy]

# Model names
model_names = ['Multilinear Regression', 'Random Forest', 'Decision Tree', 'Gradient Boosting']

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 6))

# Set the width of the bars
bar_width = 0.35

# Set the position of the bars on the x-axis
r1 = np.arange(len(train_accuracies))
r2 = [x + bar_width for x in r1]

# Darker colors
train_color = '#1f77b4'  # dark blue
test_color = '#2ca02c'   # dark green

# Plotting the bars
train_bars = ax.bar(r1, train_accuracies, color=train_color, width=bar_width, edgecolor='black', label='Training Accuracy')
test_bars = ax.bar(r2, test_accuracies, color=test_color, width=bar_width, edgecolor='black', label='Test Accuracy')

# Adding labels and title
ax.set_xlabel('Models', fontweight='bold')
ax.set_ylabel('Accuracy', fontweight='bold')
ax.set_title('Comparison of Training and Test Accuracies', fontweight='bold')
ax.set_xticks([r + bar_width / 2 for r in range(len(train_accuracies))])
ax.set_xticklabels(model_names, rotation=45)
ax.set_ylim(0, 1)  # set y-axis limit to make the differences clearer
ax.grid(axis='y', linestyle='--', color='grey', alpha=0.5)  # add gridlines on y-axis for better estimation

# Adding legend
ax.legend()

# Show plot
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
points = ['precision', 'recall', 'f1-score', 'accuracy']
values = [0.55,0.54,0.55, 0.86]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold']
patterns = ['/', 'x', 'o', '|']
point = [1, 2, 3, 4]

bar_width = 0.85

# Create an array of indices to position the bars
indices = np.arange(len(point))

# Plotting
bars = []
for i in range(len(point)):
    bar = plt.bar(i, values[i], color=colors[i], width=bar_width, edgecolor='black', hatch=patterns[i], label=points[i])
    bars.append(bar)

# Adding labels and title
plt.xlabel('Report')
plt.ylabel('Value')
plt.title('Multi liner regession')

# Adding data labels
for i, v in enumerate(values):
    plt.text(i, v + 0.02, str(v), ha='center', va='bottom')

plt.xticks(indices, point)
plt.ylim(0, 1.4)

# Create legend with patterns
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', hatch=patterns[i], label=points[i]) for i in range(len(points))]
plt.legend(handles=legend_elements, loc='upper right')

plt.show()

# Precision, recall, and F1-score for each class
precision = [0.99, 0.90, 0.88,0]
recall = [0.99, 0.92, 0.79,0]
f1_score = [0.99, 0.91, 0.83,0]

# Computing the average values
average_precision = sum(precision) / len(precision)
average_recall = sum(recall) / len(recall)
average_f1_score = sum(f1_score) / len(f1_score)

print("Average Precision:", average_precision)
print("Average Recall:", average_recall)
print("Average F1-score:", average_f1_score)

"""GRADIENT BOOOSTING

"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
points = ['precision', 'recall', 'f1-score', 'accuracy']
values = [0.69,0.67,0.68, 0.97]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold']
patterns = ['/', 'x', 'o', '|']
point = [1, 2, 3, 4]

bar_width = 0.85

# Create an array of indices to position the bars
indices = np.arange(len(point))

# Plotting
bars = []
for i in range(len(point)):
    bar = plt.bar(i, values[i], color=colors[i], width=bar_width, edgecolor='black', hatch=patterns[i], label=points[i])
    bars.append(bar)

# Adding labels and title
plt.xlabel('Report')
plt.ylabel('Value')
plt.title('Gradient Boosting')

# Adding data labels
for i, v in enumerate(values):
    plt.text(i, v + 0.02, str(v), ha='center', va='bottom')

plt.xticks(indices, point)
plt.ylim(0, 1.4)

# Create legend with patterns
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', hatch=patterns[i], label=points[i]) for i in range(len(points))]
plt.legend(handles=legend_elements, loc='upper right')

plt.show()

"""Desicion Tree

"""

# Precision, recall, and F1-score for each class
precision = [0.99, 0.97, 0.98,0]
recall = [1.00, 0.95, 0.95,0]
f1_score = [0.99, 0.96, 0.97,0]

# Computing the average values
average_precision = sum(precision) / len(precision)
average_recall = sum(recall) / len(recall)
average_f1_score = sum(f1_score) / len(f1_score)

print("Average Precision:", average_precision)
print("Average Recall:", average_recall)
print("Average F1-score:", average_f1_score)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
points = ['precision', 'recall', 'f1-score', 'accuracy']
values = [0.73,0.72,0.73, 1.00]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold']
patterns = ['/', 'x', 'o', '|']
point = [1, 2, 3, 4]

bar_width = 0.85

# Create an array of indices to position the bars
indices = np.arange(len(point))

# Plotting
bars = []
for i in range(len(point)):
    bar = plt.bar(i, values[i], color=colors[i], width=bar_width, edgecolor='black', hatch=patterns[i], label=points[i])
    bars.append(bar)

# Adding labels and title
plt.xlabel('Report')
plt.ylabel('Value')
plt.title('Desicion Tree')

# Adding data labels
for i, v in enumerate(values):
    plt.text(i, v + 0.02, str(v), ha='center', va='bottom')

plt.xticks(indices, point)
plt.ylim(0, 1.4)

# Create legend with patterns
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', hatch=patterns[i], label=points[i]) for i in range(len(points))]
plt.legend(handles=legend_elements, loc='upper right')

plt.show()

"""Random  Forest

"""

# Precision, recall, and F1-score for each class
precision = [0.99, 0.90, 0.88,0]
recall = [0.99, 0.92, 0.79,0]
f1_score = [0.99, 0.91, 0.83,0]

# Computing the average values
average_precision = sum(precision) / len(precision)
average_recall = sum(recall) / len(recall)
average_f1_score = sum(f1_score) / len(f1_score)

print("Average Precision:", average_precision)
print("Average Recall:", average_recall)
print("Average F1-score:", average_f1_score)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
points = ['precision', 'recall', 'f1-score', 'accuracy']
values = [0.69,0.67,0.68,0.99]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold']
patterns = ['/', 'x', 'o', '|']
point = [1, 2, 3, 4]

bar_width = 0.85

# Create an array of indices to position the bars
indices = np.arange(len(point))

# Plotting
bars = []
for i in range(len(point)):
    bar = plt.bar(i, values[i], color=colors[i], width=bar_width, edgecolor='black', hatch=patterns[i], label=points[i])
    bars.append(bar)

# Adding labels and title
plt.xlabel('Report')
plt.ylabel('Value')
plt.title('Random Forest')

# Adding data labels
for i, v in enumerate(values):
    plt.text(i, v + 0.02, str(v), ha='center', va='bottom')

plt.xticks(indices, point)
plt.ylim(0, 1.4)

# Create legend with patterns
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', hatch=patterns[i], label=points[i]) for i in range(len(points))]
plt.legend(handles=legend_elements, loc='upper right')

plt.show()

"""FINAL ALGORITHM ACCURACY COMPARISION

"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
points = ['MULTILINEAR REGRESSION', 'RANDOM FOREST', 'DECISION TREE', 'GRADIENT BOOSTING']
values = [0.86, 0.99, 1.00, 0.97]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold']
patterns = ['/', 'x', 'o', '|']
point = [1, 2, 3, 4]

bar_width = 0.85

# Create an array of indices to position the bars
indices = np.arange(len(point))

# Plotting
bars = []
for i in range(len(point)):
    bar = plt.bar(i, values[i], color=colors[i], width=bar_width, edgecolor='black', hatch=patterns[i], label=points[i])
    bars.append(bar)

# Adding labels and title
plt.xlabel('ALGORITHM')
plt.ylabel('ACCURACY')
plt.title('Algorithm Accuracy Comparison')

# Adding data labels
for i, v in enumerate(values):
    plt.text(i, v + 0.02, str(v), ha='center', va='bottom')

plt.xticks(indices, point)
plt.ylim(0, 1.6)

# Create legend with patterns
legend_elements = [Patch(facecolor=colors[i], edgecolor='black', hatch=patterns[i], label=points[i]) for i in range(len(points))]
plt.legend(handles=legend_elements, loc='upper right')

plt.show()