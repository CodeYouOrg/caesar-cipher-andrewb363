alphabet = 'abcdefghijklmnopqrstuvwxyz'
sentence = input('Please enter a sentence: ').lower()
shift = int(input('Please enter your shift amount: '))
new_word = []

for x in sentence:
    if x in alphabet:
        letter_location = int(alphabet.find(x))
        index = (letter_location + shift) % 26
        letter_location = alphabet[index]
        new_word.append(letter_location)
    else:
        new_word.append(x)
print("The encrypted sentence is: " + ''.join(new_word))
