from drawbot_skia.drawbot import oval, fill, saveImage 
y = 100
x = 100
step = 150
fill (5, 0, 0)
oval (x, y, 100, 100)
for i in range(5):
    for j in range(5):
        oval(x, y, 100, 100)
        y = y + step
    y = 100
    x = x + step
saveImage("HW3.pdf")