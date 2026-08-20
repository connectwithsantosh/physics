from manim import *

class SquareToCircle(Scene):

    def construct(self):
        circle = Circle(radius = 2)
        circle.set_fill(PINK, opacity=0.5)

        square = Square(side_length = 2)
        square.rotate(angle = PI/4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

        self.wait()
