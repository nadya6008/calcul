from django import forms

class CalculatorForm(forms.Form):
    CALC_CHOICES = [
        (1, 'Арифметические операции'),
        (2, 'Возведение в степень, квадрат, квадратный корень, факториал'),
        (3, 'Тригонометрические функции'),
        (4, 'Перевод в системы счисления'),
    ]

    OPERATION_CHOICES = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
        ('%', '%'),
        ('div', 'div'),
        ('mod', 'mod'),
        ('^', '^'),
        ('sqr', 'sqr'),
        ('sqrt', 'sqrt'),
        ('!', '!'),
        ('sin', 'sin'),
        ('cos', 'cos'),
        ('tg', 'tg'),
        ('2', '2'),
        ('8', '8'),
        ('16', '16'),
    ]

    calc_type = forms.ChoiceField(choices=CALC_CHOICES, label="Выберите калькулятор")
    operation = forms.ChoiceField(choices=OPERATION_CHOICES, label="Выберите операцию")
    a = forms.FloatField(label="Введите значение a")
    b = forms.FloatField(label="Введите значение b (если требуется)", required=False)
