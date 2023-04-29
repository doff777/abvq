
string = input()

def word_calc(a):
    b = " ".join(a.split())
    S = 0
    for i in range(len(b)):
        if b[i] == ' ' :
            S+=1
    return (S+1)
def wordland(a):
    S = 0
    b = " ".join(a.split())
    for i in range(len(b)):
        if b[i].isalpha():
            S+=1
    S1 = word_calc(a)
    return S/S1
print(word_calc(string))
print(wordland(string))
