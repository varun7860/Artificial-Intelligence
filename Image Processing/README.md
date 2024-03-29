# Image Processing

<img align="center" width="600" height="315" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/images/Image%20Processing.png"> 

Image Processing is a sub-branch of Artificial Intelligence which deals with improving the quality of Image Data. It consists of using a 
digital computer to process digital images using the known Algorithms. It allows using multiple algorithms which prevents building up noise,
distortion and other outliers in an image. This repository will consist of all kinds of Image Processing projects. But before going forward
this description file to get started.

### What is an Image?
<img align="center" width="600" height="252" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/images/what%20is%20image.png">

Image is a two dimensional function `F(x,y)` where x is the width and y is the height of the image. The value of F(x,y) gives the value of
the pixel at that point. The amplitude(A) of "F" is called the intensity of an image. When the values of x,y and A are finite then the image
if called a digital image otherwise the image is an analog image. As the function consists of two values ie x and y an image is represented by
two dimensional matrix with x rows and y columns. A digital image comprises of finite number of elements called pixels. Pixels are denoted as the
elements of digital image.

### Types of Images
1. Binary Image: Consist of only two pixel values 1 and 0. 0 refers to black and 1 refers to white.
2. Black and white Image: This Image consists of only black and white colour.Unlike binary image black and white image doesn't have only two pixel 
                          values(ie 1 and 0).
3. GrayScale Images: It is an image based on 8 bit colour format. It has pixel values from 0-255 where 0 is black, 1 is white and  127 is the grayscale value.
4. Colour Images: These images are based on 16 bit colour format and 24 bit colour format. 16 bit colour format is the one that is widely used in
                  colour image processing. It has 65,536 different colours in it.
                  
### Image in mathematical form
<img align="center" width="409" height="188" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/images/image%20formula.png">

          
### Important Quests of Image Processing
- Classification
- Feature Extraction
- Pattern Recognition
- Projection
- MultiScale Signal Analysis

### Techniques of Image Processing
1. `Image Restoration` : This technique involves gaining image lost properties by deblurring or denoising the image.
2. `Image Editing` : This involves manipulating images by cropping, changing aspect ratio....and many more.
3. `Neural Networks` : This is used for classifying images based on their features by using Artificial Neural Networks(ANN)
4. `Point Feature Matching` : This is used for identifying similar images corresponding to the input image.
5. `Image Linear Filtering` : This involves applying various filters on image to enchance image properties.
6. `Wavelets and Multi Resolution Processing` : Used to representing Images in degrees.
7. `Self Organizing Maps` : An Artificial Neural Network method used for image classification.
8. `Pixelation` : The process of distinguishing individual pixels.
9. `Anisotrophic Diffusion(Perona Malik Diffusion)` : Technique used to remove noise without altering the features of the Image.
10. `Partial Differential Equations` : Treating images as continous objects instead of discrete using numerical analysis and then using PDE's for image processing.
11. `Independent Component Analysis` : Used to remove randomly mixed images or videos and reconstructing the original one by independent components.
12. `2D-Hidden Markov Models(HMM)` : Used for image classification by modelling the Images using 2D Hidden Markov models.
13. `Principal Component Analysis` : Used for reducing data or Image dimensions.Highly used when image has more than 2 dimensions. Basically used in the compression
                                     of digital images.

### Difference between Image processing, Computer Vision, Artificial Intelligence and Computer Graphics
1. `Image Processing` : If the input is an Image and the output is also an Image then this is called Image processing.
2. `Computer vision` : If the input is an Image and the output is some kind of data in string or any kind of code then this is called Computer Vision.
3. `Computer Graphics` : If the input is some kind of data and the output is an Image then this is called computer Graphics.
4. `Artificial Intelligence` : If the input is data or some kind of code and the output is also some kind of label or data then this is called Artificial Intelligence.

###  Image Transformations Techniques
- `Filtering` : Used for blurring or sharpening the images.
- `Image padding in Fourier domain filtering` : Used for padding the image before using it in fourier domain.
- `Affline Transformations` : Used for scaling, rotating, translating, mirroring and shearing images.

### Applications of Image Processing

<img align="center" width="500" height="229" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/images/Applications.png">

1. Image Editing
2. Video Editing
3. Digital Camera Images
4. Used in making films
5. Computer Vision
6. Retrieving useful information.
