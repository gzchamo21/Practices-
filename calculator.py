#CALCULADORA EN PYTHON //

#CLASE DE LA CALCULADORA PARA CODEAR SUS METODOS :)
class calculator:
    
    #Inicializamos la CLASE
    def __init__(self, initialValue= 0):
                 self.initialValue = initialValue

    #Introducimos sus METODOS
    def plus(self, b= 0):
        self.initialValue = input("> Value 1: ")
        b = input("> Value 2: ")
        if self.initialValue and b.isdigit():
            print("\nResult: ", int(self.initialValue) + int(b))
        else:
            print(f"\nThe characters that you introduce was invalid, Try again\n")

    def minus(self, b= 0):
        self.initialValue = input("> Value 1: ")
        b = input("Value 2:")
        if self.initialValue.isdigit() and b.isdigit():
            print("\nResult: ", int(self.initialValue) - int(b))
        else:
            print("\nYou not gave a valid number\n")

    def times(self, b= 1):
        self.initialValue = input("> Value 1: ")
        b =  input("> Value 2: ")
        if self.initialValue.isdigit() and b.isdigit():
            print("\nResult: ", int(self.initialValue) * int(b))
        else:
            print("\nIntroduce a valid character\n")

    def division(self, b= 1):
        self.initialValue = input("> Value 1: ")
        b = input("> Value 2: ")
        if self.initialValue.isdigit() and b.isdigit():
            try:
                print("\nResult: ", int(self.initialValue) / int(b))
            except ZeroDivisionError:
                print("\nYou can't divide by zero\n")
                return False
        else:
            print("\nYou need introduce a number\n")

       #Instanciamos la CLASE
default = calculator()

#Pasamos a diseñar la interfaz ;)
def menu():
    while True:
        options = ["Plus", "Minus", "Times", "Division", "Exit"]
        print("\n--WELCOME--")
        for index, element in enumerate(options):
            print(f"{index + 1}.- {element}")
        choose = input("> ")
        if choose.lower() == "plus":
            default.plus()
        elif choose.lower() == "minus":
            default.minus()
        elif choose.lower() == "times":
            default.times()
        elif choose.lower() == "division":
            default.division()
        elif choose.lower() == "exit":
            break
        else:
            print("\n¡¡Please choose an option!!\n")
menu()
