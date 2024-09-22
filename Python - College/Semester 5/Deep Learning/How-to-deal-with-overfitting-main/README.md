# How-to-deal-with-overfitting
This repository contains a Python script for building a neural network to classify Iris flowers based on the Iris dataset. Two different techniques, dropout and batch normalization, have been employed to enhance the performance of the neural network.

## Problem Statement

Initially, a neural network model was built to classify Iris flowers using a basic architecture. However, during the training phase, the model exhibited signs of overfitting, resulting in poor generalization performance on unseen data.

## Solution

To address the overfitting issue, two approaches were implemented and evaluated:

1. **Dropout**: Dropout is a regularization technique that randomly drops neurons during training to prevent overfitting. By adding dropout layers to the neural network architecture, we aim to reduce overfitting and improve generalization.

2. **Batch Normalization**: Batch normalization is a technique used to normalize the inputs of each layer, ensuring that the distribution of inputs remains consistent throughout the training process. This helps stabilize and accelerate the training of deep neural networks.

## Usage

To run the scripts you just need to run main.ipynb step by step.

## Dataset

The Iris dataset is a classic dataset in the machine learning community, containing measurements of various features of Iris flowers. It consists of 150 samples, with each sample belonging to one of three classes: Iris-setosa, Iris-versicolor, or Iris-virginica.

## Conclusion

By incorporating dropout and batch normalization techniques into the neural network architecture, we were able to mitigate the overfitting issue and improve the model's generalization performance on the Iris dataset.

Feel free to explore the code and experiment with different parameters to further enhance the model's performance!
