f1 = open('text.txt', 'r')
f2 = open('text2.txt', 'w')

# text_lines = f1.readlines()
# print(text_lines)

i = 0
for line in f1:
    f2.write(str(i) + ': ' + line)
    i += 1

f1.close()
f2.close()