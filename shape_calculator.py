class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (self.width+self.height)*2

    def get_diagonal(self):
        return pow((pow(self.width, 2)+pow(self.height, 2)), 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = ""
        for i in range(0, self.height):
            for i in range(0, self.width):
                result += ("*")
            result += ("\n")
        return result

    def get_amount_inside(self, another_rectangle):
        return (self.width // another_rectangle.width) * (self.height // another_rectangle.height)


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, side_length):
        self.set_side(side_length)

    def set_height(self, side_length):
        self.set_side(side_length)
