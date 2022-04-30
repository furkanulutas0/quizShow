import random
from tkinter import *
from tkinter import messagebox

_questions = [("Hangi ülkenin iki tane başkenti vardır?", "A", ["Güney Afrika", "Senegal", "El Salvador", "Venezuela"], 100),  # Soru-Cevap-Şıklar-Puan
              ('"Sinekli Bakkal" romanının yazarı kimdir?', "B", ["Reşat Nuri Güntekin", "Halide Edip Adıvar", "Ziya Gökalp", "Ömer Seyfettin"], 100),  # Soru-Cevap-Şıklar-Puan
              ("Mehmet Akif İstiklal Marşını nerede yazmıştır?", "D", ["Ayasofya", "Keçiören Camii", "Galata kulesi", "Tacettin Dergahı"], 100),  # Soru-Cevap-Şıklar-Puan
              ("Asprinin ham maddesesi olan ağaç hangisidir?", "B", ["Çınar", "Söğüt", "Kavak", "Gürgen"], 100),
              ("Tiger Woods hangi sporun önemli temsilcisidir?", "D", ["Basketbol", "Futbol", "Beyzbol", "Golf"], 100),
              ("En uzun gecenin yaşandığı tarih hangisidir?", "A", ["21 Aralık", "21 Haziran", "21 Şubat", "21 Mart"], 100),
              ("FIFA'ya göre futbolun doğduğu ülke hangisidir?", "C", ["İngiltere", "Brezilya", "Çin", "Almanya"], 100),
              ('"BÜLBÜL" Destanı hangi ilimizin işgali üzerine yazılmıştır?', "C", ["İzmir", "Adana", "Bursa", "Sakarya"], 100),
              ("Bozkırın 'Tezenesi' olarak anılan halk ozanı kimdir?", "C", ["Aşık Veysel", "Musa Eroğlu", "Neşet Ertaş", "Aşık Mahsuni Şerif"], 100),
              ("Genetik olarak başarıyla kopyalanan ilk canlı hangisidir", "B", ["At", "Koyun", "Fare", "Maymun"], 100)
              # Soru-Cevap-Şıklar-Puan
              ]

trueAnswerPoint = 0
wrongAnswerPoint = 0
totalAnswerPoint = 0
queCounter = 1

def resetPoints():
    global totalAnswerPoint, trueAnswerPoint, wrongAnswerPoint, queCounter
    totalAnswerPoint = 0
    trueAnswerPoint = 0
    wrongAnswerPoint = 0
    queCounter = 1

def resetQuestions():
    global _questions
    _questions = [
        ("Hangi ülkenin iki tane başkenti vardır?", "A", ["Güney Afrika", "Senegal", "El Salvador", "Venezuela"], 100),
        # Soru-Cevap-Şıklar-Puan
        ('"Sinekli Bakkal" romanının yazarı kimdir?', "B",
         ["Reşat Nuri Güntekin", "Halide Edip Adıvar", "Ziya Gökalp", "Ömer Seyfettin"], 100),  # Soru-Cevap-Şıklar-Puan
        ("Mehmet Akif İstiklal Marşını nerede yazmıştır?", "D",
         ["Ayasofya", "Keçiören Camii", "Galata kulesi", "Tacettin Dergahı"], 100),  # Soru-Cevap-Şıklar-Puan
        ("Asprinin ham maddesesi olan ağaç hangisidir?", "B", ["Çınar", "Söğüt", "Kavak", "Gürgen"], 100),
        ("Tiger Woods hangi sporun önemli temsilcisidir?", "D", ["Basketbol", "Futbol", "Beyzbol", "Golf"], 100),
        ("En uzun gecenin yaşandığı tarih hangisidir?", "A", ["21 Aralık", "21 Haziran", "21 Şubat", "21 Mart"], 100),
        ("FIFA'ya göre futbolun doğduğu ülke hangisidir?", "C", ["İngiltere", "Brezilya", "Çin", "Almanya"], 100),
        ('"BÜLBÜL" Destanı hangi ilimizin işgali üzerine yazılmıştır?', "C", ["İzmir", "Adana", "Bursa", "Sakarya"],
         100),
        ("Bozkırın 'Tezenesi' olarak anılan halk ozanı kimdir?", "C",
         ["Aşık Veysel", "Musa Eroğlu", "Neşet Ertaş", "Aşık Mahsuni Şerif"], 100),
        ("Genetik olarak başarıyla kopyalanan ilk canlı hangisidir", "B", ["At", "Koyun", "Fare", "Maymun"], 100)
        # Soru-Cevap-Şıklar-Puan
        ]

