text = "cat dog cat"
words = text.split()
bword = ""
bcount = 0
for word in words:
    if words.count(word) > bcount:
        bword = word
        bcount = words.count(word)
print(bword)