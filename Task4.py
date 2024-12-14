import string

# Алфавит
class Alphabet:

    def __init__(self, lang, letters_str):
        self.lang = lang
        self.letters = list(letters_str)

    # Друкуемо вси букви алфавиту
    def print(self):
        print(self.letters)

    # Повертаемо килькисть букв в алфавити
    def letters_num(self):
        len(self.letters)
    
# Алнглийский алфавит
class EnAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Перевиряемо, чи належить буква до англ алфавиту
    def is_en_letter(self,letter):
        if letter.upper() in self.letters:
            return True
        return False
    
    #Повертаемо килькисть букв в алфавити
    def letters_num(self):
        return EnAlphabet.__letters_num
    
    # Друкуемо приклад тексту англ мовою
    @staticmethod
    def example():
        print("English Examole:\nDon't judge a book by it's cover.")

# Тести
if __name__ == '__main__':
    eng_alphabet = EnAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EnAlphabet.example()