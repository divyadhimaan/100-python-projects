from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LEVEL = ["slow","normal","fast","fastest"]


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()       
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.level = 0
        
    def create_snake(self):
        """Create a snake and initialize it to home position"""
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
        
           
    def add_segment(self,position):
        """Add segment to snake"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.speed("slowest")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
            
    def extend(self):
        """Extend snake for every score"""
        new_x = self.tail.xcor()
        new_y = self.tail.ycor()
        self.add_segment((new_x,new_y))
            
    def move(self):
        """Move snake on the principle of all segments following the segment at the front of it"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(x=new_x, y = new_y)

        self.head.forward(MOVE_DISTANCE)
        
    
    def reset(self):
        """Resetting all settings for snake"""
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.level = 0
        
    def change_level(self):
        self.level += 1
        print(f"Changing Level to {self.level} and speed to {LEVEL[self.level]}")
        for segment in self.segments:
            segment.speed(LEVEL[self.level])
        
    # Controlling snake 
    def up(self):
        """change direction of snake to move up, but when it is not already moving down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        """change direction of snake to move down, but when it is not already moving up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        """change direction of snake to move left, but when it is not already moving right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        """change direction of snake to move right, but when it is not already moving left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
            