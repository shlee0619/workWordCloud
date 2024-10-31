#23pos.py 

from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt
import time

print('23pos.py 문서연습')
okt = Okt()
print(' Okt() 정보 ', okt) # <konlpy.tag._okt.Okt object at 0x00000228F4CC3BC0>

text = '컴퓨터프로그래머가길동이아버지가방에들어가신다'
print(text)
print()

# norm=True : 단어를 정규화시켜 보여줌
# stem=True : 단어의 원형을 보여줌

# result1 = okt.pos(text, norm =True, stem=True)
result1 = okt.pos(text, norm =False, stem=False)
# result1 = okt.pos(text, norm =True, stem=True)

print(result1)
print()
time.sleep(0.5)

# result2 = okt.pos(text)
# print(result2)
# print()

# result3 = okt.morphs(text)
# print(result3)
# print()

# print()
# print()



# msg2 = '아버지가방에들어가신다'
# result2 = okt.nouns(msg2)
# print(result2)
