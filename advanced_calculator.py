from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		self.ans=0
		self.input=""
		self.history=[]
		self.l=[]
		self.s0="0123456789."
		self.s1="}{()+-*/"
		self.a=Stack()
		self.b=Stack()
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		pass


	def evaluate_expression(self, input_expression):
		#print(input_expression)
		self.input= input_expression
		self.a.clear()
		self.b.clear()
		return AdvancedCalculator.evaluate_list_tokens(self,AdvancedCalculator.tokenize(self,input_expression))
		'''
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		'''
		pass
	def f1(a,b,d):
		try:
			n1=float(a)
			n2=float(d)
			if b=="+":
				return (n1+n2)
			elif b=="-":
				return (n1-n2)
			elif b=="*":
				return (n1*n2)
			elif b=="/":
				return (n1/n2)
		except:
			return "Error" 

	def tokenize(self, input_expression):
		#print(input_expression)
		#print("they called tokenize")
		#print(input_expression)
		self.l=[]
		s1="}{()+-*/"
		for i in input_expression:
			if i in self.s0:
				if len(self.l)==0:
					self.l.append(i)
				elif self.l[-1][-1] in self.s0:
					self.l[-1]=self.l[-1]+i
				else:
					self.l.append(i)
			elif i not in s1:
				if i==" ":
					pass
			else:
				#if self.l[-1] in s1:
				#	if i=="-" and self.l[-1] in "})":
				#		continue
				#	elif i=="-" and self.l[-1] not in "*/":
				#		return "ERROR2"
				self.l.append(i)
		#print(self.l)
		for i in range(len(self.l)):
			if self.l[i].isnumeric(): 
				self.l[i] = int(self.l[i])
		list_token=self.l
		return list_token
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		pass		

	def check_brackets(self, list_tokens):
		#print("they called check")
		#print(list_tokens)
		s=Stack()
		for i in list_tokens:
			#print(s)
			if i==")":
				#print("yaha")
				if s.is_empty():
					return False
				elif s.peek()=="(":
					s.pop()
				else:
					return False
			elif i=="(":
				#print("nhi yha")
				s.push(i)
			elif i=="}":
				#print("bhai yha")
				if s.is_empty():
				#	print("shi bat hai")
					return False
				elif s.peek() in "{":
				#	print("ye bhi thik hai")
					s.pop()
				else:
				#	print(s,s.peek()=="{")
				#	print("kya bat kr rha hai")
					return False
			elif i=="{":
				if not s.is_empty():
					if s.peek() in "(":
						return False
				s.push(i)
		#print(s,"*******")
		for i in "}{)(":
			if s.in_stack(i):
				return False
		return True

		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		pass

	def evaluate_list_tokens(self, list_tokens):
		#print("evaluate also ran")
		try:
			if AdvancedCalculator.check_brackets(self,list_tokens):
				#print(list_tokens)
				s1="{("
				s2=")}"
				s3="*/"
				s4="-+"
				l=list_tokens
				i=0
				while i<len(l):
					if str(l[i]) in "{(":
			#			print("kidhar")
						self.a.push(l[i])

					elif str(l[i]) in "*/+-":
			#			print("udhar")
						self.a.push(l[i])
			#			print("s2")
					elif str(l[i]) in "})":
			#			print("idhar")
						while(self.a.peek() not in s1):
							s=str(AdvancedCalculator.f1(self.b.second_peek(),self.a.peek(),self.b.peek()))
							if s=="Error":
								return "Error"
							self.b.pop()
							self.b.pop()
							self.a.pop()

							self.b.push(s)
						self.a.pop()
						while(self.a.peek() in s3):
							if len(self.b)>=2:
								if self.a.peek() in s3:
									s=str(AdvancedCalculator.f1(self.b.second_peek(),self.a.peek(),self.b.peek()))
									if s=="Error":
										return "Error"
									self.b.pop()
									self.b.pop()
									self.a.pop()
									self.b.push(s)
								else:
									break
							else:
								break
			#			print("yyyyyyyyyyyyy")
					else:
			#			print("yeeee nhi chala")
						self.b.push(l[i])
						#print(self.a,"a")
						#print(self.b,"b")
						while(self.a.peek() in s3):
							if len(self.b)>=2:
								if self.a.peek() in s3:
									s=str(AdvancedCalculator.f1(self.b.second_peek(),self.a.peek(),self.b.peek()))
									if s=="Error":
										return "Error"
									self.b.pop()
									self.b.pop()
									self.a.pop()
									self.b.push(s)
								else:
									break
							else:
								break
				#				print("yeee")
						
					i+=1
					print(self.a,"a")
					print(self.b,"b")
				self.a.reverse()
				self.b.reverse()
				print(self.a,"a")
				print(self.b,"b")
				while(len(self.b)>1):
					s=str(AdvancedCalculator.f1(self.b.peek(),self.a.peek(),self.b.second_peek()))
					if s=="Error":
						return "Error"
					self.b.pop()
					self.b.pop()
					self.a.pop()
					self.b.push(s)
				self.history.append((self.input,float(self.b.peek())))
				#print(self.a)
				if self.a.is_empty():
					return float(self.b.peek())
				return "Error"
			else:
				return "Error"
			
		except:
			return "Error"


		
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		pass
	def get_history(self):
		#print("they called history")
		return self.history[::-1]
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		pass

#print(AdvancedCalculator.evaluate_expression())