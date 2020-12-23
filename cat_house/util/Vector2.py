"""class vector"""
import math

class Vector2(object):
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y
	def __str__(self):
		return "(%s, %s)"%(self.x, self.y)


	@classmethod
	def from_points(cls, P1, P2):
		return cls(P2.x-P1.x, P2.y-P1.y)

	def get_magnitude(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		magnitude = self.get_magnitude()
		self.x /= magnitude
		self.y /= magnitude

	def add(self, rhs):
		return Vector2(self.x + rhs.x, self.y + rhs.y)

	def sub(self, rhs):
		return Vector2(self.x - rhs.x, self.y - rhs.y)

	def mul(self, scalar):
		return Vector2(self.x * scalar, self.y * scalar)

	def div(self, scalar):
		return Vector2(self.x / scalar, self.y / scalar)

"""
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print("Vector AB is")
print(AB)
print("AB * 2 is")
print(AB.mul(2))
print("AB / 2 is")
print(AB.div(2))
print(AB.add(Vector2(-10, 5)))
print("Magnitude of AB is", AB.get_magnitude())
print("AB normalized is", AB.normalize())
print(AB)
"""