import cv2
import numpy as np

class QR(object):
    def __init__(self):
        self._path = "C:/Users/Admin/Desktop/Computer Vision/QR Code Scanner/Images/QR_1.png"
        self._resize = (400,400)
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.image = None
        self.output = None
        self.data = None
        self.box = None
        self.corrected_image = None

        self.scanner = cv2.QRCodeDetector()

    def extract_image(self):
        self.image = cv2.imread(self._path, 1)

    def resize(self):
        self.image = cv2.resize(self.image, self._resize)

    def show_original_image(self):
        cv2.imshow("Original Image", self.image)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

    def detect_code(self):
        self.data, self.box, self.corrected_image = self.scanner.detectAndDecode(self.image)
        if len(self.data)>0:
            print("Data: {}".format(self.data))
            self.corrected_image = np.uint8(self.corrected_image)

        else:
            print("QR Code not detected")

    def merge_data(self):
        self.image = cv2.putText(self.image, str(self.data), (20,15),
                                 self.font, 0.5,(0,0,255), 1, cv2.LINE_AA)

    def show_output_image(self):
        for i in range(len(self.box[0])):
            if i+1 is not 4:
               cv2.line(self.image, tuple(self.box[0][i]), tuple(self.box[0][i+1]), (255,0,0),5)

            elif i+1 is 4:
               cv2.line(self.image, tuple(self.box[0][0]), tuple(self.box[0][len(self.box[0])-1]), (255,0,0),5)
                     
        cv2.imshow("Output Image", self.image)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()


def main():

    #Make the scanner object
    qr_scanner = QR()

    #Set the input image
    qr_scanner.extract_image()

    #Resize the Image
    qr_scanner.resize()

    #Detect the QR_code from the Image.
    qr_scanner.detect_code()

    #Merge data in the Image
    qr_scanner.merge_data()

    #Show the Output Image
    qr_scanner.show_output_image()


if __name__ == '__main__':
    main()
