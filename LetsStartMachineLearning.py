import pandas as pd
from sklearn.model_selection import train_test_split
from keras.src.models.sequential import Sequential
from keras.src.saving.saving_api import load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

df = pd.read_csv('./Apple Dataset.csv')

X = pd.get_dummies(df.drop(['Outcome', 'Date'], axis=1))
Y = df['Outcome'].apply(lambda x: 0 if x == 0 else 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2)

X_train.head()
Y_train.head()

model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=6))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=30, batch_size=32)

