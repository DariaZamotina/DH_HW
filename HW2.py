from drawbot_skia.drawbot import rect, saveImage 
y = 100
x = 100
step = 150
for i in range(5):
    for j in range(5):
        rect(x, y, 100, 100)
        y = y + step
    y = 100
    x = x + step
    saveImage("HW2.pdf")