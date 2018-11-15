#-*- coding:utf-8 -*-
import random
from sys import version_info
print(random.randint(0,2))#get random int value,range is 0,1,2
'''
树莓派：微型电脑，麻雀虽小五脏俱全，电脑的各种硬件它全有，可以弄来耍，淘宝上百来块钱



简单介绍shell脚本：
创建test.sh文件，在test.sh文件里写几个shell命令，例如：
ls
pwd
ls /
保存test.sh
给test.sh添加可执行权限：chmod u+x test.sh
此时这个shell脚本test.sh就可执行了：test.sh+Enter --> 会依次执行里面的那几个命





python与java和C语言等编程语言对比：
C语言和java会先编译成二进制文件，再执行；
python不用编译直接执行：其实python也编译了，只不过是编译一行执行一行，类似英语行业的同声传译
python是胶水语言，因为虽然python写代码的时候快，但是运行的时候相对较慢，可与C语言或java等混合使用，以弥补运行慢的缺点
python代码是动态的，直到运行到了，才知道要执行什么代码，参考下面的‘通过input获取匿名函数’案例


python运行代码--> python x.py
python+Enter --> 进入python2的交互模式，也会显示python的版本信息；在交互模式里可以写python语法，注意在交互模式写变量名则是打印变量，exit()退出交互模式。
ipython+Enter --> 进入python2的高级交互模式，推荐的交互模式，与普通交互模式对比：可以写shell命令且支持自动补全;exit退出，注意不是exit()。
python3运行代码-->python3 x.py
python3+Enter --> 进入python3的交互模式。
ipthon3+Enter --> 进入python3的高级交互模式，参考python2的高级交互模式。推荐的交互模式。
运行python代码的另一种方式，在代码第一行写入执行时的python解释器路径(#!/user/bin/python)，编辑完后需要对此python文件添加'x'权限。
这样在执行.py时，只需./hello.py然后Enter即可执行。




python2和python3的区别：
1：
python2有中文问题，无论中文出现在注释里还是代码里，用python2运行都会报错；
python3不存在中文问题；
解决方案有两种：推荐第二种方案
#coding=utf-8
#-*- coding:utf-8 -*-  
将上面任意一种解决方案放到代码的第一行即可。
2:
注意：input方法python2和python3完全不同；参考'通过input获取匿名函数'案例
python3中，是指以字符串的方式返回用户的输入结果；
但是在python2中，则把用户输入的内容作为python语法语句返回，
例如:a = input("请输入")，如果用户输入了hello，则实际效果是hello以表达式的方式赋值给a,即a=hello，因此会因为hell未定义报错
再例如,如果用户输入1+2，则a=3,会把1+2计算后返回。
其实在python2中并不用input接收用户输入，而是使用raw_input("请输入")代替。
3:
<> not equal,python2 have it,but python3 don't have it.
4:
get all keys composed collection
python2 return:['name','age','addr']
python3 return:dict_keys(['name','age','addr']),infact is object
get all values composed collection
python2 return:['18','jack','ah']
python3 retrun:dict_values(['18','jack','ah']),infacit is object
5:
print"this is python2 print"
 python2's print method no need bracket,python3 must use bracket.
6:
super:python2-->super(SonClassName,self);python3-->super() no para
7:
同时捕获多个异常：
python2:Error1,Error2;
python3:(Error1,Error2),in fact is a tuple.
任何异常都捕获：
python2:except: that's all.but except Exception is OK? take care about it.
python3:except Exception.
8:
python2:range(1,4),如果你print(range(1,4))会输出[1,2,3],因此range(1,10000000000)会内存溢出
python3:range(1,4),如果你print(range(1,4))会输出'range(1,4)',因此range(1,10000000000)不会内存溢出
实际上，python3对此做了优化，当你来取的时候我才给你值，取一个给一个，防止内存溢出:
range(1,5)[2]可以取出，list = range(1,5),list[0]也可以取出



查看python都有哪些关键字：
ipython3交互模式下：
第一步：import keyword   导入keywor包
第二步：keyword.kwlist  调用包里的内容，查看所有关键字

'''



'''
数据类型参考文档
python是弱类型语言，类似js，无需声明变量类型，系统会根据你给定的值，自动确定类型
type(变量)：返回当前变量的数据类型,看下面的例子,也可以用isinstance(instance,class)代替，eg:isinstance(123,int)
str转换为int:b=int(a),数据类型转换参考文档
int转换未str：b=str(a)  string = str(任何类型)
python格式化输出，参考文档：百度网盘-->前段-在学-->前段工具-->Linux

None just like java's null.eg:obj == None;obj = None

"" None 0 [] {} () --> False 
'''
#基本类型
print(type(123)==int)
print(type("123")==str)
print(type([])==list)
print(type((1,3,4))==tuple)
print(type({})==dict)
#对象类型,使用types中的常亮
print("#############类型##########")
import types
def mytp():
	pass
