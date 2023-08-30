import re
import glob
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

x = glob.glob(r"C:\Users\aiueo\Downloads/*.csv")
x.sort()
data = []
for i in x:
    with open(i, encoding="shift-jis") as f:
        data += f.read().split("\n")

result = []
date_list = []
for i in data:
    temp = re.search('"\\\-?[0-9]*,?[0-9]+"', i)
    if temp is None:
        continue
    x = temp.group()
    numbers_only = re.sub(r'[^-\d]', "", x)
    result.append(int(numbers_only))
    date = re.search(pattern=r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})', string=i)
    dt =datetime.strptime(date.group(), "%Y/%m/%d %H:%M:%S")
    date_list.append(dt)
result = np.array(result)
sums = 68392-result.sum()
result = result+sums
plt.plot(date_list,result)
plt.show()