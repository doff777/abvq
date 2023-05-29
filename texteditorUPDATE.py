import string

def word_calc(str):
    b = " ".join(str.split())
    S = 0
    for i in range(len(b)):
        if b[i] == ' ' :
            S+=1
    return (S+1)

def wordland(str):
    S = 0
    b = " ".join(str.split())
    for i in range(len(b)):
        if b[i].isalpha():
            S+=1
    S1 = word_calc(str)
    return S/S1

def getWordFrequency(str, mode = 0):

    if len(str) == 0 or str==None:
        return 0

    text = str.lower()
    deteteChars = string.punctuation + '\n\t«»–'
    text = "".join([ch for ch in text if ch not in deteteChars])
    text = " ".join(text.split())
    print(text)
    dict = {}

    if mode == 0:
        for i in text.split():

            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] += 1

    elif mode == 1:
        for i in text.split():
            if len(i)>2:
                if i not in dict.keys():
                    dict[i] = 1
                else:
                    dict[i] += 1
    else:
        return None

    return dict

def popular_words(str):
    punct = ',.!?:;'
    ltxt = [w.rstrip(punct).lower() for w in str.split() if len(w.rstrip(punct)) > 1]
    print(*sorted(set(ltxt), key=ltxt.count, reverse=True)[:10], sep='\n')

b=input()
with open(b+'.txt','r',encoding = 'utf-8') as sr:
    str = sr.read()



print(getWordFrequency(str,1,),2*"\n")
popular_words(str)
