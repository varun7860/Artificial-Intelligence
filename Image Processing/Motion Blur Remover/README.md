# Motion Blur Remover Using Image Processing
<img align = "center" width = "600" height = "330" src = "https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Motion%20Blur%20Remover/Assets/Image%20Deblurring.jpg">
  
In this task the goal is to remove Blur from an image using image processing concepts.Your program should remove the
from the image to such an extent that the viewer should be able to see the details clearly in the image. Your program
take an input blurred image and output an image which is deblurred. Following things should be achieved when this task is
completed:

1. `Completely deblurred output image.`
2. `Output image should be displayed on the screen.`
3. `The program should be general. This means that it should work for any image which are blurred equally.`
4. `The code should neatly commented and linted. Pylint can be used to lint the code.`
5. `The program should be fast and accurate.`
6. `Ringing Effect obtained after deblurring should be as minimum as possible.`

## What is Motion Blur?
<img align = "center" width = "300" height = "250" src = "https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Motion%20Blur%20Remover/Assets/Blurred%20Image.gif">

Motion Blur is a degradation of image caused due to the moment of the object relative to the sensor in the camera when the
shutter is open. Motion Blur can also be caused due to the movement of camera as well. For example if you take a picture while
moving your camera the resultant image will be motion blurred. There are 3 types of blur:

- `Horizontal Blur`: Linear motion is horizontal direction
- `Vertical Blur`: Linear motion in vertical direction
- `Circular Blur`: Linear motion is circular direction

The motion blur can be completely removed by process called deconvolution in image processing. Based on the type of of motion
blur, the kernel used for deconvolution will be different for each blur. For example, for horizontal blur the horizontal deconvolution
kernel will be used.

## Filters used for deblurring

## Learning Modules

## Expected Output
