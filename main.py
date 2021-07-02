lang = [
    '<SingleChar>', 'ALT', 'BREAK', 'CAPSLOCK', 'CONTROL', 'CTRL',
    'CTRL-SHIFT', 'DEFAULTDELAY', 'DEFAULT_DELAY', 'DELAY', 'DELETE', 'DOWN',
    'DOWNARROW', 'END', 'ENTER', 'ESC', 'ESCAPE', 'F1', 'F10', 'F11', 'F12',
    'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'GUI', 'HOME', 'INSERT',
    'LEFT', 'LEFTARROW', 'NUMLOCK', 'PAGEDOWN', 'PAGEUP', 'PAUSE',
    'PRINTSCREEN', 'REM', 'RIGHT', 'RIGHTARROW', 'SCROLLOCK', 'SHIFT', 'SPACE',
    'STRING', 'TAB', 'UP', 'UPARROW', 'WINDOWS'
]
DEFAULT_DELAY = 8
DEFAULTDELAY = 7
DELAY = 9
STRING = 45
WINDOWS = 49
GUI = 29
SHIFT = 43
DELETE = 10
HOME = 30
INSERT = 31
PAGEUP = 36
PAGEDOWN = 35
WINDOWS = 49
GUI = 29
UPARROW = 48
DOWNARROW = 12
LEFTARROW = 33
RIGHTARROW = 41
TAB = 46
ALT = 1
END = 13
ESC = 15
ESCAPE = 16
F1 = 17
F2 = 21
F3 = 22
F4 = 23
F5 = 24
F6 = 25
F7 = 26
F8 = 27
F9 = 28
F10 = 18
F11 = 19
F12 = 20
SingleChar = 0
SPACE = 44
TAB = 46
CONTROL = 4
BREAK = 2
PAUSE = 37
ESCAPE = 16
ESC = 15
CTRL = 5
DOWNARROW = 12
DOWN = 11
LEFTARROW = 33
LEFT = 32
RIGHTARROW = 41
RIGHT = 40
UPARROW = 48
UP = 47
BREAK = 2
PAUSE = 37
CAPSLOCK = 3
DELETE = 10
END = 13
ENTER = 14
ESC = 15
ESCAPE = 16
HOME = 30
INSERT = 31
NUMLOCK = 34
PAGEUP = 36
PAGEDOWN = 35
PRINTSCREEN = 38
SCROLLOCK = 42
SPACE = 44
TAB = 46
CTRL_SHIFT = 6

lineNum = 0


def aKey(words):
    aKeyList = [
        END, ESC, ESCAPE, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12,
        SingleChar, SPACE, TAB
    ]
    print(" len:", len(words))
    print(words)
		#makes sure there is only 1 command and 1 arg (length = 2)
    if (len(words) != 2):
        raise Exception(
            "Invalid use of ALT; no argument or too many arguments; line",
            lineNum)
    key = words[1]
    keyVal = lang.index(key)
    if (keyVal in aKeyList):
        pass
    else:
        raise Exception("Invalid argument for ALT; line", lineNum)

def ctrlCmd(words):
    cKeyList = [
        BREAK, PAUSE, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12,
        ESCAPE, ESC, SingleChar
    ]
    print(" len:", len(words))
    print(words)
		#makes sure there is only 1 command and 1 arg (length = 2)
    if (len(words) != 2):
        raise Exception(
            "Invalid use of CTRL; no argument or too many arguments; line",
            lineNum)
    key = words[1]
    keyVal = lang.index(key)
    if (keyVal in cKeyList):
        pass
    else:
        raise Exception("Invalid argument for CTRL; line", lineNum)

def delayCmd(words):
    print(" len:", len(words))
    print(words)
		#makes sure there is only 1 command and 1 arg (length = 2)
    if (len(words) != 2):
        raise Exception(
            "Invalid use of DELAY; no argument or too many arguments; line",
            lineNum)
    key = words[1]
    keyVal = lang.index(key)
    if (keyVal.isnumeric()):
        pass
    else:
        raise Exception("Invalid argument for DELAY; line", lineNum)

def guiCmd(words):
    print(" len:", len(words))
    print(words)
		#makes sure there is only 1 command and 1 arg (length = 2)
    if (len(words) != 2):
        raise Exception(
            "Invalid use of ALT; no argument or too many arguments; line",
            lineNum)
    key = words[1]
    keyVal = lang.index(key)
		#is alpha numeric but not space
    if (keyVal.isalnum() and keyVal != ' '):
        pass
    else:
        raise Exception("Invalid argument for ALT; line", lineNum)

def shiftCmd(words):
		#TODO: make skey list in ('dscript grammer.txt':93)
    sKeyList = [
        BREAK, PAUSE, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12,
        ESCAPE, ESC, SingleChar
    ]
    print(" len:", len(words))
    print(words)
		#makes sure there is only 1 command and 1 arg (length = 2)
    if (len(words) != 2):
        raise Exception(
            "Invalid use of SHIFT; no argument or too many arguments; line",
            lineNum)
    key = words[1]
    keyVal = lang.index(key)
    if (keyVal in sKeyList):
        pass
    else:
        raise Exception("Invalid argument for SHIFT; line", lineNum)


def parseLine(line):
    line = line.replace('\n', "").replace("\r", "")
    words = line.split(" ")
    if (words[0] in lang):
        cmd = lang.index(words[0])
        if cmd == 39:  #rem
            pass
        else:
            print(cmd)
            if (cmd == 1):  #alt
                aKey(words)
            elif (cmd == 4 or cmd == 5):  #control
                ctrlCmd(words)
            elif (cmd == 9):  #delay
                delayCmd(words)
            elif (cmd == 29):  #gui
                guiCmd(words)
            elif (cmd == 43):  #shift
                shiftCmd(words)
            elif (cmd == 45):  #string
                pass
            elif (cmd == 49):  #windows
                pass
            print()
    else:
        raise Exception("INVALID", line, "\n on line", lineNum)


file = open("in.txt", 'r')

while True:
    line = file.readline()
    lineNum += 1
    if len(line) == 0:
        break
    else:
        line = line.replace("\n", "")
        print(line, end=" ")
        try:
            parseLine(line)
        except ValueError as err:
            print(err.args)
