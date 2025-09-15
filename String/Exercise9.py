''' Exercise 9: Split the sentence "Python is fun" into words, 
then join them back with a dash (-) '''

sentence = "Python is fun"
words = sentence.split()
print(words)            # ['Python', 'is', 'fun']
print("-".join(words))  # Python-is-fun

