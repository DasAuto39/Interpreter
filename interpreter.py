import math_lib

placeholders = {}

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
        if line.startswith("jika"):
            i = handle_conditional(line, lines, i)
        elif line.startswith("selama"):
            i = handle_loop(line, lines, i)
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
        if len(parts) != 2:
            print("Format perintah tidak valid. Gunakan: konversi <angka> dari <basis> ke <basis>")
            return
        handle_conversion(parts[1])
    elif action == "baca":
        if len(parts) != 2:
            print("Format perintah tidak valid. Gunakan: baca <placeholder>")
            return
        handle_baca(parts[1])
    elif action == "berhenti":
        print("Interpreter berhenti.")
        exit()
    elif action in ["tambah", "kurang", "kali", "bagi", "pangkat", "akar"]:
        if len(parts) != 2:
            print(f"Format perintah tidak valid. Gunakan: {action} <angka1> <angka2>")
            return
        handle_math(action, parts[1])
    else:
        print("Perintah tidak dikenal.")

def handle_conditional(line, lines, i):
    parts = line.split(maxsplit=2)
    if len(parts) != 3 or parts[2] != "maka":
        print("Format perintah tidak valid. Gunakan: jika <kondisi> maka <perintah>")
        return i + 1

    condition = parts[1]
    if eval(condition, {}, placeholders):
        process_command(lines[i + 1].strip())
    return i + 2

def handle_loop(line, lines, i):
    parts = line.split(maxsplit=2)
    if len(parts) != 3 or parts[2] != "lakukan":
        print("Format perintah tidak valid. Gunakan: selama <kondisi> lakukan <perintah>")
        return i + 1

    condition = parts[1]
    loop_start = i + 1
    while eval(condition, {}, placeholders):
        process_command(lines[loop_start].strip())
    return loop_start + 1

def handle_conversion(command):
    parts = command.split()
    if len(parts) != 5:
        print("Format perintah tidak valid. Gunakan: konversi <angka> dari <basis> ke <basis>")
        return

    number, _, input_base, _, output_base = parts
    try:
        decimal_number = to_decimal(number, input_base)
        placeholders[number] = (decimal_number, input_base)
        if output_base.lower() == "desimal":
            print(f"Desimal: {decimal_number}")
        elif output_base.lower() == "biner":
            print(f"Biner: {to_binary(decimal_number)}")
        elif output_base.lower() == "oktal":
            print(f"Oktal: {to_octal(decimal_number)}")
        elif output_base.lower() == "heksadesimal":
            print(f"Heksadesimal: {to_hexadecimal(decimal_number)}")
        else:
            print("Basis output tidak dikenal.")
    except ValueError:
        print("Angka atau basis tidak valid.")

def handle_baca(expression):
    try:
        # Attempt to evaluate the expression as a Python expression
        value = eval(expression, {}, placeholders)
        print(value)
    except NameError:
        print(f"Placeholder '{expression}' tidak ditemukan.")
    except SyntaxError:
        print(f"Format placeholder '{expression}' tidak valid.")

def handle_math(action, command):
    parts = command.split()
    if len(parts) < 1 or (action != "akar" and len(parts) != 2):
        print(f"Format perintah tidak valid. Gunakan: {action} <angka1> <angka2>")
        return

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

def to_decimal(number, base):
    bases = {"biner": 2, "desimal": 10, "oktal": 8, "heksadesimal": 16}
    return int(number, bases[base.lower()])

def to_binary(number):
    return bin(number)[2:]  # Menghapus prefix '0b'

def to_octal(number):
    return oct(number)[2:]  # Menghapus prefix '0o'

def to_hexadecimal(number):
    return hex(number)[2:]  # Menghapus prefix '0x'

if __name__ == "__main__":
    main()
