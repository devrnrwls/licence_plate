#https://yunwoong.tistory.com/76

IMAGE_PATH = "data/9.jpg"

from pororo import Pororo
print("[Pororo] OCR'ing input image...")
# IMAGE_PATH = "1.jpeg"
ocr = Pororo(task="ocr", lang="ko")
print(ocr(IMAGE_PATH))

from easyocr import Reader
langs = ['ko', 'en']

print("[easyocr] OCR'ing input image...")
reader = Reader(lang_list=langs, gpu=True)
results = reader.readtext(IMAGE_PATH)

for i in results:
    print(i[1])