
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
Keyboard.begin();
delay(3000);
// Target: WINDOWS VISTA/7
// Encoder V2.4
// Using the run command for a broader OS base.
delay(3000);
delay(400);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('r');
Keyboard.releaseAll();
delay(1000);
Keyboard.print("cmd /Q /D /T:7F /F:OFF /V:ON /K");
delay(500);
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(750);
delay(400);
Keyboard.press(KEY_LEFT_ALT);
Keyboard.press(32);
Keyboard.releaseAll();
Keyboard.print("M");
for(int i = 0; i < 100; i++){
delay(400);
Keyboard.press(KEY_DOWN_ARROW);
Keyboard.releaseAll(); 
}
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
}
void loop() {}