def selectQue():
    global selectQuestion, selectedQuestion, selectedAnswer, selectedPoint, selectedOption1, selectedOption2, selectedOption3, selectedOption4
    if queCounter == 11:
        window.destroy()
        winGame()
    elif len(_questions) == 0:
        window.destroy()
        nonQuestionScreen()
    else:
        selectQuestion = random.choice(_questions)

        selectedQuestion = selectQuestion[0]
        selectedAnswer = selectQuestion[1]
        selectedOption1 = selectQuestion[2][0]
        selectedOption2 = selectQuestion[2][1]
        selectedOption3 = selectQuestion[2][2]
        selectedOption4 = selectQuestion[2][3]
        selectedPoint = selectQuestion[3]

        _questions.remove(selectQuestion)

        if queCounter == 2:
            queProgress_1.config(bg='green')
            queProgress_2.config(bg='orange')
        elif queCounter == 3:
            queProgress_2.config(bg='green')
            queProgress_3.config(bg='orange')
        elif queCounter == 4:
            queProgress_3.config(bg='green')
            queProgress_4.config(bg='orange')
        elif queCounter == 5:
            queProgress_4.config(bg='green')
            queProgress_5.config(bg='orange')
        elif queCounter == 6:
            queProgress_5.config(bg='green')
            queProgress_6.config(bg='orange')
        elif queCounter == 7:
            queProgress_6.config(bg='green')
            queProgress_7.config(bg='orange')
        elif queCounter == 8:
            queProgress_7.config(bg='green')
            queProgress_8.config(bg='orange')
        elif queCounter == 9:
            queProgress_8.config(bg='green')
            queProgress_9.config(bg='orange')
        elif queCounter == 10:
            queProgress_9.config(bg='green')
            queProgress_10.config(bg='orange')
##
        if totalAnswerPoint < 100 :
            pointProgress_1.config(bg='orange')
        elif totalAnswerPoint == 100:
            pointProgress_1.config(bg='blue')
            pointProgress_2.config(bg='orange')
        elif totalAnswerPoint == 200:
            pointProgress_2.config(bg='blue')
            pointProgress_3.config(bg='orange')
        elif totalAnswerPoint == 300:
            pointProgress_3.config(bg='blue')
            pointProgress_4.config(bg='orange')
        elif totalAnswerPoint == 400:
            pointProgress_4.config(bg='blue')
            pointProgress_5.config(bg='orange')
        elif totalAnswerPoint == 500:
            pointProgress_5.config(bg='blue')
            pointProgress_6.config(bg='orange')
        elif totalAnswerPoint == 600:
            pointProgress_6.config(bg='blue')
            pointProgress_7.config(bg='orange')
        elif totalAnswerPoint == 700:
            pointProgress_7.config(bg='blue')
            pointProgress_8.config(bg='orange')
        elif totalAnswerPoint == 800:
            pointProgress_8.config(bg='blue')
            pointProgress_9.config(bg='orange')
        elif totalAnswerPoint == 900:
            pointProgress_9.config(bg='blue')
            pointProgress_10.config(bg='green')

def writeQue():
    questionAreaText.config(text=f'{selectedQuestion}')
    OptionText_1.config(text=f'{selectedOption1}')
    OptionText_2.config(text=f'{selectedOption2}')
    OptionText_3.config(text=f'{selectedOption3}')
    OptionText_4.config(text=f'{selectedOption4}')

def checkAnswer():
    global trueAnswerPoint, wrongAnswerPoint, totalAnswerPoint, queCounter
    trueAnswer = str(selectedAnswer)

    if trueAnswer == userAnswer:
        trueAnswerPoint = trueAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint + selectedPoint
        queCounter = queCounter + 1
        print(f"Doğru Cevap: Kaçıncı soru {queCounter}")
        selectQue()
        writeQue()
    elif trueAnswer == userAnswer:
        trueAnswerPoint = trueAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint + selectedPoint
        queCounter = queCounter + 1
        print(f"Doğru Cevap: Kaçıncı soru {queCounter}")
        selectQue()
        writeQue()
    elif trueAnswer == userAnswer:
        trueAnswerPoint = trueAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint + selectedPoint
        queCounter = queCounter + 1
        print(f"Doğru Cevap: Kaçıncı soru {queCounter}")
        selectQue()
        writeQue()
    elif trueAnswer == userAnswer:
        trueAnswerPoint = trueAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint + selectedPoint
        queCounter = queCounter + 1
        print(f"Doğru Cevap: Kaçıncı soru {queCounter}")
        selectQue()
        writeQue()
    else:
        print("Yanlış Cevap")
        wrongAnswerPoint = wrongAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint - selectedPoint
        window.destroy()
        eliminatedScreen()

