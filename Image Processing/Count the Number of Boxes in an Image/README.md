# Counting Number of boxes in a given Image - Problem Statement
In this task you need to count the number of boxes from the input image. The input image from which you need to detect boxes is present in the 
images folder. Also apart from just counting mark all the boxes which are detected in the given image and then save the image as output in the
output folder. To get started you can use the given image below:


<img align="center" width="600" height="260" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Count%20the%20Number%20of%20Boxes%20in%20an%20Image/Images/Basic%20Example.png">


### Input Image

Given below is an example of expected output. You can use a different input image as well if you want to. Just make sure that input image contains
boxes which are square or rectangle shaped.

<img align="center" width="400" height="533" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Count%20the%20Number%20of%20Boxes%20in%20an%20Image/Images/Boxes.jpg">


### Expected Output

Given below is an example of expected output. This is not the only expected output and your output can be different and even better. As long
as you are able to detect boxes your output is correct.

<img align="center" width="400" height="400" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Count%20the%20Number%20of%20Boxes%20in%20an%20Image/Output/output.jpg">

### Hint
As you need to detect the number of boxes in a given image you need to detect squares in a given image as all the boxes are square in shape. So
you can detect all the contours present in the given image and pick out the ones which have 4 sides. Then from that to get just the boxes from
all the squares present in the image figure out the contours which have area similar to the boxes present in the given image and then draw them.

### Tips
- Learn about the OpenCv python library in depth.
- Always use object oriented approach for programming as it is faster and cleaner.


### Demonstration Video - Expected Output
