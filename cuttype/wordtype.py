import jieba
from jieba import posseg
jieba.load_userdict('./tw.dict.txt')
def cutwithtype(p):
    words=posseg.cut(p)
    noun=[]
    for i,j in words:
        if j[0]=="n" or j[0]=="t" or j=="ORG" :
            if len(i)>1:
                noun.append(str(i))
    sort_noun=list(set(noun))
    sort_noun.sort(key=noun.index)
    return sort_noun


