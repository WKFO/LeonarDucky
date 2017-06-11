#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[Author] : KeyLo99
[Contact] : twitter.com/KeyLo_99
"""

commands = ["REM", "DEFAULT_DELAY|DEFAULTDELAY|DELAY", "STRING", "WINDOWS|GUI", "MENU|APP", "SHIFT", "ALT", "CONTROL|CTRL",
            "DOWNARROW|DOWN", "LEFTARROW|LEFT", "RIGHTARROW|RIGHT", "UPARROW|UP", "BREAK|PAUSE", "CAPSLOCK", "DELETE", "END", "ESC|ESCAPE", "HOME",
            "INSERT", "NUMLOCK", "PAGEUP", "PAGEDOWN", "PRINTSCREEN", "SCROLLLOCK", "SPACE", "TAB", "REPLAY|REPEAT", "ENTER"]

arduinoCommands = ["// %", "delay(%);",
                   "Keyboard.print(%);",
                   "delay(delayms);\nKeyboard.press(KEY_LEFT_GUI);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_LEFT_SHIFT);\nKeyboard.press(KEY_F10);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_LEFT_SHIFT);\nKeyboard.press(%);\nKeyboard.releaseAll();",
                   "delay(delayms);\nKeyboard.press(KEY_LEFT_ALT);\nKeyboard.press(%);\nKeyboard.releaseAll();",
                   "delay(delayms);\nKeyboard.press(KEY_LEFT_CTRL);\nKeyboard.press(%);\nKeyboard.releaseAll();",
                   "delay(delayms);\nKeyboard.press(KEY_DOWN_ARROW);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_LEFT_ARROW);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_RIGHT_ARROW);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_UP_ARROW);\nKeyboard.releaseAll(); //.%",
                   "",
                   "delay(delayms);\nKeyboard.press(KEY_CAPS_LOCK);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_DELETE);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_END);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_ESC);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_HOME);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_INSERT);\nKeyboard.releaseAll(); //.%",
                   "",
                   "delay(delayms);\nKeyboard.press(KEY_PAGE_UP);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_PAGE_DOWN);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(206);\nKeyboard.releaseAll(); //.%",
                   "",
                   "delay(delayms);\nKeyboard.press(32);\nKeyboard.releaseAll(); //.%",
                   "delay(delayms);\nKeyboard.press(KEY_TAB);\nKeyboard.releaseAll(); //.%",
                   "",
                   "delay(delayms);\nKeyboard.press(KEY_RETURN);\nKeyboard.releaseAll(); //.%"]

shif_alt_ctrl = {5: "KEY_LEFT_SHIFT", 6: "KEY_LEFT_ALT", 7: "KEY_LEFT_CTRL"}

shiftCommands = ["DELETE", "HOME", "INSERT", "PAGEUP", "PAGEDOWN", "WINDOWS", "GUI", "UPARROW", "DOWNARROW", "LEFTARROW", "RIGHTARROW", "TAB"]
arduinoShift = ["KEY_DELETE", "KEY_HOME", "KEY_INSERT", "KEY_PAGE_UP", "KEY_PAGE_DOWN", "KEY_LEFT_GUI", "KEY_LEFT_GU", "KEY_UP_ARROW", "KEY_DOWN_ARROW", "KEY_LEFT_ARROW", "KEY_RIGHT_ARROW", "KEY_TAB"]

altCommands = ["END", "ESC", "ESCAPE", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "SPACE", "TAB"]
arduinoAlt = ["KEY_END", "KEY_ESC", "KEY_ESC", "KEY_F1", "KEY_F2", "KEY_F3", "KEY_F4", "KEY_F5", "KEY_F6", "KEY_F7", "KEY_F8", "KEY_F9", "KEY_F10", "KEY_F11", "KEY_F12", "32", "KEY_TAB"]

ctrlCommands = ["BREAK", "PAUSE","F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "ESCAPE"]
arduinoCtrl = ["", "", "KEY_F1", "KEY_F2", "KEY_F3", "KEY_F4", "KEY_F5", "KEY_F6", "KEY_F7", "KEY_F8", "KEY_F9", "KEY_F10", "KEY_F11", "KEY_F12", "KEY_ESC"]

_sig_ = "\n/* Converted by LeonarDucky v1.0 */\n\n"
_code_ = "#include <Keyboard.h>\nvoid setup() {\nint delayms = <delay>;\nKeyboard.begin();\ndelay(3000);\n%setup%}\nvoid loop() {}"
_function_ = "void duckyScript(){\nint delayms = <delay>;\n%setup%}"
build = ""
codeBlocks = []

def Compile(lines, delaytime, createfunction):
    for line in lines:
        command = line.split(" ")
        checkCommand(str(command[0]).upper(), str(line).replace(command[0], ""))

    if(str(createfunction) == "True") or (str(createfunction) == "true"):
        if (len(str(delaytime)) == 1) and ("0" in str(delaytime)):
            return _sig_ + _function_.replace("%setup%", build).replace("//.", "").replace("delay(delayms);", "").replace("int delayms = <delay>;\n", "")
        else:
            return _sig_ + _function_.replace("%setup%", build).replace("//.", "").replace("<delay>", str(delaytime))
    else:
        if (len(str(delaytime)) == 1) and ("0" in str(delaytime)):
            return _sig_ + _code_.replace("%setup%", build).replace("//.", "").replace("delay(delayms);", "").replace("int delayms = <delay>;\n", "")
        else:
            return _sig_ + _code_.replace("%setup%", build).replace("//.", "").replace("<delay>", str(delaytime))

def checkCommand(line, argument):
    for command in commands:
        if ("|" in command):
            innerCommand = command.split("|")
            for inc in innerCommand:
                if line.replace("\n", "") == inc:
                    changeCommand(commands.index(command), argument)
        else:
            if line.replace("\n", "") == command:
                changeCommand(commands.index(command), argument)

def changeCommand(command, argument):
    if(commands[command].strip() == "SHIFT") or (commands[command].strip() == "ALT") or ("CTRL" in commands[command].strip()):
        shiftAltCtrl(command, argument, shif_alt_ctrl[command])
    elif ("REPLAY" in commands[command].strip()):
         replayCommand(argument.strip().replace("\n", ""))
    else:
        if(len(argument) > 1) and ("Keyboard.press" in arduinoCommands[command]):
            code = arduinoCommands[command].replace("Keyboard.releaseAll(); //.%", "Keyboard.press(\'" + argument.strip().replace("\n", "")[:1] + "\');\nKeyboard.releaseAll();")
            addCode(code)
        elif(commands[command] == "STRING"):
            code = arduinoCommands[command].replace("%", "\""+argument.strip().replace("\n", "").replace("\\", "\\\\").replace("\"", "\\\"")+"\"")
            addCode(code)
        else:
            code = arduinoCommands[command].replace("%", argument.strip().replace("\n", ""))
            addCode(code)
def addCode(code):
    global build
    build += code + "\n"
    codeBlocks.append(code)

def shiftAltCtrl(command, args, key):
    try:
        if(key == "KEY_LEFT_SHIFT"):
            code = arduinoCommands[command].replace("%", arduinoShift[
                shiftCommands.index(args.upper().strip().replace("\n", ""))])
            addCode(code)
        elif(key == "KEY_LEFT_ALT"):
            code = arduinoCommands[command].replace("%", arduinoAlt[
                altCommands.index(args.upper().strip().replace("\n", ""))])
            addCode(code)
        elif(key == "KEY_LEFT_CTRL"):
            code = arduinoCommands[command].replace("%", arduinoCtrl[
                ctrlCommands.index(args.upper().strip().replace("\n", ""))])
            addCode(code)
            if ("PAUSE" in args.strip().upper()) or ("BREAK" in args.strip().upper()):
                code = code.replace("Keyboard.press();", "")
                code = code.replace("Keyboard.press(KEY_LEFT_CTRL);\n", "Keyboard.press(KEY_LEFT_CTRL);")
                addCode(code)
    except:
        if (len(args) < 1):
            code = "delay(500);\nKeyboard.press("+key+");\nKeyboard.releaseAll();"
            addCode(code)
        else:
            code = arduinoCommands[command].replace("%", "\'" + args.strip().replace("\n", "")[:1] + "\'")
            addCode(code)

def replayCommand(count):
    try:
        global build
        rCode = "for(int i = 0; i < %; i++){\n&\n}"
        rCode = rCode.replace("%", count).replace("&", codeBlocks[len(codeBlocks) - 1])
        build = str(build).replace(codeBlocks[int(len(codeBlocks)) - 1], rCode)
        codeBlocks.pop(int(len(codeBlocks) - 1))
        codeBlocks.append(rCode)
    except:
        pass
