import pyautogui, time
time.sleep(5)
file=open(r"C:\Users\SHUBHAM\Desktop\spamBotText.txt","r")
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")