from math import hypot

#特殊なメソッド型
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):#文字列表現
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):#スカラー値
        return hypot(self.x, self.y)
    def __bool__(self):#ブール値
        return bool(abs(self))
    def __add__(self, other):#算術演算子
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):#算術演算子
        return Vector(self.x * scalar, self.y * scalar)
