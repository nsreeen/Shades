from shades.adjustcolors import darken_color, lighten_color

class TestAdjustcolor():
    lightcolor = '#bfe2ca'
    darkcolor = '#5f826a'
    steps = 6

    def test_darken_color(self):
        assert darken_color(self.lightcolor, self.steps) == self.darkcolor

    def test_lighten_color(self):
        assert lighten_color(self.darkcolor, self.steps) == self.lightcolor