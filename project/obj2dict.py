# -*- encoding: UTF-8 -*-

class Pen:
	def __init__(self, color, size):
		self.color = color
		self.size = size
	def __str__(self):
	#	return str(convert_to_dict(self))
		return "fuck"
	def __repr__(self):
		return str(convert_to_dict(self))
	

class Student:
	def __init__(self, name, age, pen):
		self.name = name
		self.age = age
		self.pen = pen

def convert_to_dict(obj):
	'''把单个Object对象转换成Dict对象'''
	dict = {}
	dict.update(obj.__dict__)
	return dict

def convert_to_dicts(objs):
	'''把对象列表转换为字典列表'''
	obj_arr = []
	for o in objs:
		#把Object对象转换成Dict对象
		dict = {}
		dict.update(o.__dict__)
		obj_arr.append(dict)
	return obj_arr

def class_to_dict(obj):
	'''把对象(支持单个对象、list、set)转换成字典或字典列表'''
	is_list = obj.__class__ == [].__class__
	is_set = obj.__class__ == set().__class__
	if is_list or is_set:
		obj_arr = []
		for o in obj:
			#把Object对象转换成Dict对象
			dict = {}
			dict.update(o.__dict__)
			obj_arr.append(dict)
		return obj_arr
	else:
		dict = {}
		dict.update(obj.__dict__)
		return dict

if __name__ == '__main__':
	pen = Pen('orange',3.14)
	stu = Student('zhangsan', 20, pen)
	print('------convert_to_dict(stu)-----')
	print(convert_to_dict(stu))
	print('-----convert_to_dicts([stu, stu])------')
	print(convert_to_dicts([stu, stu]))
	print('-----class_to_dict(stu)------')
	print(class_to_dict(stu))
	print('-----class_to_dict([stu, stu])------')
	print(class_to_dict([stu, stu]))
	stua = Student('zhangsan', 20, pen)
	stub = Student('lisi', 10, pen)
	stu_set = set()
	stu_set.add(stua)
	stu_set.add(stub)
	print('------class_to_dict(stu_set)------')
	print(class_to_dict(stu_set))
