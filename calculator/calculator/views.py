from django.shortcuts import render
from .forms import CalculatorForm
import math

def calculate(calc_type, operation, a, b):
    if calc_type == '1':
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b
        elif operation == '%':
            return (b / 100) * a
        elif operation == 'div':
            return a // b
        elif operation == 'mod':
            return a % b
    
    elif calc_type == '2':
        if operation == '^':
            return a ** b
        elif operation == 'sqr':
            return a ** 2
        elif operation == 'sqrt':
            return math.sqrt(a)
        elif operation == '!':
            return math.factorial(int(a))
    
    elif calc_type == '3':
        if operation == 'sin':
            return math.sin(math.radians(a))
        elif operation == 'cos':
            return math.cos(math.radians(a))
        elif operation == 'tg':
            return math.tan(math.radians(a))
    
    elif calc_type == '4':
        if operation == '2':
            return bin(int(a))[2:]
        elif operation == '8':
            return oct(int(a))[2:]
        elif operation == '16':
            return hex(int(a))[2:]

    return None

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            calc_type = form.cleaned_data['calc_type']
            operation = form.cleaned_data['operation']
            a = form.cleaned_data['a']
            b = form.cleaned_data['b'] or 0

            result = calculate(calc_type, operation, a, b)
    else:
        form = CalculatorForm()

    return render(request, 'calculator/calculator.html', {'form': form, 'result': result})
