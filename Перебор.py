# буквы 'ъ', 'ш' вырезаны, т. к. точно не присутствуют в расшифровке;
# буквы 'ы', 'я' вырезаны, т. к. не подходят; буквы 'ё' в морзянке нет
morze = ['.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
         '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '--.-', '-..-', '..-..', '..--']
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'щ', 'ь', 'э', 'ю']
all_variants = []
phrase = '--....-.--...---.-..--..-....---'
start = ['г', 'з', 'м', 'т']
# в следующей строке подставьте вместо '9' число букв, и в файле будут содержаться все варианты расшифровки начала
# шифра, содержащее это количество букв
for j in range(9):
    output = open('output.txt', 'w')
    all_variants.clear()
    for i in start:
        if i.endswith('!'):
            all_variants.append(i)
        else:
            phrase = '--....-.--...---.-..--..-....---'
            summ = 0
            previous_alphabet = list(i)
            for q in previous_alphabet:
                q = morze[alphabet.index(q)]
                summ += len(q)
            if summ == len(phrase):
                all_variants.append(i + '!')
            else:
                phrase = phrase[summ:]
                for q in morze:
                    if phrase.startswith(q):
                        all_variants.append(i + alphabet[morze.index(q)])
    start.clear()
    for i in all_variants:
        start.append(i)
    print('\t'.join(all_variants), file=output)
    output.close()
