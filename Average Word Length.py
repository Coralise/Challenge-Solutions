average_word_length=lambda s:'{:.2f}'.format(sum([len(__import__('re').findall('[a-z|A-Z]', i)) for i in s.split()])/(len(s.split())))

print(average_word_length("A B C."))
print(average_word_length("What a gorgeous day."))
print(average_word_length("Dude, this is so awesome!"))