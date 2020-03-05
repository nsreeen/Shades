from shades.conversions import to_hexcolor, to_rgba

class TestConversions():
    hexstring = '#ef291f'
    rgb = (239, 41, 31)
    rgba = (239, 41, 31, 255)

    def test_to_hexcolor(self):
        assert to_hexcolor(self.rgb[0], self.rgb[1], self.rgb[2]) == self.hexstring

    def test_to_rgba(self):
        assert to_rgba(self.hexstring) == self.rgba
