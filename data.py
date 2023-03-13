a=[ ["The HTML5 standard was published in 2014.",'True'],
    ["The first computer bug was formed by faulty wires.",'False'],
    ["FLAC stands for 'Free Lossless Audio Condenser'.",'False'],
    ["All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",'False'],
    ["Linus Torvalds created Linux and Git.",'True'],
    ["The programming language 'Python' is based off a modified version of 'JavaScript'",'False'],
    ["AMD created the first consumer 64-bit processor.",'True'],
    ["'HTML' stands for Hypertext Markup Language.",'True'],
    ["In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",'True'],
    ["The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",'False'] ]
class Qst:
    def __init__(self):
        self.c=-1
        self.e=0
    def ask(self):
        self.d=input(f"\nQ{self.c+1}. {a[self.c][0]} [True/False] ?:").title()
    def Check(self):
        if self.d==a[self.c][1]:
            self.d='right'
            self.e+=1
        else:
            self.d='wrong'
    def rslt(self):
        print(f"\n{self.d} answer\nThe right answer was {a[self.c][1]}\nYour current score is: {self.e}/{self.c+1}")
    def next(self):
        if self.c+1 <len(a):
            self.c+=1
            return True
        print(f"\nYou've completed the quiz.\nYour final score was: {self.e}/10")
        return False