def solution(n):
    openchars = ["[","{","("]
    closedchars = ["]","}",")"]
    characters = []

    for i in n:
        if i in openchars:
            characters.append(i)
        elif i in closedchars:
            char_type = closedchars.index(i)
            if len(characters)>0 and characters[len(characters)-1] == openchars[char_type]:
                characters.pop()
            else:
                return 0
    if len(characters) == 0:
        return 1
    else:
        return 0

print(solution("{[]}"))
print(solution("[{)(]}"))
print(solution("()[]"))

        