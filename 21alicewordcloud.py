import matplotlib
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


font_name = font_manager.FontProperties


file = open('./data/alice.txt', 'r', encoding='utf-8')
rfile = file.read()
print(rfile)
print()

spwords = set(STOPWORDS)

# spwords.add('은')
# spwords.add('은')
spwords.add(['그', '저', '니'])
spwords.add('said')
spwords.update(['hahaha', 'hohoho'])

mywc = WordCloud(max_font_size = 350, stopwords = spwords, 
                 font_path = 'C:/Windows/fonts/malgun.ttf',
                 background_color='black', width = 800, height=800)


