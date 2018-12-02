<p align="center"><i>
  Final Project <br/>
  SC-T-796-DEEP, Introduction to Deep Learning, 2018-3 <br/>
  Reykjavík University - School of Computer Science, Menntavegi 1, IS-101 Reykjavík, Iceland
</i></p>

<img src="images/header.png" alt="Reykjavik University Logo" align="middle"/>

<p align="center">
A facial expression classifier that recognizes 8 common emotions:<br/> happy, angry, sad, contemptuous, disgusted, fearful, surprised, and neutral.
</p>


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_WWtejTCCB8kfKhd2Qy7kf0VS0baFtUY)


## Table of Contents
<!-- ⛔️ MD-MAGIC-EXAMPLE:START (TOC:collapse=true&collapseText=Click to expand) -->
<details>
<summary>Click to expand</summary>

1. [Introduction](#1-introduction)
2. [The Database](#2-the-database)
3. [The Model](#3-the-model)
4. [Model Validation](#4-model-validation)
6. [Authors](#5-authors)
8. [License](#6-license)
7. [References](#7-references)

</details>
<!-- ⛔️ MD-MAGIC-EXAMPLE:END -->

## 1 Introduction
Facial emotion/expression classifier can be used to predict what a person is feeling from just looking at an image of a person. Even though a person can express countless expression, in this project we create a classifier that can distinguish between 8 common emotions: happy, angry, sad, contemptuous, disgusted, fearful, surprised, and neutral. The goal is to present a statistical comparison between several convolutional neural network (CNN) model architectures to measure their performances.


## 2 The Dataset
The dataset that was chosen was the **RaFD image set** from the **Radboud Faces Database**.

In total, the set contains 67 models:
* 20 Caucasian male adults
* 19 Caucasian female adults
* 4 Caucasian male children
* 6 Caucasian female children
* 18 Moroccan male adults

Each model was trained by a FACS (Facial Action Coding System) coder, to show each of the following emotional expressions:
* happy
* angry
* sad
* contemptuous
* disgusted
* neutral
* fearful
* surprised

<p align="center">
<img src="http://bp1.blogger.com/_OCFkCH4MWdw/SIclzKfIVeI/AAAAAAAAABA/zL_Fg4JYFoE/s200/olli_emotions_bigger.jpg" alt="8 different emotional expressions" align="middle"/>
</p>
Each emotion was shown with three different gaze directions (without changing head orientation):
* looking left
* looking frontal
* looking right

Further, each picture was taken from five different camera angles simultaneously:

<p align="center">
<img src="http://bp1.blogger.com/_OCFkCH4MWdw/SIcjUsBq5VI/AAAAAAAAAA4/F5oVaRP1Poo/s400/Gijs_Surprised.jpg" alt="5 different camera angles" align="middle"/>
</p>

Summary:
* 2400 images of Caucasian male adults
* 2280 images of Caucasian female adults
* 480 images of Caucasian male children
* 720 images of Caucasian female children
* 2160 images of Moroccan male adults

**Total Images: 8040**

## 3 The Model

## 4 Model Validation

## 5 Authors
* [Atli Egilsson](https://github.com/atliegils) - MSc. Computer Science Student
* [Egill Anton Hlöðversson](https://github.com/egillanton) - MSc. Language Technology Student

## 6 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 7 References
* [Radboud Faces Database](http://www.socsci.ru.nl:8180/RaFD2/RaFD?p=main)
* [Keras](https://keras.io)

🌟 PLEASE STAR THIS REPO IF YOU FOUND SOMETHING INTERESTING 🌟
