# Introduction to TensorFlow 2

## Overview

This MDC contains comprehensive information about TensorFlow 2, extracted from Appendix B of "Artificial Intelligence, Machine Learning, and Deep Learning" by Oswald Campesato (2020).

## What This Appendix Covers

This appendix provides detailed coverage of:

- **TensorFlow 2 Fundamentals:**
  - Eager execution
  - Keras integration
  - Simplified API

- **Model Building:**
  - Sequential API
  - Functional API
  - Layer types

- **Training and Evaluation:**
  - Compilation (optimizer, loss, metrics)
  - Training (fit)
  - Evaluation (evaluate)
  - Predictions (predict)

- **Advanced Features:**
  - Custom training loops
  - Callbacks
  - Model saving/loading

## Key Features

✅ **Complete APIs:** All major TensorFlow 2/Keras APIs covered  
✅ **Code Examples:** Ready-to-use Python code  
✅ **Common Patterns:** Templates for different problem types  
✅ **Best Practices:** Recommendations for efficient development  
✅ **Production Ready:** Model saving, loading, deployment patterns  

## How to Use This MDC

### For Quick Reference

1. **Finding an API:** Use the "Core APIs and Classes" section
2. **Code Examples:** Check "Code Examples and Snippets" for implementation
3. **Common Patterns:** See "Common Patterns" for templates
4. **Best Practices:** Review "Best Practices and Recommendations"

### For Implementation

1. **Choose Your Pattern:** Select appropriate pattern for your problem
2. **Copy Code Example:** Use examples as starting point
3. **Adapt to Your Data:** Modify for your specific dataset
4. **Follow Best Practices:** Use recommendations for optimal results

### For Learning

1. **Read API Sections:** Understand available APIs
2. **Study Code Examples:** Learn by example
3. **Run Examples:** Execute and experiment
4. **Build Your Own:** Create models for your problems

## Code Examples Included

- Simple Sequential model
- Functional API model
- CNN model
- LSTM model
- Complete training pipeline
- Model saving and loading
- Custom training loop
- Callbacks usage

## Prerequisites

- Python 3.6+
- Understanding of deep learning concepts
- Familiarity with NumPy
- Basic Python programming

## Installation

```bash
# CPU version
pip install tensorflow

# GPU version (requires CUDA)
pip install tensorflow-gpu
```

## Quick Start

### Example: Simple Model

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```

### Example: CNN Model

```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

## Related Chapters

- **Chapter 3:** Classifiers (uses TensorFlow/Keras)
- **Chapter 4:** Deep Learning Introduction (uses TensorFlow/Keras)
- **Chapter 5:** RNNs and LSTMs (uses TensorFlow/Keras)
- **Chapter 6:** NLP and RL (uses TensorFlow)

## Key Concepts

### TensorFlow 2 Features

- **Eager Execution:** Immediate operation evaluation
- **Keras Integration:** High-level API
- **Simplified API:** Easier to use than TF 1.x

### Model Building

- **Sequential API:** Linear stack of layers
- **Functional API:** More flexible architectures
- **Layers:** Dense, Conv2D, LSTM, etc.

### Training

- **Optimizers:** Adam, SGD, RMSprop
- **Loss Functions:** Categorical crossentropy, MSE, etc.
- **Metrics:** Accuracy, precision, recall, etc.

## Best Practices

1. **Start Simple:** Use Sequential API for linear models
2. **Use Functional API:** For complex architectures
3. **Optimizer:** Adam is good default
4. **Callbacks:** Use EarlyStopping, ModelCheckpoint
5. **Normalize Data:** Scale inputs appropriately
6. **Monitor Validation:** Avoid overfitting
7. **Save Models:** Persist trained models

## Common Patterns

### Classification
- Dense layers with ReLU
- Softmax output
- Categorical crossentropy loss

### Regression
- Dense layers with ReLU
- Linear output (no activation)
- MSE loss

### Image Classification
- Conv2D + MaxPooling
- Flatten + Dense
- Softmax output

### Sequence Models
- LSTM/GRU layers
- Dense output
- Categorical crossentropy loss

## Additional Resources

- TensorFlow: https://www.tensorflow.org/
- Keras: https://keras.io/
- TensorFlow Tutorials: https://www.tensorflow.org/tutorials
- TensorFlow API: https://www.tensorflow.org/api_docs

## Citation

**Source:** Artificial Intelligence, Machine Learning, and Deep Learning  
**Author:** Oswald Campesato  
**Publisher:** Mercury Learning and Information  
**Year:** 2020  
**Appendix:** B

