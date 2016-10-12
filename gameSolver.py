import pyautogui

img=pyautogui.screenshot().crop([])

p1=pyautogui.locate('s.png',img,grayscale=False)
p1=pyautogui.locate('e.png',img,grayscale=False)

ifp1!=None and p2!=None:
	img=img.crop(p1[0],p1[1],p2[0],p2[1])
	img.save('test.png')