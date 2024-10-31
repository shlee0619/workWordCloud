#22okt.py 문서 10.31 목요일 작성

from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt
import time

okt = Okt()
print(' Okt() 정보 ', okt) # <konlpy.tag._okt.Okt object at 0x00000228F4CC3BC0>

msg = '나는 과일중에 사과,체리 추출하여 워드 클라우드로 그려 봅시다'
print(msg)
result1 = okt.nouns(msg)
print(result1)
print()
time.sleep(0.5)

result2 = okt.pos(msg)
print(result2)
print()

result3 = okt.morphs(msg)
print(result3)
print()

# msg2 = '아버지가방에들어가신다'
# result2 = okt.nouns(msg2)
# print(result2)
