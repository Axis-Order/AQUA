STATUS = 0

class Stack:
    def __init__(self):
        self.stk = []

    def push(self, data):
        self.stk.append(data)

    def pop(self):
        return self.stk.pop()

    def getLen(self):
        return len(self.stk)

    def isEmpty(self):
        if len(self.stk) == 0:
            return True
        else:
            return False


def isNumeric(num):
    num += "\n"
    pos = 0
    stat = 0
    isnum = False
    while True:
        ch = num[pos]
        if stat == 0:
            if ch == "+":
                pos += 1
                continue
            elif ch == "-":
                pos += 1
                continue
            elif "0" <= ch <= "9":
                pos += 1
                stat = 1
                continue
            elif ch == "\n":
                return False
            else:
                return False
        if stat == 1:
            if "0" <= ch <= "9":
                pos += 1
                continue
            elif ch == ".":
                stat = 2
                pos += 1
                continue
            elif ch == "\n":
                stat = 2
                continue
            else:
                return False
        if stat == 2:
            if "0" <= ch <= "9":
                pos += 1
            else:
                isnum = False
        if stat == 1 and ch == '\n':
            isnum = True
            break
        if stat == 2 and ch == "\n":
            isnum = True
            break
    return isnum

    pass


def repl():
    global STATUS
    op = None
    num = 0
    stack = Stack()
    PAR = 0
    while True:
        print(stack.stk)
        print(str(STATUS) + " is now!")
        com = input()
        if com == "quit":
            return
        elif com == "=":
            while not stack.isEmpty():
                if stack.getLen() == 1:
                    p = stack.pop()
                    print(p)
                    stack.push(p)
                    break
                else:
                    b = stack.pop()
                    op = stack.pop()
                    a = stack.pop()
                    if op == "+":
                        p = a + b
                    elif op == "-":
                        p = a - b
                    print(p)
                    stack.push(p)
            continue
        if STATUS == 0:
            if com == "(":
                stack.push(com)
                STATUS = 0
                PAR += 1
                continue
            if isNumeric(com):
                stack.push(float(com))
                STATUS = 1
                continue
        elif STATUS == 1:
            if com == ")":
                if PAR == 0:
                    print("LPAR is few")
                    continue
                PAR -= 1
                b = stack.pop()
                op = stack.pop()
                # if op in "+-":
                #     if op == "+":
                #         p = stack.pop() + b
                #         tmp = stack.pop()
                #         stack.push(p)
                #         print("P is added:" + str(p))
                #     else:
                #         p = stack.pop() - b
                #         stack.pop()
                #         stack.push(p)
                #     op = stack.pop()
                #     #if op != "(":
                #      #   stack.push(op)
                # else: # op is LPAR
                #     pass
                if stack.getLen() == 0:
                    stack.push(b)
                    STATUS = 1
                    continue
                if op in "*/-+":
                    print(a)
                    a = stack.pop()
                    if op == "+":
                        p = a + b
                    if op == "-":
                        p = a - b
                    if op == "*":
                        p = a * b
                    if op == "/":
                        p = a / b
                    STATUS = 1
                    stack.pop()#LPAR skip
                    stack.push(p)
                    continue
            elif com not in "+-*/":
                print(com)
                print("not operator")
                continue
            elif com == "*":
                STATUS = 2
                stack.push(com)
                continue
            elif com == "/":
                STATUS = 2
                stack.push(com)
                continue
            # elif com == "+" or com == "-":
            #     STATUS = 2
            #     stack.push(com)
            #     continue
            else:
                if stack.getLen() >= 3:
                    rop = stack.pop()
                    op1 = stack.pop()
                    if op1 in "+-":
                        lop = stack.pop()
                        if op1 == "+":
                            p = lop + rop
                        else:
                            p = lop - rop
                        #stack.push(lop)
                        stack.push(p)

                    else:
                        stack.push(op1)
                        stack.push(rop)
                        #stack.push(com)

            if com != ")":
                stack.push(com)
                print("change two")
                STATUS = 2
            else:
                STATUS = 1
            continue
        if STATUS == 2:
            if com == "(":
                PAR += 1
                stack.push(com)
                STATUS = 0
                continue
            if isNumeric(com):
                b = float(com)
                op = stack.pop()
                a = stack.pop()
                if op in "*/":
                    if op == "*":
                        p = a * b
                    elif op == "/":
                        p = a / b
                    stack.push(p)
                else:
                    stack.push(a)
                    stack.push(op)
                    stack.push(b)
                STATUS = 1
                continue
            elif com in "+-":
                print("syntax error")
                if op in "+-":
                    if op == "+":
                        p = a + b
                    elif op == "-":
                        p = a - b
                    stack.push(p)
                STATUS = 2
                continue


if __name__ == "__main__":
    repl()