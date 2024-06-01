from art import logo
print(logo)
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def coder(type ,massage, shift):
    if type == 'encode':
        blank = []
        for i in range(len(massage)):
            number_of_index = 0
            if massage[i] == " ":
                blank.append(" ")
            elif massage[i] not in alphabet:
                blank.append(massage[i])
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
            elif massage[i] not in alphabet:
                blank.append(massage[i])
            else:
                number_of_index = int(alphabet.index(massage[i])) - shift
                if number_of_index < 0:
                    number_of_index += 26
                blank.append(alphabet[number_of_index])
        print("".join(blank))


stop = False
while stop == False:
    type = (input("encode or decode? \n")).lower()
    massage = (input("Input the massage : \n")).lower()
    shift = int(input("Shift : "))
    if shift > 25:
        shift = shift % 26
    coder(type, massage, shift)
    decision = (input("Do you want to start again? Y/N ")).lower()
    if decision == 'n':
        stop = True

    

