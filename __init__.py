from typing import Union

import cv2
import numpy as np


def easy_resize_image(
    img: np.ndarray,
    width: Union[int, None] = None,
    height: Union[int, None] = None,
    percent: Union[int, None] = None,
    interpolation: int = cv2.INTER_AREA,
) -> np.ndarray:
    if width is not None and height is None:
        ratio = img.shape[0] / img.shape[1]
        height = width * ratio
        dim = (int(width), int(height))
        img = cv2.resize(img, dim, interpolation=interpolation)
    elif width is None and height is not None:
        ratio = img.shape[1] / img.shape[0]
        width = height * ratio
        dim = (int(width), int(height))

        img = cv2.resize(img, dim, interpolation=interpolation)

    elif width is not None and height is not None:
        dim = (int(width), int(height))
        img = cv2.resize(img, dim, interpolation=interpolation)

    elif width is None and height is None and percent is not None:
        dim = int((img.shape[1] / 100) * percent), int((img.shape[0] / 100 * percent))
        img = cv2.resize(img, dim, interpolation=interpolation)
    return img


def add_easy_resize_to_cv2():
    cv2.easy_resize_image = easy_resize_image


# from a_cv2_easy_resize import add_easy_resize_to_cv2
# from a_cv_imwrite_imread_plus import add_imwrite_plus_imread_plus_to_cv2
# add_imwrite_plus_imread_plus_to_cv2()
# add_easy_resize_to_cv2()
# import cv2
# pic = cv2.imread_plus(r"https://raw.githubusercontent.com/hansalemaos/screenshots/main/splitted1.jpeg")
# pic1 = cv2.easy_resize_image(
#     pic.copy(), width=200, height=None, percent=None, interpolation=cv2.INTER_AREA
# )
# pic2 = cv2.easy_resize_image(
#     pic.copy(), width=None, height=200, percent=None, interpolation=cv2.INTER_AREA
# )
# pic3 = cv2.easy_resize_image(
#     pic.copy(), width=100, height=200, percent=None, interpolation=cv2.INTER_AREA
# )
# pic4 = cv2.easy_resize_image(
#     pic.copy(), width=None, height=None, percent=40, interpolation=cv2.INTER_AREA
# )
# pic5 = cv2.easy_resize_image(
#     pic.copy(), width=None, height=None, percent=None, interpolation=cv2.INTER_AREA
# )  # returns original
# cv2.imwrite('f:\\papagei\\pic1.png', pic1)
# cv2.imwrite('f:\\papagei\\pic2.png', pic2)
# cv2.imwrite('f:\\papagei\\pic3.png', pic3)
# cv2.imwrite('f:\\papagei\\pic4.png', pic4)
# cv2.imwrite('f:\\papagei\\pic5.png', pic5)
