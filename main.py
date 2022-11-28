
inputfile = open("sample.txt", "r")
output = open("output.txt", "w")
lexefile = open("lexemes.txt", "r")
outputlist = open("outputlist.txt", "w")

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
    elms = line.split(" ")
    tp = 0
    for elm in elms:
        if elm != "":
            outputlist.write(elm + "\n")
            temp = 0
            for lex in lexemes:
                if lex in elm:
                    if lex == "for":
                        print("for найлден")
                    output.write(elm + " - " + lexopers[temp] + "\n")
                    break
                temp += 1
        tp += 1
# закрываем файл
inputfile.close()
output.close()
lexefile.close()
outputlist.close()