def selectAnswerA():
    global userAnswer
    userAnswer = str(Option_1_button.cget('text'))
    userAnswer.upper()

def selectAnswerB():
    global userAnswer
    userAnswer = str(Option_2_button.cget('text'))
    userAnswer.upper()

def selectAnswerC():
    global userAnswer
    userAnswer = str(Option_3_button.cget('text'))
    userAnswer.upper()

def selectAnswerD():
    global userAnswer
    userAnswer = str(Option_4_button.cget('text'))
    userAnswer.upper()

def startScreen():
    window = Tk()
    window.title("Bilgi Yarışması")
    window.geometry("800x600")

    mainCanvas = Canvas(window, height=800, width=600)
    mainCanvas.pack()

    frameBG = Canvas(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    versionText = Label(window, text='version v.2.1', bg='grey')
    versionText.place(relx=0.90, rely=0.97, relheight=0.025, relwidth=0.095 )

    buttonsArea = Frame(window, bg='white')
    buttonsArea.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.1)

    buttonStart = Button(buttonsArea, text='Başla!', bg='#32a852', font='Calbri 12 bold',
                         command=lambda: [window.destroy(), mainScreen()])
    buttonStart.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    buttonHelp = Button(buttonsArea, text='Nasıl Oynanır?', bg='#2596be', font='Calbri 12',
                        command=lambda: [window.destroy(), helpScreen()])
    buttonHelp.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    window.mainloop()

def helpScreen():
    infoText = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

    window = Tk()
    window.title("Bilgi Yarışması")
    window.geometry("800x600")

    mainCanvas = Canvas(window, height=800, width=600)
    mainCanvas.pack()

    frameBG = Canvas(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    topicArea = Frame(window, bg='#6B6D6D')
    topicArea.place(relx=0.35, rely=0.15, relwidth=0.3, relheight=0.08)
    topicLabel = Label(topicArea, text='NASIL OYNANIR?', font='calbri 11 bold', bg='#6B6D6D')
    topicLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    infoArea = Frame(window, bg='#6B6D6D')
    infoArea.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)
    infoLabel = Label(infoArea, text=f'{infoText}', font='calbri 11 bold', bg='#6B6D6D', justify=CENTER, )
    infoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    backButtonArea = Frame(window)
    backButtonArea.place(relx=0.6, rely=0.82, relwidth=0.1, relheight=0.05)
    backButton = Button(backButtonArea, text='Ana Menü', bg='white', font='calbri 10',
                        command=lambda: [window.destroy(), startScreen()])
    backButton.place(relx=0, rely=0, relwidth=1, relheight=1)

    window.mainloop()

