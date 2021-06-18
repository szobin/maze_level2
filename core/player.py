import tkinter as tk

from .conf import CW, CH, DX, DY, PLAYER_START_POS, PLAYER_START_DIRECTION, MAX_STEP_COUNT, MAX_SCORE, \
    FOOD_IMAGE, SPACE_IMAGE
from .figure import Figure
from .helper import get_x, get_y, get_image


class Player(Figure):

    def __init__(self, canvas, board, control):
        super().__init__(canvas, board, control, 'player', PLAYER_START_POS, PLAYER_START_DIRECTION)
        self.image_wow = get_image(f"./images/player82_wow.png")
        self.score = 0

    def respawn(self):
        super().respawn()
        self.score = 0

    def is_finish(self):
        return (self.step_count >= MAX_STEP_COUNT) or (self.score >= MAX_SCORE)

    def draw(self):
        x, y = get_x(self.p[0]) + CW // 2 - DX, get_y(self.p[1]) + CH // 2 - DY
        image = self.images[self.d - 1]
        if self.is_finish():
            image = self.image_wow
        self.canvas.create_image(x, y, image=image, anchor=tk.CENTER, tag=self.name)

    def set_pos(self, p_new):
        if not self.board.check(self, p_new):
            return False

        cell = self.board.get_cell(self.p)
        if cell == FOOD_IMAGE:
            self.board.set_cell(self.p, SPACE_IMAGE)

        self.hide()
        self.p = p_new
        self.draw()

        cell = self.board.get_cell(p_new)
        if cell == FOOD_IMAGE:
            self.score += 1
        return not self.is_finish()
