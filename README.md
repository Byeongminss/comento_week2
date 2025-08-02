# 2D to 3D Conversion Project

# unit test code입니다.

<!-- import numpy as np
import pytest
import cv2

def generate_depth_map(image):
    if image is None:
        raise ValueError("입력된 이미지가 없습니다.")
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    depth_map = cv2.applyColorMap(grayscale, cv2.COLORMAP_JET)
    return depth_map

def test_generate_depth_map():
    image = np.zeros((100, 100, 3), dtype = np.uint8)
    depth_map = generate_depth_map(image)

    assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다"
    assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."

if __name__ == "__main__": 
    pytest.main() -->

# 실행 결과입니다.

<!-- $ pytest test_case.py
==================================== test session starts =====================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\Users\minkb\comento_week2
collected 1 item

test_case.py .                                                                          [100%]

===================================== 1 passed in 0.09s ====================================== -->

# 변환 결과 이미지

![image](output_image.jpg)
