import numpy as np
import random
import konlpy
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from palettable.colorbrewer.qualitative import Dark2_8
import os

# setting current Path
currentPath = os.getcwd()
os.chdir(currentPath+"/hw2/hw02_19101198")

# setting color
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Dark2_8.colors[random.randint(0,7)])

# setting font path
font = "./nanum-pen/NanumPen"
font_path = "%s.ttf" % font

# setting mask img path
icon = "BomBom_Mask_2"
icon_path = "%s.png" % icon

# read text file
f = open("bombom.txt", 'r')
message = f.read()
# print(message)
f.close()

# setting mask
icon = Image.open(icon_path)
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

# generate word cloud
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
# wc.generate_from_text(message)

# use Hannanum & show nouns
han = konlpy.tag.Hannanum()
noun = han.nouns(message)
count = Counter(noun)
noun_list = count.most_common(10000)
# for v in noun_list:
#     print(v)

# store noun_list at the noun_list txt file
with open("noun_list.txt", 'w', encoding='utf-8') as f:
    for v in noun_list:
        f.write(" ".join(map(str,v)))
        f.write("\n")

# generate word cloud from frequencies & extract the result img file
wc.generate_from_frequencies(dict(noun_list))
wc.recolor(color_func=color_func, random_state=3)
wc.to_file("BomBom.png")