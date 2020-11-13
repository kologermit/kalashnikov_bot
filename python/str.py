def words(line):
    answer = []
    line = line.strip()
    a = next_word(line)
    while (a[0]):
        answer.append(a[0])
        a = next_word(a[1])
    return answer

def next_word(line):
    line = line.strip()
    space = line.find(" ")
    enter = line.find("\n")
    if line == "":
        return ("", "")
    if space == -1 and enter == -1:
        return (line, "")
    min = 1e10
    if space != -1 and min > space:
        min = space
    if enter != -1 and min > enter:
        min = enter
    return (line[0: min], line[min + 1:])

def next_line(text):
    text = text.strip()
    if len(text) == 0:
        return ""
    else:
        if text.find("\n") == -1:
            return text
        else:
            return text[0: text.find("\n")]