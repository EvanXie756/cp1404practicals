text = input("Text: ")

word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0)+1


width = max(len(word) for word in word_count)
for word in sorted(word_count):
    print(f"{word:{width}} : {word_count[word]}")
