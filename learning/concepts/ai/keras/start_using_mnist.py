import keras.datasets.mnist as mnist
import keras
import warnings
warnings.filterwarnings("ignore")
(x_tr, y_tr), (x_te, y_te) = mnist.load_data()
print(x_tr.shape)

model = keras.Sequential([
    keras.layers.Dense(512, activation = "relu"),
    keras.layers.Dense(10, activation = "softmax")
])
model.compile(optimizer = "rmsprop", 
              loss = "sparse_categorical_crossentropy",
              metrics = ["accuracy"])
x_tr = x_tr.reshape((60000, 28 * 28)).astype("float32") / 255
x_te = x_te.reshape((10000, 28 * 28)).astype("float32") / 255
model.fit(x_tr, y_tr, epochs = 5, batch_size = 128)
test_loss, test_acc = model.evaluate(x_te, y_te)
test = model.predict(x_te)
import matplotlib.pyplot as plt
plt.imshow(x_te[0].reshape(28, 28), cmap = plt.cm.viridis) #type:ignore
plt.show()