# -*- coding: utf-8 -*-
"""Googleplaystore.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14YSjbpV1I2PP7SonUmRBmDMtQ7wbe0UF
"""

import pandas as pd          
import numpy as np 
import seaborn as sns # For mathematical calculations
import matplotlib.pyplot as plt  # For plotting graphs

# Load the datasets
df1 = pd.read_csv('google_play(1).csv')
df2 = pd.read_csv('google_play(2).csv')

df1.head()

df2.head()

df2=df2.drop('Reviews',axis=1)

common_column = 'id'

# Merge the two datasets on a common column
df = pd.merge(df1, df2, on=common_column)
df.replace(['?', '/', '#','NaN'], np.nan, inplace=True)

df.head()

#Check the shape of dataframe
df.shape

# Viewing the data statistics
df.describe(include='all')

df.info()

df.columns

# Identifying the unique number of values in the dataset
df.nunique()

#Checking unique categories in the data
df['Category'].unique()

# The gradation of installations in the dataframe
df.Installs.unique()

# Looking unique ratings in the dataframe
df['Rating'].unique()

# Viewing the content rating; who is permitted to download these apps
df["Content Rating"].unique()

#Dropping duplicated rows
#On play store, two apps may have same name, but all the size, installs, rating, reviews, price need not be same. so using these categories, we will drop the duplicates in the data
df.drop_duplicates(['App','Size','Installs','Rating','Price','Android Ver'], inplace=True)

df.shape

#Checking each column in the data for null values
df.isnull().sum()

df['Genres'].value_counts()

mode_val = df['Genres'].mode()[0]

df['Genres'].fillna(mode_val, inplace=True)

df['Current Ver'].value_counts()

mode_val = df['Current Ver'].mode()[0]

df['Current Ver'].fillna(mode_val, inplace=True)

df['Android Ver'].value_counts()

mode_val = df['Android Ver'].mode()[0]

df['Android Ver'].fillna(mode_val, inplace=True)

df['Rating'].value_counts()

mode_val = df['Rating'].mode()[0]

df['Rating'].fillna(mode_val, inplace=True)

df['Size'].value_counts()

mode_val = df['Size'].mode()[0]

df['Size'].fillna(mode_val, inplace=True)

df['Type'].value_counts()

mode_val = df['Type'].mode()[0]

df['Type'].fillna(mode_val, inplace=True)

df = df.rename(columns={'Content Rating': 'Content_Rating'})

ca1=df['Genres'].mode()[0]
df['Genres'].fillna(ca1,inplace=True)

ca2=df['Rating'].mode()[0]
df['Rating'].fillna(ca2,inplace=True)
ca3=df['Size'].mode()[0]
df['Size'].fillna(ca3,inplace=True)
ca4=df['Type'].mode()[0]
df['Type'].fillna(ca4,inplace=True)
ca=a=df['Content_Rating'].mode()[0]
df['Content_Rating'].fillna(ca,inplace=True)

df.isnull().sum()

df.drop('id',axis=1)

df['Price'].unique()

df.describe()

