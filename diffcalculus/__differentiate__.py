import math as __m
from .functions import *
from string import ascii_lowercase as __lower

__availFunctions = [sinInv, cosInv, tanInv, cosecInv, secInv, cotInv,
					log,
					polynomial, x,
					sin, cos, tan, cosec, sec, cot,
					e, a,
					complexFn,
					int, float]

def differentiate(function):
	""" Differentiates the Given Function and
		Returns the result as an object of diffcalculus.functions.*
		Note :- It is a Recursive Function.
	"""

	fn, result, times = function, complexFn(), 0

	if type(fn) in __availFunctions:
		if type(fn) in (int, float):
			return 0
		else:

			# Main Differntiation
			#if (times == 0):
			while True:
				fnName = type(fn).__name__

				if (type(fn) in __availFunctions) and (fnName != "polynomial"):
					param = fn.param

				if fnName == "x":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= 1
						else:
							result += 1
					else:
						if bool(repr(result)):
							result *= complexFn([power, x(power-1)], op="*")
							break
						else:
							return complexFn([power, x(power-1)], op="*")

				if fnName == "sinInv":
					power = fn.power

					if power == 1:
						denomX = complexFn([0, param], op="+", raisedTo=2)
						den = complexFn([1, denomX], op="-", raisedTo=0.5)

						if bool(repr(result)):
							result *= complexFn([1, den], op="/")
						else:
							result += complexFn([1, den], op="/")

						fn = fn.param
					else:
						newFunc = sinInv(param, power-1)
						result *= complexFn([power, newFunc], op="*")
						fn = sinInv(param)

					times += 1
					continue

				elif fnName == "cosInv":
					power = fn.power

					if power == 1:
						denomX = complexFn([0, fn.param], op="+", raisedTo=2)
						den = complexFn([1, denomX], op="-", raisedTo=0.5)

						if bool(repr(result)):
							result *= complexFn([-1, den], op="/")
						else:
							result += complexFn([-1, den], op="/")

					else:
						newFunc = cosInv(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "tanInv":
					power = fn.power

					if power == 1:
						denomX = complexFn([0, fn.param], op="+", raisedTo=2)
						den = complexFn([1, denomX], op="+", raisedTo=0.5)

						if bool(repr(result)):
							result *= complexFn([1, den], op="/")
						else:
							result += complexFn([1, den], op="/")
					else:
						newFunc = tanInv(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "secInv":
					power = fn.power

					if power == 1:
						denom1 = complexFn([0, fn.param], op="+", raisedTo=2)
						denom2 = complexFn([denom1, 1], op="-", raisedTo=0.5)
						den = param*denom2

						if bool(repr(result)):
							result *= complexFn([1, den], op="/")
						else:
							result += complexFn([1, den], op="/")

					else:
						newFunc = secInv(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "cosecInv":
					power = fn.power

					if power == 1:
						denom1 = complexFn([0, fn.param], op="+", raisedTo=2)
						denom2 = complexFn([denom1, 1], op="-", raisedTo=0.5)
						den = param*denom2

						if bool(repr(result)):
							result *= complexFn([-1, den], op="/")
						else:
							result += complexFn([-1, den], op="/")

					else:
						newFunc = cosecInv(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "cotInv":
					power = fn.power

					if power == 1:
						denomX = complexFn([0, fn.param], op="+", raisedTo=2)
						den = complexFn([1, denomX], op="+", raisedTo=0.5)

						if bool(repr(result)):
							result *= complexFn([-1, den], op="/")
						else:
							result += complexFn([-1, den], op="/")

					else:
						newFunc = cotInv(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "log":
					power = fn.power

					if fn.base == "e":
						if power == 1:
							if bool(repr(result)):
								result *= complexFn([1, param], op="/")
							else:
								result += complexFn([1, param], op="/")

						else:
							newFunc = log(param, power-1)
							result *= complexFn([power, newFunc], op="*")

					else:
						if power == 1:
							den = fn*param
							result *= complexFn([1, den], op="/")
						else:
							newFunc = log(param, base=fn.base)
							result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "polynomial":
					dictPoly, newDict, newCoeff = fn.equation, dict(), []

					if 1 in dictPoly:
						constant = dictPoly[1]
					else:
						constant = 0

					for power in list(dictPoly.keys())[1:]:
						newDict[power-1] = dictPoly[power] * power

					maxCoeff = max(list(newDict.keys()))

					for coeff in range(1, maxCoeff+1):
						if coeff in newDict:
							newCoeff.append(newDict[coeff])
						else:
							newCoeff.append(0)

					if bool(repr(result)):
						result *= polynomial(newCoeff[::-1], constant)
						times += 1
					else:
						return polynomial(newCoeff[::-1], constant)

				# Trigonometric Functions
				elif fnName == "sin":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= cos(param)
						else:
							result += cos(param)
					else:
						newFunc = sin(param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "cos":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= (-sin(param))
						else:
							result += (-sin(param))
					else:
						newFunc = sin(param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "tan":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= (sec(param, 2))
						else:
							result += (sec(param, 2))
					else:
						newFunc = tan(param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "cosec":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= (-cosec(param) * cot(param))
						else:
							result += (-cosec(param) * cot(param))
					else:
						newFunc = cosec(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "sec":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= (sec(param) * tan(param))
						else:
							result += (sec(param) * tan(param))
					else:
						newFunc = sec(fn.param, power-1)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "cot":
					power = fn.power

					if power == 1:
						if bool(repr(result)):
							result *= -cosec(param, 2)
						else:
							result += -cosec(param, 2)
					else:
						newFunc = cot(fn.param)
						result *= complexFn([power, newFunc], op="*")

					fn = param
					times += 1
					continue

				elif fnName == "e":
					if bool(repr(result)):
						result *= fn
					else:
						result += f

					fn = param
					times += 1
					continue

				elif fnName in ('1','2','3','4','5','6','7','8','9'):
					if bool(repr(result)):
						result *= fn * log(int(fnName))
					else:
						result += fn * log(int(fnName))

					fn = param
					times += 1
					continue

				elif fnName == "complexFn":
					u, v, op = param[0], param[1], fn.op
					du, dv = differentiate(u), differentiate(v)

					if op in ("+", "-"):
						if bool(repr(result)):
							result *= complexFn([du, dv], op=op)
							fn = param
						else:
							result += complexFn([du, dv], op=op)

					elif op == "*":
						duV, Udv = (du * v), (u * dv)

						if bool(repr(result)):
							result *= duV + Udv
							fn = param
						else:
							result += duV + Udv

					elif op == "/":
						duV, Udv = (du * v), (u * dv)
						num = duV - Udv
						den = complexFn([0, v], op="+", raisedTo=2)

						if bool(repr(result)):
							result *= num/den
							fn = param
						else:
							result += num/den

					else:
						raise OperationError(f"Please Provide an Operation.")

					break

				if (fnName in ("x", "polynomial")) or (times != 0):
					break

			return result

	else:
		raise FunctionError(f"Invalid Function : {fn}; Requires an object of diffcalculus.functions.*")

def substitute(function, value):
	""" Substitutes the Given Value for x in the Function
		Returns the result as a floating point number.
		Note :- It is a Recursive Function.
	"""

	fn = function
	fnName, times, result = type(fn).__name__, 0, 0

	if (times == 0):
		if fnName == "x":
			if bool(result):
				result *= (value ** fn.power)
			else:
				return (value ** fn.power)

		elif fnName == "sinInv":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.degrees(__m.asin(Value))) ** fn.power
			else:
				result += (__m.degrees(__m.asin(Value))) ** fn.power

			times += 1

		elif fnName == "cosInv":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.degrees(__m.acos(Value))) ** fn.power
			else:
				result += (__m.degrees(__m.acos(Value))) ** fn.power

			times += 1

		elif fnName == "tanInv":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.degrees(__m.atan(Value))) ** fn.power
			else:
				result += (__m.degrees(__m.atan(Value))) ** fn.power

			times += 1

		elif fnName == "cosecInv":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.degrees(__m.asin(1/Value))) ** fn.power
			else:
				result += (__m.degrees(__m.asin(1/Value))) ** fn.power

			times += 1

		elif fnName == "secInv":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.degrees(__m.acos(1/Value))) ** fn.power
			else:
				result += (__m.degrees(__m.acos(1/Value))) ** fn.power

			times += 1

		elif fnName == "cotInv":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.degrees(__m.atan(1/Value))) ** fn.power
			else:
				result += (__m.degrees(__m.atan(1/Value))) ** fn.power

			times += 1

		elif fnName == "log":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.log(Value, base)) ** fn.power
			else:
				result += (__m.log(Value, base)) ** fn.power

			times += 1

		elif fnName == "polynomial":
			eqn, subRes = fn.equation, 0

			for power in eqn:
				NValue = value ** power
				subRes += (eqn[power] * NValue)

			if bool(result):
				result *= subRes
			else:
				result += subRes

			return result

		elif fnName == "sin":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.sin(Value) ** fn.power)
			else:
				result += (__m.sin(Value) ** fn.power)

			times += 1

		elif fnName == "cos":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.cos(value)) ** fn.power
			else:
				result += (__m.cos(value)) ** fn.power

			times += 1

		elif fnName == "tan":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= (__m.tan(Value)) ** fn.power
			else:
				result += (__m.tan(Value)) ** fn.power

			times += 1

		elif fnName == "cosec":
			Value = substitute(fn.param, value)
			den = (__m.sin(Value)) ** fn.power

			if den == 0.0:
				if bool(result):
					result *= __m.inf
				else:
					result += __m.inf
			else:
				if bool(result):
					result *= 1/den
				else:
					result += 1/den

			times += 1

		elif fnName == "sec":
			Value = substitute(fn.param, value)
			den = (__m.cos(Value)) ** fn.power

			if den == 0.0:
				if bool(result):
					result *= __m.inf
				else:
					result += __m.inf
			else:
				if bool(result):
					result *= 1/den
				else:
					result += 1/den

			times += 1

		elif fnName == "cot":
			Value = substitute(fn.param, value)
			den = (__m.tan(Value)) ** fn.power

			if den == 0.0:
				if bool(result):
					result *= __m.inf
				else:
					result += __m.inf
			else:
				if bool(result):
					result *= 1/den
				else:
					result += 1/den

			times += 1

		elif fnName == "e":
			Value = substitute(fn.param, value)

			if bool(result):
				result *= __m.exp(Value)
			else:
				result += __m.exp(Value)

			times += 1

		elif fnName == "complexFn":
			param, op, power = fn.param, fn.op, fn.power

			if op in ("+", "-", "*", "/"):
				if type(param[0]) in (int, float):
					u = param[0]
				else:
					u = substitute(param[0], value)

				if type(param[1]) in (int, float):
					v = param[1]
				else:
					v = substitute(param[1], value)

				if op == "+":
					if bool(result):
						result *= (u + v) ** power
					else:
						result += (u + v) ** power
				elif op == "-":
					if bool(result):
						result *= (u - v) ** power
					else:
						result += (u - v) ** power
				elif op == "*":
					if bool(result):
						result *= (u * v) ** power
					else:
						result += (u * v) ** power
				elif op == "/":
					if v == 0:
						if bool(result):
							result *= __m.inf
						else:
							result += __m.inf
					else:
						if bool(result):
							result *= (u / v) ** power
						else:
							result += (u / v) ** power
			else:
				OperationError(f"Invalid Operation for Substitution : {op}; Please Provide an Operation.")

		else:
			Value = substitute(fn.param, value)

			if bool(result):
				result *= fn.base ** Value
			else:
				result += fn.base ** Value

			times += 1


	if type(result) in (int, float):
		return round(result, 2)
	else:
		return result

def differentiateAtPoint(function, point):
	""" Differentiates the Given Function at the Given Point
		Returns the result as a floating point number.
 	"""

	if type(function) in __availFunctions:
		DVal = differentiate(function)
		return substitute(DVal, point)
	else:
		raise FunctionError(f"Invalid Function : {function}; Requires an object of diffcalculus.functions.*")