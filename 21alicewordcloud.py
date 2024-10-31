import matplotlib
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

# 폰트 설정 (필요 시 주석 해제)
# font_name = font_manager.FontProperties(fname='C:/Windows/fonts/malgun.ttf').get_name()
# rc('font', family=font_name)

# 텍스트 파일 읽기
with open('./data/alice.txt', 'r', encoding='utf-8') as file:
    rfile = file.read()
print(rfile)
print()

# 불용어 설정
spwords = set(STOPWORDS)
# 한국어 불용어 추가
spwords.update(['그', '저', '니'])
# 영어 불용어 추가
spwords.add('said')
spwords.update(['hahaha', 'hohoho'])

# 마스크 이미지 로드
image_file = './data/alice.png'
img_file = Image.open(image_file)
alice_mask = np.array(img_file)

# 워드클라우드 생성
mywc = WordCloud(
    max_font_size=350,
    stopwords=spwords,
    font_path='C:/Windows/fonts/malgun.ttf',  # 한글 폰트 경로
    background_color='black',
    width=800,
    height=800,
    mask=alice_mask,
    contour_width=1,
    contour_color='steelblue'
)

# 텍스트로부터 워드클라우드 생성
mywc.generate(rfile)

# 워드클라우드 시각화
plt.figure(figsize=(12, 8))
plt.imshow(mywc, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
print()
print()