df['Installs'] = df['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else str(x))
df['Installs'] = df['Installs'].apply(lambda x: str(x).replace('Free', '0') if 'Free' in str(x) else str(x))
df['Installs'] = df['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else str(x))
df['Installs'] = df['Installs'].apply(lambda x: float(x))


df['Price'] = df['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
df['Price'] = df['Price'].apply(lambda x: '0' if x == 'Everyone' else x)
df['Price'] = df['Price'].apply(lambda x: float(x))
# convert the data types of the numerical variables

df['Size'] = df['Size'].apply(lambda x: ''.join(filter(lambda c: c.isdigit() or c == '.', str(x))))
df['Size'] = df['Size'].apply(lambda x: np.nan if x == '' or x == 'Varies with device' else float(x))

df.corr() # the correlation between the columns

# Plotting the heatmap of correlation between features
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(),annot=True);

df = df.drop('id', axis=1)

# defining numerical & categorical columns
numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

# print columns
print('We have {} numerical features : {}'.format(len(numeric_features), numeric_features))
print('\nWe have {} categorical features : {}'.format(len(categorical_features), categorical_features))

discrete_feature=[feature for feature in numeric_features if len(df[feature].unique())<25]
print("Discrete Variables Count: {}".format(len(discrete_feature)))

discrete_feature

continuous_feature=[feature for feature in numeric_features if feature not in discrete_feature]
print("Continuous feature Count {}".format(len(continuous_feature)))

continuous_feature



fig, ax = plt.subplots(figsize=(25, 15))
sns.set_style('whitegrid')
sns.countplot(x='Installs',data=df,ax=ax)

fig, ax = plt.subplots(figsize=(10, 10))
sns.set_style('whitegrid')
sns.countplot(x='Content_Rating',data=df,ax=ax)

for feature in numeric_features:
    data=df.copy()
    data[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(feature)
    plt.show()

fig = plt.figure(figsize=(15, 20))

for i in range(0, len(numeric_features)):
    ax = plt.subplot(10, 2, i+1)

    sns.scatterplot(data= df ,x='Price', y=numeric_features[i], color='b')
  
    plt.tight_layout()

fig, ax = plt.subplots(figsize=(10,6))
sns.set_style('whitegrid')
sns.histplot(x='Price', bins=200, kde=True, color = 'b',data=df,ax=ax)

fig, ax = plt.subplots(figsize=(30,8))
sns.set_style('whitegrid')
sns.barplot(x=df['Content_Rating'], y=df.Price)

# Countplot of Category
plt.figure(figsize=(15,8))
sns.countplot(x='Category', data=df, order=df['Category'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Count of Apps by Category')
plt.show()

# Histogram of Rating
plt.figure(figsize=(10,5))
sns.histplot(df['Rating'], bins=30)
plt.title('Distribution of Rating')
plt.show()

# select the relevant features
selected_features = ['Category', 'Rating', 'Reviews','Size', 'Installs', 'Type', 'Price', 'Content_Rating', 'Genres']

# create a new dataframe with the selected features
df_selected = df[selected_features]

# convert categorical variables to numerical using one-hot encoding
df_selected = pd.get_dummies(df_selected, columns=['Category', 'Type', 'Content_Rating', 'Genres'])

sns.boxplot(x=df['Size'])
plt.show()

sns.boxplot(x=df['Installs'])
plt.show()

sns.boxplot(x=df['Price'])
plt.show()

# Identify the columns with potential outliers
outlier_cols = ['Installs','Size']

# Replace outliers with the upper and lower bounds
for col in outlier_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    upper_bound = q3 + 1.5*iqr
    lower_bound = q1 - 1.5*iqr
    df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
    df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])

sns.boxplot(x=df['Size'])
plt.show()

sns.boxplot(x=df['Installs'])
plt.show()

sns.boxplot(x=df['Price'])
plt.show()

df.info()

df.head()

df=df.drop(['Last Updated'],axis=1)

# remove 'M' from the strings
df['Reviews'] = df['Reviews'].str.replace('M', '')

# convert the column 'A' from string to float
df['Reviews'] = df['Reviews'].astype(float)

from sklearn.preprocessing import LabelEncoder
# Initializing the label encoder
le = LabelEncoder()

# Encoding the categorical columns
df['App'] = le.fit_transform(df['App'])
df['Category'] = le.fit_transform(df['Category'])
df['Rating'] = le.fit_transform(df['Rating'])
df['Android Ver'] = le.fit_transform(df['Android Ver'])
df['Current Ver'] = le.fit_transform(df['Current Ver'])

df['Genres'] = le.fit_transform(df['Genres'])
df['Reviews'] = le.fit_transform(df['Reviews'])

df['Size']=le.fit_transform(df['Size'])
df['Genres']=le.fit_transform(df['Genres'])

# Convert type column to binary
df['Type'] = df['Type'].apply(lambda x: 1 if x == 'Paid' else 0)

# Convert content rating column to numeric
content_rating_dict = {'Everyone': 0, 'Everyone 10+': 10, 'Teen': 13, 'Mature 17+': 17, 'Adults only 18+': 18}
df['Content_Rating'] = df['Content_Rating'].map(content_rating_dict)

df=df.drop('Content_Rating',axis=1)

df.isnull().sum()

df = df.rename(columns={'Current Ver': 'Current_Ver','Android Ver': 'Android_Ver'})

import numpy as np

import numpy as np

class DecisionTreeRegressor:
    def __init__(self, max_depth=5, min_samples_split=2, min_impurity_decrease=0.0):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_impurity_decrease = min_impurity_decrease

    def fit(self, X, y):
        self.n_features_ = X.shape[1]
        self.tree_ = self._build_tree(X, y)

    def predict(self, X):
        return np.array([self._predict_one(x) for x in X])

    def _build_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape

        # check for stopping criteria
        if depth >= self.max_depth or n_samples < self.min_samples_split or self._impurity(y) <= self.min_impurity_decrease:
            return np.mean(y)

        # select best split based on information gain
        best_feature, best_threshold = self._find_best_split(X, y)

        # split data into left and right subsets
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = X[:, best_feature] > best_threshold
        left_X, left_y = X[left_mask], y[left_mask]
        right_X, right_y = X[right_mask], y[right_mask]

        # create a new node and recursively build the tree
        node = {
            "feature": best_feature,
            "threshold": best_threshold,
            "left": self._build_tree(left_X, left_y, depth + 1),
            "right": self._build_tree(right_X, right_y, depth + 1),
        }

        return node

    def _find_best_split(self, X, y):
        best_gain = -np.inf
        best_feature = None
        best_threshold = None

        for feature in range(self.n_features_):
            values = X[:, feature]
            thresholds = np.unique(values)
            for threshold in thresholds:
                left_mask = values <= threshold
                right_mask = values > threshold
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue
                left_y = y[left_mask]
                right_y = y[right_mask]
                gain = self._information_gain(y, left_y, right_y)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _information_gain(self, y, left_y, right_y):
        p = len(left_y) / len(y)
        return self._impurity(y) - p * self._impurity(left_y) - (1 - p) * self._impurity(right_y)

    def _impurity(self, y):
        mean = np.mean(y)
        return np.mean((y - mean) ** 2)

    def _predict_one(self, x):
        node = self.tree_
        while isinstance(node, dict):
            if x[node["feature"]] <= node["threshold"]:
                node = node["left"]
            else:
                node = node["right"]
        return node

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df[['Size', 'Reviews', 'Price', 'Installs']] = scaler.fit_transform(df[['Size', 'Reviews', 'Price', 'Installs']])

#defining dependent and independent variable as y and x
X = df.drop('Price',axis=1).values
y = df['Price'].values

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.30,random_state=42)

#from decisiontree1 import DecisionTreeRegressor

regressor = DecisionTreeRegressor(max_depth=4, min_samples_split=2)
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

y_pred

import numpy as np
def mean_squared_error(y_true, y_pred):
    """
    Calculates the mean squared error between y_true and y_pred.
    :param y_true: A list or array of true values
    :param y_pred: A list or array of predicted values
    :return: The mean squared error between y_true and y_pred
    """
    # Get the length of the arrays
    n = len(y_true)
    
    # Calculate the sum of squared differences
    sum_squared_diff = sum((y_true[i] - y_pred[i])**2 for i in range(n))
    
    # Calculate the mean squared error
    mse = sum_squared_diff / n
    
    return mse

mse = mean_squared_error(y_test, y_pred)

mse

### Create a Pickle file using serialization 
import pickle
pickle_out = open("regressor.pkl","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()

df.head()

df.columns

regressor.predict([[800,9,112,13,8943,1,40,345,2345,1]])


