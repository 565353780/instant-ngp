import pyautogui as pg

start_x = 1800
start_y = 600

x_move_dist = 700
y_move_dist = 100

move_speed = 5

pg.moveTo(start_x, start_y, 0.1)
pg.dragTo(start_x - x_move_dist,
          start_y + y_move_dist,
          move_speed,
          button='left')
pg.dragTo(start_x - 2.0 * x_move_dist,
          start_y,
          move_speed,
          button='left')
