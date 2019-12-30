class Shark:
    @staticmethod
    def swim():
        print("The shark is swimming.")

    @staticmethod
    def be_awesome():
        print("The shark is being awesome.")

def main():
    Jones = Shark()
    Jones.swim()
    Jones.be_awesome()

if __name__ == "__main__":
    main()