def mainScreen():
    global questionAreaText, Option_1_button, Option_2_button, Option_3_button, Option_4_button, OptionText_1, OptionText_2, OptionText_3, OptionText_4
    global time_progressBar, time_progressBarText, window, queProgress_1, queProgress_2, queProgress_3,queProgress_4,queProgress_5,queProgress_6,queProgress_7,queProgress_8,queProgress_9,queProgress_10
    global pointProgress_1, pointProgress_2, pointProgress_3,pointProgress_4,pointProgress_5,pointProgress_6,pointProgress_7,pointProgress_8,pointProgress_9,pointProgress_10
    window = Tk()
    window.title("Bilgi Yarışması")
    window.geometry("800x600")

    mainCanvas = Canvas(window, height=800, width=600)
    mainCanvas.pack()

    frameBG = Canvas(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    versionText = Label(window, text='version v.2.1', bg='grey')
    versionText.place(relx=0.90, rely=0.97, relheight=0.025, relwidth=0.095 )

    questionArea = Frame(frameBG, bg='green')
    questionArea.place(relx=0.15, rely=0.35, relwidth=0.7, relheight=0.1)

    questionAreaText = Label(questionArea, text=f"", font='calbri 10', wraplength=550)
    questionAreaText.place(relx=0, rely=0, relwidth=1, relheight=1)

    time_progressBar = Frame(frameBG, bg='yellow')
    time_progressBar.place(relx=0.15, rely=0.47, relwidth=0.7, relheight=0.02)

    #    time_progressBarText = Label(time_progressBar, text=f"Time")
    #    time_progressBarText.pack()

    answerArea = Frame(frameBG, bg='cyan')
    answerArea.place(relx=0.15, rely=0.50, relwidth=0.7, relheight=0.15)

    ###### ŞIKLAR

    Option_1_area = Frame(answerArea, bg='white', )
    Option_1_area.place(relx=0, rely=0, relwidth=0.1, relheight=0.5)

    Option_1_button = Button(Option_1_area, bg='grey', activebackground='orange', text="A", font='calbri 12 bold', )
    Option_1_button.place(relx=0, rely=0, relwidth=1, relheight=1)

    OptionTextArea_1 = Frame(answerArea, bg='grey', )
    OptionTextArea_1.place(relx=0.1, rely=0, relwidth=0.4, relheight=0.5)

    OptionText_1 = Label(OptionTextArea_1, text='Şık 1', wraplength=300, bg='white', foreground='black')
    OptionText_1.place(relx=0, rely=0, relwidth=1, relheight=1)

    Option_2_area = Frame(answerArea, bg='grey')
    Option_2_area.place(relx=0.9, rely=0, relwidth=0.1, relheight=0.5)

    Option_2_button = Button(Option_2_area, bg='white', activebackground='orange', text="B", font='calbri 12 bold', )
    Option_2_button.place(relx=0, rely=0, relwidth=1, relheight=1)

    OptionTextArea_2 = Frame(answerArea, bg='grey', )
    OptionTextArea_2.place(relx=0.5, rely=0, relwidth=0.4, relheight=0.5)

    OptionText_2 = Label(OptionTextArea_2, text='Şık 2', wraplength=300, bg='grey', foreground='black')
    OptionText_2.place(relx=0, rely=0, relwidth=1, relheight=1)

    Option_3_area = Frame(answerArea, bg='grey')
    Option_3_area.place(relx=0, rely=0.5, relwidth=0.1, relheight=0.5)

    Option_3_button = Button(Option_3_area, bg='white', activebackground='orange', text="C", font='calbri 12 bold', )
    Option_3_button.place(relx=0, rely=0, relwidth=1, relheight=1)

    OptionTextArea_3 = Frame(answerArea, bg='grey', )
    OptionTextArea_3.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)

    OptionText_3 = Label(OptionTextArea_3, text='Şık 3', wraplength=300, bg='grey', foreground='black')
    OptionText_3.place(relx=0, rely=0, relwidth=1, relheight=1)

    Option_4_area = Frame(answerArea, bg='white')
    Option_4_area.place(relx=0.9, rely=0.5, relwidth=0.1, relheight=0.5)

    Option_4_button = Button(Option_4_area, bg='grey', activebackground='orange', text="D", font='calbri 12 bold', )
    Option_4_button.place(relx=0, rely=0, relwidth=1, relheight=1)

    OptionTextArea_4 = Frame(answerArea, bg='grey')
    OptionTextArea_4.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.5)

    OptionText_4 = Label(OptionTextArea_4, text='Şık 4', wraplength=300, bg='white', foreground='black')
    OptionText_4.place(relx=0, rely=0, relwidth=1, relheight=1)

    strtBtnArea = Frame(window, bg='white')
    strtBtnArea.place(relx=0.7, rely=0.7, relwidth=0.07, relheight=0.05)

    strtBtn = Button(strtBtnArea, bg='green', activebackground='orange', text="BAŞLA", font='calbri 8',
                     command=lambda: [selectQue(), writeQue(), resetPoints(), resetQuestions(), strtBtn.destroy(), strtBtnArea.destroy(),
                                      queProgress_1.config(bg='orange'),
                                      Option_1_button.config(command=lambda: [selectAnswerA(), checkAnswer()]),
                                      Option_2_button.config(command=lambda: [selectAnswerB(), checkAnswer()]),
                                      Option_3_button.config(command=lambda: [selectAnswerC(), checkAnswer()]),
                                      Option_4_button.config(command=lambda: [selectAnswerD(), checkAnswer()])])
    strtBtn.place(relx=0, rely=0, relwidth=1, relheight=1)

    ###### Sağ Kısım

    queProgress_area = Frame(frameBG, bg='#2b2b2b')
    queProgress_area.place(relx=0.05, rely=0.2, relwidth=0.02, relheight=0.6)

    queProgress_1 = Frame(queProgress_area, bg='grey')
    queProgress_1.place(relx=0, rely=0.98, relwidth=1, relheight=0.02)
    queProgress_2 = Frame(queProgress_area, bg='grey')
    queProgress_2.place(relx=0, rely=0.88, relwidth=1, relheight=0.02)
    queProgress_3 = Frame(queProgress_area, bg='grey')
    queProgress_3.place(relx=0, rely=0.77, relwidth=1, relheight=0.02)
    queProgress_4 = Frame(queProgress_area, bg='grey')
    queProgress_4.place(relx=0, rely=0.66, relwidth=1, relheight=0.02)
    queProgress_5 = Frame(queProgress_area, bg='grey')
    queProgress_5.place(relx=0, rely=0.55, relwidth=1, relheight=0.02)
    queProgress_6 = Frame(queProgress_area, bg='grey')
    queProgress_6.place(relx=0, rely=0.44, relwidth=1, relheight=0.02)
    queProgress_7 = Frame(queProgress_area, bg='grey')
    queProgress_7.place(relx=0, rely=0.33, relwidth=1, relheight=0.02)
    queProgress_8 = Frame(queProgress_area, bg='grey')
    queProgress_8.place(relx=0, rely=0.22, relwidth=1, relheight=0.02)
    queProgress_9 = Frame(queProgress_area, bg='grey')
    queProgress_9.place(relx=0, rely=0.11, relwidth=1, relheight=0.02)
    queProgress_10 = Frame(queProgress_area, bg='grey')
    queProgress_10.place(relx=0, rely=0.00, relwidth=1, relheight=0.02)

    ###### Sol Kısım

    pointProgress_area = Frame(frameBG, bg='#2b2b2b')
    pointProgress_area.place(relx=0.93, rely=0.2, relwidth=0.02, relheight=0.6)

    pointProgress_1 = Frame(pointProgress_area, bg='grey')
    pointProgress_1.place(relx=0, rely=0.98, relwidth=1, relheight=0.02)
    pointProgress_2 = Frame(pointProgress_area, bg='grey')
    pointProgress_2.place(relx=0, rely=0.88, relwidth=1, relheight=0.02)
    pointProgress_3 = Frame(pointProgress_area, bg='grey')
    pointProgress_3.place(relx=0, rely=0.77, relwidth=1, relheight=0.02)
    pointProgress_4 = Frame(pointProgress_area, bg='grey')
    pointProgress_4.place(relx=0, rely=0.66, relwidth=1, relheight=0.02)
    pointProgress_5 = Frame(pointProgress_area, bg='grey')
    pointProgress_5.place(relx=0, rely=0.55, relwidth=1, relheight=0.02)
    pointProgress_6 = Frame(pointProgress_area, bg='grey')
    pointProgress_6.place(relx=0, rely=0.44, relwidth=1, relheight=0.02)
    pointProgress_7 = Frame(pointProgress_area, bg='grey')
    pointProgress_7.place(relx=0, rely=0.33, relwidth=1, relheight=0.02)
    pointProgress_8 = Frame(pointProgress_area, bg='grey')
    pointProgress_8.place(relx=0, rely=0.22, relwidth=1, relheight=0.02)
    pointProgress_9 = Frame(pointProgress_area, bg='grey')
    pointProgress_9.place(relx=0, rely=0.11, relwidth=1, relheight=0.02)
    pointProgress_10 = Frame(pointProgress_area, bg='grey')
    pointProgress_10.place(relx=0, rely=0.00, relwidth=1, relheight=0.02)

    window.mainloop()

