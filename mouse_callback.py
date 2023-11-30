import cv2

# 마우스 클릭 이벤트 핸들러 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'마우스 클릭 좌표: ({x}, {y})')

# 이미지 불러오기
image = cv2.imread('data/3.jpg')  # 이미지 경로를 자신의 이미지 경로로 변경하세요

# 윈도우 생성 및 마우스 이벤트 콜백 함수 등록
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
    cv2.imshow('Image', image)

    # ESC 키를 누르면 루프 종료
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