print(type(mytp)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


#print"this is python2 print" python2's print method no need bracket
name = "张学友"
age=19
add = "成都"
bfloat = 3.14
booy = True
print("输出变量age=%d"%age)
print("多种类型同时输出：%s%d%s"%(name,age,add))
print(type(age))
print(type(add))
print(type(bfloat))
print(type(booy))
strvalue = "23"
intvalue = int(strvalue)#字符串类型的数字，转为int类型的数

print("字符串转为数字：%d"%intvalue)





'''
接收用户输入,返回字符串结果
注意：input方法python2和python3完全不同；
python3中，是指以字符串的方式返回用户的输入结果；
但是在python2中，则把用户输入的内容作为python语法语句返回，
例如:a = input("请输入")，如果用户输入了hello，则实际效果是hello以表达式的方式赋值给a,即a=hello，因此会因为hell未定义报错
再例如,如果用户输入1+2，则a=3,会把1+2计算后返回。
其实在python2中并不用input接收用户输入，而是使用raw_input("请输入")代替。
'''
#result = input("请输入您的姓名：")
#print("接受输入结果：%s"%result)
print(age)#can output variable directly
#print("any-content",end="")#line tip end with "",instead of line feed,in fact end="anycontent" is ok,python2 can not use end.
print("")#line feed,start a new line


'''
python语言中一般不用{}大括号区分代码块，因此强制使用tab键区分代码块，例如if语句中，if后面联系几个tab开头的语句都是if语句的内容，直到某个
不是tab开头的语句才结束，elif和else语句也是一样
in python have no do-while,switch-case
'''
if age<18:
	print("我未成年")
	print("你呢")
elif age>18:
	print("我成年了")
	print("你呢")
elif age>100:
	pass#pass类似于java的todo，暂时不写代码，先放在这里占个位置
else:
	print("我刚好18岁")
	print("我是大人了")
print("我不属于if-else")



'''
= 赋值符号，在python中，该符号永远是指左边的变量指向右边的表达式所对应的内存区域，例如：a=10,a指向10的内存区域;b="hello",b指向'hello'的内存区域;c=[1,2],c指向[1,2]的内存区域。
+ 加法
- 减法
* 乘法,数学乘法和字符串乘法，所谓字符串乘法："H"*5="HHHHH"
/ 除法，返回实际的数学结果，例如：5/2=2.5
// 除法，返回商，例如：5//2=2
% 除法，返回余数，例如：5%2=1
** 求次方，例如2**2=2的2次方，2**3等于2的3次方，2××100=2的100次方

a+=1 just like a=a+1，但是二者是有区别的，当a指向可变类型时，例如a=[0],则a+=[1,2]是对a原来指向的[0]内存区域进行修改，a的指向不变；而a=a+[1,2]是开辟新的内存区域存放a+[1,2,]，然后让a指向的这块新的内存区域，即a的指向改变。其他-= *= /=等等也是同样的道理
-=
*=
/=
//=
%=
**=
but attention this:
a*=2+4+6 just like a=a*(2+4+6) not like a=(a*2+4+6)
in python have no a++,a--

> greater-than sign 
< less-than sign
>= greater-equal sign 
<= less-equal sign
!= not equal
<> not equal,python2 have it,but python3 don't have it.
== equal


or just like java's ||
and just like java's &&
not just like java's !



'''
print("字符串乘法:"+"H"*5)

amulti = 2
amulti*=2+4+6
print(amulti)#a=a*(2+4+6)

aoan = "a"
boan = "b"
coan = "c"
if aoan == "a" or boan == "b":
	print("how to use 'or'")

if aoan == "a" and boan == "b":
	print("how to use 'and'")

if not(aoan == "a" and boan == "c"):
	print("how to use 'not'")

if (aoan == "a" or boan == "b") and coan == "c":
	print("logic-bracket")


#python交换两个变量的值
print("****************交换两个变量的********************")
va =3
vb =4
va=va+vb
vb=va-vb
va=va-vb
print("va=%d,vb=%d"%(va,vb))

vc=8
vd=9
vc,vd=vd,vc
print("vc=%d,vd=%d"%(vc,vd))



'''
表达式：
a,b,c = 3 --> 报错，并不是a=3,b=3,c=3,而是3不是可迭代的对象，报错
a,b,c = "345" --> a="3",b="4",c="5","345"是可迭代的对象
a,b,c = [3,4,5] --> a=3,b=4,c=5 [3,4,5]是可迭代的对象
'''



'''
可变类型和不可变类型
immutable variable:numbers,string,tuple
volatile variable:others are all volatile,eg:list,dictionary
dictionary's key can be any immutalbe variable,but cann't be volatile variable,because volatile have no hashcode,immutable have hashcode.yy
'''




'''
str
eg:name = "hellokitty"
order:0,1,2,3,4,5,6,7,8,9
inverted order:-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

get one char:
name[index];
eg:name[0]<-->name[-10], name[9]<-->name[-1]

get substring:
name[startIndex,endIndexNext,oneStepIndexCount]
startIndex:have connection with order.can ignore,if the order is from left to right,then default value is 0.
	if the order if from right to left,then default value is -1.
endIndexNext:have connection with order.can ignore,no matter what order,the default value is until the last one;
	if you type it,according to order, the resulted substring not contain name[endIndexNext].
oneStepIndexCount:can ignore,default value is 1,if it's value is positive number then step from left to right;
	if it's value is negative number then step from right to left.
	what's mean of it's value:index is 0,1,2,3,4,5,6,7. if it's value is 2 then get 0,2,4,6.if it's value is
	3 then get 0,3,6,if it's value is 1 then get 0,1,2,3,4,5,6,7.
'''
s1451 = "abcdefgh"
#string can not splice with int value.eg:s1451+10 is error
print("str's length:%d"%len(s1451))#get str's length:len(strvar)
s1515 = "ijk"
#string splice string with +
s1518 = s1451+s1515
print(s1518)
print("str splice:%s"%(s1451+s1515))
print(s1451[3])#get char by index
print(s1451[1:])#bcdefgh
print(s1451[::-1])
print(s1451[-2::-1])
print(s1451[:1:-1])




'''
string's functions
str = "abc"

str.find("sub") --> from left find the first appear child string,if find then return the index of the child string's first char,if not find then retrun -1.
str.rfind(sub) --> from right find the first appear child string.
str.index("sub") --> reference find("sub"),but if not find will report error,not retrun -1.
str.rindex("sub") --> reference rfind("sub"),but if not find will report error,not return -1.

str.count("sub") --> return the count of "sub" appear in str.

str.replace("oldsub","newsub") --> use "newsub" replace all "oldsub" in str.attentiion that string is immutable variable,this function will return a new string,old string never change.
str.replace("oldsub","newsub",1) --> the third para means that how many "oldsub" will be replace if oldsub appear many count.

str.split("anychar") --> according given char split string into a list.eg:"aa bb cc".split(" ")-->["aa","bb","cc"]
str.split() --> without para,according invisible char in str to split.such as /t /n...

str.capitalize() --> let str's first letter uppercase.attention only str's first letter,not every word's first letter.
str.title() --> let every word's first letter uppercase in str.

str.lower() --> all letters in str will convert into lowercase.
str.upper() --> all letters in str will convert into uppercase.

str.startswith("sub") --> if str start with "sub" return True,then return False.
str.endswith("sub") --> reference startswith("sub").

str='hello'
str.center(100) --> redefine a string which length is 100,and the str is in center of it.eg:'     hello     '
str.ljust(100) -->  redefine a string which length is 100,and the str is in left of it.  eg:'hello          '
str.rjust(100) -->  redefine a string which length is 100,and the str is in right of it. eg:'          hello'

str.lstrip() --> strip left blank char of str then return.
str.rstrip() --> strip right blank char of str then return.
str.strip() --> strip both left and right blank char of str then return. 

str.partition("sub") --> from left find the first "sub",then according this "sub" split str."sub"'s left is a part,maybe "";"sub" is a part;"sub"'s right is a part,maybe "";then composed these three string as a tuple return. eg:"a b c".partition("a")-->("","a"," b c");"a b c".partition("b")-->("a ","b"," c");"a b c".partition("c")-->("a b ","c","")
str.rpartition("sub") --> reference str.partition("sub"),but attention this is from right find the first "sub".

str="a\nb\nc\n"
str.splitlines() --> according lines split str,then composed as a list return. eg:["a","b","c"]

str.isalpha() --> if all chars of str is letter return True,then return False.
str.isdigit() --> if all chars of str is digit return True,then return False.
str.isalnum() --> if all chars of str is letter or digit or letter and digit return True.then return False.
str.isspace() --> if str only contain blanks return True,then return False.

names=["aa","bb","cc"]
names="aabbcc"
str="-"
str.join(names) --> "aa-bb-cc","aoaobobococ"


'''
print("*******************string function*************************")
spstr = "hello world, I'm comeing"
print(spstr.split(" "))

print(spstr.ljust(10))

print(spstr.partition("hello"))

jostr="aabbcc"
fstr = "o"
print(fstr.join(jostr))#fouocok

'''
while circulation
in python have no do-while,switch-case
'''
cir = 0
while cir<=10:
	print(cir)
	cir+=1	


'''
for circulation
string can be cycle by for
break;continue;


range(startIndex,endIndexNext,oneStepIndexCount) reference string
python2:range(1,4),如果你print(range(1,4))会输出[1,2,3],因此range(1,10000000000)会内存溢出
python3:range(1,4),如果你print(range(1,4))会输出'range(1,4)',因此range(1,10000000000)不会内存溢出
实际上，python3对此做了优化，当你来取的时候我才给你值，取一个给一个，防止内存溢出:
range(1,5)[2]可以取出，list = range(1,5),list[0]也可以取出

judge one obj is can iterable:
from collections import Iterable
isinstance('abc', Iterable) return Ture or False.

tranverse the index and the element at the same time:
enumerate(iterableObj)
'''
print("**************for circulation**************")
strfor = "hellokitty"
for temp in strfor:
	print(temp)
else:#if you use 'break' in for circulation,'else' will not run.then else will stil run.
	print("for's else")

for i in range(0,5):
	print(i)

ranlist = range(0,10,2)
print(ranlist[2]) 
print(range(1000,1100,2)[2])
print(range(800,804))
print(range(4))#[0,1,2,3]

#列表生成式：forlist = [expression forcirculation... filter]
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
forlist = [i for i in range(4)]
print(forlist)#[0,1,2,3]
forlist = [i+10 for i in range(10,20,3)]
print(forlist)#[20, 23, 26, 29]
forlist = ["yes" for i in range(0,4)]
print(forlist)#["yes","yes","yes","yes"]
forlist = [i for i in range(0,10) if i%2==0]
print(forlist)#[0,2,4,6,8]
forlist = [(i,j) for i in range(0,2) for j in range(0,3)]
print(forlist)#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

#列表生成器：generator，参考廖雪峰的博客,适合数据量很大的列表，一边取一边生成

#迭代器:Iterator,迭代器是惰性序列，取到时才加载，但是可通过list(迭代器)一次性加载，注意可迭代的对象iterableObj不一定是迭代器，参考廖雪峰的博客

#judge one obj is can iterable
from collections import Iterable
print(isinstance('abc', Iterable))#True
print(isinstance([1,2,3],Iterable))#True
print(isinstance(123,Iterable))#False

#tranverse the index and the element at the same time.
print("**************enumerate*****************")
mindList = ["a","b","c","d"]
for index,ele in enumerate(mindList):
	print("index=%d,ele=%s"%(index,ele))

mindtuple = ("aa","bb","cc")
for index,ele in enumerate(mindtuple):
	print("tuple:index=%d,ele=%s"%(index,ele))



'''
列表：collection
can store multi type value.
'''
#list[startIndex,endIndexNext,oneStepIndexCount]:reference string 
inList = [0,1,2,3,4,5,6,7]
print(inList[0])#0
print(inList[-1])#7
print(inList[::-1])#[7,6,5,4,3,2,1,0]
print(inList[1:5])#[1,2,3,4]
print(inList[-2:1:-1])#[6,5,4,3,2]

#append element at the tip
mlist = ["a",20,3.14,"123"]#multi type value
mlist.append("fuck")

#insert element at specific position,the original element at the positon move to backward
mlist.insert(2,200)#the first parameter is the index which will be inserted.
print(mlist)

#two can collection joint with "+"
slist = [1,2,3]
alist = mlist+slist
print(alist)

#one collection can append at the tip of the other collection
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1.extend(list2)#extend() have no return value
print(list1)#[1,2,3,4,5,6] been append
print(list2)#[4,5,6] not change
print(list3)#None extend() have no return value


#delete and return the last element
dlist = [1,2,3,4,5,6,7,8]
dee = dlist.pop()
print(dlist)#[1,2,3,4,5,6,7]
print(dee)#8

#delete specific element.if the collection have some the same element,then just delete the first appear element
#remove(para):the parameter is element not index,and have no return value
rmList = [1,2,2,3]
rmList.remove(2)
print(rmList)#[1,2,3]

#delete element by index
delList = [1,2,3,4,5]
del delList[1]
print(delList)#[1,3,4,5]

#replace element by index
fixList = [1,2,3,4,5]
fixList[2] = "abc"
print(fixList)#[1,2,'abc',4,5]

#search element from a collection
#judge which element is in a collection
seaList = ["abc","d","ef","ghi"]
if "d" in seaList:
	print("'d' is in seaList")
if "fuck" not in seaList:
	print("'fuck' not in seaList")

#collection's for circulation 
forList = [111,222,333,444,555]
for temp in forList:
	print(temp)

#collection's length
lenList = [1,2,3,4,5]
print("collection's length:%d"%len(lenList))

print("************* sort ***************")
#number have default sort rule
sortList=[34,9,123,0,82,44]
sortList.sort()
print(sortList)

#string have default sort rule too.
strSortList=["cc","tttt","b","23","lll","89","wwww","aaa","1"]
strSortList.sort()
print(strSortList)

#custom sort rule:
#give sort() a anonymous function para,this anonymous function have only one para,inner sort() will call this anonymous function and list'seach element will as para transfer into this anonymous function,and this anonymous function's expression will decide the sort rule for list.
mapList=[{'name':'jace','age':18},{'name':'zs','age':22},{'name':'body','age':90},{'name':'fuck','age':4}]
mapList.sort(key=lambda kv:kv['name'])
print(mapList)




'''
set:cann't have repeated element.
'''
print("(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
aset = {1,2,3,1,2}
print(aset)#{1,2,3} auto wipe off repeat element 




'''
元祖:tuple,can not change.
in add,delete,modify,search
tuple just can operate 'search'.can not 'add','delete','modify'.

empty tuple:()
one element tuple:(1,).attention there is a comma.
'''
myt = (1,2,3)
#get tuple's lenth
print("tuple's lenth:%d"%len(myt))

#search someone element vlaue
print("get a element from a tuple:%d"%myt[1])

#unpack:mya=myt[0],myb=myt[1],myb=myt[2]
#left variable count must equal tuple's lenth,eg:mya,myb=myt is error; 
mya,myb,myc = myt
print("tuple's every element:%d,%d,%d"%(mya,myb,myc))

#for circulation
for temp in myt:
	print(temp)




'''
set,list,tuple convert each other.
'''
#set --> list
s2list = list(aset)
print(s2list)#[1,2,3]
#set --> tuple
l2tuple = tuple(aset)
print(l2tuple)
#list --> set
aset = set(s2list)
print(aset)#{1,2,3}
#list --> tuple
l2tuple = tuple(s2list)
print(l2tuple)#(1,2,3)
#tuple --> list
s2list = list(l2tuple)
print(s2list)#[1,2,3]
#tuple --> set
aset = set(l2tuple)
print(aset)#{1,2,3}






'''
字典dictionary:just like java's map.nothing on order,this is deference of collection
key-value
dictionary's key can be any immutalbe variable,but cann't be volatile variable,because volatile have no hashcode,immutable have hashcode.yy
'''
infos = {"name":"jack","addr":"chengdu","age":18}
print(infos)#output all
print("my name is %s,my address is %s,I'm %d."%(infos["name"],infos["addr"],infos["age"]))#out every key
print("dictionary's length:%d"%len(infos))

#add
infos["tel"] = "10086"
print(infos)

#delete,if have no this key,then report an error
del infos["addr"]
print(infos)

#modify
infos["tel"] = "10010"
print(infos)

#search
#if have no this key,then report an error
oInfo = infos["name"]
print(oInfo)
#if have no this key ,then will not report error
gInfo1 = infos.get("tel")
gInfo2 = infos.get("fuck")
print(gInfo1)#10010
print(gInfo2)#None,not error

maps = {"name":"jack","age":18,"addr":"ah"}
#traverse the dict directly,in face is traverse all keys.
for key in maps:
	print(key)#age,name,addr

#get all keys composed collection
#python2 return:['name','age','addr']
#python3 return:dict_keys(['name','age','addr']),infact is object
keyList = maps.keys()
print(keyList)
#no matter python2 or python3, the result can for circulation certainly.
for temp in keyList:
	print(temp)

#get all values composed collection
#python2 return:['18','jack','ah']
#python3 retrun:dict_values(['18','jack','ah']),infact is object
valList = maps.values()
print(valList)
#no matter python2 or python3,the result can for circulation certainly.
for temp in valList:
	print(temp)

#get k-v composed collection,each k-v composed as a tuple,all tuple composed as a collection.
#python2 retrun:[('age', 18), ('name', 'jack'), ('addr', 'ah')]
#python3 return:dict_items([('age', 18), ('name', 'jack'), ('addr', 'ah')]),infact is object
kvList = maps.items()
print(kvList)
#no matter python2 or python3,the result can for circulation certainly.
for tupleTemp in kvList:
	print(tupleTemp)#tupleTemp is a tuple.
for ta,tb in kvList:#tuple auto unpack into ta and tb.
	print(ta)
	print(tb)

print("&&&&&&&&&&&&&&&&&&&&&&liao xuefeng&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
dl = {'a': 1, 'b': 2, 'c': 3}
for key in dl:
	print(key)

for myk in dl.keys():
	print(myk)

"""
函数:function;golbal variable;local variable
but attention tab indent,just like if-else.
don't need define return type,because you can return any type.
def funName(necessaryParas,defaultParas,*tuple,**dictionary),attention these paras's order.the only difference between defaultPara and necessaryPara is defaultPara has a default value,you can omit it.others are the same.
eg:
def funName(a,b,c=1,d=2,*args,**kwargs):
	pass
funName(1,2,3,4,,5,6,name="jack",age=18)
a=1,b=2,c=3,d=4,args=(5,6),kwargs={"name":"jack","age":18}

function paras's transfer:formal para point to actual para's memory block.

python code execute order just like html run from top to bottom:
1:define global variable
2:define function and reference global variable
3:call the function 

print function's manual:
help(funName)

高阶函数：参考廖雪峰的博客
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
reduceI()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数(x1,x2)，reduce把结果继续和序列的下一个元素(x3)做累积计算
filter():和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
sorted():自定义排序规则

函数对象类型的变量，下面有例子：
def fun():
	pass
a = fun
a() --> 可执行

函数作为返回值，下面有例子，参考廖雪峰的博客

装饰器decorator，下面有例子,参考廖雪峰的博客，参考图片decorator1.png

偏函数，参考廖雪峰的博客,当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

"""

def funName():
	print("function body")
funName()

def funName2():
	print("f2")
	return "f2"
funResult2 = funName2()
print(funResult2)

def funName3(a,b):
	print(a+b)
	return a+b
print(funName3(1,2))

#retrun tuple;'return a,b,c' is equivalent to 'return (a,b,c)'. 
def funName4(a,b,c):
	return a,b,c #return (a,b,c)
fun4R = funName4(1,2,3)
print(fun4R)

varg = 10#global variable
def fun5():
	varl = 9#local variable
	print(varg)#reference global variable directly
fun5()

varg2=11
def fun6():
	global varg2#tell anyone this is a global variable,but you can omit this line.
	print(varg2)
fun6()


varg3=12
def fun7():
	#global varg3   can omit this line
	varg3=13#reference global varg3
	print(varg3)
fun7()

#namedPara
def fun8(a,b):
	print(a+b)
fun8(b=1,a=2)
fun8(a=14,b=15)
fun8(16,b=17)
#fun8(a=18,19) error:if have anonymousPara, namedPara must after anonymousPara.

#defaultPara must after necessaryPara.
def fun9(a,b,c=3):
	print(a+b+c)
fun9(1,2)#1+2+3=6
fun9(1,2,4)#1+2+4=7
fun9(1,2,c=4)#1+2+4=7
fun9(a=1,b=2,c=4)#1+2+4=7

def fun10(a,b,c=3,d=4):
	print(a+b+c+d)
fun10(1,2)#1+2+3+4=10
fun10(1,2,d=5)#1+2+3+5=11
fun10(1,2,c=5)#1+2+5+4=12
fun10(1,2,5,6)#1+2+5+6=14
fun10(1,2,c=5,d=6)#1+2+5+6=14

#args-->tuple
#tuple used to complement the front of
def fun11(a,b,c=3,d=4,*args):
	print("a=%d,b=%d,c=%d,d=%d"%(a,b,c,d))
	print(args)
fun11(1,2)#a=1,b=2,c=3,d=4,args=()
fun11(1,2,d=5)#a=1,b=2,c=3,d=5,args=()
fun11(1,2,c=5)#a=1,b=2,c=5,d=4,args=()
#fun11(1,2,c=5,d=6,7,8) error:namedPara must after anonymousPara
fun11(1,2,5,6,7,8)#a=1,b=2,c=5,d=6,args=(7,8)
fun11(1,2,5,6,7)#a=1,b=2,c=5,d=6,args=(7,)
targs=(5,6,7)
print("~~~~~~~~~~~~~~~~~~~~~~~~")
fun11(1,2,*targs)#a=1,b=2,c=5,d=6,args=(7,)  targs used to complement previous all necessaryParas and defaultParas,if which necessaryPara not given,then fetch from targs according order;if which defaultPara not given,don't use default value,but fetch from trags according to order;the rest of element in targs composed to args as a final tuple. 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
fun11(*targs)#a=5,b=6,c=7,d=4,args=()

#kwargs-->dictionary
def fun12(a,b,c=3,d=4,*args,**kwargs):
	print("a=%d,b=%d,c=%d,d=%d"%(a,b,c,d))
	print(args)
	print(kwargs)
fun12(1,2,3,4,5,6,name=7,age=8)#a=1,b=2,c=3,d=4,args=(5,6),kwargs={'name':7,'age':8}
fun12(1,2,3,4,5,6)#a=1,b=2,c=3,d=4,args=(5,6),kwargs={}
fun12(1,2,3,4,name=5,age=6)#a=1,b=2,c=3,d=4,args=(),kwargs={'name':5,'age':6}
fun12(1,2,name=5,age=6)#a=1,b=2,c=3,d=4,args=(),kwargs={'name':5,'age':6}
fun12(1,2)#a=1,b=2,c=3,d=4,args=(),kwargs={}
tupleargs = (5,6)
dictargs={"add":7,"tel":8}
fun12(1,2,3,4,*tupleargs,**dictargs)#a=1,b=2,c=3,d=4,args=(5,6),kwargs={'add':7,'tel':8}
print("**************************")
fun12(1,2,*tupleargs,**dictargs)#a=1,b=2,c=5,d=6,args=(),kwargs={'add':7,'tel':8}
fun12(*tupleargs,**dictargs)#a=5,b=6,c=3,d=4,args=(),kwargs={'add':7,'tel':8}

#函数变量
def myvarfun():
	print("函数变量")
mvr = myvarfun#变量复制
mvr()#可指向，mvr和myvarfun指向同一个函数对象

#函数作为返回值
def myrefun():
	def myinfun():
		print("我是函数，我被返回")
	return myinfun
myin = myrefun()
print(myin)#myin指向对应函数对象的内存地址，<function myrefun.<locals>.myinfun at 0x7f6af4351840>
myin()

print("*****************************装饰器start***************************")
import functools
#装饰器decorator,无参数，now不再指向原来的now函数，而是指向wrapper函数

def log(func):
#	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		print("now函数之前:%s"%func.__name__)#now
		return func(*args,**kwargs)
	return wrapper

@log
def now(a):
	print("now函数,%d"%a)

print("1函数名%s"%now.__name__)#wrapper,如果写@functools.wraps(func)则仍是now
now(110)#now(a)-->wrapper(a)-->log(now)(a)-->now=log(now)-->now==wrapper
print("2函数名%s"%now.__name__)#wrapper,如果写@functools.wraps(func)则仍是now

#装饰器decorator,有参数,cut不再指向原来的cut函数，而是指向wrapper函数
def log(text):
	def decorator(func):
#		@functools.wraps(func)
		def wrapper(*args,**kwargs):
			print("有参数%d，cut函数之前：%s"%(text,func.__name__))
			return func(*args,**kwargs)
		return wrapper
	return decorator

@log(10086)
def cut(b):
	print("cut函数体:%d"%b)

print("3函数名：%s"%cut.__name__)#wrapper,如果写@functools.wraps(func)则仍是cut
cut(120)#cut(120)<-->log(10086)(cut)(120)
print("4函数名：%s"%cut.__name__)#wrapper,如果写@functools.wraps(func)则仍是cut

print("****************************装饰器end*******************************")



'''
引用:just like java
immutable variable:numbers,string,tuple
volatile variable:others are all volatile,eg:list,dictionary
dictionary's key can be any immutalbe variable,but cann't be volatile variable,because volatile have no hashcode,immutable have hashcode.yy
'''
varadd = 10
print(id(varadd))#output variable's memory address

'''
匿名函数:anonymous function
func = lambda paras..:expression
func point to the anonymous function's body.
after ':' must be expression,because anonymous function default have retrun value,the return value is the expression's result.
func = lambda x,y:x+y
func(1,2),the retrun value is x+y.
'''
anonyfunc = lambda x,y:x+y
anonyresult = anonyfunc(1,2)
print(anonyresult)


#custom sort rule:
#give sort() a anonymous function para,this anonymous function have only one para,inner sort() will call this anonymous function and list'seach element will as para transfer into this anonymous function,and this anonymous function's expression will decide the sort rule for list.
mapList1=[{'name':'jace','age':18},{'name':'zs','age':22},{'name':'body','age':90},{'name':'fuck','age':4}]
mapList1.sort(key=lambda kv:kv['name'])
print(mapList1)

#通过input获取匿名函数
#this explained that python is a dynamic language,you never know what code will be run until run it.
#you can input:lambda x,y:x+y
'''
anonf = input("input a anonymous function:")
def testAnonf(a,b,func):
	result = func(a,b)
	print(result)
from sys import version_info
if version_info.major == 2:#python2
	testAnonf(21,22,anonf)
if version_info.major == 3:#python3
	anonf = eval(anonf)#eval():transform general string to python language,eg:make '[1,2,3]' to [1,2,3] and so on.
	testAnonf(31,32,anonf)
'''




'''
operate file's step:
1:open file.
f=open("filePath","fileVisitMode") reference file_visit_mode.png,f point to the file which is opened.if fileVisitMode is 'r' then you cam omit it.and if the filePath is not exist and fileVisitMode is 'r' will report error.
eg:f=open("1.txt","r");f=open("/yzjgogo/home/1.txt","w")

2:operate file.
such as read it,write it.

3:close file.
attention:after operate file finish,you must close it.don't forget it.
f.close()
'''
print("***************file about*****************")
#wirte content into file.
myfile = open("f.txt","w+")
wcon = myfile.write("abcdefghigklmnopqrst")#write("content") return the char count of write into file.after wirte the point move to after the last char.so point at "",the empyt char.
print(wcon)
myfile.close()

#read(count) read() :read content from file.
#open file with "r" mode,the default point of file is at the first char position.
myfile = open("f.txt","r")
print(myfile.read(1))#零,the point move to next char.
print(myfile.read(1))#一,the point move to next char.
print(myfile.read(1))#二,the point move to next char.
print(myfile.read(1))#三,the point move to next char.
print(myfile.read(1))#四,the point move to next char.
print(myfile.read())#五六七八九十,after read the point move to after the last char.so point at "",the empty char.
print(myfile.read(1))#''
myfile.close()

#f.readline()-->from the point,read one line from f and return as a string.
#f.readline(count)-->if this function have para that mean read how many char from current line,attention the you most get all of the char in current line,cann't get char from other line.
myfile = open("./f.txt","r")
print(myfile.readline(13))
print(myfile.read(1))
myfile.close()

#f.readlines()-->all the lines of f composed as a list and return.
myfile = open("./f.txt","r")
print(myfile.readlines())#the point move to the next of the last char.means that point at "",the empty char.
myfile.close

#f.tell()-->tell you where the point is at now,return the index of char in the file's content.attention:the point's position start from 0 not 1
myfile = open("f.txt","r")
print(myfile.tell())
myfile.close()

#set the point's position,with this you can move the point's position anywhere.
#f.seek(offset,from),offset is byte count,so becareful chinese char and in python2 can be negative number but python3 can not.from==0-->at the first char's index;from=1-->at the current position of file;from=2-->at the next postion of the last char "",is empty char
#eg:seek(2,0)-->from the first char move two byte count.
print("&&&&&&&&&&&&&&&&&")
myfile = open("f.txt","r")
myfile.seek(0,0)
print(myfile.tell())
print(myfile.read(1))
myfile.close()

#file and folder
import os
#os.rename("./f.txt","./ff.txt")#change file's name
#os.rename("myfolder","mfolder")#change folder's name
#os.remove("a.txt")
#os.remove("af")#can not delete folder
#os.rmdir("af")#delete folder
#os.mkdir("dir")

#os.chdir("/home/yzjgogo")#change current path
#print(os.getcwd())#get current path
#print(os.listdir("/home/yzjgogo/python"))#get which path's all file name and folder name then composed as a list return.


'''
面向对象OOP

self --> just like java's 'this' keyword,means current object.but maybe it can't ignore?
cls --> class's obj,everyting is object.
super:python2-->super(SonClassName,self);python3-->super() no para
__dict__ --> is an obj's attribute,not a function;it's a dict,used to store self.attr.eg:{'name':'HshiQi','age':8}
class Dog(objec):
	def __init__(self,name,age):
		self.name = name
		self.age = age


just like java's constructor:__new__(cls)(create a obj) and __init__(self)(init created obj)
__new__(cls,...) --> top father object's function.used to create a obj.the para is 'class obj' point to the class.you also can define more para used to give __init__(sefl,...),if you rewrite this function you must return the object which is created by top father's __new__(cls,...)
__init__(self,...) --> top father object's function.call inner __new__(cls),used to init the obj which created through __new__(cls),such as define object's attribute in there.

__str__(self) --> just like java's toString().you must return String.

__repr__(self) --> 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

__iter__(self) --> 参考廖雪峰的博客，配合__next__(self),让对象可以for循环

__getitem__() --> 参考廖雪峰的博客，可以for循环的对象，实现像list那样按下表取元素，参考__iter__(self)

__getattr__() --> 参考廖雪峰的博爱，正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错，要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。 

__call__(self) --> 参考廖雪峰的博客，把实例本身当方法调用。通过callable()函数，我们就可以判断一个对象是否是“可调用”对象.
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
调用方式如下：
>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.



__del__(self) --> when the object have no any variable point at it.this function will be call,and delete the object free the memory.if untill execute all the porgram finish,the object still not delete,this function will be call too.because the porgram finish will free memory apce,so the object will be delete too.

del obj_variable --> make the obj_varibale become undefined,not point at the obj,but the obj still exist. until have no any varibale point at the obj,the obj's __del__() function will be call.

sys.getrefcount(obj_variable) --> return the count of how many varibale point at the obj,the para is the variable of anyone point at the obj.the attention is function's para is a reference of the obj too.so general you should mimus 1.eg:count = sys.getrefcount(obj_variable)-1.

define yourself's function,you must at least transfer into 'self' para.

add instance attribute:
you can add attribute through obj instance,eg:obj.name = "zs",define name attribute and give value.but this just effect with current obj,not effect with other instance.

add instance function:
you can give current instance add a new function,but just effect with this instance,not effect with other instance.
>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25

add class attribute and function,this will effect with all the instance of this class:
>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score

limit all the instances's attributes of the class,but not effect the sonclass's instance:
eg:limit all the instances just can have 'name' and 'age' attribute:
class Student(object):
    __slots__ = ('name', 'age') #use tuple define it.
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'

@property:参考廖雪峰的博客,Python内置的@property装饰器就是负责把一个方法变成属性调用的,广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


private attribute:startwith '__';eg:__name,__secret,you should define setXXX() and getXXX().as a private attribute you just can call it inner an object and through self.xxx call it.

private function:startwith '__';eg:__wank();as a private function you just can call it inner an object and through sefl.__XXX call it.

class attribute:just like java's static attribute,this attribute belong to class,every instance enjoy.you can visit it such as:className.attribute or obj.attribute


class method:just like java's static method,decorate with @classmethod, you must transfer a 'cls' para,means current class's obj,everything is object.you can call it such as:calssName.xxx() or obj.xxx()


static method:just like java's static method,decorate with @staticmethod,no need transfer any para.this also is difference of calssmethod.you can call it such as:calssName.xxx() or obj.xxx()

isinstance(instance, class)判断某个对象实例是不是某个类的类型
eg:dog = Dog()
isinstance(dog,Dog) --> True
也可以判断某个对象是不是多个类型中的一个：
isinstance([], (list, tuple)),判断[]是不是list或tuple中的任意一个

dir(instance):获取对象的所有属性和方法，以list的方式返回，切list的元素都是字符串

定义对象的len(obj)方法:需要在类中定义__len__(self)函数即可。
len(obj) == obj.__len__()

判断对象有没有某个属性或方法以及设置属性
hasattr(obj, '属性名或方法名') 判断有没有该属性或方法，返回true或false
setattr(obj, '属性名', "jack") 添加属性或给属性重新赋值,只给某个对象添加属性，不给类添加
getattr(obj, '属性名或方法名') 获取属性值或方法名,如果不存在则报错
getattr(obj, '属性名或方法名',defaultvalue) 获取属性值或方法名,如果不存在则返回默认值

枚举类:参考廖雪峰的博客。

动态创建类：参考廖雪峰的博客，type()和metaclass元类

'''
class Student(object):

	num = 0 #class attribute:just like java's static attribute,this attribute belong to class,every instance enjoy.

	def __new__(cls,name,age,secret):
		print("execute__new__")
		#return super().__new__(cls)
		return object.__new__(cls)

	def __init__(self,name,age,secret):
		print("call init,and define 'name','age','tools' three attribute")
		self.name = name
		self.age = age
		self.tools = []
		self.__secret = secret#private attribute
		Student.num+=1

	def __str__(self):
		print("call private function:%s"%self.__wank())#through sefl.__XXX call it.
		return "this student's name is %s,age is %d,he have many tools,such as %s"%(self.name,self.age,str(self.tools))

	def __del__(self):
		print("I'm __del__ function")

	def __len__(self):#通过len(obj)调用即可
		return 10010

	def setSecret(self,secret):
		self.__secret = secret#call private attribute through self,and give it value

	def getSecret(self):
		return self.__secret

	def __wank(self):
		return "like wank"

	@classmethod
	def addNum(cls):#class method,you must transfer a cls para,means current class's obj,everything is object.
		cls.num+=10
    
	@staticmethod
	def show():#static method:decorate with @staticmethod,no need transfer any para.this also is difference of calssmethod.
		print("static method")

	#yourself's function,you must at least transfer into 'self' para
	def addTool(self,tool):
		self.tools.append(tool)
	

class Book:
	def __str__(self):
		return "book"
class Pen:
	def __str__(self):
		return "pen"

#create a object and output it.
stu = Student("jack",18,"a secret")#create a stu object
#stu.sex=1 you can add attribute through obj instance
book = Book()#create a book object
pen = Pen()#create a pen object

stu.addTool(book)
stu.addTool(pen)
print(stu)

print("#############dir############")
#dir(obj)
print(dir("ABC"))
print(dir(stu))
print(dir(object))
print(len(stu))
print(stu.__len__())

#属性
print(hasattr(stu,"fuck"))
setattr(stu,"fuck","ok")
print(getattr(stu,"fuck"))
setattr(stu,"fuck","ookk")
print(getattr(stu,"fuck"))
gstu = Student("nikoo",88,"nikoo's secret")
print(getattr(gstu,"fuck","没有fuck属"))#说明setattr()只给某个对象添加属性，不给类添加


#private attribute and private function.
#print(stu.__secret) you cann't call private attribute out object
#print(stu.__wank()) you cann't call private function out object
print("original secret:%s"%stu.getSecret())
stu.setSecret("new secret")
print("new secret:%s"%stu.getSecret())

#del reference
#stu,stua,stub,stuc all point at the same obj.
import sys
stua = stu
stub = stua
stuc = stub
print("current obj's reference count:%d"%(sys.getrefcount(stu)-1))#4,stu stua stub stuc
del stuc#after del the variable will be undefined
print("current obj's reference count:%d"%(sys.getrefcount(stu)-1))#4,stu stua stub 
del stub
print("current obj's reference count:%d"%(sys.getrefcount(stu)-1))#4,stu stua 
del stua
print("current obj's reference count:%d"%(sys.getrefcount(stu)-1))#4,stu 
del stu#after del stu,no variable point the obj,so will call __del__() function delete the obj.
print("*******invider********")
#if until execute all code the obj still not be del,the __del() will be call too,because the program release the memory space the obj del too.

#class attribute
print("*********calss attribute********")
stud = Student("jack",18,"a secret")
print(stud.num)
print(Student.num)

#class method
Student.addNum()
print(Student.num)
print(stud.num)

#static method
Student.show()
stud.show()

print(isinstance(stud,Student))#True

'''
继承

super:python2-->super(SonClassName,self);python3-->super() no para

the 'object' is all obj's top father class.

son can rewrite father's function,just need hava the same name,no need have the same paras.

call father's funciton have two ways:
Father.XXX(self)
super().XXX() you don't need transfer self para.if you transfer will report error.

private attribute can't be extend,but you can through public function indirect call it.
private function can't be extend,but you can through public function indirect call it.


'''
class Animal(object):#(object) can ignore.
	def __init__(self):
		self.__name = "jack"#private attribute

	def __wank(self):#private function
		print("can wank")

	def getName(self):
		return self.__name

	def callWank(self):
		self.__wank()

	def eat(self):
		print("Animal can eat food")

	def run(self,a,b,c):
		print("Animal can run")

class Dog(Animal):
	def bark(self):
		print("Dog can bark")

	def eat(self):#rewrite father's function
		Animal.eat(self)#call father's function
		print("Dog can eat food too")

	def run(self,d):#rewrite father's function,just need have the same function name,no need have the same paras.
		if version_info.major == 2:#python2
			super(Dog,self).run(1,2,3)
		if version_info.major == 3:#python3
			super().run(1,2,3)#call father's function,you don't need transfer self para,if you transfer will report error.
		print("Dog can run too %s"%d)

mydog = Dog()
mydog.eat()
mydog.run("hahaha")
#print(mydog.__name) private attribute can't be extend,but you can through public function indirect call it.
print(mydog.getName())
#mydog.__wank() private function can't be extend,but you can through public function indirect call it.
mydog.callWank()

'''
多继承:most of the feature are the same of single extend,multi parent not affect each other.
multi parent should best have no the same function.

class.__mro__ : return the call order,just like the extend order,if multi parent have the same function,then call according to the call order.eg:C-->A-->B-->object,if classA and classB have the same function 'test()',then if you execute 'c.test()',in fact execute A's test() not B's test().
'''
class A(object):
    def testA(self):
        print("testA")

class B(object):
    def testB(self):
        print("testB")

class C(A,B):
    pass

objc = C()
objc.testA()
objc.testB()
print(C.__mro__)#the call order is:C--A--B--object


'''
所谓多态就是指程序中定义的引用变量所指向的具体类型和通过该引用变量发出的方法调用在编程时并不确定，而是在程序运行期间才确定，即一个引用变量倒底会指向哪个类的实例对象，该引用变量发出的方法调用到底是哪个类中实现的方法，必须在由程序运行期间才能决定。因为在程序运行时才确定具体的类，这样，不用修改源程序代码，就可以让引用变量绑定到各种不同的类实现上，从而导致该引用调用的具体方法随之改变，即不修改程序代码就可以改变程序运行时所绑定的具体代码，让程序可以选择多个运行状态，这就是多态性。

      比如你是一个酒神，对酒情有独钟。某日回家发现桌上有几个杯子里面都装了白酒，从外面看我们是不可能知道这是些什么酒，只有喝了之后才能够猜出来是何种酒。你一喝，这是剑南春、再喝这是五粮液、再喝这是酒鬼酒….在这里我们可以描述成如下：

            酒 a = 剑南春

            酒 b = 五粮液

            酒 c = 酒鬼酒

             …

 这里所表现的的就是多态。剑南春、五粮液、酒鬼酒都是酒的子类，我们只是通过酒这一个父类就能够引用不同的子类，这就是多态——我们只有在运行的时候才会知道引用变量所指向的具体实例对象。
'''



'''
单例模式:single instance
all objs created by this class is point at the same memory space.
'''
class Bear(object):
	__instance = None
	__init_flag = False
	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	
	def __init__(self,name):#just init once
		if Bear.__init_flag == False:
			self.name = name
			Bear.__init_flag = True
			
	def show(self):
		print("sefl.name=%s"%self.name)

bear = Bear("dog bear")
print(id(bear))
bear2 = Bear("beiji bear")
print(id(bear2))
bear.show()
bear2.show()


'''
异常
Exception is all errors's top father class.

at the same time catch multi error:
python2:Error1,Error2;
python3:(Error1,Error2),in fact is a tuple.

no mater what error just catch it:
python2:except: that's all. but except Exception is OK? take care about it.
python3:except Exception.


except Error as result:
catch an error and get it's obj,you can output it.

raise xxxError:used to throw a error.
raise: after catch the error throw it again

else:
if have no any error will execute it.

finally:
no mater what,'finally' will run always.
'''
if version_info.major == 2:#python2
	print("this is python2")
'''
	try:
		#mynum+=1
		#open("fuck.txt")
		#11/0
		print("code")
	except NameError:
		print("******NameError******")
	except ZeroDivisionError:
		print("********ZeroDivisionError************")
	except IOError as result:#result point at the error obj.
		print("**********IOError**************")
		print(result)
	except NameError,IOError:#python2,split with , not a tuple
		print("**********multi error************")
	except:#python2 catch all errors,just :
		print("catch all the errors")
	else:# if no any error,'else' will run.
		print("no any error")
	finally:#no mater what,'finally' will run always.
		print("finally execute aways")
'''
if version_info.major == 3:#python3
	print("this is python3")
	try:
		#mynum+=1
		#open("fuck.txt")
		#11/0
		print("code")
	except NameError:
		print("******NameError******")
		#raise    after catch the error throw it again
	except ZeroDivisionError:
		print("********ZeroDivisionError************")
	except IOError as result:#result point at the error obj.
		print("**********IOError**************")
		print(result)
	except (NameError,IOError):#python3,catch multi a tuple
		print("**********multi error************")
	except Exception:#python3 catch all errors.
		print("catch all the errors")
	else:# if no any error,'else' will run.
		print("no any error")
	finally:#no mater what,'finally' will run always.
		print("finally execute aways")



'''
自定义异常
Exception is all error's top father class.
raise xxxError:used to throw a error.
raise: after catch the error throw it again
'''

class MyError(Exception):
	def __init__(self,errorContent):
		self.error = errorContent

	def __str__(self):
		return self.error

#use you diy erro
try:
	myerror = MyError("you are error") 
	raise myerror
except Exception as res:
	print(res)
	#raise   after catch the error throw it again


'''
模块：module
import random --> random is a module,when you import the module will execute all it's code.

install a module: eg,'pygame' is a popular module 
python2:sudo pip install moduleName
python3:sudo pip3 install moduleName
after install finished,import moduleName and use it.

if you import custom module,current path will generate a '__pycache__' folder,inner this folder have the cache of the module which you just imported.inner the '__pycache__' have the file like 'module1.cpython-34.pyc'.this is a bytecode file also a binary file.among 'module1.cpython-34.pyc' 'cpython' means python interpreter is code by C lanugage,and python's version is 3.4.In fact,when execute python *.py,if *.py import some module,then interpreter will make these module into 'moduleName.cpython-version.pyc' as binary.if you run *.py again then just need read from 'moduleName.cpython-version.pyc',so will very save time,because as a module usual have no problem.

__name__:
inner a module you can through '__name__' judge what status when this module is running.reference module1.py
if current module run as a independent program '__name__' is '__main__'
if current module as a module run depend on other *.py,'__name__' is current module's name.

__all__:is a list,reference module4.py
if you use 'from module4 import *' import a module, inner the module you can through '__all__' store functions or classes which is can be call in main program.notice:if you use 'import module4' then '__all__' is useless.

包package:package folder contain __init__.py,module5.py,module6.py...some module file,inner __init__.py you shoule define __all__=["module5","module6"] make these modules go into effect.when you 'from packageName import *' the __init__.py will execute all itself code,and you can through 'module5.test5()' call module's functions and classes.maybe have other use way.

module publish,install,useage:reference module_publish.png,module_install_use.png
'''
#moduleName.__file__ --> return current module's path
print(random.__file__)#/usr/lib/python3.4/random.py

#import yourself module
#way1 recommed!
import module1
module1.testM1()

#way2 or you can:
#from module import test1,test2
#from module import *
#not recommend because maybe some module have the same function name.
from module2 import testM2
testM2()

#way3 give target module a alias
import module3 as mm
mm.testM3()

#__all_=["Test","test1"] --> see annotation
from module4 import *
myt = Test()
myt.test()
test1()
#test2() error:because __all__ not contain 'test2'


#包package,meybe have other use way.
from package5 import *
module5.test5()


'''
program's paras
import sys

python3 base.py
sys.argv --> ['base.py']
python3 base.py a b c
sys.argv --> ['base.py','a','b','c']

'''
print(sys.argv)


'''
range
'''




