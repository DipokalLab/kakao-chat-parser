import re
import json


data = [{
    "name": "NON",
    "date": "18/03/2023 오후 2:27",
    "msg": "TEST"
}]

def readFile(path):
    f = open(path, 'r')
    lines = f.readlines()
    isMultiline = False
    exceptLineNumberRange = 5

    for i in range(len(lines)):
        if exceptLineNumberRange > i:
            continue

        line = lines[i]
        parseHead = getHead(line)
        
        if str(parseHead) == "[]":
            isMultiline = True

        if isMultiline:
            data[len(data) - 1]["msg"] += line
            isMultiline = False
        else:
            parseName, parseMsg = getName(parseHead[0], line)

            data.append({
                "date": parseHead[0],
                "name": parseName,
                "msg": parseMsg
            })

    writeJson(data)
    f.close()


def writeJson(value):
    with open('./output.json', 'w', encoding="UTF-8") as outfile:
        json.dump(value, outfile, ensure_ascii=False)

def getHead(line):
    headReg = re.compile('[0-9]{2}\/[0-9]{2}\/[0-9]{4} [ㄱ-ㅎㅏ-ㅣ가-힣]{2} [0-9]+:[0-9]{2},')
    result = headReg.findall(line)
    return result


def getName(head, line):
    headLength = len(head) + 1
    removeHead = line[headLength:]
    parseLine = removeHead.split(":")
    parseName = parseLine[0]
    parseMsg = "".join(parseLine[1:])

    return parseName, parseMsg

readFile("./data.txt")