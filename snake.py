from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVEMENT = 20
up= 90
down= 270
right= 0
left= 180

class Snake:
    
    # Snake body creation logic
    def __init__(self):
        self.segment = []
        for position in STARTING_POSITIONS:
            new_body = Turtle("square")
            new_body.color("white")
            new_body.penup()
            new_body.goto(position)
            self.segment.append(new_body)
            
    
    # Snake movement logic
    def snake_move(self):
        for body_part_num in range(len(self.segment)-1,0,-1):
            x_pos = self.segment[body_part_num - 1].xcor()
            y_pos = self.segment[body_part_num - 1].ycor()
            self.segment[body_part_num].goto(x_pos, y_pos)
        
        self.segment[0].forward(MOVEMENT)


# Snake movement control logic
    def snake_control(self, key):
        if key == "w":
            if self.segment[0].heading() != down:
                self.segment[0].setheading(up)
        elif key == "s":
            if self.segment[0].heading() != up:
                self.segment[0].setheading(down)
        elif key == "a":           
            if self.segment[0].heading() != right:
                self.segment[0].setheading(left)
        elif key == "d":           
            if self.segment[0].heading() != left:
                self.segment[0].setheading(right)

    # Snake body extension logic
    def snake_extend(self):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(self.segment[-1].position())
        self.segment.append(new_body)
