#!/usr/bin/env python
# sudo python3 bat.py -r 32 --led-cols=64 --led-slowdown-gpio=4
# http://www.mattlag.com/bitfonts/bit5x3.png
from base import SampleBase
from rgbmatrix import graphics
import time

class BattleshipBoard(SampleBase):
    def __init__(self, *args, **kwargs):
        super(BattleshipBoard, self).__init__(*args, **kwargs)
    
    def boot_sequence(self):
        board = self.matrix
        
        blue = graphics.Color(0, 0, 255)
        
        # Outline
        graphics.DrawLine(board, 0, 0, 63, 0, blue)
        graphics.DrawLine(board, 0, 0, 0, 31, blue)
        graphics.DrawLine(board, 0, 31, 63, 31, blue)
        graphics.DrawLine(board, 63, 0, 63, 31, blue)
        
        graphics.DrawLine(board, 31, 1, 31, 30, blue)
        graphics.DrawLine(board, 32, 1, 32, 30, blue)        
        
        # A-J
        board.SetPixel(2, 1, 255, 0, 0)
        board.SetPixel(1, 2, 255, 0, 0)
        board.SetPixel(3, 2, 255, 0, 0)
        board.SetPixel(1, 3, 255, 0, 0)
        board.SetPixel(2, 3, 255, 0, 0)
        board.SetPixel(3, 3, 255, 0, 0)
        board.SetPixel(1, 4, 255, 0, 0)
        board.SetPixel(3, 4, 255, 0, 0)
        board.SetPixel(1, 5, 255, 0, 0)
        board.SetPixel(3, 5, 255, 0, 0)
        time.sleep(5)
        # 1-10
        
        #time.sleep(5)
        #board.Fill(240, 255, 255)
        graphics.DrawLine(board, 0, 0, 63, 0, blue)
        graphics.DrawLine(board, 0, 0, 0, 31, blue)
        graphics.DrawLine(board, 0, 31, 63, 31, blue)
        graphics.DrawLine(board, 63, 0, 63, 31, blue)
        
        graphics.DrawLine(board, 31, 1, 31, 30, blue)
        graphics.DrawLine(board, 32, 1, 32, 30, blue)
        
        for x in range(2, 30, 3):
            for y in range(2, 30, 3):
                board.SetPixel(x, y, 143, 188, 143)
        for x in range(34, 62, 3):
            for y in range(2, 30, 3):
                board.SetPixel(x, y, 143, 188, 143)
                
        time.sleep(5)
        
    def run(self):
        self.boot_sequence()
        board = self.matrix
        
        while(True):
            time.sleep(10)
            print("Game running...")

# Main function
if __name__ == "__main__":
    battle = BattleshipBoard()
    if (not battle.process()):
        battle.print_help()

