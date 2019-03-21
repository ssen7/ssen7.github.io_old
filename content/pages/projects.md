Title: Projects
Date: 2019-03-21 13:56
Slug: projects
hide_copyright: true
Summary: Projects by Saurav Sengupta.
Status: published

## Building CNNs to classify duodenal biopsy images into diseases – Child Health Research Center, UVA
* We use Convolutional Neural Networks (CNN) to classify high resolution digitized biopsy images into Celiac Disease, Environmental Enteropathy and Normal tissues. 
* We are using existing architectures like Resnet34 and Resnet50 in our analysis, since they are the deep and perform well on a diverse set of images. We use the fabulous fastai library.
* We are also using metabolomics data to find important features of classification.
* Funded and supported by the **Bill and Melinda Gates** foundation and the **Aga Khan University**.
* [GitHub](https://github.com/UVA-DSI-2019-Capstones/CHRC).

## (Ongoing) Self Drawing Agent (Reinforcement Learning Project)

* A text to image creator. Our agent will take a number in text format and draw an image equivalent of that number. 
* This agent could be a starting point for a creative tool that can draws illustrations based on text or other image inputs as reference. 
* We use OpenAI gym based environment that gives us a way to train agents to draw ImageNet objects on a black-and-white canvas. 
* Use MNIST dataset to develop a reward function that guides our agent online while drawing the image equivalents. 
* Use Neural Network based classification to build our reward function. Our reward function should be able to capture not just a single image equivalent of a number but also the variance in original dataset and use that variance to recreate multiple image equivalents for each number. 
* Inspired by previous work undertaken by [DeepMind](https://deepmind.com/blog/learning-to-generate-images) where they trained a robot to create images and train a virtual agent to draw the images.

## Music Genre classification
* Created EC2 AWS instance to get data from the Million Song Dataset. 
* Wrote scripts to get data from S3 bucket and run Jupyter notebooks on EC2.
* Used Text mining on song lyrics and song features to predict 13 different genre types. Used feature selection to reduce the number of features and reduce overfitting. 58.6% Accuracy. 
* [GitHub](https://github.com/ssen7/sys6018-final-project).

## Modeling brainwave activity
* Used Muse™ headset to collect brain activity data in the form of frequency measurements of alpha, beta, gamma, delta and theta waves to classify actions like moving hands, motor imagination.
* Found correlation between alpha waves and motion. 
* Used Logistic Regression for real time modeling and classification of thought and used it to move object in a mobile game environment.

## Modeling quality of barbell lifts using accelerometer data
* The goal was to use data from accelerometers on the belt, forearm, arm, and dumbbell of 6 participants, to predict how well they do barbell lifts.
* Tested accuracy of models built using Tree Algorithm, Random Forest, and Model Stacking using the caret package in R. 
* [GitHub Pages](https://ssen7.github.io/practical-machine-learning-coursera/) Link.
