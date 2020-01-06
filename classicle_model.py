from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow.keras.models import load_model
import os

def classicle_model(seed_text, model_name, max_length=120,padding_type='post'):
    # loading the tokenizer
    with open(os.path.join(os.path.dirname(__file__), 'tokenizer.pickle'), 'rb') as handle:
        tokenizer = pickle.load(handle)

    # loading the model
    model = load_model(os.path.join(os.path.dirname(__file__), model_name + '.h5'))
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list_padded = pad_sequences([token_list], maxlen=max_length, padding=padding_type)
    predicted = model.predict_classes(token_list_padded, verbose=0)

    # loading the label word index
    with open(os.path.join(os.path.dirname(__file__), 'label_word_index.pickle'), 'rb') as handle:
        label_word_index = pickle.load(handle)
    
    # getting the right category out of the five indexes
    for label in label_word_index.values():
      if predicted[0] == label:
        category = list(label_word_index.keys())[label-1]
        
    return category
