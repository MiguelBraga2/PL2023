import sys

count = 0 # Keeps the sum
flag = True
buffer = ""
number = ""

for line in sys.stdin:
    for c in line:
        b_cap = buffer.upper()
        c_cap = c.upper()
        if (b_cap == "" and c_cap == 'O') or \
           ((b_cap == "O") and (c_cap == 'F' or c_cap == 'N')) or \
           (b_cap == "OF" and c_cap == 'F'):
            buffer += c
            # Se leu as strings Off ou On
            if buffer.upper() == "OFF":
                flag = False
                buffer = ""
            if buffer.upper() == "ON":
                flag = True
                buffer = ""
            continue
        if flag == True:
            if c in ['0','1','2','3','4','5','6','7','8','9']:
                # Se leu algum número
                number += c
            # If after c == '=' doesn't work
            if number != "" and c not in ['0','1','2','3','4','5','6','7','8','9']:
                count += int(number)
                number = ""
        if c == '=':
            print(count)