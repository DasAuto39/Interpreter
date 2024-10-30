# math_lib.py

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def pangkat(a, b):
    return a ** b

def akar(a):
    return a ** 0.5

def decimal(number, base):
    bases = {"biner": 2, "desimal": 10, "oktal": 8, "heksadesimal": 16}
    return int(number, bases[base.lower()])
def binary(number):
    return bin(number)[2:] 
def octal(number):
    return oct(number)[2:]  
def hexadecimal(number):
    return hex(number)[2:]