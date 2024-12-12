def f(equation):
    e_list = equation.split(" ")
    operators = ["+", "-", "*", "/", "^"]
    op_times = 0
    for i in e_list:
        for operator in operators:
            if i == operator:
                op_times += 1
    for j in range(op_times):
        for i in range(len(e_list)):
            do_break = False
            for operator in operators:
                if e_list[i] == operator:
                    if e_list[i] == "^":
                        e_list[i] = "**"
                    res = eval(f"{e_list[i-2]}{e_list[i]}{e_list[i-1]}")
                    e_list.pop(i)
                    e_list.pop(i-1)
                    e_list[i-2] = res
                    do_break = True
                    break
            if do_break:
                break
    return e_list[0]
                
if __name__ == "__main__":
    print(f("7 4 + 1 / 8 9 - 2 * + 6 /"))   
    print(f("4 3 + 9 -"))
    print(f("8 5 * 3 6 2 ^ - 9 + 1 / -"))
    