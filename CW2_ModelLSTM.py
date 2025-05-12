import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
import pickle

'''
This file trains an LSTM model which recognizes 
which category the input sentence belongs to,
a total of 4 categories are set: animal, landscape, portrait, others.
for instance, "a cute cat under the table" belongs to animal,
"a man sitting on a chair" belongs to portrait.
'''

# 1. Load dataset
df = pd.read_csv('data/DatasetCoursework.csv')
texts = df['description']
labels = df['label']

# Map labels to numeric values
label_map = {'animal': 0, 'portrait': 1, 'landscape': 2, 'others': 3}
labels = labels.map(label_map)

# 2. Data pre-processing
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

X = pad_sequences(sequences, maxlen=100)
y = to_categorical(labels, num_classes=4)

# 3. Build LSTM model
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=128, input_length=100))  # Embedding layer
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))  # LSTM layer
model.add(Dropout(0.5))  # Dropout to prevent overfitting
model.add(Dense(4, activation='softmax'))  # Output layer with 4 classes

# 4. Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 5. Train model
history = model.fit(X, y, epochs=2, batch_size=128)

# 6. Save model and tokenizer
model.save('trained_lstm_model.h5')
print("✅ Model has been saved as trained_lstm_model.h5")

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
print("✅ Tokenizer has been saved as tokenizer.pickle")

