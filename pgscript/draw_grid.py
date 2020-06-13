import pygame

class draw_grid():
    def __init__(self, DISPLAY, columns, rows):
        self.width = DISPLAY.get_width()
        self.height = DISPLAY.get_height()
        self.columns = columns
        self.rows = rows
        self.cell = (DISPLAY.get_width()/columns, DISPLAY.get_height()/rows)

    def get_row(self, row):
        return int(self.height * row/self.rows)

    def get_column(self, column):
        return int(self.width * column/self.columns)
