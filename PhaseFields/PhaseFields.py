from manimlib import *
from numpy import sin, cos, tan, log

class PhaseField(Scene):

    def move_forward(self, vt, amount):
        initial_value = vt.get_value()
        self.play(
            vt.animate.set_value(initial_value+ amount),
            run_time = amount, rate_func=linear
        )

    def construct(self):
        ax = Axes()

        t = ValueTracker(0)
        def phasefunc1(points):
            vec_array = np.zeros_like(points)
            for i, point in enumerate(points):
                vec_array[i,0] = cos(2*t.get_value())
                vec_array[i,1] = sin(2*t.get_value())
            return vec_array
        
        def phasefunc2(points):
            vec_array = np.zeros_like(points)
            for i, point in enumerate(points):
                vec_array[i,0] = cos(2*t.get_value() + points[i,0])
                vec_array[i,1] = sin(2*t.get_value() + points[i,0])
            return vec_array
        phasefield1 = always_redraw(lambda: VectorField(
            phasefunc1, ax
        ))
        phasefield2 = always_redraw(lambda: VectorField(
            phasefunc2, ax
        ))
        self.play(ShowCreation(phasefield2))

        self.embed()