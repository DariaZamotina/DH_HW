from drawbot_skia.drawbot import rect, saveImage 
y = 150
step = 150
for i in range(5):
    rect(100, y, 100, 100)
    y = y + step
    saveImage("HW.pdf")