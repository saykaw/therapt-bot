from tensorflow.keras.models import load_model
import numpy as np
from training import train_x,train_y
model = load_model('test_chatbot_model.h5')
test_x = [train_x]  # list of input sequences for testing
test_y = [train_y]  # list of output sequences for testing
loss, accuracy = model.evaluate(np.array(test_x), np.array(test_y), verbose=0)
print("Accuracy:", accuracy)
