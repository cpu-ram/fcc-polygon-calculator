class Rectangle:
    width=0
    height=0
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self):
        pass
    def set_height(self):
        pass
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return (self.width+self.height)*2
    def get_diagonal(self):
        return pow((pow(self.width,2)+pow(self.height,2)),0.5)
    def get_picture(self):
        pass
    def get_amount_inside(self):
        pass
class Square(Rectangle):
    def __init__(self,side_length):
        self.width=side_length
        self.height=side_length
    def __str__(self):
        return f"Square(side={self.width})"
    def set_side(self, side_length):
        self.width=side_length
        self.height=side_length
    def set_width(self, side_length):
        self.set_side(side_length)
    def set_height(self, side_length):
        self.set_side(side_length)
    