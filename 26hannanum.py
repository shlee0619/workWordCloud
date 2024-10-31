'''
# 코엔엘파이 
https://konlpy.org/ko/latest/

#KoNLPy의 말뭉치(corpus)
Hannanum  : 말뭉치를 이용해 생성된 사전  KAIST연구진 
Kkma : 세종 말뭉치를 이용해 생성된 사전(꼬꼬마)
Mecab : KoNLPy지원안됨 세종 말뭉치로 만들어진 CSV 형태의 사전
Twitter(Okt): 오픈 소스 한글 형태소 분석기
Komoran : 실습안함 Java 로 쓰여진 오픈소스 한글 형태소 분석기
'''

from konlpy.tag import Hannanum
from konlpy.tag import Kkma

print('Hannanum() 개체로 접근')
h = Hannanum()
msg1 = h.morphs('한국어는 주변 언어와 둘리악당들 방탄 어떤 친족 관계도 밝혀지지 않은 언어다')
print(msg1)
print()
msg2 = h.nouns('한국어는 주변 언어와 둘리악당들 방탄 어떤 친족 관계도 밝혀지지 않은 언어다')
print(msg2)
print()
msg3 = h.pos('한국어는 주변 언어와 둘리악당들 방탄 어떤 친족 관계도 밝혀지지 않은 언어다')
print(msg3)
print()
print(h.tagset) #더더더 자세한 설명  
import time
time.sleep(0.5)

print('- ' * 50)
print('Kkma() 개체로 접근 ')
k = Kkma()
msg1 = k.morphs('한국어는 주변 언어와 둘리악당들 방탄 어떤 친족 관계도 밝혀지지 않은 언어다')
print(msg1)
print()
msg2 = k.nouns('한국어는 주변 언어와 둘리악당들 방탄 어떤 친족 관계도 밝혀지지 않은 언어다')
print(msg2)
print()
print()
msg3 = k.pos('한국어는 주변 언어와 둘리악당들 방탄 어떤 친족 관계도 밝혀지지 않은 언어다')
print(msg3)
print()

print(k.tagset) #더더더 자세한 설명  
print()