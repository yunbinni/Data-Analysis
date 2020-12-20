from konlpy.tag import Okt
from konlpy.utils import pprint

okt = Okt()

# 단어별 빈도수 출력 함수
def nounList(lines):
    nouns = []
    cnt = []
    text = []
    
    # 명사 list 추출 (x축, nouns)
    for line in lines:
        text = okt.nouns(u'%s' % line)
        for wd in text:
            if wd not in nouns: # 중복 방지 코드
                nouns.append(wd)
                
    # 명사별 빈도수 계산 (y축, cnt)
    for noun in nouns:
        wordcount = 0
        for line in lines:
            text = okt.nouns(u'%s' % line)
            wordcount += text.count(noun)
        cnt.append(wordcount)
    
    # 빈도별 내림차순 정렬
    table = dict(zip(nouns, cnt))
    table = sorted(table.items(), key=lambda x: x[1], reverse=True)
    table = dict(table)
    
    return table

txt = open('./lyrics.txt', encoding='utf-8')
txt = txt.readlines()

# matplotlib 한글설정
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

f_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)

# 시각화용 aes 설정
x = list(nounList(txt).keys())[:20]
y = list(nounList(txt).values())[:20]

# 시각화
plt.figure(figsize = (16, 9))
plt.bar(x, y)
plt.xticks(fontsize=14, rotation=90)
plt.yticks(fontsize=16)
plt.show()
