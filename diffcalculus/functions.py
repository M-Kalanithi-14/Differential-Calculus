"""
Contains Classes of Differentiable Functions that creates Differentiable Functions Objects.
"""

from .errors import *

# Complex Functions
class complexFn:
	"""Creates a Differentiable Complex Function using the simple functions."""

	def __init__(self, params=[], op=None, raisedTo=1):
		if len(params) in (0, 2):
			self.__params = params
		else:
			raise ParameterError(f"Invalid Parameter : {params}; Requires either a Empty List or a 2-Elemented List")

		if raisedTo > 0:
			self.__power = raisedTo
		else:
			raise ExponentError(f"Invalid Exponent : {raisedTo}; Requires a positive real number")

		if op in ("+", "-", "*", "/", None):
			self.__op = op
		else:
			raise OperationError(f"Invalid Differentiable Operation : {op}")

	@property
	def param(self):
		return self.__params

	@property
	def power(self):
		return self.__power

	@property
	def op(self):
		return self.__op

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], op="+")

	def __sub__(self, other):
		return complexFn([self, other], op="-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

	# Boolean Evaluation
	def __bool__(self):
		return any(self.param)

	def __repr__(self):
		result, param, op, power = "", self.param, self.op, self.power

		if any(param):
			u, v, result = param[0], param[1], ""

			if bool(repr(u)) and (u != 0) and (u != 1):
				result += f"{u}"
			elif u == 0:
				if op == "-":
					result += f"-"
				elif op in ("*", "/"):
					return "0"
			elif u == 1:
				if op != "*":
					result += f"1"

			# Operator Representation
			if any(result):
				if result != "-":
					if op == "/":
						result += f"{op}"
					else:
						result += f" {op}"
				else:

					# Unary Negation Representation
					result = f"(-{v})"

					if power == 1:
						return str(result)
					elif power == 0.5:
						return f"sqrt({result})"
					else:
						return f"{result}^{power}"

			# Second Term Representation
			if v != 1:
				if op == "/":
					result += f"{v}"
				else:
					result += f" {v}"
			elif (v == 1) and (op in ("+", "-")):
				result += f" 1"
			else:
				result = result[::-1][2:][::-1]

			# Power Representation
			if power == 1:
				return str(result)
			elif power == 0.5:
				return f"sqrt({result})"
			else:
				return f"{result}^{power}"
		else:
			return ""

# Basic X Function
class x:
	""" To create a differentiable square, cube root etc... function.
		By default, creates a square root function.
		For Polynomials use diffcalculus.functions.polynomial
	"""

	def __init__(self, raisedTo=0.5):
		self.__power = raisedTo

	@property
	def param(self):
		if self.__power == 1:
			return 1
		else:
			return None

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"x^{self.power}"
		else:
			return "x"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

# Inverse Functions
class sinInv:
	""" Creates a differentiable arcsin function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(sin⁻¹({self.param}))^{self.power}"
		else:
			return f"sin⁻¹({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class cosInv:
	""" Creates a differentiable arccos function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(cos⁻¹({self.param}))^{self.power}"
		else:
			return f"cos⁻¹({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class tanInv:
	""" Creates a differentiable arctan function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(tan⁻¹({self.param}))^{self.power}"
		else:
			return f"tan⁻¹({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class cosecInv:
	""" Creates a differentiable arccosec function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(cosec⁻¹({self.param}))^{self.power}"
		else:
			return f"cosec⁻¹({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class secInv:
	""" Creates a differentiable arcsec function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(sec⁻¹({self.param}))^{self.power}"
		else:
			return f"sec⁻¹({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class cotInv:
	""" Creates a differentiable arccot function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(cot⁻¹({self.param}))^{self.power}"
		else:
			return f"cot⁻¹({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

# Logarithmic Function
class log:
	""" Creates a differentiable logarithmic function."""

	def __init__(self, param=x(1), base="e", raisedTo=1):
		self.__param = param
		self.__power = raisedTo

		if base == "e":
			self.__base = base
		elif int(base) >= 1:
			self.__base = base
		else:
			raise BaseError(f"Unsupported base : {base}")

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	@property
	def base(self):
		return self.__base

	def __repr__(self):
		if self.base == "e":
			if self.power == 1:
				return f"ln({self.param})"
			else:
				return f"(ln({self.param}))^{self.power}"
		else:
			if self.power == 1:
				return f"log{self.base}({self.param})"
			else:
				return f"(log{self.base}({self.param}))^{self.power}"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

# Algebraic Functions
class polynomial:
	""" Creates a differentiable polynomial function.
		Requires an iterable with coefficients in the order,
		xⁿ + xⁿ⁻¹ +...x² + x.
		Mention the constant to the constant variable.
	"""

	def __init__(self, coeff=[1], constant=0):
		self.__correctCoeff, __power = coeff[::-1], 1
		self.__res = {0:constant}

		for i in self.__correctCoeff:
			if bool(i):
				self.__res[__power] = i
			__power += 1

	@property
	def param(self):
		return None

	@property
	def power(self):
		return self.__power

	@property
	def equation(self):
		return self.__res

	def __repr__(self):
		__str_res = ""

		for i in list(self.__res.keys())[::-1]:
			if i == 0:
				if self.__res[i] != 0:
					__str_res += f"{self.__res[i]} + "
			elif i == 1:
				__str_res += f"{self.__res[i]}x + "
			else:
				if self.__res[i] == 1:
					__str_res += f"x^{i} + "
				else:
					__str_res += f"{self.__res[i]}x^{i} + "

		return __str_res[::-1][3:][::-1]

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

# Trigonometric Functions
class sin:
	""" Creates a differentiable sin function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(sin({self.param}))^{self.power}"
		else:
			return f"sin({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class cos:
	""" Creates a differentiable cos function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(cos({self.param}))^{self.power}"
		else:
			return f"cos({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class tan:
	""" Creates a differentiable tan function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(tan({self.param}))^{self.power}"
		else:
			return f"tan({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class cosec:
	""" Creates a differentiable cosec function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(cosec({self.param}))^{self.power}"
		else:
			return f"cosec({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class sec:
	""" Creates a differentiable sec function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(sec({self.param}))^{self.power}"
		else:
			return f"sec({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class cot:
	""" Creates a differentiable cot function."""

	def __init__(self, param=x(1), raisedTo=1):
		self.__param = param
		self.__power = raisedTo

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if self.power != 1:
			return f"(cot({self.param}))^{self.power}"
		else:
			return f"cot({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

# Exponential Functions
class e:
	""" Creates a differentiable exponential function."""

	def __init__(self, param=x(1)):
		self.__param = param
		self.__power = 1

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	def __repr__(self):
		if repr(self.param) == "x":
			return f"e^x"
		else:
			return f"e^({self.param})"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")

class a:
	""" Creates a differentiable aˣ function."""

	def __init__(self, param=x(1), base=1):
		self.__param = param
		self.__power = 1

		if type(base) in (int, float):
			self.__base = base
		else:
			raise BaseError(f"Invalid Base : {base}; Requires a real number")

	@property
	def param(self):
		return self.__param

	@property
	def power(self):
		return self.__power

	@property
	def base(self):
		return self.__base

	def __repr__(self):
		if repr(self.param) == "x":
			return f"{self.base}^x"
		else:
			return f"{self.base}^{self.param}"

	# Arithmetic Operations
	def __add__(self, other):
		return complexFn([self, other], "+")

	def __sub__(self, other):
		return complexFn([self, other], "-")

	def __mul__(self, other):
		return complexFn([self, other], "*")

	def __truediv__(self, other):
		if (type(self) == type(other)):
			if (self.param == other.param) and (self.power == other.power):
				return 1
			else:
				return complexFn([self, other], "/")
		else:
			return complexFn([self, other], "/")

	# Unary Negation
	def __neg__(self):
		return complexFn([0, self], "-")