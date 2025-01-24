# %%
import pandas as pd

data=pd.read_csv('merged_data.csv')
data.info()


# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load Data
data = pd.read_csv("merged_data.csv")

# Preprocess Data
# Convert categorical columns into numerical data using Label Encoding
label_encoder = LabelEncoder()

# Encoding Age Group
data['Age_Group'] = label_encoder.fit_transform(data['Age_Group'])

# Handle missing values
data.fillna({'Preferred_Bus_Type': 'Unknown', 'Rating': data['Rating'].mean()}, inplace=True)

# One-hot encode categorical columns (e.g., 'Preferred_Bus_Type', 'Gender')
data_encoded = pd.get_dummies(data, columns=['Preferred_Bus_Type', 'Gender'], drop_first=True)

# Features and Target
X = data_encoded[['Age_Group', 'Seats_Booked', 'Distance (km)', 'Ticket_Price (INR)']]
y = data_encoded['Destination']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

# Evaluate Model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


# Example Recommendation for a Test Customer
test_customer = X_test.iloc[0].to_frame().T  # Convert to a DataFrame with a single row
predicted_destination = clf.predict(test_customer)
print("Customer Details:\n", test_customer)



print(f"Recommended Destination: {predicted_destination[0]}")


# %%



