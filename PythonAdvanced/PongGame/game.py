class Game:
    def __init__(self):
        self.width = 800
        self.high = 400
        self.__ball_pos = (0, 0)
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.paddle_a_pos = (-self.width / 2 + 50, 0)
        self.paddle_b_pos = (self.width / 2 - 50, 0)
        self.paddle_height = self.high / 4
        self.paddle_width = 20

        self.points_a = 0
        self.points_b = 0

    def tick(self):
        self.__border_check()
        self.__paddle_hit()
        x, y = self.__ball_pos
        self.__ball_pos = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    def __border_check(self):
        x, y = self.__ball_pos
        if abs(y) >= self.high / 2:
            self.__ball_delta_y *= -1
        if x <= - self.width/2:
            self.points_b+=1
            self.__ball_pos = (0,0)
        if x >=  self.width / 2:
            self.points_a += 1
            self.__ball_pos = (0,0)

    def ball_pos(self):
        return self.__ball_pos

    def paddle_a_up(self):
        x, y = self.paddle_a_pos
        if y <= self.high / 2 - self.paddle_height / 2:
            self.paddle_a_pos = (x, y + 20)

    def paddle_a_down(self):
        x, y = self.paddle_a_pos
        if y >= -self.high / 2 + self.paddle_height / 2:
            self.paddle_a_pos = (x, y - 20)

    def paddle_b_up(self):
        x, y = self.paddle_b_pos
        if y <= self.high / 2 - self.paddle_height / 2:
            self.paddle_b_pos = (x, y + 20)

    def paddle_b_down(self):
        x, y = self.paddle_b_pos
        if y >= -self.high / 2 + self.paddle_height / 2:
            self.paddle_b_pos = (x, y - 20)

    def __paddle_hit(self):
        x, y = self.__ball_pos
        a_x, a_y = self.paddle_a_pos
        is_paddle_a_hit = (a_x+self.paddle_width == x and a_y - self.paddle_height / 2 <= y <= a_y + self.paddle_height / 2)

        b_x, b_y = self.paddle_b_pos
        is_paddle_b_hit = (b_x-self.paddle_width == x and b_y - self.paddle_height / 2 <= y <= b_y + self.paddle_height / 2)
        if is_paddle_b_hit or is_paddle_a_hit:
            self.__ball_delta_x *= -1