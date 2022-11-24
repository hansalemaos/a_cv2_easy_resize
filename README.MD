### Different ways of resizing pictures in OpenCV

```python
pip install a-cv2-easy-resize

from a_cv2_easy_resize import add_easy_resize_to_cv2
from a_cv_imwrite_imread_plus import add_imwrite_plus_imread_plus_to_cv2
add_imwrite_plus_imread_plus_to_cv2()
add_easy_resize_to_cv2()
import cv2
pic = cv2.imread_plus(r"https://raw.githubusercontent.com/hansalemaos/screenshots/main/splitted1.jpeg")
pic1 = cv2.easy_resize_image(
    pic.copy(), width=200, height=None, percent=None, interpolation=cv2.INTER_AREA
)
pic2 = cv2.easy_resize_image(
    pic.copy(), width=None, height=200, percent=None, interpolation=cv2.INTER_AREA
)
pic3 = cv2.easy_resize_image(
    pic.copy(), width=100, height=200, percent=None, interpolation=cv2.INTER_AREA
)
pic4 = cv2.easy_resize_image(
    pic.copy(), width=None, height=None, percent=40, interpolation=cv2.INTER_AREA
)
pic5 = cv2.easy_resize_image(
    pic.copy(), width=None, height=None, percent=None, interpolation=cv2.INTER_AREA
)  # returns original
cv2.imwrite('f:\\papagei\\pic1.png', pic1)
cv2.imwrite('f:\\papagei\\pic2.png', pic2)
cv2.imwrite('f:\\papagei\\pic3.png', pic3)
cv2.imwrite('f:\\papagei\\pic4.png', pic4)
cv2.imwrite('f:\\papagei\\pic5.png', pic5)

```


<img src="https://github.com/hansalemaos/screenshots/raw/main/pic1.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/pic2.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/pic3.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/pic4.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/pic5.png"/>


