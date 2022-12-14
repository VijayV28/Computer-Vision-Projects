# Computer Vision Projects

[![license](https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law&logoColor=white)](https://github.com/VijayV28/Computer-Vision-Projects/blob/main/LICENSE.md "license MIT")

Mini working projects developed using the Open-CV Framework

## 🧑‍🍳 What's cooking here?

This is just a collection of small, beginner-friendly computer vision projects that can give you an
about the [Open-CV](https://opencv.org/) framework.

Well if you have no idea what Open CV is, it is basically a library that gives you access to machine learning
and computer vision algorithms and as the names suggests, you guesses it, it's open source.

Each project's details and use cases can be found below.

I'll try to keep adding projects as I go through more of the content, so do [![stars](https://custom-icon-badges.demolab.com/github/stars/DenverCoder1/custom-icon-badges?logo=star)](https://github.com/VijayV28/Computer-Vision-Projects/stargazers "star") this repository and check this place regularly.

## 1. 🖼️ Image Filters

We all have an idea on the various filters available to while clicking a picture. In the Computer Vision world, it turns out that these filters have a very strong use case such as smoothing out the noise, detecting important and specific features and so on. 

The Image Filters.py in this repo will show you how to gain access and display footage from your system's camera in Python (which isn't as hard as it may sound) and then allows you to try out the following filters:

    1. Preview - Nothing interesting. Shows you your own face with the image FLIPPED!

    2. Blur - Nothing interesting again. Blurs the image feed, but you can always play with the kernel matrix in the code to try out different levels of blurring.

    3. Canny - This is that weird filter that you would've thought had no purpose in your camera. Look below for an example. Turns out this is object detection and     plays a vital role in Computer Vision

    4. Features = This might be the most interesting one here. It lets you detect corners in real-time!! You have to try it to see how cool it actually is. 
 
![canny](https://user-images.githubusercontent.com/81868201/207626401-316f6f46-a7d7-435a-ac32-c1cb9034cf76.png)

## 2. 🪡 Stitching Images

Remember that almost useless functionality that lies at the last place in your phone's camera? The Panorama feature! This program does exactly that by stiching together consecutive images.

It is important to note that the quality depends entirely on the number of keypoints shared by every two consecutive images. This means that two images can be stitched together perfectly without any distortion if there are a number of keypoints that are similar between them. Also, if you are to try with your own set of images, make sure that the lighting doesn't change between the images and try to take it from the height for better quality.

It's pretty straight forward. Nothing to play around with.

## 🤗 Feedback

All sorts of [feedbacks](https://github.com/VijayV28/Computer-Vision-Projects/labels/feedback) are welcomed with grace and gratitude.

## 💬 Questions?

Feel free to [open an issue](https://github.com/VijayV28/Computer-Vision-Projects/issues/new).
