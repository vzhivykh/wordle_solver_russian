with open('russian.txt', encoding='windows-1251') as f:
    dictionary = f.readlines()

dictionary = [i.strip().lower() for i in dictionary if len(i.strip()) == 5]

missing_letters = input('Введи отсутствующие буквы в виде - "абвгд".\n')
included_letters = input('Введи присутствующие буквы в виде - "ёпрст".\n')
hidden_word = input('Введи искомое слово в виде - "*у**о".\n')


def resolve(hidden_word, missing_letters, included_letters, dictionary):

    # remove words with missing letters
    dictionary = [i for i in dictionary if 
                  all(e not in i for e in missing_letters)]

    # remove words without included letters
    dictionary = [i for i in dictionary if 
                  all(e in i for e in included_letters)]

    for i in range(5):
        if hidden_word[i] != '*':
            dictionary = [w for w in dictionary if w[i] == hidden_word[i]]
    
    return dictionary


print(resolve(hidden_word, missing_letters, included_letters, dictionary))