def eliminatedScreen():
    window = Tk()

    window.title("Bilgi Yarışması")
    window.geometry("800x600")

    mainCanvas = Canvas(window, height=800, width=600)
    mainCanvas.pack()

    frameBG = Canvas(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    versionText = Label(window, text='version v.2.1', bg='grey')
    versionText.place(relx=0.90, rely=0.97, relheight=0.025, relwidth=0.095 )

    eliminateTextArea = Frame(frameBG, bg='#3c3f41')
    eliminateTextArea.place(relx=0.33, rely=0.2, relwidth=0.33, relheight=0.03)

    eliminateText = Label(eliminateTextArea, text="E  L  E  N  D  I  N  !", bg='#3c3f41', foreground='red',
                          font='trebuchetms 16 bold')
    eliminateText.place(relx=0, rely=0.1, relwidth=1, relheight=0.99)

    scoreBoardArea = Frame(frameBG, bg='#2f2f2f')
    scoreBoardArea.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)

    scoreBoardTrueScore = Label(scoreBoardArea, text=f'Doğru Cevap: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardTrueScore.place(relx=0, rely=0, relwidth=0.8, relheight=0.3)

    scoreText = Label(scoreBoardArea, bg='white', text=f'{trueAnswerPoint}')
    scoreText.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.3)

    scoreBoardWrongScore = Label(scoreBoardArea, text=f'Yanlış Cevap: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardWrongScore.place(relx=0, rely=0.35, relwidth=0.8, relheight=0.3)

    scoreText2 = Label(scoreBoardArea, bg='white', text=f'{wrongAnswerPoint}')
    scoreText2.place(relx=0.8, rely=0.35, relwidth=0.2, relheight=0.3)

    scoreBoardPointScore = Label(scoreBoardArea, text=f'Toplam Puan: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardPointScore.place(relx=0, rely=0.7, relwidth=0.8, relheight=0.3)

    scoreText3 = Label(scoreBoardArea, bg='white', text=f'{totalAnswerPoint}')
    scoreText3.place(relx=0.8, rely=0.7, relwidth=0.2, relheight=0.3)

    buttonsArea = Frame(window, bg='white')
    buttonsArea.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.08)

    buttonStart = Button(buttonsArea, text='Yeniden Başla', bg='#32a852', font='Calbri 12 bold', wraplength=100,
                         command=lambda: [window.destroy(), resetPoints(), resetQuestions(), mainScreen()])
    buttonStart.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    buttonExit = Button(buttonsArea, text='Çıkış', bg='#a83232', font='Calbri 12', command=lambda: [window.destroy()])
    buttonExit.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    homeButton = Button(frameBG, text='Ana Menü', bg='#2596be', font='Calbri 12',
                        command=lambda: [window.destroy(), startScreen()])
    homeButton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.05)

    window.mainloop()

