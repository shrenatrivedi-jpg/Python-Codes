content="Percy Jackson is a demigod, the son of Poseidon, and the main protagonist of the Percy Jackson and the Olympians series by Rick Riordan.\n He discovers his true identity as a demigod and embarks on various quests to prevent catastrophic events in the world of Greek mythology.\n Throughout the series, Percy faces numerous challenges, battles mythical creatures, and learns about friendship, loyalty, and bravery.\n "

with open("PercyJackson.txt", "w") as file:
    file.write(content)

with open("PercyJackson.txt", "r") as file:
    text=file.read().lower()

for ch in ['.', ',', '!', '?', '\n']:
    text=text.replace(ch, '')

words=text.split()
word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

def get_count(item):
    return item[1]

sorted_word_count=sorted(word_count.items(), key=get_count, reverse=True)

print(content)
print("Word Occurrences:")
print(word_count)

print("\nTop 10 Word Occurrences:")
for word, count in sorted_word_count[:10]:
    print(f"{word}: {count}")

