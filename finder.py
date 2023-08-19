import pandas as pd
df = pd.read_excel(r"AllDB.xlsx")
# cls,room,no = int(input("Class: ")) , int(input("Room: ")), int(input("No: "))

def search(cls,room,no):
    ret =  df.loc[(df['Class']==cls) & (df['Room']==room) & (df['No']==no)]
    idk = ret.index.tolist()
    fst = ret.values.tolist()
    for i in range(len(fst)):
        fst[i].append(idk[i]);
    return fst

# print(df.loc[(df['Class']==cls) & (df['Room']==room) & (df['No']==no)])
# print(search(6,1,35))

