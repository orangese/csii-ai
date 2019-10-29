# getting stuff from easyai
from easyai import NN
from easyai.layers import Input, FC
from easyai.support.datasets import Builtins
from easyai.support.draw import DrawMNIST

# loads mnist dataset
(x_train, y_train), (x_test, y_test) = Builtins.load_mnist(mode="mlp")

# creates model
nn = NN(Input(784), FC(100), FC(50), FC(10))
nn.summary()

# trains model
nn.train(x_train, y_train, epochs=3)

# tests model on different data than training
nn.evaluate(x_test, y_test)

# interactive digit classifier!
drawer = DrawMNIST(nn)
drawer.run()
