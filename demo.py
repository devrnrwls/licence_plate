#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

import cv2
import numpy as np

def paste_image_on_blank_background(image, output_path):
    # 빈 배경 이미지를 생성합니다.
    background = np.zeros((1000, 2000, 3), dtype=np.uint8)  # 가로 500, 세로 500, 3채널(RGB)

    # 배경 이미지의 중앙에 이미지를 붙입니다.
    background_height, background_width, _ = background.shape

    # 이미지가 배경의 중앙에 오도록 좌표를 계산합니다.
    x_offset = (background_width - image.shape[1]) // 2
    y_offset = (background_height - image.shape[0]) // 2

    # 빈 배경에 이미지를 붙입니다.
    background[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image

    # 결과 이미지를 저장합니다.
    cv2.imwrite(output_path, background)

    return background

if __name__ == "__main__":

    # 이미지 크기 설정
    image_width = 500
    image_height = 500
    background = np.zeros((image_height, image_width, 3), dtype=np.uint8)

    img = cv2.imread('data/4.jpg')

    # [x,y] 좌표점을 4x2의 행렬로 작성
    # 좌표점은 좌상->좌하->우상->우하
    pts1 = np.float32([[146, 132],[148, 220],[510, 196],[514, 296]])

    # 내가 pts1을 매칭시키고 싶은 크기를 고려하여 좌표 제시
    pts2 = np.float32([[10,10],[10,500],[1000,10],[1000,500]])

    # pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
    cv2.circle(img, (int(pts1[0][0]), int(pts1[0][1])), 20, (255,0,0),-1)
    cv2.circle(img,(int(pts1[1][0]), int(pts1[1][1])) , 20, (0,255,0),-1)
    cv2.circle(img,(int(pts1[2][0]), int(pts1[2][1])) , 20, (0,0,255),-1)
    cv2.circle(img,(int(pts1[3][0]), int(pts1[3][1])) , 20, (0,0,0),-1)

    M = cv2.getPerspectiveTransform(pts1, pts2)

    # 배경 없이 번호판만 조절
    dst = cv2.warpPerspective(img, M, (1000,500))

    # 배경에 붙이고 중앙에 배치하므로 성능 향상 기대(필요시 활용)
    output_paste_image_on_blank_background = paste_image_on_blank_background(dst, "output_image.jpg")

    from easyocr import Reader
    langs = ['ko', 'en']

    print("[easyocr] OCR'ing input image...")
    reader = Reader(lang_list=langs, gpu=True)
    # results = reader.readtext('output_image.jpg')
    results = reader.readtext(dst)

    for i in results:
        print(i[1])

    from pororo import Pororo
    print("[Pororo] OCR'ing input image...")
    ocr = Pororo(task="ocr", lang="ko")
    # print(ocr('output_image.jpg'))
    print(ocr(dst))

    # output_image = cv2.imread('output_image.jpg')

    plt.subplot(121),plt.imshow(img),plt.title('image')
    # plt.subplot(122),plt.imshow(output_image),plt.title('Perspective')
    plt.subplot(122), plt.imshow(dst), plt.title('Perspective')
    plt.show()