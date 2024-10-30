import math_lib

def main():
    try:
        with open("program.oll", "r") as file:
            lines = file.readlines()
            process_lines(lines)
    except FileNotFoundError:
        print("File 'program.oll' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script ini.")

def process_lines(lines):
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            i += 1
            continue
        else:
            process_command(line)
            i += 1

def process_command(command):
    parts = command.split(maxsplit=1)
    if len(parts) < 1:
        print("Format perintah tidak valid.")
        return

    action = parts[0].lower()
    if action == "konversi":
        handle_conversion(parts[1])
    elif action == "baca":
        handle_print(parts[1])
    elif action == "berhenti":
        print("Interpreter berhenti.")
        exit()
    elif action in ["tambah", "kurang", "kali", "bagi", "pangkat", "akar"]:
        handle_math(action, parts[1])
    else:
        print("Perintah tidak dikenal.")

def handle_conversion(command):
    parts = command.split()
    number, _, input_base, _, output_base = parts
    try:
        decimal_number = math_lib.decimal(number, input_base)
        if output_base.lower() == "desimal":
            print(f"Desimal: {decimal_number}")
        elif output_base.lower() == "biner":
            print(f"Biner: {math_lib.binary(decimal_number)}")
        elif output_base.lower() == "oktal":
            print(f"Oktal: {math_lib.octal(decimal_number)}")
        elif output_base.lower() == "heksadesimal":
            print(f"Heksadesimal: {math_lib.hexadecimal(decimal_number)}")
        else:
            print("Basis output tidak dikenal.")
    except ValueError:
        print("Angka atau basis tidak valid.")

def handle_print(expression):
    print(expression)

def handle_math(action, command):
    parts = command.split()
    try:
        if action == "akar":
            a = float(parts[0])
            result = math_lib.akar(a)
        else:
            a = float(parts[0])
            b = float(parts[1])
            if action == "tambah":
                result = math_lib.tambah(a, b)
            elif action == "kurang":
                result = math_lib.kurang(a, b)
            elif action == "kali":
                result = math_lib.kali(a, b)
            elif action == "bagi":
                result = math_lib.bagi(a, b)
            elif action == "pangkat":
                result = math_lib.pangkat(a, b)
        print(result)
    except ValueError:
        print("Angka tidak valid.")

if __name__ == "__main__":
    main()
