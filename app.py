#   Email validation
#   Importing responsories
import validators as v

def main():
    print(Validation(input("What is your e-mail addres?:")))

def Validation(arg):
    return 'Valid' if v.email(arg) else 'Invalid'

if __name__== '__main__':
    main()