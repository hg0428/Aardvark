from Aardvark import *


class none:
	def __repr__(self):
		return "none"


@Aardvark.type("none")
def nonecheck(what, line_num):
	if what == "none" or type(what) == none:
		return True, none()
	else:
		return False, what
