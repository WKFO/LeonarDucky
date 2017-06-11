
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
Keyboard.begin();
delay(3000);
delay(3000);
delay(400);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('r');
Keyboard.releaseAll();
delay(500);
Keyboard.print("notepad");
delay(500);
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(750);
Keyboard.print("Hello World!!!");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
}
void loop() {}