def nonQuestionScreen():
    window = Tk()

    window.title("Bilgi Yarışması")
    window.geometry("800x600")

    mainCanvas = Canvas(window, height=800, width=600)
    mainCanvas.pack()

    frameBG = Canvas(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    versionText = Label(window, text='version v.2.1', bg='grey')
    versionText.place(relx=0.90, rely=0.97, relheight=0.025, relwidth=0.095 )

    eliminateTextArea = Frame(frameBG, bg='#3c3f41')
    eliminateTextArea.place(relx=0.33, rely=0.2, relwidth=0.33, relheight=0.03)

    eliminateText = Label(eliminateTextArea, text="Oyun Bitti  !", bg='#3c3f41', foreground='orange',
                          font='trebuchetms 16 bold')
    eliminateText.place(relx=0, rely=0.1, relwidth=1, relheight=0.99)

    scoreBoardArea = Frame(frameBG, bg='#2f2f2f')
    scoreBoardArea.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)

    scoreBoardTrueScore = Label(scoreBoardArea, text=f'Doğru Cevap: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardTrueScore.place(relx=0, rely=0, relwidth=0.8, relheight=0.3)

    scoreText = Label(scoreBoardArea, bg='white', text=f'{trueAnswerPoint}')
    scoreText.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.3)

    scoreBoardWrongScore = Label(scoreBoardArea, text=f'Yanlış Cevap: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardWrongScore.place(relx=0, rely=0.35, relwidth=0.8, relheight=0.3)

    scoreText2 = Label(scoreBoardArea, bg='white', text=f'{wrongAnswerPoint}')
    scoreText2.place(relx=0.8, rely=0.35, relwidth=0.2, relheight=0.3)

    scoreBoardPointScore = Label(scoreBoardArea, text=f'Toplam Puan: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardPointScore.place(relx=0, rely=0.7, relwidth=0.8, relheight=0.3)

    scoreText3 = Label(scoreBoardArea, bg='white', text=f'{totalAnswerPoint}')
    scoreText3.place(relx=0.8, rely=0.7, relwidth=0.2, relheight=0.3)

    buttonsArea = Frame(window, bg='white')
    buttonsArea.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.08)

    buttonStart = Button(buttonsArea, text='Yeniden Başla', bg='#32a852', font='Calbri 12 bold', wraplength=100,
                         command=lambda: [window.destroy(),resetPoints(), resetQuestions(),mainScreen()])
    buttonStart.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    buttonExit = Button(buttonsArea, text='Çıkış', bg='#a83232', font='Calbri 12', command=lambda: [window.destroy()])
    buttonExit.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    homeButton = Button(frameBG, text='Ana Menü', bg='#2596be', font='Calbri 12',
                        command=lambda: [window.destroy(), startScreen()])
    homeButton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.05)
    messagebox.showwarning("Oyun Bitmek Zorunda Kaldı!", "Yetersiz soru sayısı nedeniyle oyun sonlandı.")
    window.mainloop()

