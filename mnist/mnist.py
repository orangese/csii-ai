from easyai import NN
from easyai.layers import Input, FC
from easyai.support.datasets import Builtins

(x_train, y_train), (x_test, y_test) = Builtins.load_mnist(mode="mlp")

mlp = NN(Input(784), FC(100), FC(10))

mlp.train(x_train, y_train)
mlp.evaluate(x_test, y_test)
