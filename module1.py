def testM1():
	print("*******testM1*********")

#if current module run as a independent program '__name__' is '__main__'
#if current module as a module run depend on other *.py,'__name__' is current module's name.
print(__name__)
if __name__ == "__main__":
	print("module is a independent program")
	testM1()
elif __name__ == "module1":
	print("module depend on other")
