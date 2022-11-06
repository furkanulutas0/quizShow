
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import homePage
#import main
import random
import time
import pygame
import sounds
import winScreen, loseScreen

_questions = [
    ("Hangi ülkenin iki tane başkenti vardır?", "Güney Afrika", ["Güney Afrika", "Senegal", "El Salvador", "Venezuela"],
     100),  # Soru-Cevap-Şıklar-Puan
    ('"Sinekli Bakkal" romanının yazarı kimdir?', "Halide Edip Adıvar",
     ["Reşat Nuri Güntekin", "Halide Edip Adıvar", "Ziya Gökalp", "Ömer Seyfettin"], 100),  # Soru-Cevap-Şıklar-Puan
    ("Mehmet Akif İstiklal Marşını nerede yazmıştır?", "Tacettin Dergahı",
     ["Ayasofya", "Keçiören Camii", "Galata kulesi", "Tacettin Dergahı"], 100),  # Soru-Cevap-Şıklar-Puan
    ("Asprinin ham maddesesi olan ağaç hangisidir?", "Söğüt", ["Çınar", "Söğüt", "Kavak", "Gürgen"], 100),
    ("Tiger Woods hangi sporun önemli temsilcisidir?", "Golf", ["Basketbol", "Futbol", "Golf", "Beyzbol"], 100),
    ("En uzun gecenin yaşandığı tarih hangisidir?", "21 Aralık", ["21 Aralık", "21 Haziran", "21 Şubat", "21 Mart"],
     100),
    ("FIFA'ya göre futbolun doğduğu ülke hangisidir?", "Çin", ["İngiltere", "Brezilya", "Çin", "Almanya"], 100),
    ('"BÜLBÜL" Destanı hangi ilimizin işgali üzerine yazılmıştır?', "Bursa", ["İzmir", "Adana", "Sakarya", "Bursa"],
     100),
    ("Bozkırın 'Tezenesi' olarak anılan halk ozanı kimdir?", "Neşet Ertaş",
     ["Aşık Veysel", "Musa Eroğlu", "Neşet Ertaş", "Aşık Mahsuni Şerif"], 100),
    ("Uzayda yetiştirilen ilk bitki nedir?", "Patates",["Patates", "Havuç", "Dereotu", "Sinir Olduğun Kişi"], 100)
    # Soru-Cevap-Şıklar-Puan
]

trueAnswerPoint = 0
wrongAnswerPoint = 0
totalAnswerPoint = 0
queCounter = 1
comboCounter = 0


def resetPoints():
    global totalAnswerPoint, trueAnswerPoint, wrongAnswerPoint, queCounter, comboCounter
    totalAnswerPoint = 0
    trueAnswerPoint = 0
    wrongAnswerPoint = 0
    comboCounter = 0
    queCounter = 1

def resetQuestions():
    global _questions
    _questions = [
        ("Hangi ülkenin iki tane başkenti vardır?", "Güney Afrika",
         ["Güney Afrika", "Senegal", "El Salvador", "Venezuela"],
         100),  # Soru-Cevap-Şıklar-Puan
        ('"Sinekli Bakkal" romanının yazarı kimdir?', "Halide Edip Adıvar",
         ["Reşat Nuri Güntekin", "Halide Edip Adıvar", "Ziya Gökalp", "Ömer Seyfettin"], 100),  # Soru-Cevap-Şıklar-Puan
        ("Mehmet Akif İstiklal Marşını nerede yazmıştır?", "Tacettin Dergahı",
         ["Ayasofya", "Keçiören Camii", "Galata kulesi", "Tacettin Dergahı"], 100),  # Soru-Cevap-Şıklar-Puan
        ("Asprinin ham maddesesi olan ağaç hangisidir?", "Söğüt", ["Çınar", "Söğüt", "Kavak", "Gürgen"], 100),
        ("Tiger Woods hangi sporun önemli temsilcisidir?", "Golf", ["Basketbol", "Futbol", "Golf", "Beyzbol"], 100),
        ("En uzun gecenin yaşandığı tarih hangisidir?", "21 Aralık", ["21 Aralık", "21 Haziran", "21 Şubat", "21 Mart"],
         100),
        ("FIFA'ya göre futbolun doğduğu ülke hangisidir?", "Çin", ["İngiltere", "Brezilya", "Çin", "Almanya"], 100),
        ('"BÜLBÜL" Destanı hangi ilimizin işgali üzerine yazılmıştır?', "Bursa", ["İzmir", "Adana", "Sakarya", "Bursa"],
         100),
        ("Bozkırın 'Tezenesi' olarak anılan halk ozanı kimdir?", "Neşet Ertaş",
         ["Aşık Veysel", "Musa Eroğlu", "Neşet Ertaş", "Aşık Mahsuni Şerif"], 100),
        ("Uzayda yetiştirilen ilk bitki nedir?", "Patates", ["Patates", "Havuç", "Dereotu", "Sinir Olduğum Kişi"], 100) # Soru-Cevap-Şıklar-Puan
        ]

def selectQue():
    global selectQuestion, selectedQuestion, selectedAnswer, selectedPoint, selectedOption1, selectedOption2, selectedOption3, selectedOption4
    if queCounter == 11:
        window.destroy()
        winScreen.winGame()
    elif len(_questions) == 0:
        window.destroy()
        messagebox.showerror("HATA", "Program bir hatayla karşılaştı. \n Tahmini Hata : Yetersiz soru sayısı.")
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

