# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget, QApplication, QHBoxLayout, QListWidget, QLineEdit, QTextEdit
import json
# Cоздание окна и приложения
app = QApplication([])
window = QWidget()

 czech_republic_text = '''
Че́хия (чеш. Česko, МФА (чешск.): [ˈʧɛskɔ]), официальное название[7] — Че́шская Респу́блика (аббревиатура — ЧР);
чеш. Česká republika (аббревиатура — ČR), МФА (чешск.): [ˈʧɛskaː ˈrɛpuˌblɪka]) — государство в Центральной Европе.
Граничит с Польшей на севере (длина границы — 796 км), Германией — на северо-западе и западе (810 км),
Австрией — на юге (466 км) и Словакией — на востоке (252 км)[8]. Общая протяжённость границы — 2324 км. 
Площадь — 78 866 км².Современная Чехия образовалась в результате распада Чехословакии (Бархатный развод)
1 января 1993 года. Страна включает исторические области — Богемию (собственно Чехия), Моравию и часть Силезии.
 Унитарное государство. Относится к развитым странам. Столица Прага — туристическая достопримечательность и крупнейший город страны.
 С 12 марта 1999 года Чехия — член НАТО, с 1 мая 2004 года — член Европейского союза.
 '''
 mexico_text = '''
 Ме́ксика (исп. México [ˈmexiko]), официально — Мексика́нские Соединённые Шта́ты[7] (исп. Estados Unidos Mexicanos [esˈtaðos uˈniðoz mexiˈkanos]) — государство в Северной Америке,
 на севере граничит с Соединёнными Штатами Америки, на юго-востоке — с Белизом и Гватемалой,
 на западе омывается водами Калифорнийского залива и Тихого океана, на востоке — водами Атлантического океана,
 Мексиканского залива и Карибского моря[8]. Крупнейшая в мире по населению испаноязычная страна.
 '''
 finland_text = '''
 Финля́ндия-  государство в Северной Европе на восточном побережье Балтийского моря.
 На востоке граничит с Россией, на севере с Норвегией и на западе со Швецией.
 На юге ближайшим соседом является Эстония к югу от Финского залива.
 Столица и крупнейший город Финляндии — Хельсинки.
 Финляндия, по состоянию на 1 мая 2022 года, — относительно малонаселенная страна с населением в 5 549 184 человека,
 сосредоточенными в основном в южных и центральных частях страны.Конституция Финляндии определяет финский и шведский языки как национальные языки.
 В конце 2021 года говорящие на финском языке составляли 86,5 % населения (4 800 243 чел.), говорящие на шведском языке — 5,2 % населения (287 933 чел.),
 а говорящие на саамских языках — 0,04 % населения (2 023 чел.)[8]. Говорящие на других языках составляли 8,3 % (458 042 чел.) населения
 '''
 kazakhstan_text = '''
 Казахста́н (каз. Қазақстан, Qazaqstan, официальное название — Респу́блика Казахста́н (каз. Қазақстан Республикасы; Qazaqstan Respublikasy [qɑzɑqˈstɑn respublikɑ'sɯ]),
 (аббревиатура РК) — государство в центре Евразии, бо́льшая часть которого относится к Азии, меньшая — к Европе. Площадь территории — 2 724 902 км².
 Население, по оценке государственного комитета по статистике на 1 января 2022 года,
 составляет 19 082 467 человек[4]. Плотность населения является одной из самых низких в мире:
 менее 7 человек на квадратный километр. Столица — Нур-Султан. Крупнейший город с населением свыше 2 млн человек — Алма-Ата.
 Занимает 9-е место в мире по территории, 2-е место среди стран постсоветского пространства (после России), 42-е — по объёму
 ВВП по ППС и 64-е — по численности населения.
 '''
 japan_text = '''
 Япония — государство в Восточной Азии, раскинувшееся на архипелаге, состоящем из 6852 островов, в западной части Тихого океана.
 Четыре крупнейших острова — Хонсю, Хоккайдо, Кюсю и Сикоку — составляют 97% общей площади архипелага.
 Государственно-политическое устройство — конституционная монархия.
 '''

text_edit_countries = QTextEdit()
line_head = QHBoxLayout()
line_countries = QVBoxLayout()
line_label = QVBoxLayout()

 list_dict = {
     'Чехия': czech_republic_text,
     'Финляндия': finland_text,
     'Япония': japan_text,
     'Казахстан': kazakhstan_text,
     'Мексика': mexico_text 
 }


 with open('countries.json', 'w', encoding='utf-8') as file:
     json.dump(list_dict, file)

country_add = QLineEdit()
button_add_country = QPushButton("Добавить страну")
button_clear = QPushButton('Очистить')
button_del = QPushButton('Удалить страну')
button_edit = QPushButton('Изменить данные')
country_add.setPlaceholderText('Введите страну для добавления')
line_buttons = QHBoxLayout()



widget_countries = QListWidget()
with open('countries.json', 'r', encoding='utf-8') as file:
    dict_countries = json.load(file)
    widget_countries.addItems(dict_countries.keys())

line_countries.addWidget(widget_countries)
line_label.addWidget(text_edit_countries, stretch = 2)
line_label.addWidget(country_add, stretch=1)
line_buttons.addWidget(button_add_country, alignment=Qt.AlignCenter, stretch=1)
line_buttons.addWidget(button_del, alignment=Qt.AlignCenter, stretch=1)
line_buttons.addWidget(button_edit, alignment=Qt.AlignCenter, stretch=1)
line_buttons.addWidget(button_clear, alignment=Qt.AlignCenter, stretch=1)
line_label.addLayout(line_buttons, stretch=1)
line_head.addLayout(line_countries, stretch=2)
line_head.addLayout(line_label, stretch=3)
window.setLayout(line_head)

def info_country():
    country = widget_countries.currentItem().text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
        text_edit_countries.setText(dict_countries[country])

def add_country():
    dict_countries = ''
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
    with open('countries.json', 'w', encoding='utf-8') as file:
        country = country_add.text()
        dict_countries[country] = text_edit_countries.toPlainText()
        json.dump(dict_countries, file)
        widget_countries.clear()
        widget_countries.addItems(dict_countries.keys())

def clear_widgets():
    country_add.clear()
    text_edit_countries.clear()

def delete_country():
    country = widget_countries.currentItem().text()
    dict_countries = ''
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
    del dict_countries[country]
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(dict_countries, file)
        clear_widgets()
        widget_countries.clear()
        widget_countries.addItems(dict_countries.keys())

def edit_country():
    country = widget_countries.currentItem().text()
    description = text_edit_countries.toPlainText()
    dict_countries = ''
    with open('countries.json', 'r', encoding='utf-8') as file:
        dict_countries = json.load(file)
    with open('countries.json', 'w', encoding='utf-8') as file:
        dict_countries[country] = description
        json.dump(dict_countries, file)
        clear_widgets()
        widget_countries.clear()
        widget_countries.addItems(dict_countries.keys())
    

button_add_country.clicked.connect(add_country)
button_del.clicked.connect(delete_country)
button_clear.clicked.connect(clear_widgets)
button_edit.clicked.connect(edit_country)
widget_countries.itemClicked.connect(info_country)

window.show()
app.exec()
