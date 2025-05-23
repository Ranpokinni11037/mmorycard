#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,  QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
#создание приложения и главного окна
app = QApplication([])
from random import *
#создание элементов интерфейса
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 400)

main_win.cur_question = -1
class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3  

main_win.score = 0
main_win.total = 0

tetxt = QLabel('Какой национальности не существует')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чульмцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_main = QVBoxLayout()
button = QPushButton('Ответить')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#расположение виджетов по лэйаутам
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_main.addWidget(tetxt,  alignment = Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)


RadioGroupBox2 = QGroupBox('Результат теста')
res = QLabel('Прав ты или нет')
resu1 = QLabel('Энцы')
layout_ans11 = QVBoxLayout()
layout_ans11.addWidget(res, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ans11.addWidget(resu1, alignment = Qt.AlignCenter, stretch = 2)
RadioGroupBox2.setLayout(layout_ans11)
layout_main.addWidget(RadioGroupBox2, alignment = Qt.AlignCenter) 
layout_main.addWidget(button, alignment = Qt.AlignCenter )       
main_win.setLayout(layout_main)
RadioGroupBox2.hide()

def show_result():
    #показать панель ответов
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    button.setText('Следующий вопрос')
     

def show_question():
    #показать панель вопросов
    RadioGroupBox.show()
    RadioGroupBox2.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

#button.clicked.connect(start_test)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    tetxt.setText(q.question)
    resu1.setText(q.right_answer)
    show_question()
    

def check_answer():
    if answers[0].isChecked():
        res.setText('Правильно')
        show_result()
        main_win.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        res.setText('Неправильно')
        show_result()
    main_win.total += 1
    stat = main_win.score/main_win.total * 100
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Статистика:', round(stat, 1))
    #button.clicked.connect(ask)
#создание виджетов главного окна
quesstions = []
q1 =Question('Какой национальности не существует?', 'Энцы', 'Чульмцы', 'Смурфы', 'Алеуты' )
q2 = Question('Государственный язык Португалии -', 'Португальский', 'Английский', 'Испанский', 'Французский')
q3 = Question('Какой элемент таблицы Менделеева имеет символ "O"?', 'Кислород', 'Золото', 'Углерод', 'Азот')
q4 = Question('В каком году состоялась первая высадка человека на Луну?', '1969', '1965', '1972', '1980')
q5 = Question('Какой из художников известен своими картинами в стиле импрессионизма?', 'Клод Моне', 'Пабло Пикассо', 'Винсент Ван Гог', 'Сальвадор Дали')

quesstions.append(q2)
quesstions.append(q3)
quesstions.append(q4)
quesstions.append(q5)
quesstions.append(q1)

def next_question():
    main_win.cur_question = randint(0, len(quesstions) - 1)
    qqq = quesstions[main_win.cur_question]
    ask(qqq)

#q = Question('Вопрос какой-то', 'ответик1', 'ответик2', 'ответик3', 'ответик4')
#ask(q)
button.clicked.connect(start_test)
#обработка нажатий на переключатели

app.exec_()