alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

type = (input("encode or decode? \n")).lower()
massage = (input("Input the massage : \n")).lower()
shift = int(input("Shift : "))

def coder(type ,massage, shift):
    if type == 'encode':
        blank = []
        for i in range(len(massage)):
            number_of_index = 0
            if massage[i] == " ":
                blank.append(" ")
            else:
                number_of_index = int(alphabet.index(massage[i])) + shift
                if number_of_index > 26:
                    number_of_index -= 26
                blank.append(alphabet[number_of_index])
        print("".join(blank))
    if type == 'decode':
        blank = []
        for i in range(len(massage)):
            number_of_index = 0
            if massage[i] == " ":
                blank.append(" ")
            else:
                number_of_index = int(alphabet.index(massage[i])) - shift
                if number_of_index < 0:
                    number_of_index += 26
                blank.append(alphabet[number_of_index])
        print("".join(blank))


coder(type, massage, shift)
