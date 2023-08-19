from stack import Stack

class SimpleCalculator:
	def __init__(self):
		self.c1=0
		self.c2="+"
		self.c3=0
		self.history=[]
		"""
		Instantiate any data attributes
		"""
		pass
	def isnum(n):
		s1="-.0123456789"
		for i in n:
			if i not in s1:
				return False
		return True

	def evaluate_expression(self, input_expression):
		history=self.history
		#print(input_expression,"simple")
		l1=["+","-","*","/"]
		l=[]
		#print(input_expression)
		for i in range(4):
			if l1[i] in input_expression:
				l=list(input_expression.split(l1[i]))
				l[0]=l[0].strip()
				if l[0]=="":
					return "ERROR"
				if l[-1]!="":
					l[-1]=l[-1].strip()
				else:
					return "ERROR"
				k=i
		if l==[]:
			return "ERROR"
		for i in range(3):
			if l1[i] in l[0]:
				return "ERROR"
		if l[0].count(".")>1 or l[-1].count(".")>1:
			return "ERROR"
		s=''
		for i in l[0]:
			if i!=' ':
				s+=i
		l[0]=s
		s=''
		for i in l[-1]:
			if i!=' ':
				s+=i
		l[-1]=s
		if not SimpleCalculator.isnum(l[0]):
			return "ERROR"
		if not SimpleCalculator.isnum(l[-1]):
			return "ERROR"
		self.c1=int(l[0])
		self.c2=l1[k]
		self.c3=int(l[-1])
		if k==0:
			history.append((input_expression,int(self.c1+self.c3)))
			return self.c1+self.c3
		elif k==1:
			history.append((input_expression,int(self.c1-self.c3)))
			return self.c1-self.c3
		elif k==2:
			history.append((input_expression,int(self.c1*self.c3)))
			return self.c1*self.c3
		else:
			if self.c3!=0:
				history.append((input_expression,self.c1/self.c3))
				return self.c1/self.c3
			else:
				return "ERROR"

		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		pass
	def get_history(self):
		return self.history[::-1]
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""

		pass

