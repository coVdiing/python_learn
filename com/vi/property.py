# _*_ coding:UTF-8 _*_
class Screen(object):
    def __init__(self):
        self._resolution = 786432
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height= height
    @property
    def resolution(self):
        return self._resolution

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')