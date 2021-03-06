class Hunter(object):
    def __init__(self, board):
        self.position_x = 0
        self.position_y = board.matrix_dimension[0] - 1
        self.smell_distance = 2
        self.smell_visible = False
        self.moved = False
        self.arrow = True
        self.smell = "../res/images/hunter/smell.png"
        self.direction = "FRONT"
        self.image = "../res/images/hunter/hunter_front.png"

    def position(self):
        return self.position_x, self.position_y

    def increment_x(self):
        self.image = "../res/images/hunter/hunter_right.png"
        self.moved = False

        if self.direction == "RIGHT":
            self.position_x += 1
            self.moved = True
        self.direction = "RIGHT"

    def decrement_x(self):
        self.image = "../res/images/hunter/hunter_left.png"
        self.moved = False

        if self.direction == "LEFT":
            self.position_x -= 1
            self.moved = True
        self.direction = "LEFT"

    def increment_y(self):
        self.image = "../res/images/hunter/hunter_front.png"
        self.moved = False

        if self.direction == "FRONT":
            self.position_y += 1
            self.moved = True
        self.direction = "FRONT"

    def decrement_y(self):
        self.image = "../res/images/hunter/hunter_back.png"
        self.moved = False

        if self.direction == "BACK":
            self.position_y -= 1
            self.moved = True
        self.direction = "BACK"
        
    def arrow_direction(self):
        if self.direction == "FRONT":
            return "../res/images/arrow/arrow_down.png"
        elif self.direction == "BACK":
            return "../res/images/arrow/arrow_up.png"
        elif self.direction == "RIGHT":
            return "../res/images/arrow/arrow_right.png"
        elif self.direction == "LEFT":
            return "../res/images/arrow/arrow_left.png"
            
    def arrow_position(self, distance):
        if self.direction == "FRONT":
            return (self.position_x, self.position_y + distance)
        elif self.direction == "BACK":
            return (self.position_x, self.position_y - distance)
        elif self.direction == "RIGHT":
            return (self.position_x + distance, self.position_y)
        elif self.direction == "LEFT":
            return (self.position_x - distance, self.position_y)

    def set_small_positions(self, positions):
        self.smell_positions = positions

    def clean_small_positions(self):
        self.smell_positions = []

    def __str__(self):
        return '({}, {})'.format(self.position_x, self.position_y)

    def __repr__(self):
        return self.__str__()
