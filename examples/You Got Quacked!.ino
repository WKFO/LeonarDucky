
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
Keyboard.begin();
delay(3000);
delay(500);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('d');
Keyboard.releaseAll();
delay(500);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.releaseAll(); 
delay(800);
Keyboard.print("https://i.imgflip.com/1dv8ac.jpg");
delay(500);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(100);
// Opens up window and goes to a image I created xD
delay(500);
Keyboard.press(KEY_LEFT_CTRL);
Keyboard.press('s');
Keyboard.releaseAll();
delay(800);
Keyboard.print("%userprofile%\\Desktop\\QUACKED");
delay(500);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// saving the picture to the user Desktop, pic name QUACKED...
delay(100);
delay(500);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('d');
Keyboard.releaseAll();
// shows desktop
delay(500);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('r');
Keyboard.releaseAll();
delay(800);
Keyboard.print("%userprofile%\\Desktop\\QUACKED.jpg");
delay(500);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// opens the png file
delay(500);
Keyboard.press(KEY_LEFT_SHIFT);
Keyboard.press(KEY_F10);
Keyboard.releaseAll(); 
delay(500);
Keyboard.press(KEY_DOWN_ARROW);
Keyboard.releaseAll(); 
delay(500);
Keyboard.press(KEY_DOWN_ARROW);
Keyboard.releaseAll(); 
delay(500);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(500);
Keyboard.press(KEY_LEFT_ALT);
Keyboard.press(KEY_F4);
Keyboard.releaseAll();
// sets the background, and closes.
delay(500);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('d');
Keyboard.releaseAll();
delay(500);
Keyboard.press(KEY_LEFT_SHIFT);
Keyboard.press(KEY_F10);
Keyboard.releaseAll(); 
delay(500);
Keyboard.press(KEY_DOWN_ARROW);
Keyboard.releaseAll(); 
delay(500);
Keyboard.press(KEY_RIGHT_ARROW);
Keyboard.releaseAll(); 
Keyboard.print("d");
}
void loop() {}