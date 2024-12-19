def game():
    return 44

score = game()
with open("C:\\Users\\lenovo\\Desktop\\-\\PYTHON HARRY\\CH 09\\hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("C:\\Users\\lenovo\\Desktop\\-\\PYTHON HARRY\\CH 09\\hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("C:\\Users\\lenovo\\Desktop\\-\\PYTHON HARRY\\CH 09\\hiscore.txt", "w") as f:
        f.write(str(score))