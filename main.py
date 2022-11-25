
inputfile = open("sample.txt", "r")
output = open("output.txt", "w")
lexefile = open("lexemes.txt", "r")

inputt = inputfile.readlines()
# массив для самих лексем
lexemes = []
lexopers = []
lexlines = lexefile.readlines()
# заполняем лексемы и иноформацию о них
for line in lexlines:
    splex = line.split(", ")
    lexemes.append(splex[0])
    lexopers.append(splex[1])
for line in inputt:
    # проверка на остальные лексемы

    for
    elms = line.split(" ")
    for elm in elms:
        if elm != "":
            print(elm)
# закрываем файл
inputfile.close()
output.close()
