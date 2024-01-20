# opencv

## 环境配置

### 安装

通过 pip 安装

```shell
> pip install opencv-python
```

如需 `cv2.face` 应安装 `opencv-contrib-python`

```shell
> pip install opencv-contrib-python
```

### opencv 源码

> 如需源码前往官网下载，官网: [https://opencv.org](https://opencv.org)

## 导入模块

```python
import cv2
```

其他模块

```python
from cv2.data import haarcascades  # 级联分类器xml文件所在目录
```

## 属性

| 函数 | 描述 |
| --- | --- |
| waitKey | 等待键盘操作，参数为等待时限，返回按键对应的ASCII码 |
| destroyWindow | 销毁一个窗口，传入窗口标题名 |
| destroyAllWindows | 销毁所有窗口 |
| **图像处理** |  |
| [imread](#imread) | 读取一张图片，返回 Mat 对象 |
| [imwrite](#imwrite) | 写入图片 |
| [imshow](#imshow) | 在窗口中显示一张图片 |
| [cvtColor](#cvtcolor) | 颜色转换 |
| [resize](#resize) | 修改图像大小 |
| [rectangle](#rectangle) | 绘制矩形 |
| [circle](#circle) | 绘制圆形 |
| [putText](#puttext) | 添加文本 |

| 类 | 描述 |
| --- | --- |
| [Mat](#mat) | 图像对象 |
| [CascadeClassifier](#cascadeclassifier) | 创建级联分类器 |
| **视频处理** |  |
| [VideoCapture](#videocapture) | 视频读取 |

### imread

读取一张图片。第一个参数为图片路径，第二个参数为打开图片模式。

示例：

```python
img = cv2.imread("test.png")
```

### imwrite

写入一张图片。第一个参数为写入的图片路径，第二个参数为图像(Mat)

示例：

```python
img = cv2.imread("test.png")
cv2.imwrite("test2.png", img)
```

### imshow

显示一张图片。第一个参数为展示的窗口的标题，第二个参数为 Mat 对象

示例：

```python
img = cv2.imread("test.png")
cv2.imshow("Test", img)
```

### cvtColor

第一个参数传入 Mat 对象，第二个参数表示怎么转换，已经定义在 cv2 中了，一般以 COLOR_ 为前缀

示例：

```python
img = cv2.imread("test.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB转灰度
```

### resize

第一个参数传入 Mat 对象，第二个参数传入修改后的尺寸

示例：

```python
img = cv2.imread("test.png")
img = cv2.resize(img, (800, 500))
```

### rectangle

第一个参数是 Mat，第二个参数是第一个点的坐标和长宽，也可以只写坐标，第三个参数为第二个点的坐标(如参数二已写明长宽则忽略)，第四个参数是颜色，第五个参数是厚度

示例：

```python
img = cv2.imread("test.png")
# 在坐标 100, 100 绘制一个宽高 200*200 的矩形，BGR颜色(0, 255, 0)，2 像素宽
cv2.rectangle(img, (100, 100, 200, 200), color=(0, 255, 0), thickness=2)
# 在坐标 150, 150 绘制一个到坐标 350, 350 的矩形
cv2.rectangle(img, (150, 150), (350, 350), color=(0, 255, 0), thickness=2)
```

### circle

第一个参数是 Mat，第二个参数是中心点坐标，第三个参数是半径，第四个参数是颜色，第五个参数是厚度

示例：

```python
img = cv2.imread("test.png")
cv2.circle(img, (200, 200), 100, color=(255, 0, 0), thickness=2)
```

### putText

第一个参数是图像(Mat)，第二个参数是文本，第三个参数是坐标，第四个参数是字体(已定义在 cv2 中，一般以 FONT_ 开头)，第五个参数是缩放，第六个参数是颜色，第七个参数是厚度。

| 参数 | 描述 |
| --- | --- |
| ... | ... |
| bottomLeftOrigin | 以左下角为起点 |

示例：

```python
img = cv2.imread("test.png")
cv2.putText(img, "hello world", (100, 100), 0, 1, (0, 0, 0), 2)
```

### Mat

读取图片后返回的对象

下标操作，Mat 对象下标共有三个维度，每个维以逗号分隔，第一维是高度，第二维是宽度，第三维是颜色

示例：

```python
img = cv2.imread("test.png")
img1 = img[::-1]  # 高度坐标翻转
img2 = img[:, ::-1]  # 宽度坐标翻转
img3 = img[:, :, ::-1]  # 颜色信息翻转
```

### CascadeClassifier

创建级联分类器，传入文件路径

| 方法 | 描述 |
| --- | --- |
| detectMultiScale | 多次缩放检测 |

#### detectMultiScale

第一个参数为图片(Mat)，第二个参数为每次迭代图像的缩放倍率，第三个参数为最少检测到多少次算人脸，第四个参数不管或默认填0，第五个参数表示检测到人脸的最小尺寸，第六个参数为检测到人脸的最大尺寸

示例：

```python
import os

import cv2
from cv2.data import haarcascades

img = cv2.imread("test.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_classifier = cv2.CascadeClassifier(os.path.join(haarcascades, "haarcascade_frontalface_default.xml"))
# 每次迭代的倍率 1.05，最少检测到 5 次，最小尺寸 (50, 50)，最大尺寸 (500, 500)
face = face_classifier.detectMultiScale(gray_img, 1.05, 5, 0, (50, 50), (500, 500))
# face = face_classifier.detectMultiScale(img)  # 懒人写法
for coor in face:
    cv2.rectangle(img, coor, color=(0, 255, 0), thickness=2)

cv2.imshow("Face", img)
cv2.waitKey()
cv2.destroyAllWindows()
```

### VideoCapture

传入要读取的视频路径或者数字(表示要读取的摄像头，0 是默认摄像头)

返回一个对象，这个对象的方法

| 方法 | 描述 |
| --- | --- |
| read | 读取一帧 |
| release | 释放资源 |

示例：

```python
cap = cv2.VideoCapture(0)  # 打开默认摄像头
```

#### read

返回两个值，一是否读取成功，二读取到的帧

示例：

```python
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        break
    cv2.imshow("Capture", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
```

## cv2.face

| 类 | 描述 |
| --- | --- |
| [`LBPHFaceRecognizer_create`](#cv2facelbphfacerecognizer_create) |  |

### cv2.face.LBPHFaceRecognizer_create

训练人脸特征数据

| 方法 | 描述 |
| --- | --- |
| train | 训练一组数据 |
| read | 读取一组训练好的数据 |
| write | 写入数据 |
| predict | 识别图像 |

训练数据示例：

```python
import os

import PIL.Image
import numpy as np
import cv2
from cv2.data import haarcascades

# 假设只训练一张图像
face_sample = []  # 人脸样本
ids = np.array([0])  # 样本对应的 label/id

# 转换灰度图的numpy数组
img = PIL.Image.open("images/9.jpeg").convert("L")
img_array = np.array(img, "uint8")

# 人脸识别级联分类器
face_classifier = cv2.CascadeClassifier(os.path.join(haarcascades, "haarcascade_frontalface_default.xml"))
# 获取人脸位置，添加到样本中
x, y, w, h = face_classifier.detectMultiScale(img_array)[0]
face_sample.append(img_array[y:y+h, x:x+w])

# 创建识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 开始训练
recognizer.train(face_sample, ids)
# 将训练好的数据写入文件
recognizer.write("face.yml")
```

人脸识别示例：

```python
import os
import time

import cv2
from cv2.data import haarcascades

detect_results = {}
detect_time = 0

# 人脸识别级联分类器
face_classifier = cv2.CascadeClassifier(os.path.join(haarcascades, "haarcascade_frontalface_default.xml"))
# 识别器
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 读取训练好的数据 (假设数据中只有一张人脸)
recognizer.read("face.yml")
# 开启摄像头
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        break
    if time.perf_counter() - detect_time > 0.5:
        # 检测灰度图像
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        know_num = 0
        for coor in face_classifier.detectMultiScale(gray_img, 1.05, 10):
            x, y, w, h = coor
            # 截取人脸检测，返回 label/id 和置信度
            id, confidence = recognizer.predict(gray_img[y:y+h, x:x+w])
            match_time = time.perf_counter()
            if confidence > 80:
                know_num += 1
                key = -know_num
                name = "Uknow"
            else:
                key = id
                name = "Ethan"
            detect_results[key] = (match_time, coor, name, confidence)
        detect_time = time.perf_counter()
    # 在图像中画出人脸的位置和文字
    for k, v in tuple(detect_results.items()):
        match_time, rect, name, confidence = v
        if time.perf_counter() - match_time > 0.5:
            del detect_results[k]
            continue
        cv2.rectangle(frame, rect, color=(0, 255, 0), thickness=2)
        cv2.putText(frame, "Name: " + name, (rect[0] + 5, rect[1] + rect[3] + 20), 0, 0.5, (0, 255, 0), 1)
        cv2.putText(frame, "Confidence: %d" % confidence, (rect[0] + 5, rect[1] + rect[3] + 40), 0, 0.5, (0, 255, 0), 1)
    # 显示图像
    cv2.imshow("Capture", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()

cv2.destroyAllWindows()
```

## cv2.FaceDetectorYN

人脸检测模块

| 函数/方法 | 描述 |
| --- | --- |
| [`create`](#cv2facedetectoryncreate) | 创建人脸检测器 |

人脸检测示例:

```python
import cv2
import numpy as np


def detect(img):
    # 调整图片大小, 设置 InputSize
    width = img.shape[1]
    height = img.shape[0]
    img = cv2.resize(img, (width, height))
    face_detector.setInputSize((width, height))
    # 检测
    faces = face_detector.detect(img)
    return faces


def visualize(img, faces, thickness=2):
    if faces[1] is not None:
        for face in faces[1]:
            coords = face[:-1].astype(np.int32)
            cv2.rectangle(img, (coords[0], coords[1]), (coords[0] + coords[2], coords[1] + coords[3]), (0, 255, 0), thickness)
            cv2.circle(img, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv2.circle(img, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv2.circle(img, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv2.circle(img, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv2.circle(img, (coords[12], coords[13]), 2, (0, 255, 255), thickness)


face_detector = cv2.FaceDetectorYN.create(
    "model/onnx/face_detection_yunet_2022mar.onnx",
    "",
    (320, 320),
    0.9,
    0.3,
    5000,
)

img = cv2.imread("img.png")
faces = detect(img)
visualize(img, faces)
cv2.waitKey()
cv2.destroyAllWindows()
```

### cv2.FaceDetectorYN.create

示例:

```python
face_detector = cv2.FaceDetectorYN.create(
    "model/onnx/face_detection_yunet_2022mar.onnx",
    "",
    (320, 320),
    0.9,
    0.3,
    5000,
)
```

## cv2.FaceRecognizerSF

人脸识别模块

| 函数/方法 | 描述 |
| --- | --- |
| [`create`](#cv2facerecognizersfcreate) | 创建人脸识别器 |

示例:

```python
import cv2
import numpy as np


def detect(img):
    # 调整图片大小, 设置 InputSize
    width = img.shape[1]
    height = img.shape[0]
    img = cv2.resize(img, (width, height))
    face_detector.setInputSize((width, height))
    # 检测
    faces = face_detector.detect(img)
    return faces


def recognize(img, faces, cmp_face_feature, mode=1):
    if faces[1] is not None:
        for face in faces[1]:
            face_align = face_recognizer.alignCrop(img, face)
            face_feature = face_recognizer.feature(face_align)
            coords = face[:-1].astype(np.int32)

            cosine_score = face_recognizer.match(face_feature, cmp_face_feature, cv2.FaceRecognizerSF_FR_COSINE)
            l2_score = face_recognizer.match(face_feature, cmp_face_feature, cv2.FaceRecognizerSF_FR_NORM_L2)

            msg = 'different identities'
            if cosine_score >= cosine_similarity_threshold:
                msg = 'the same identity'
            print('They have {}. Cosine Similarity: {}, threshold: {} (higher value means higher similarity, max 1.0).'.format(msg, cosine_score, cosine_similarity_threshold))

            msg = 'different identities'
            if l2_score <= l2_similarity_threshold:
                msg = 'the same identity'
            print('They have {}. NormL2 Distance: {}, threshold: {} (lower value means higher similarity, min 0.0).'.format(msg, l2_score, l2_similarity_threshold))


face_detector = cv2.FaceDetectorYN.create(
    "model/onnx/face_detection_yunet_2022mar.onnx",
    "",
    (320, 320),
    0.9,
    0.3,
    5000,
)
face_recognizer = cv2.FaceRecognizerSF.create(
    "model/onnx/face_recognition_sface_2021dec.onnx", "")

cosine_similarity_threshold = 0.363
l2_similarity_threshold = 1.128

# 获取基础人脸的特征数据
base_img = cv2.imread("base.png")
base_faces = detect(base_img)
assert base_faces[1] is not None
base_face_align = face_recognizer.alignCrop(base_img, base_faces[1][0])
base_face_feature = face_recognizer.feature(base_face_align)
# 获取要比较的人脸的数据
target_img = cv2.imread("target.png")
target_img_faces = detect(target_img)
# 识别
recognize(target_img, target_img_faces, base_face_feature)
```

### cv2.FaceRecognizerSF.create

示例:

```python
face_recognizer = cv2.FaceRecognizerSF.create(
    "model/onnx/face_recognition_sface_2021dec.onnx", "")
```
