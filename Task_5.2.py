# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_f = open("out_file.txt", "r")
my_str = []
lines_counter = 0
words_counter = 0
line_str = []
for line in my_f:
    lines_counter += 1
    my_str.append(line)
    words_counter += my_str.count(" ") + 1
    
    #print(line)
print(my_str)
print(lines_counter, words_counter)
my_f.close()