def winGame():
    window = Tk()

    window.title("Bilgi Yarışması")
    window.geometry("800x600")

    mainCanvas = Canvas(window, height=800, width=600)
    mainCanvas.pack()

    frameBG = Canvas(window, bg='#3c3f41')
    frameBG.place(relx=0, rely=0, relwidth=1, relheight=1)

    versionText = Label(window, text='version v.2.1', bg='grey')
    versionText.place(relx=0.90, rely=0.97, relheight=0.025, relwidth=0.095 )

    eliminateTextArea = Frame(frameBG, bg='#3c3f41')
    eliminateTextArea.place(relx=0.33, rely=0.2, relwidth=0.33, relheight=0.03)

    eliminateText = Label(eliminateTextArea, text="TEBRİKLER  !", bg='#3c3f41', foreground='GREEN',
                          font='trebuchetms 16 bold')
    eliminateText.place(relx=0, rely=0.1, relwidth=1, relheight=0.99)

    scoreBoardArea = Frame(frameBG, bg='#2f2f2f')
    scoreBoardArea.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.2)

    scoreBoardTrueScore = Label(scoreBoardArea, text=f'Doğru Cevap: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardTrueScore.place(relx=0, rely=0, relwidth=0.8, relheight=0.3)

    scoreText = Label(scoreBoardArea, bg='white', text=f'{trueAnswerPoint}')
    scoreText.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.3)

    scoreBoardWrongScore = Label(scoreBoardArea, text=f'Yanlış Cevap: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardWrongScore.place(relx=0, rely=0.35, relwidth=0.8, relheight=0.3)

    scoreText2 = Label(scoreBoardArea, bg='white', text=f'{wrongAnswerPoint}')
    scoreText2.place(relx=0.8, rely=0.35, relwidth=0.2, relheight=0.3)

    scoreBoardPointScore = Label(scoreBoardArea, text=f'Toplam Puan: ', bg='grey', font='calbri 11', justify=LEFT)
    scoreBoardPointScore.place(relx=0, rely=0.7, relwidth=0.8, relheight=0.3)

    scoreText3 = Label(scoreBoardArea, bg='white', text=f'{totalAnswerPoint}')
    scoreText3.place(relx=0.8, rely=0.7, relwidth=0.2, relheight=0.3)

    buttonsArea = Frame(window, bg='white')
    buttonsArea.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.08)

    buttonStart = Button(buttonsArea, text='Yeniden Başla', bg='#32a852', font='Calbri 12 bold', wraplength=100,
                         command=lambda: [window.destroy(),resetPoints(), resetQuestions(),mainScreen()])
    buttonStart.place(relx=0, rely=0, relwidth=0.5, relheight=1)

    buttonExit = Button(buttonsArea, text='Çıkış', bg='#a83232', font='Calbri 12', command=lambda: [window.destroy()])
    buttonExit.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    homeButton = Button(frameBG, text='Ana Menü', bg='#2596be', font='Calbri 12',
                        command=lambda: [window.destroy(), startScreen()])
    homeButton.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.05)
    messagebox.showinfo("TEBRİKLER!", "Tüm sorular doğru cevaplandı, nesin sen Einstein mı?")
    window.mainloop()

startScreen()


#Bu Satır GitHubdan eklendi --> Git kontrol
