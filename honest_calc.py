msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
correct_operators_list = ["+", "-", "*", "/"]
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
end_calculations = False
memory = 0
result = 0
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list = ["", msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_one_digit(a):
    if -10 < a < 10 and a.is_integer():
        return True
    else:
        return False


def check(a, b, c):
    msg = ""
    if is_one_digit(a) and is_one_digit(b):
        msg = msg + msg_6
    if (a == 1 or b == 1) and c == "*":
        msg = msg + msg_7
    if (a == 0 or b == 0) and (c == "*" or c == "+" or c == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


while not end_calculations:
    is_zero = False
    try:
        x, oper, y = input("Enter an equation ").split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        check(x, y, oper)
        if oper not in correct_operators_list:
            print(msg_2)
            continue
        elif oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif y == 0:
            is_zero = True
            print(msg_3)
            continue
        elif oper == "/" and not is_zero:
            result = x / y
        print(result)
        while True:
            answer1 = input(msg_4)
            if answer1 == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index <= 12:
                        answer3 = input(msg_list[msg_index])
                        if answer3 == "y":
                            msg_index += 1
                        elif answer3 == "n":
                            break
                    if msg_index > 12:
                        memory = result
                        break
                    else:
                        break
                else:
                    memory = result
                    break
            elif answer1 == "n":
                break
        while True:
            answer2 = input(msg_5)
            if answer2 == "y":
                break
            elif answer2 == "n":
                end_calculations = True
                break




