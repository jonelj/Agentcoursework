import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

'''
This is designed to check the accuracy of the trained model
'''
# 1. load the saved model
model = load_model('trained_lstm_model.h5')
print("✅ load model successfully！")

# 2. load Tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
print("✅ Tokenizer load successfully！")

# 3. define the map (have to be same as the training)
label_map = {'animal': 0, 'portrait': 1, 'landscape': 2, 'others': 3}
inv_label_map = {v: k for k, v in label_map.items()}

# 4. define predicting function
def predict_text(text):
    """input the text，return the name of kinds"""
    seq = tokenizer.texts_to_sequences([text])
    padded_seq = pad_sequences(seq, maxlen=100)
    prediction = model.predict(padded_seq, verbose=0)
    predicted_class = np.argmax(prediction, axis=1)[0]
    return inv_label_map.get(predicted_class, "unknown")

if __name__ == '__main__':
    # 5. load testing dataset from test_dataset csv file
    test_df = pd.read_csv('data/test_dataset.csv')
    test_texts = test_df['description'].tolist()
    true_labels = test_df['label'].tolist()

    # 6. calculate the accuracy
    correct = 0
    for text, true_label in zip(test_texts, true_labels):
        predicted_label = predict_text(text)
        if predicted_label == true_label:
            correct += 1

    accuracy = correct / len(test_texts)
    print(f"\nDone! those are {len(test_texts)} samples")
    print(f"The accuracy: {accuracy:.2%}")
    '''
    Accuracy: 89% - 1000 samples
    '''
