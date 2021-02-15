def hello(dec):
	def inner():
		print("hai world")
		dec()
	return inner	
def asi(asus):
	def inner():
		print("hgdhdh")
		asus()
	return inner		
@hello
@asi
def hello():
	print("jdshshs")	
hello()	
def klm():
	print("gsyss")
klm()		