#Сделано RedFoxMain 
#Git hub: https://github.com/RedFoxMain

import os
import secrets

def hide(words):
    try:
        res = ""
        rnd = secrets.SystemRandom()
        for ind in range(0,len(words)):
            elem = rnd.randint(0,ind)
            res += words[ind].replace(words[elem],f"{ind}")
        return res
    except Exception as e:
        print(e)
    
def CheckMistake(originalWord,pos,letter,health):
    if letter != originalWord[int(pos)]:
      health = health - 1
    else:
      if health < 3:
          health = health + 1
      else:
          health = health
    return health
      
def CheckAccuracy(originalWord, hideWord):
    state = []
    if hideWord.isalpha() == True:
        for ind in range(0,len(originalWord)):
            state.append(originalWord[ind] == hideWord[ind])
    else:
        return None      
    return all(state)
         
def nextStep(hideWord,words,pos,letter,health):
    hideWord = hideWord.replace(pos,letter)
    return hideWord
               
if __name__ == "__main__":
    wordList = ["Дом","Баня","Дача","Дым","Дыня","Программист"]
    words = secrets.choice(wordList)
    hideWord = hide(words)
    health = 3
    while True:
        os.system("clear")
        print("Зашифрованное слово: "+hideWord+"\nВаши жизни: "+ str(health))
        pos = input("Введите куда вставить слово: ")
        letter = input("Какую букву вставить: ")
        hideWord = nextStep(hideWord,words,pos,letter,health)
        health = CheckMistake(words,pos,letter,health)
        if health == 0:
            print("Вы проиграли!")
            break
        if health == 1:
            os.system("clear")
            hideWord = hide(words)
        win = CheckAccuracy(words,hideWord)
        if win:
            os.system("clear")
            print("Вы угадали слово: "+hideWord)
            print("Победа!")
            break
