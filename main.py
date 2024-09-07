import os

import cv2
import time


ACCOUNT = os.getenv('CAM_ACCOUNT')
PASSWORD = os.getenv('CAM_PASSWORD')
HOST = os.getenv('CAM_HOST')


class Camera:

    def __init__(self, account, password, host, port=554):
        self.account = account
        self.password = password
        self.host = host
        self.port = port
        self.url = f'rtsp://{account}:{password}@{host}:{port}/stream1'


    def show_liveview(self, img, width, height):
        cv2.namedWindow('rtsp', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('rtsp', width, height)
        cv2.imshow('rtsp', img)
        cv2.waitKey(1)

    def connect(self):
        vid = cv2.VideoCapture(self.url)
        if not vid.isOpened():
            raise Exception('裝置讀取失敗')

        status, img = vid.read()
        height, width, _ = img.shape
        height = int(height / 2)
        width = int(width / 2)

        while status:
            status, img = vid.read()
            self.show_liveview(img, width, height)


if __name__ == '__main__':
    camera = Camera(ACCOUNT, PASSWORD, HOST)
    camera.connect()


