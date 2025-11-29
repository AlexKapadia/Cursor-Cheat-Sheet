# Classifiers in Machine Learning

## Overview

This MDC contains comprehensive information about classification algorithms in machine learning, extracted from Chapter 3 of "Artificial Intelligence, Machine Learning, and Deep Learning" by Oswald Campesato (2020).

## What This Chapter Covers

This chapter provides detailed coverage of:

- **Classification Algorithms:**
  - kNN (k Nearest Neighbor)
  - Decision Trees
  - Random Forests
  - SVMs (Support Vector Machines)
  - Bayesian Classifiers (Naive Bayes)
  - Logistic Regression

- **Activation Functions:**
  - Sigmoid, Tanh, ReLU, ELU, SELU
  - Softmax, Softplus, Hardmax
  - When and why to use each

- **Classification Types:**
  - Binary classification
  - Multiclass classification
  - Multilabel classification

- **Evaluation Metrics:**
  - Precision, Recall, Accuracy
  - F1 Score
  - ROC Curves
  - Confusion Matrices

## Key Features

✅ **Complete Algorithms:** Detailed explanations of how each classifier works  
✅ **Code Examples:** Ready-to-use Python code with scikit-learn and Keras  
✅ **Mathematical Formulas:** All formulas in LaTeX format  
✅ **Best Practices:** Recommendations for choosing and using classifiers  
✅ **Activation Functions:** Comprehensive guide with TensorFlow/Keras APIs  

## How to Use This MDC

### For Quick Reference

1. **Finding an Algorithm:** Use the "Algorithms" section for detailed explanations
2. **Code Examples:** Check "Code Examples and Snippets" for implementation
3. **Formulas:** See "Mathematical Foundations" for all mathematical content
4. **Best Practices:** Review "Best Practices and Recommendations"

### For Implementation

1. **Choose Your Classifier:** Based on your problem type (see "Best Practices")
2. **Copy Code Example:** Use the appropriate code snippet as a starting point
3. **Adapt to Your Data:** Modify for your specific dataset
4. **Evaluate:** Use the evaluation metrics provided

### For Learning

1. **Read Algorithms Section:** Understand how each classifier works
2. **Study Formulas:** Learn the mathematical foundations
3. **Run Code Examples:** Execute and experiment with the code
4. **Compare Techniques:** Understand tradeoffs between different approaches

## Code Examples Included

- Decision Tree with scikit-learn (basic and wine dataset)
- Random Forest classifier
- SVM classifier
- Logistic Regression with Keras (Iris dataset)
- Activation functions in Python
- Complete preprocessing pipelines

## Prerequisites

- Python 3.x
- NumPy, Pandas
- scikit-learn
- TensorFlow 2.x / Keras
- Matplotlib (for visualization)

## Installation

```bash
pip install numpy pandas scikit-learn tensorflow matplotlib
```

## Quick Start

### Example: Decision Tree Classification

```python
from sklearn import tree

X = [[0, 0], [1, 1], [2, 2]]
Y = [0, 1, 1]

tree_clf = tree.DecisionTreeClassifier()
tree_clf = tree_clf.fit(X, Y)

print(tree_clf.predict([[-1., -1.]]))  # [0]
print(tree_clf.predict([[2., 2.]]))     # [1]
```

### Example: Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```

## Related Chapters

- **Chapter 2:** Introduction to Machine Learning (prerequisites)
- **Chapter 4:** Deep Learning Introduction (uses activation functions)
- **Chapter 5:** Deep Learning: RNNs and LSTMs (uses sigmoid/tanh)

## Key Concepts

### Classification Types

- **Binary:** Two classes (spam/not-spam)
- **Multiclass:** More than two classes (MNIST digits)
- **Multilabel:** Multiple labels per instance

### Activation Functions

- **ReLU:** Preferred for hidden layers
- **Sigmoid:** For binary classification output
- **Softmax:** For multiclass classification output
- **Tanh:** Used in LSTMs/GRUs

### Evaluation Metrics

- **Precision:** TP/(TP + FP)
- **Recall:** TP/(TP + FN)
- **Accuracy:** (TP + TN)/(P + N)
- **F1 Score:** Harmonic mean of precision and recall

## Best Practices

1. **For Simple Problems:** Use kNN or linear classifiers
2. **For Structured Data:** Use decision trees or random forests
3. **For Small, Clean Datasets:** Use SVMs
4. **For Text Classification:** Use Naive Bayes
5. **For Complex Patterns:** Use neural networks

## Limitations

- Does not cover Linear Discriminant Analysis
- Does not cover kMeans (unsupervised learning)
- Some algorithms have limitations (see "Limitations and Assumptions" section)

## Additional Resources

- Activation Functions: https://en.wikipedia.org/wiki/Activation_function
- Multilabel Classification: https://medium.com/@vijayabhaskar96/multi-label-image-classification-tutorial-with-keras-imagedatagenerator-cd541f8eaf24
- scikit-learn Documentation: https://scikit-learn.org/
- TensorFlow/Keras Documentation: https://www.tensorflow.org/

## Citation

**Source:** Artificial Intelligence, Machine Learning, and Deep Learning  
**Author:** Oswald Campesato  
**Publisher:** Mercury Learning and Information  
**Year:** 2020  
**Chapter:** 3

