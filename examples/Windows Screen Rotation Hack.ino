
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
int delayms = 500;
Keyboard.begin();
delay(3000);
delay(delayms);
Keyboard.press(KEY_LEFT_CTRL);
Keyboard.press(KEY_ESC);
Keyboard.releaseAll();
delay(50);
Keyboard.print("Screen Resolution");
delay(50);
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(100);
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_DOWN_ARROW);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_DOWN_ARROW);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_TAB);
Keyboard.releaseAll(); 
delay(delayms);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// if you find an error email me at "brayden.h96@gmail.com".
}
void loop() {}