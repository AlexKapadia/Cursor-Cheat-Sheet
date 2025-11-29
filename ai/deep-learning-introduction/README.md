# Deep Learning Introduction

## Overview

This MDC contains comprehensive information about deep learning fundamentals, extracted from Chapter 4 of "Artificial Intelligence, Machine Learning, and Deep Learning" by Oswald Campesato (2020).

## What This Chapter Covers

This chapter provides detailed coverage of:

- **Deep Learning Fundamentals:**
  - What is deep learning
  - Problems it can solve
  - Challenges and limitations

- **Core Building Blocks:**
  - Perceptrons
  - Artificial Neural Networks (ANNs)
  - Multilayer Perceptrons (MLPs)

- **Convolutional Neural Networks (CNNs):**
  - Architecture and components
  - Convolution operation
  - Max pooling
  - Complete CNN implementation

- **Hyperparameters:**
  - Number of layers and neurons
  - Activation functions
  - Loss functions
  - Optimizers
  - Learning rate
  - Dropout

- **Training Process:**
  - Forward propagation
  - Backward error propagation (backprop)
  - Weight updates

## Key Features

✅ **Complete Architectures:** Detailed explanations of MLPs and CNNs  
✅ **Code Examples:** Ready-to-use Python code with Keras/TensorFlow 2  
✅ **Mathematical Formulas:** All formulas in LaTeX format  
✅ **Hyperparameter Guide:** Comprehensive guide to all hyperparameters  
✅ **MNIST Examples:** Complete MLP and CNN implementations  

## How to Use This MDC

### For Quick Reference

1. **Finding an Architecture:** Use the "Algorithms" section for MLP and CNN details
2. **Code Examples:** Check "Code Examples and Snippets" for implementation
3. **Formulas:** See "Mathematical Foundations" for all mathematical content
4. **Hyperparameters:** Review "Hyperparameters" section

### For Implementation

1. **Choose Your Architecture:** MLP for simple problems, CNN for images
2. **Copy Code Example:** Use MNIST examples as starting point
3. **Adapt to Your Data:** Modify for your specific dataset
4. **Tune Hyperparameters:** Use best practices guide

### For Learning

1. **Read Algorithms Section:** Understand how MLPs and CNNs work
2. **Study Formulas:** Learn the mathematical foundations
3. **Run Code Examples:** Execute and experiment with the code
4. **Compare Architectures:** Understand when to use MLP vs CNN

## Code Examples Included

- XOR function with neural network
- MNIST classification with MLP
- MNIST classification with CNN
- Image display and visualization
- Linear regression with deep learning

## Prerequisites

- Python 3.x
- TensorFlow 2.x / Keras
- NumPy
- Matplotlib (for visualization)

## Installation

```bash
pip install tensorflow numpy matplotlib
```

## Quick Start

### Example: Simple MLP for MNIST

```python
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```

### Example: CNN for MNIST

```python
import tensorflow as tf

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))
train_images, test_images = train_images/255.0, test_images/255.0

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)
test_loss, test_acc = model.evaluate(test_images, test_labels)
```

## Related Chapters

- **Chapter 3:** Classifiers in Machine Learning (prerequisites: activation functions)
- **Chapter 5:** Deep Learning: RNNs and LSTMs (sequential architectures)
- **Chapter 6:** NLP and Reinforcement Learning (applications)

## Key Concepts

### Deep Learning

- Subset of machine learning
- Focuses on neural networks
- Requires at least 2 hidden layers
- Very deep: 10+ hidden layers

### Architectures

- **MLP:** Fully connected feed-forward network
- **CNN:** Convolutional layers for images
- **RNN/LSTM:** Sequential data (Chapter 5)

### Hyperparameters

- **Layers/Neurons:** Architecture size
- **Activation:** ReLU (hidden), Softmax (output)
- **Loss:** MSE or Cross-entropy
- **Optimizer:** Adam (recommended)
- **Learning Rate:** 0.001 to 0.05
- **Dropout:** 0.2 to 0.5 for regularization

## Best Practices

1. **For Images:** Use CNNs
2. **For Simple Problems:** Start with MLPs
3. **Activation Functions:** ReLU for hidden layers
4. **Optimizers:** Adam is good default
5. **Regularization:** Use dropout to prevent overfitting
6. **Data Preprocessing:** Normalize inputs (0-1)

## Challenges

- Bias in algorithms
- Adversarial attacks
- Limited generalization
- Lack of explainability
- Correlation vs causality

## Additional Resources

- CNNs: https://en.wikipedia.org/wiki/Convolutional_neural_network
- Network Initialization: http://www.deeplearning.ai/ai-notes/initialization/
- Bias in AI: https://www.technologyreview.com/s/612876/this-is-how-ai-bias-really-happensand-why-its-so-hard-to-fix
- TensorFlow Documentation: https://www.tensorflow.org/
- Keras Documentation: https://keras.io/

## Citation

**Source:** Artificial Intelligence, Machine Learning, and Deep Learning  
**Author:** Oswald Campesato  
**Publisher:** Mercury Learning and Information  
**Year:** 2020  
**Chapter:** 4

