import webbrowser
from tkinter import *
import translator
import random
import getData


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


class Main:
    def __init__(self, master, modes):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.languages = [["English", "en"], ["Spanish", "es"], ["Japanese", "ja"], ["Italian", "it"],
                          ["French", "fr"], ["Latin", "la"], ["Greek", "el"], ["Russian", "ru"], ["Hindi", "hi"],
                          ["Chinese", "zh-cn"], ["Arabic", "ar"], ["Bengali", "bn"], ["Portuguese", "pt"],
                          ["Indonesian", "id"]]
        self.language_index = 0
        self.language = self.languages[self.language_index]

        self.highScore = open("highscores.txt", "r+").read()
        self.highScoresL = Label(self.frame, text="High Score: " + str(self.highScore))
        self.highScoresL.grid(row=5, column=2)

        self.modes = modes
        self.mode_index = 0
        self.mode = data[self.mode_index]
        self.answer = translator.translate(self.mode[self.mode_index], self.language[1])

        self.instructionB = Button(self.frame, text="Instructions", command=self.open_instructions)
        self.instructionB.grid(row=0, column=0)

        self.languageB = Button(self.frame, text="English", command=self.toggle_language)
        self.languageB.grid(row=0, column=1)

        self.modeB = Button(self.frame, text="Mode", command=self.toggle_mode)
        self.modeB.grid(row=0, column=2)

        self.curPrompt = 0
        self.nextWord = Button(self.frame, text="Next", command=self.next_prompt)
        self.nextWord.grid(row=4, column=1)
        self.prompt = Label(self.frame, text="Word: " + self.mode[self.curPrompt])
        self.prompt.grid(row=1, column=1, pady=(50, 0))

        self.input = Entry(self.frame)
        self.input.grid(row=2, column=1, padx=15)

        self.submit = Button(self.frame, text="Submit", command=self.check_answer)
        self.submit.grid(row=3, column=1)
        self.correct = False

        self.showAnswer = Label(self.frame, text="_" * len(self.answer))
        self.showAnswer.grid(row=2, column=2)
        self.showAnswerB = Button(self.frame, text="Show Answer", command=self.show_answer)
        self.showAnswerB.grid(row=3, column=2)

        self.score = 0
        self.scoreL = Label(self.frame, text="Score: " + str(self.score))
        self.scoreL.grid(row=5, column=0)

        self.newTopic = Entry(self.frame)
        self.newTopic.grid(row=5, column=1, padx=20)
        self.newTopicB = Button(self.frame, text="Change Topic", command=self.change_topic)
        self.newTopicB.grid(row=6, column=1)

        self.colors = ['white', 'red', 'green', 'blue', 'purple', 'orange', 'pink', 'yellow', 'grey', 'brown']
        self.color = 0
        self.colorB = Button(self.frame, text="Color", command=self.change_color)
        self.colorB.grid(row=2, column=0)
        self.frame.configure(bg=self.colors[self.color])

    def toggle_language(self):
        self.language_index += 1
        if self.language_index == len(self.languages):
            self.language_index = 0

        self.language = self.languages[self.language_index]
        self.languageB['text'] = self.language[0]

        if self.mode_index == 0:
            self.answer = translator.translate(self.answer, self.language[1])
        else:
            self.choose_random()
        self.showAnswer['text'] = "_" * len(self.answer)

    def toggle_mode(self):
        self.correct = False
        self.curPrompt = 0
        if self.mode_index == 0:
            self.mode_index = 1
            self.mode = self.modes[1]
            self.choose_random()
        else:
            self.mode_index = 0
            self.mode = self.modes[0]
            self.prompt['text'] = "Word: " + self.mode[self.curPrompt]
            self.answer = translator.translate(self.mode[self.curPrompt], self.language[1])

        self.showAnswer['text'] = "_" * len(self.answer)

    def check_answer(self):
        if self.correct:
            return
        if self.input.get() == self.answer:
            self.submit.configure(fg="green")
            self.score += 10
            self.correct = True
            if self.score > int(self.highScore):
                self.highScoresL['text'] = "High Score: " + str(self.score)
                hs = open("highscores.txt", "w+")
                hs.write(str(self.score))
        else:
            self.submit.configure(fg="red")
            if self.score >= 5:
                self.score -= 5
        self.scoreL['text'] = "Score: " + str(self.score)

    def show_answer(self):
        self.correct = True
        self.showAnswer['text'] = self.answer

    def next_prompt(self):
        self.curPrompt += 1
        self.correct = False
        if self.curPrompt == len(self.mode):
            self.curPrompt = 0
        if self.mode_index == 0:
            self.prompt['text'] = "Word: " + self.mode[self.curPrompt]
            self.answer = translator.translate(self.mode[self.curPrompt], self.language[1])
        else:
            self.choose_random()
        self.showAnswer['text'] = "_" * len(self.answer)

    def choose_random(self):
        words = []
        sentence = translator.translate(self.mode[self.curPrompt], self.language[1])
        start = end = 0
        for i in range(len(sentence)):
            if sentence[i].isalpha():
                end += 1
            elif start != end:
                words.append([sentence[start:end], (start, end + 1)])
                start = end = i + 1
            else:
                start = end = i + 1

        rand = random.randint(0, len(words) - 1)
        word = words[rand][0]
        self.answer = translator.translate(word, self.language[1])
        start, end = words[rand][1]
        self.prompt['text'] = sentence[:start] + "_" * len(self.answer) + sentence[end - 1:]

    def change_topic(self):
        topic = self.newTopic.get()
        self.modes = getData.get_data(topic)
        self.curPrompt = 0
        self.next_prompt()
        
    def change_color(self):
        self.color += 1
        if self.color == len(self.colors):
            self.color = 0
        self.frame.configure(bg=self.colors[self.color])

    def open_instructions(self):
        new_window = Toplevel(self.master)
        new_window.title("Instructions")
        Label(new_window, text="To toggle the mode, select the mode button. \n\n"
                               "To play mode 1, type in your guess for the displayed word into the \n"
                               "language you currently have selected and press submit. \n\n"
                               "To play mode 2, type in your guess for the word that fills \n"
                               "in the blank for the sentence into the selected language. \n\n"
                               "To change to a different language to practice with, toggle the\n"
                               "language button.\n\n"
                               "To change the color, toggle the color button.\n\n"
                               "To go to the next word/prompt, press the next button. \n\n To view the answer, press "
                               "the show answer button.\n\n"
                               "Your high score is tracked and saved each time you load the program.\n\n"
                               "Many languages require the use of diacritical marks for certain letters\n"
                               "Please follow the link below to learn how to write them on your OS.\n\n"
                               "To change the topic, type in the title of a valid Wikipedia article \n"
                               "in the bottom input and select change topic. If there are spaces in the\n"
                               "head of the article, use underscores. i.e. Amazon_Prime\n\n"
                               "Advanced Users: If you would like to get access to the data yourself\n"
                               "open the getData.py file to manipulate the data to select what you want.").pack()
        link = Label(new_window, text=r"https://rom.uga.edu/inserting-diacritical-marks", fg="blue", cursor="hand")
        link.pack()
        link.bind("<Button-1>", callback)


if __name__ == "__main__":
    data = getData.get_data('Oregon_State_University')
    root = Tk()
    root.title("Language Game")
    game = Main(root, data)
    root.mainloop()
