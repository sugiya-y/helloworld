import numpy as np
import cv2

def main():
    img = cv2.imread("test.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite('gray.jpg',gray)
    cv2.imshow('img',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
