# Deep Learning: RNNs and LSTMs

## Overview

This MDC contains comprehensive information about RNNs (Recurrent Neural Networks) and LSTMs (Long Short Term Memory), extracted from Chapter 5 of "Artificial Intelligence, Machine Learning, and Deep Learning" by Oswald Campesato (2020).

## What This Chapter Covers

This chapter provides detailed coverage of:

- **RNNs (Recurrent Neural Networks):**
  - Architecture and statefulness
  - BPTT (Back Propagation Through Time)
  - Vanishing and exploding gradient problems
  - Code examples with Keras

- **LSTMs (Long Short Term Memory):**
  - Architecture with three gates (forget, input, output)
  - Cell state and hidden state
  - Formulas for all gates
  - Bidirectional LSTMs
  - Hyperparameter tuning

- **GRUs (Gated Recurrent Units):**
  - Simplified LSTMs with two gates
  - Comparison with LSTMs

- **Autoencoders:**
  - Dimensionality reduction
  - Feature extraction
  - Variational Autoencoders (VAEs)

- **GANs (Generative Adversarial Networks):**
  - Generator and discriminator
  - Training process
  - Adversarial attacks

## Key Features

✅ **Complete Algorithms:** Detailed explanations of RNNs, LSTMs, GRUs  
✅ **Mathematical Formulas:** All LSTM gate formulas in LaTeX format  
✅ **Code Examples:** Ready-to-use Python code with Keras/TensorFlow 2  
✅ **Best Practices:** Hyperparameter tuning and training recommendations  
✅ **Advanced Topics:** Autoencoders, VAEs, and GANs  

## How to Use This MDC

### For Quick Reference

1. **Finding an Algorithm:** Use the "Algorithms" section for RNN/LSTM details
2. **Code Examples:** Check "Code Examples and Snippets" for implementation
3. **Formulas:** See "Mathematical Foundations" for all LSTM formulas
4. **Best Practices:** Review "Best Practices and Recommendations"

### For Implementation

1. **Choose Your Architecture:** RNN for simple sequences, LSTM for long-term dependencies
2. **Copy Code Example:** Use RNN/LSTM examples as starting point
3. **Adapt to Your Data:** Modify for your specific sequential data
4. **Tune Hyperparameters:** Use best practices guide

### For Learning

1. **Read Algorithms Section:** Understand how RNNs and LSTMs work
2. **Study Formulas:** Learn the mathematical foundations
3. **Run Code Examples:** Execute and experiment with the code
4. **Compare Architectures:** Understand when to use RNN vs LSTM vs GRU

## Code Examples Included

- Simple RNN with Keras
- RNN with MNIST dataset
- Bidirectional LSTM
- GAN generator and discriminator
- GAN with CNN-like architecture

## Prerequisites

- Python 3.x
- TensorFlow 2.x / Keras
- NumPy
- Understanding of deep learning fundamentals (Chapter 4)

## Installation

```bash
pip install tensorflow numpy matplotlib
```

## Quick Start

### Example: Simple RNN

```python
import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.SimpleRNN(units=512,
                                     dropout=0.2,
                                     input_shape=(30, 12)))
model.add(tf.keras.layers.Dense(5, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
```

### Example: LSTM

```python
import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.LSTM(128, input_shape=(timesteps, features)))
model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
```

### Example: Bidirectional LSTM

```python
from tensorflow.keras.layers import Bidirectional, LSTM, Dense

model = tf.keras.models.Sequential()
model.add(Bidirectional(LSTM(10, return_sequences=True), 
                        input_shape=(5,10)))
model.add(Bidirectional(LSTM(10)))
model.add(Dense(5, activation='softmax'))
```

## Related Chapters

- **Chapter 4:** Deep Learning Introduction (prerequisites)
- **Chapter 6:** NLP and Reinforcement Learning (applications)

## Key Concepts

### RNN vs LSTM vs GRU

- **RNN:** Simple, stateful, struggles with long-term dependencies
- **LSTM:** Three gates, handles long-term dependencies, more complex
- **GRU:** Two gates, simpler than LSTM, faster training

### LSTM Gates

- **Forget Gate:** Decides what information to discard
- **Input Gate:** Decides what new information to store
- **Output Gate:** Decides what information to output
- **Cell State:** Long-term memory (tanh activation)
- **Hidden State:** Short-term memory

### Gradient Problems

- **Vanishing Gradient:** Use LSTM instead of simple RNN
- **Exploding Gradient:** Use truncated BPTT or gradient clipping

## Best Practices

1. **For Simple Sequences:** Use SimpleRNN
2. **For Long-term Dependencies:** Use LSTM
3. **For Faster Training:** Use GRU
4. **For NLP Tasks:** Use Bidirectional LSTM
5. **Learning Rate:** Start with 0.001, vitally important
6. **Optimizers:** RMSprop, AdaGrad, or momentum
7. **Regularization:** Use dropout (0.2-0.5) to prevent overfitting
8. **Weight Initialization:** Xavier initialization

## Additional Resources

- RNNs: https://en.wikipedia.org/wiki/Recurrent_neural_network
- LSTMs: https://en.wikipedia.org/wiki/Long_short-term_memory
- GRUs: https://en.wikipedia.org/wiki/Gated_recurrent_unit
- GANs: https://github.com/tensorflow/cleverhans
- Autoencoders: https://www.datascience.com/blog/fraud-detection-with-tensorflow
- TensorFlow Documentation: https://www.tensorflow.org/
- Keras Documentation: https://keras.io/

## Citation

**Source:** Artificial Intelligence, Machine Learning, and Deep Learning  
**Author:** Oswald Campesato  
**Publisher:** Mercury Learning and Information  
**Year:** 2020  
**Chapter:** 5

