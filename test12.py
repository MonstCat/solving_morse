morze = ['.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
         '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '--.-', '-.--', '-..-', '..-..', '..--', '.-.-']
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
data = ['эют', 'ний', 'дей', 'дио', 'ухо', 'лей', 'евт', 'лют', 'иют', 'атт', 'рий', 'еум', 'еий', 'бам', 'сам', 'еют', 'рсо', 'ией', 'иум', 'лум', 'есо', 'фий', 'еей', 'эей']
phrase = '--....-.--...---.-..--..-....---'
for i in data:
    x = sum([len(morze[alphabet.index(o)]) for o in i])
    for q in range(1, 5):
        print(alphabet[morze.index(phrase[-x - q:-x])], i)