def writeQue():
    global selectedQuestion
    canvas.itemconfig(questionAreaText,text=f'{selectedQuestion}')
    canvas.itemconfig(A_button_text,text=f'{selectedOption1}')
    canvas.itemconfig(B_button_text,text=f'{selectedOption2}')
    canvas.itemconfig(C_button_text,text=f'{selectedOption3}')
    canvas.itemconfig(D_button_text,text=f'{selectedOption4}')

def checkAnswer():
    global trueAnswerPoint, wrongAnswerPoint, totalAnswerPoint, queCounter, comboCounter
    trueAnswer = str(selectedAnswer)

    if trueAnswer == userAnswer:

        trueAnswerPoint = trueAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint + selectedPoint
        queCounter = queCounter + 1
        comboCounter = comboCounter +1
        canvas.itemconfig(questionCounter, text=f"{queCounter}/10")
        if comboCounter >= 5:
            sounds.comboSound()
        else:
            sounds.correctAnswerSound()
        selectQue()
        writeQue()
    else:
        print("Yanlış Cevap")
        wrongAnswerPoint = wrongAnswerPoint + 1
        totalAnswerPoint = totalAnswerPoint - selectedPoint
        window.destroy()
        loseScreen.loseGameScreen()
        sounds.wrongAnswerSound()

def selectAnswerA():
    global userAnswer
    userAnswer = str(canvas.itemcget(A_button_text,'text'))

def selectAnswerB():
    global userAnswer
    userAnswer = str(canvas.itemcget(B_button_text,'text'))

def selectAnswerC():
    global userAnswer
    userAnswer = str(canvas.itemcget(C_button_text,'text'))

def selectAnswerD():
    global userAnswer
    userAnswer = str(canvas.itemcget(D_button_text,'text'))
     
def questionScreen(): # EKRAN FONKSİYONU ----------------------------
    global window, canvas, A_button_text, B_button_text, C_button_text,D_button_text, bg_image
    global questionAreaText, questionCounter, pointCounter,timeCount
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/questionScreen")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    resetPoints()
    resetQuestions()
    window = Tk()

    window.geometry("1920x1080")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    bg_image = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=bg_image
    )

    exitButton_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    exitButton = Button(
        image=exitButton_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy(),
        relief="flat"
    )
    exitButton.place(
        x=1800.0,
        y=50.0,
        width=73.0,
        height=53.0
    )

    mainmenuButton_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    mainmenuButton = Button(
        image=mainmenuButton_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), homePage.homepage()),
        relief="flat"
    )
    mainmenuButton.place(
        x=1736.0,
        y=50.0,
        width=50.0,
        height=54.0
    )

    D_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    D_button = Button(
        image=D_image,
        borderwidth=0,
        highlightthickness=5,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    D_button.place(
        x=1446.0,
        y=649.0,
        width=107.0,
        height=66.0
    )

    C_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    C_button = Button(
        image=C_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    C_button.place(
        x=367.0,
        y=650.0,
        width=107.0,
        height=66.0
    )

    B_image = PhotoImage(
        file=relative_to_assets("button_5.png"))
    B_button = Button(
        image=B_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    B_button.place(
        x=1446.0,
        y=539.0,
        width=107.0,
        height=66.0
    )

    A_image = PhotoImage(
        file=relative_to_assets("button_6.png"))
    A_button = Button(
        image=A_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    A_button.place(
        x=367.0,
        y=540.0,
        width=107.0,
        height=66.0
    )

    startButton_image = PhotoImage(
        file=relative_to_assets("startButton.png"))
    start_Button = Button(
        image=startButton_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (start_Button.destroy(),sounds.gameStartSound() ,selectQue(), writeQue(),resetPoints(), resetQuestions(),
                         A_button.config(command=lambda: [selectAnswerA(), checkAnswer()]),
                         B_button.config(command=lambda: [selectAnswerB(), checkAnswer()]),
                         C_button.config(command=lambda: [selectAnswerC(), checkAnswer()]),
                         D_button.config(command=lambda: [selectAnswerD(), checkAnswer()])),
        relief="flat"
    )
    start_Button.place(
        x=891.0,
        y=739.0,
        width=138.0,
        height=139.0
    )

    questionAreaText = canvas.create_text(
        469.0,
        370.0,
        anchor="nw",
        text="Başlamak için aşağıdaki butona basınız. ",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    A_button_text = canvas.create_text(
        618.0,
        558.0,
        anchor="nw",
        text="CEVAP 1",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    B_button_text = canvas.create_text(
        1163.0,
        558.0,
        anchor="nw",
        text="CEVAP 2",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    D_button_text = canvas.create_text(
        1163.0,
        668.0,
        anchor="nw",
        text="CEVAP 4",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    C_button_text = canvas.create_text(
        618.0,
        668.0,
        anchor="nw",
        text="CEVAP 4",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    questionCounter = canvas.create_text(
        432.0,
        877.0,
        anchor="nw",
        text=f"{queCounter}/10",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    pointCounter = canvas.create_text(
        1426.0,
        877.0,
        anchor="nw",
        text=f"{totalAnswerPoint}",
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    window.attributes("-fullscreen", True)
    window.mainloop()