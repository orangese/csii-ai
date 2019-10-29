# getting stuff from easyai
from easyai import NN
from easyai.layers import Input, FC
from easyai.support.datasets import Builtins
from easyai.support.draw import Draw
from tkinter import *

# loads mnist dataset
(x_train, y_train), (x_test, y_test) = Builtins.load_mnist(mode="mlp")

# creates model
nn = NN(Input(784), FC(100), FC(10))

# trains model
nn.train(x_train, y_train, epochs=3)

# tests model on different data than training
nn.evaluate(x_test, y_test)

# interactive digit classifier!
root = Tk()
Draw(root, nn)
Draw.run_root(root, title="MNIST")
