from manim import *

class MyScene(ThreeDScene):
    def construct(self):
        text1 = Text("Thanks 3blue1brown").scale(0.4) # Scale down the text1
        text2 = Text("for").scale(0.4)
        text3 = Text("Manim").scale(0.6)
        sphere = Sphere().scale(0.2)
        cube = Cube().scale(0.16)

        self.add_fixed_orientation_mobjects(text1) # Fix the orientation of the text1
        self.play(Write(text1), run_time=3.3) #animates writing the text1
        self.wait(1) #wait for 1 seconds to let the text1 be visible
        self.play(FadeOut(text1))

        self.add_fixed_orientation_mobjects(text2)
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))   

        self.add_fixed_orientation_mobjects(text3)
        sphere.next_to(text3, UP, buff=1) # Position the sphere below the text3
        cube.next_to(text3, RIGHT, buff=0.7)

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(Write(text3), Create(sphere), Create(cube), run_time=5) #animate the creation of a sphere
        self.play(FadeOut(text3), FadeOut(sphere), FadeOut(cube), run_time=4)

        self.wait(10) #End screen