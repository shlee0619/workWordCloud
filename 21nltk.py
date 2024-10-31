import matplotlib
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
  
font_name = font_manager.FontProperties(fname='C:/Windows/fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)


import nltk    
nltk.download()  
print('nltk  test 12:37' )

