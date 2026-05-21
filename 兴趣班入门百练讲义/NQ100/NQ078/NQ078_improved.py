import sys

class ExpressionEvaluator:
    def __init__(self, expr):
        self.expr = expr
        self.pos = 0
    
    def peek(self):
        if self.pos < len(self.expr):
            return self.expr[self.pos]
        return None
    
    def get(self):
        if self.pos < len(self.expr):
            self.pos += 1
            return self.expr[self.pos - 1]
        return None
    
    def factor_value(self):
        result = 0
        c = self.peek()
        if c == '(':
            self.get()  # 读入左括号
            result = self.expression_value()
            self.get()  # 读入右括号
        else:
            while c and c.isdigit():
                result = 10 * result + int(c)
                self.get()
                c = self.peek()
        return result
    
    def term_value(self):
        result = self.factor_value()
        while True:
            op = self.peek()
            if op == '*' or op == '/':
                self.get()
                value = self.factor_value()
                if op == '*':
                    result *= value
                else:
                    result //= value
            else:
                break
        return result
    
    def expression_value(self):
        result = self.term_value()
        more = True
        while more:
            op = self.peek()
            if op == '+' or op == '-':
                self.get()
                value = self.term_value()
                if op == '+':
                    result += value
                else:
                    result -= value
            else:
                more = False
        return result

def main():
    expr = input().strip()
    evaluator = ExpressionEvaluator(expr)
    print(evaluator.expression_value())

if __name__ == "__main__":
    main()
