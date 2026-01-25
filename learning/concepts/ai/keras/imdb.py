from keras.datasets import imdb
import keras, warnings, matplotlib.pyplot as plt, numpy as np
warnings.filterwarnings("ignore")

(x_tr, y_tr), (x_te, y_te) = imdb.load_data()
word_index = imdb.get_word_index()
rev_index = {v: k for (k, v) in word_index.items()}
decoded = [" ".join([rev_index.get(i-3, "??") for i in x_tr[0]])]
def vector_maker(sequences, dim = 1000):
    results = np.zeros((len(sequences), dim))
    for i, sequence in enumerate(sequences):
        for j in sequence:
            if j < dim:
                results[i,j] = 1
    return results
x_tr = vector_maker(x_tr)
x_te = vector_maker(x_te)
y_tr = np.array(y_tr).astype("float32")
y_te = np.array(y_te).astype("float32")
model = keras.Sequential([
    keras.layers.Dense(16, activation = "relu", input_shape = (1000,)),
    keras.layers.Dense(16, activation = "relu"),
    keras.layers.Dense(1, activation = "mse")
])
model.compile(optimizer = "rmsprop", loss = keras.losses.BinaryCrossentropy(), metrics = ["accuracy"])
history = model.fit(x_tr, y_tr, epochs = 5, batch_size = 512, validation_split = 0.2)
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
plt.clf()
plt.plot(acc, "b:", label = "Training Accuracy",)
plt.plot(val_acc, "r:", label = "Validation accuracy")
plt.legend()
plt.show()
results =  model.evaluate(x_te, y_te)
print(results)

model2 = keras.Sequential([ ####overfited model
    keras.layers.Dense(64, activation = "tanh", input_shape = (1000,)),
    keras.layers.Dense(64, activation = "tanh"),
    keras.layers.Dense(64, activation = "tanh"),
    keras.layers.Dense(46, activation = "sigmoid")
])

model2.compile(optimizer = "adagrad", loss = "categorical_crossentropy", metrics = ["accuracy"])
y_tr2 = keras.utils.to_categorical(y_tr, num_classes = 46)
y_te2 = keras.utils.to_categorical(y_te, num_classes = 46)
hist = model2.fit(x_tr, y_tr2, epochs = 15, batch_size = 12, validation_split = 0.2)
plt.clf()
plt.plot(hist.history["val_accuracy"], "b--", label = "training accuracy of model 2")
plt.plot(val_acc, "r--",label = "validation accuracy of model 1")
plt.show()
print(model2.evaluate(x_te, y_te2))
print(np.argmax(model2.predict(x_te[0:1])))