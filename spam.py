import pyautogui, time
time.sleep(5)
file=open(r"spamTextLocation","r")
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
