import random
def generated_password(filename):
    word_list = []
    with open(filename, 'r') as f:
        for word in f:
            words = word.strip().lower()
            if 3 < len(words) < 8:
                word_list.append(words)
    return word_list


wordlist = generated_password('word.txt')
print(random.choice(wordlist) + random.choice(wordlist) + random.choice(wordlist))