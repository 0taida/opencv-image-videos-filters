import cv2
import numpy as np

# this will create a mitrex of ones 5 rows  5 culom
# we will use it with img dilate
kernel = np.ones((5, 5), np.uint8)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def open_video():
    cap = cv2.VideoCapture("res/test.mp4")

    # zero to open the default webcam
    # cap = cv2.VideoCapture(0)

    while True:
        # success it will be true if it read, if not will be false
        success, vid = cap.read()

        vid = cv2.resize(vid, (680, 480))
        img_gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(vid, (17, 17), 0)
        img_canny = cv2.Canny(vid, 20, 100)
        img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

        all_img = stack_image(0.8, ([vid, img_gray, img_blur], [img_canny, img_dilation, vid]))
        all_img = cv2.resize(all_img, (900, 500))
        cv2.imshow("original", all_img)
        # waiting for the user to press q to exit the app
        if cv2.waitKey(1) & 0xff == ord('q'):
            break


def open_img():
    path = "res/img.png"
    img = cv2.imread(path)
    img = cv2.resize(img, (500, 500))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray", img_gray)

    # 7,7 should be odd
    img_blur = cv2.GaussianBlur(img, (7, 7), 0)
    # cv2.imshow("img blur", img_blur)

    img_canny = cv2.Canny(img, 50, 50)
    # cv2.imshow("img canny", img_canny)

    # increase the size of canny line by iterations
    img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
    # cv2.imshow("dilate", img_dilation)

    all_img = stack_image(0.8, ([img, img_gray, img_blur], [img_canny, img_dilation, img]))
    all_img = cv2.resize(all_img, (900, 500))
    cv2.imshow("original", all_img)
    # cv2.moveWindow("original", 500, 200)
    cv2.waitKey(0)


def crop_img():
    path = "res/img.png"
    img = cv2.imread(path)
    print(img.shape)
    width, height = 400, 400
    img_resize = cv2.resize(img, (width, height))
    cv2.imshow("resize", img_resize)

    img_crop = img[500:1080, 1000:1920]
    cv2.imshow("crop", img_crop)
    img_crop_resize = cv2.resize(img_crop, (img.shape[1], img.shape[0]))

    cv2.imshow("resize the crop", img_crop_resize)
    # cv2.imshow("original", img)
    # cv2.moveWindow("original", 500, 200)
    cv2.waitKey(0)


def create_img():
    # the number 3 is mean the img have 3 channel which mean the img have color
    # if it 2 it means the img will be in back and white
    # the np.uint8 to convert the float to integer case we don't have color in float value
    img = np.zeros((512, 512, 3), np.uint8)
    img[:] = 255, 0, 0
    img[100:200, 100:200] = 1, 1, 1

    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
    cv2.rectangle(img, (400, 20), (300, 100), (0, 0, 255), cv2.FILLED)
    cv2.circle(img, (150, 400), 50, (255, 150, 20), 3)
    cv2.putText(img, "Hell is coming", (200, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

    cv2.imshow("img", img)
    print(img)
    cv2.waitKey(0)


def stack_image(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_avilable = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_avilable:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2: img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale,
                                          scale)
            if len(img_array[x].shape) == 2: img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor

    return ver


open_video()
# open_img()
