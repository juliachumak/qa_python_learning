# f = open('text.txt', 'w')
# f.write('Hello, World!\n')
# f.write('hi everybody!\n')
#
# f.close()
#
# f = open('text.txt', 'r')
#
# print(f.read())
#
# f.close()s


# f = open('text.txt', 'w')

# for line in f:
#     print(line.rstrip() + "!")
#
# f = open('text.txt', 'r+')
#
# print('\n Hi)))', file=f)
#
# print(f.read())

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