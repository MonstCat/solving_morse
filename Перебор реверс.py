morze = ['.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '----', '--.-', '.--.-.', '-.--', '-..-', '..-..', '..--', '.-.-']
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
all_variants = []
phrase = '---....-..--..-.---...--.-....--'
start = ['м', 'о', 'ч']
for i in start:
    phrase = '---....-..--..-.---...--.-....--'
    summ = 0
    previous_alphabet = list(i)
    for q in previous_alphabet:
        q = morze[alphabet.index(q)]
        summ += len(q)
    phrase = phrase[summ:]
    for q in morze:
        if phrase.startswith(q):
            all_variants.append(i + alphabet[morze.index(q)])
print(all_variants)