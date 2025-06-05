# class Point:
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y

#      def draw(self):
#          print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# point.draw()



# MY OWN 
class FinalScore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def point(self):
        print(f"Game Over ({self.x}, {self.y})")
final_points = FinalScore(7, 5)
final_points.point()
