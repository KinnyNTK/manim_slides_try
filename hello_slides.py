"""Starter manim-slides scene. Render and present from the project root."""

from manim import *
from manim_slides import Slide
from manim_slides import ThreeDSlide 

class JMThirtyThreeSlides(ThreeDSlide):
    def construct(self):


        self.move_camera(phi=75 * DEGREES, theta=180 * DEGREES, run_time=2)
        
        title = Text("JM32", font_size=48).to_edge(UP, buff=0.5)
        subtitle = Text("Areas & Volumes III", font_size=40).next_to(
            title, DOWN, buff=0.6
        )
        
        self.add_fixed_in_frame_mobjects(title, subtitle)
 

        self.play(Write(title))
        self.next_slide()

        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.next_slide()

        cone = Cone(
            base_radius=1.0,
            height=3,
            fill_opacity=0.6,             
            checkerboard_colors=[GOLD_D, GOLD_E], 
            stroke_color=WHITE,           
            stroke_width=2
        ).move_to([-1.4, -4.5, 0])
        
        self.play(Create(cone))
        self.next_slide()
        
        sphere = Sphere(
            radius=1.0,
            resolution=(16, 32),
            fill_opacity=0.6,
            checkerboard_colors=[GOLD_D, GOLD_E],
            stroke_color=WHITE, 
            stroke_width=2
        ).move_to([-3.1, -1.7, 0]) 
 
        self.play(Create(sphere))
        self.next_slide()

        tri_pyramid = Tetrahedron(
            edge_length=2.2,
            faces_config={
                "fill_opacity": 0.6,
                "fill_color": BLUE_D,
                "stroke_color": WHITE,
                "stroke_width": 2,
            },
        ).move_to([-2.9, 0.9, 0]) 
        self.play(Create(tri_pyramid))
        self.next_slide()

        quad_pyramid = Polyhedron(
            vertex_coords=[
                [1, 1, 0],
                [1, -1, 0],
                [-1, -1, 0],
                [-1, 1, 0],
                [0, 0, 2],
            ],
            faces_list=[
                [0, 1, 4],
                [1, 2, 4],
                [2, 3, 4],
                [3, 0, 4],
                [0, 1, 2, 3],
            ],
            faces_config={
                "fill_opacity": 0.6,
                "fill_color": TEAL_D,
                "stroke_color": WHITE,
                "stroke_width": 2,
            },
        ).move_to([-1.8, 3.7, 0])
        self.play(Create(quad_pyramid))
        self.next_slide()
        

        self.play(FadeOut(title, subtitle, cone, sphere, tri_pyramid, quad_pyramid  ))
