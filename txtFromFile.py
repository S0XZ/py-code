def getLines():
    f = open("test.md")
    lines = f.readlines()
    f.close()
    return '\n'.join(lines)