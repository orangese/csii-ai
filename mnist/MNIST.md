# MNIST: "Hello AI World!"

## What is MNIST?

MNIST is an image recognition dataset that contains 70,000 handwritten digits. It's a standard benchmark dataset that is used as an introduction to AI and a proof-of-concept for various machine learning algorithms.

Below are some examples of digit images from MNIST:

![MNIST example](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

## How do MNIST and neural networks connect?

The input to a neural network would be the MNIST digit image represented as 28 * 28 (size of the image) pixels. We'd hope that the output of the network would be the digit contained in the input image.

In order to train such a network, we start with random weights (think new factory workers) and one by one, feed the 70,000 digits images into the network. For each set (or _batch_) of images, we're going to update the weights using the derivative term (i.e., improving the worker's skill level based on what they did wrong).

Repeating this process many times will hopefully result in a network that can correctly classify digit images. Let's try it!
