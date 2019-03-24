Title: Projects
Date: 2019-03-21 13:56
Slug: projects
hide_copyright: true
Category: projects
Tags: projects, reinforcement learning
Summary: Projects by Saurav Sengupta.
Status: published

## Building CNNs to classify duodenal biopsy images into diseases – Child Health Research Center, UVA
* Used Convolutional Neural Networks **(CNN)** to classify high resolution digitized biopsy images into Celiac Disease, Environmental Enteropathy and Normal tissues. 
* Used pretrained **Resnet50** in our analysis, performs well on diverse set of images.
* Achieved close to 98% biopsy level accuracy. Paper accepted in **IEEE BHI 2019 conference at Chicago, Illinois**.
* Backed by the **Bill and Melinda Gates Foundation** and **Aga Khan University**.
* We are also using metabolomics data to find important features of classification.
* [GitHub](https://github.com/UVA-DSI-2019-Capstones/CHRC).

## Music Genre classification
* Classification of songs into one of 13 genres like rock/pop and country etc. Using **ensemble models** for song features and lyrical data.
* Song data features available from [AWS Public Dataset](https://aws.amazon.com/datasets/million-song-dataset/). Used genre data from different Kaggle datasets.
* Created AWS EC2 instance, mounted snapshot, ran Jupyter notebooks on EC2 to get data. (Find out more [here](https://ssen7.github.io/blog/aws_putty/))
* Used **Random Forests, SVM, Naïve Bayes** for model using song features. Used **tf-idf** and **topic modeling** for lyrical data. 
* Ensembled both these models. Around 58.06% accuracy, close to the [state of art](https://ieeexplore.ieee.org/document/1021072) of 61% but we classify more genres.
* [GitHub](https://github.com/ssen7/sys6018-final-project)

## Modeling brainwave activity using Muse™ headset
* Used **Logistic Regression** for real time classification of brain wave signals like alpha waves into left-right, up-down motion. Tested model by moving objects in a game environment.

## (Ongoing) Self Drawing Agent (Reinforcement Learning Project)

* A text to image creator. Our agent will take a number in text format and draw an image equivalent of that number. 
* This agent could be a starting point for a creative tool that can draws illustrations based on text or other image inputs as reference. 
* We use [OpenAI gym](https://github.com/agermanidis/gym-drawobjects) based environment that gives us a way to train agents to draw ImageNet objects on a black-and-white canvas. 
* Use MNIST dataset to develop a reward function that guides our agent online while drawing the image equivalents. 
* Use Neural Network based classification to build our reward function. Our reward function should be able to capture not just a single image equivalent of a number but also the variance in original dataset and use that variance to recreate multiple image equivalents for each number. 
* Inspired by previous work undertaken by **[DeepMind](https://deepmind.com/blog/learning-to-generate-images)** where they trained a robot to create images and train a virtual agent to draw the images.

## (Ongoing) Distracted driver image recognition using Bayesian Neural Networks

* Systems that can detect if a driver is still attentive enough can add to security. 
* CNN results are bound by the kind of data we feed to it. This can become dangerous in cases where inattentive drivers are wrongly identified. 
* Bayesian Neural Nets (BNN) incorporate a measure of uncertainty that can be important in decision making systems.
* The data we will be using for this project is [Distracted Driving imageset](https://www.kaggle.com/c/state-farm-distracted-driver-detection/data) from StateFarm. 
* Use a BNN to model the data. BNN extends the standard neural nets by using Bayesian inference to make better estimates of weights and biases.

## (Ongoing) Predict the stock price in one sector using events in stock price of another sector
 
