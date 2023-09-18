#Area of a triangle

def areaOftri(l,h):
    l1 = int(l)
    h1 = int(h)

    val = 0.5 * (l1*h1)
    print(val)

areaOftri(3,2)

#Power calculator

def powerCalc(vol, cur):
    print(vol * cur)

powerCalc(230,10)

#Sum of numbers

def sumOfNum(a,b):
    print(a+b)

sumOfNum(3,2)

#Age to days

def ageToDays(age):
    leap = age // 4
    if age > 0:
        print((age * 365) - leap)

ageToDays(65)

#Morse code
morseVal = [['.-','-.--'],['.-','-.--'],['.-','-.--']]
def morseCode(morseVal):
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ")": '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    d_swap = {v: k for k, v in char_to_dots.items()}
    for x in morseVal:
        print(x)

morseCode(morseVal)

#Profit calc

def profitCalc(cost, sell, inv):
    costTotal = cost * inv
    sellTotal = sell * inv
    profit = sellTotal - costTotal
    print(profit)

profitCalc(32.67,45.00,1200)