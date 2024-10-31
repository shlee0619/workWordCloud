
from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt
import time


okt = Okt()
text = '컴퓨터프로그래머가길동이아버지가방에들어가시나요ㅎㅎ'
print(text)
print()

# pos함수 품사 tagging 
# norm=True : 단어를 정규화시켜 보여줌
# stem=True : 단어의 원형을 보여줌
# ret = okt.pos(text, norm=True, stem=True )
# ret = okt.pos(text, norm=False, stem=False )
ret = okt.pos(text)
print(ret)
print('\n타입확인 ' , type(ret))
time.sleep(0.5)

for myitem in ret:
    if len(myitem[0]) > 1:
        print(myitem[0], end=' ')



print()
print()