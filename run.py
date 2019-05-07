import sys
import time
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 5
options.disable_hardware_pulsing = True
#options.show_refresh_rate = True

font = graphics.Font()
font.LoadFont("/home/pi/display16x32/rpi-rgb-led-matrix/fonts/output.bdf")
percentFont = graphics.Font()
percentFont.LoadFont("/home/pi/display16x32/rpi-rgb-led-matrix/fonts/7x13.bdf")

matrix = RGBMatrix(options = options)
canvas = matrix.CreateFrameCanvas()
pos1 = canvas.width
pos2 = canvas.width
goFlag1 = True
goFlag2 = False

text1 = "★미유미유★"
text2 = "고양이동아리"
textSpace = 30

len1 = graphics.DrawText(canvas, font, 0, 14, graphics.Color(0, 0, 0), text1)
len2 = graphics.DrawText(canvas, font, 0, 14, graphics.Color(0, 0, 0), text2)

graphics.DrawText(canvas, percentFont, 32, 12, graphics.Color(255, 255, 255), "Starting Up....")
canvas = matrix.SwapOnVSync(canvas)
time.sleep(3)
matrix.Clear()
canvas = matrix.SwapOnVSync(canvas)

try:
    print("Press CTRL-C to stop.")
    while True:
        canvas.Clear()
        if(goFlag1):
            pos1 -= 1

        if(goFlag2):
            pos2 -= 1

        if(pos1 < canvas.width - textSpace - len1):
            goFlag2 = True

        if(pos2 < canvas.width - textSpace - len2):
            goFlag1 = True

        if (pos1 + len1 < 0):
            goFlag1 = False
            pos1 = canvas.width
            
        if (pos2 + len2 < 0):
            goFlag2 = False
            pos2 = canvas.width
            
        white = graphics.Color(255, 255, 255)
        red = graphics.Color(255, 0, 0)
            
        a = graphics.DrawText(canvas, font, pos1, 14, graphics.Color(255, 0, 255), text1[0])
        b = graphics.DrawText(canvas, font, pos1 + a, 14, white if round((pos1 / 40) % 2) else red, text1[1:5])
        c = graphics.DrawText(canvas, font, pos1 + a + b, 14, graphics.Color(255, 0, 255), text1[-1:])

        d = graphics.DrawText(canvas, font, pos2, 14, graphics.Color(255, 255, 255), text2[0:3])
        e = graphics.DrawText(canvas, font, pos2 + d, 14, graphics.Color(255, 255, 0), text2[3:])
        
        time.sleep(0.03)
        canvas = matrix.SwapOnVSync(canvas)
        
except KeyboardInterrupt:
    print()
    sys.exit(0)
