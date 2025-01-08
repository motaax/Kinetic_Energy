from manim import *

class Exercicio1(Scene):
    def equations_sequence(self, initial, equations):
        self.play(Write(initial))
        self.wait()

        current_step = initial
        for step in equations:
            self.play(ReplacementTransform(current_step, step))
            self.wait()
            current_step = step

        self.play(Circumscribe(equations[-1]), buff = 1.5)

    def construct(self):
        title = MathTex(r'\text{Prova do produto dos logaritmos}', font_size = 60, color = YELLOW) 
        title.shift(0.5 * UP)
        self.play(Write(title))
        self.wait()

        self.play(FadeOut(title))

        eq_inicial = MathTex(r'\log_b(xy)').scale(1.5)

        eq_passo_1 = MathTex(r'\log_b(xy) = c').scale(1.5)
        eq_passo_2 = MathTex(r'b^c = xy').scale(1.5)
        eq_passo_3 = MathTex(r'b^c = b^a \cdot b^d').scale(1.5)
        eq_passo_4 = MathTex(r'b^c = b^{a + d}').scale(1.5)
        eq_passo_5 = MathTex(r'c = a + d').scale(1.5)
        eq_passo_6 = MathTex(r'\log_b(xy) = \log_b x + \log_b y').scale(1.5)

        self.equations_sequence(eq_inicial, [eq_passo_1, eq_passo_2, eq_passo_3, eq_passo_4, eq_passo_5, eq_passo_6])
        self.play(FadeOut(eq_passo_6))