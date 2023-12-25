# Image Cartoonization using GAN

## Overview

This repository contains the implementation of a project on image cartoonization using Generative Adversarial Networks (GANs). The project was conducted as part of CMPSC 445 – Machine Learning in Applied Data Science.

**Author:** Sai Meghana Kolla

## Abstract

In this project, a Generative Adversarial Network (GAN) was developed to transform real images into cartoon versions, allowing users to choose the desired cartoon style. The goal was to reduce the effort required to create cartoons from scratch, offering a more accessible and user-friendly solution.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Contributions](#11-contributions)
3. [Material and Methods](#2-material-and-methods)
4. [Dataset Description](#21-dataset-description)
5. [Methodology](#22-methodology)
6. [Performance Evaluation](#23-performance-evaluation)
7. [Experimental Analysis](#3-experimental-analysis)
8. [Conclusion](#4-conclusion)
9. [References](#references)

## 1. Introduction

Cartoons play a significant role in various aspects of life, and creating them from real images requires creativity and effort. This project leverages GANs, a machine learning model, to automate the process of image cartoonization. GANs operate in a cooperative zero-sum game framework, where a generator transforms real images into cartoon versions, and a discriminator evaluates the output.

## 1.1 Contributions

- Explored various techniques for image cartoonization and compared them.
- Chose GAN as the preferred method and studied its architecture.
- Implemented CartoonGAN and developed a user interface for image input and style selection using Gradio.

## 2. Material and Methods

### 2.1 Dataset Description

The project utilized a dataset comprising real images and cartoon images for different styles. The training set included 5,402 real images and various cartoon images for Shinkai, Hosoda, Hayao, and Paprika styles.

### 2.2 Methodology

The image transformation was performed using pre-trained CartoonGAN, consisting of a generator and a discriminator. The user uploads a real image through a web application, and after processing through the generator and discriminator, a cartoonized version is displayed.

### 2.3 Performance Evaluation

Performance was evaluated based on 900 test images, with an average inference time of less than 4 seconds.

## 3. Experimental Analysis

The user interface allows users to input images and select cartoonization styles. Figures demonstrate the image transformation for different styles, such as Shinkai, Hayao, Hosoda, and Paprika.

# My Project

![Image 1](https://github.com/saimeghana26/image-cartoonization/blob/34501ff78024def7081ba7558b7894630871c3fe/images/Shinkai.png)

Image transformation using Shinkai style.

![Image 2](https://github.com/saimeghana26/image-cartoonization/blob/34501ff78024def7081ba7558b7894630871c3fe/images/Hayao.png)

Image transformation using Hayao style.

![Image 3](https://github.com/saimeghana26/image-cartoonization/blob/34501ff78024def7081ba7558b7894630871c3fe/images/hosoda.png)

Image transformation using Hosodo style.

![Image 4](https://github.com/saimeghana26/image-cartoonization/blob/34501ff78024def7081ba7558b7894630871c3fe/images/paprika.png)

Image transformation using Paprika style.


## 4. Conclusion

The implemented Cartoon GAN successfully converts real-world images into high-quality cartoon-style graphics. Future work may involve extending the application to handle various video formats.

## References

1. Brownlee, Jason. "A Gentle Introduction to Generative Adversarial Networks (GANs)." Machine Learning Mastery, 19 July 2019, https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/.
2. Advancement of Techniques for Image Cartoonization, Aditi Lohomi.
3. Abid, A., Abdalla, A., Abid, A., Khan, D., Alfozan, A., & Zou, J. (2019, June 6). Gradio: Hassle-free sharing and testing of ML models in the wild. arXiv.org. Retrieved from https://arxiv.org/abs/1906.02569.
