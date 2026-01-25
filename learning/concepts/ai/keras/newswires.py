import keras
from keras.datasets import reuters
import numpy as np, matplotlib.pyplot as plt, warnings as wg
wg.filterwarnings("ignore")

(x_tr, y_tr), (x_te, y_te) = reuters.load_data()

def con_to_text(index_in_dataset, train = True):
    w_index = reuters.get_word_index()
    rev_index = {v: k for (k, v) in w_index.items()}
    part = x_tr if train else x_te
    decoded = [" ".join([rev_index.get(i-3, "???") for i in part[index_in_dataset]])]
    return decoded

def vector_maker(sequences, dim = 10000):
    results = np.zeros((len(sequences), dim))
    for i, sequence in enumerate(sequences):
        for j in sequence:
            if j < dim:
                results[i,j] = 1
    return results
x_tr = vector_maker(x_tr)
x_te = vector_maker(x_te)
y_tr = keras.utils.to_categorical(y_tr, num_classes = 46)
y_te = keras.utils.to_categorical(y_te, num_classes = 46)
model = keras.Sequential([
    keras.layers.Dense(64*2, "relu"),
    keras.layers.Dense(64*2, "relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(46, "softmax")
])
model.compile(loss = "categorical_crossentropy", metrics = ["accuracy"])


hist = model.fit(x_tr, y_tr, 
                epochs = 8,
                validation_split = 0.2, 
                callbacks = [keras.callbacks.EarlyStopping(
                     monitor = "val_loss",
                     patience = 3)], 
                batch_size = 512)
acc = hist.history["accuracy"]
val_acc = hist.history["val_accuracy"]
result = model.evaluate(x_te, y_te)
print(result)

plt.plot(acc, "b:", label = "accuracy")
plt.plot(val_acc, "r--", label = " validation accuracy")
plt.legend()
plt.show()