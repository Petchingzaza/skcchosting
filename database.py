import pandas as pd
import math
from random import shuffle

def cond(cell):
    if isinstance(cell,str): return cell != '-'
    return not math.isnan(cell)
df = pd.read_excel(r"C:\Users\Admin\Downloads\แบบฟอร์มรับสมัครทีมในการแข่งขัน RoV E-sports (Responses).xlsx")
df.dropna(how='all', inplace=True)
df.reset_index(drop=True, inplace=True)
array_2d = df.values.tolist()
normal = array_2d
shuffle(normal)
c=0
ch=["A","B","C","D"]
final = []
for i in normal:
    head = i[:6]
    head.insert(0,ch[int(c/8)])
    head.insert(0,'RoV')
    print(head)
    final.append(head)
    header = head[:2]
    header.append(head[2])
    c+=1
    oth = i[6:]
    for j in range(0,len(oth),5):
        if(oth[j]!=oth[j]) : continue
        print(header+oth[j:j+5])
        final.append(header+oth[j:j+5])


df = pd.DataFrame(final, columns =["เกม","สาย","ทีม" ,"ชื่อ-สกุล ผู้สมัคร","ระดับชั้น","ห้อง","เลขที่"	,"ชื่อในเกม"])
print(df)
df.to_excel("RoVSheet.xlsx")
