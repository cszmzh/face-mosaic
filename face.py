import cv2
import mediapipe as mp


class FaceDetector:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils

    def rectangle(self, image, mosaic_level):
        success = False
        cv2.imwrite('middle_pic/before_handle.jpg', image)
        with self.mp_face_detection.FaceDetection(
                min_detection_confidence=0.5) as face_detection:

            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            # image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = face_detection.process(image)

            # Draw the face detection annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    h, w, c = image.shape

                    xmin = int(detection.location_data.relative_bounding_box.xmin * w)
                    ymin = int(detection.location_data.relative_bounding_box.ymin * h)
                    width = int(detection.location_data.relative_bounding_box.width * w)
                    height = int(detection.location_data.relative_bounding_box.height * h)
                    xmax = xmin + width
                    ymax = ymin + height
                    if xmax > w:
                        width = w - xmin
                    if ymax > h:
                        height = h - ymin

                    self.do_mosaic(image, xmin, ymin, width, height, int(mosaic_level * 0.2 * width))
                    # 画矩形框
                    # image = cv2.rectangle(image, (xmin, ymin), (xmin + width, ymin + height), (0, 255, 0), 2)
                    success = True
                    cv2.imwrite('middle_pic/after_handle.jpg', image)

            return image, success

    # 正规马赛克
    def do_mosaic(self, img, x, y, w, h, neighbor):
        """
        :param rgb_img
        :param int x :  马赛克左顶点
        :param int y:  马赛克左顶点
        :param int w:  马赛克宽
        :param int h:  马赛克高
        :param int neighbor:  马赛克每一块的宽
        """
        for i in range(0, h, neighbor):
            for j in range(0, w, neighbor):
                rect = [j + x, i + y]
                color = img[i + y][j + x].tolist()  # 关键点1 tolist
                left_up = (rect[0], rect[1])
                x2 = rect[0] + neighbor - 1  # 关键点2 减去一个像素
                y2 = rect[1] + neighbor - 1
                if x2 > x + w:
                    x2 = x + w
                if y2 > y + h:
                    y2 = y + h
                right_down = (x2, y2)
                cv2.rectangle(img, left_up, right_down, color, -1)  # 替换为为一个颜值值

        return img
