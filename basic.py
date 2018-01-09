# input与print
# user = input('请输入你的名字:');
# print('你好:',user);
# input ("Please Enter:");

#字符串
#转义符\
print('1\\234566');
#当一句话转义太多时可以前面加r，则里面就不需要再\表示转义，会默认转义
print(r'1\2\3\4\5\6');
print(r'Hello,"Lisa!"')
#以下两种方式都可以进行黄航
print('aa\nbb\ncc');
print('''aa
bb
cc''');
print(r'''Hello,"a"
Lisa!''')


#布尔值(注意大小写,和js不同)
print(True);
print(False);
boolean = 1 > 2;
print(boolean);
#python里and表示&&or表示||not表示not
print(not boolean);

#变量
a = 'ABC'
b = a
a = 'XYZ'
#结果是ABC跟js一样 a指向ABC b指向a指向的ABC a重新指向到XYZ 最后b还是指向ABC
print(b)

#常量（通常用全部大小表示，但python并没有任何机制保证PI不被改变，只是习惯上全部大写表示常量，这和ES6之前一样，ES6用const表示常量）
PI = '3.1415926'

#运算
#以下结果等于6 称为地板除 相当于是向下取整
print(20 // 3);

#字符编码
#ord()单个字符转Unicode对应的数字	chr()数字转字符
print(ord('a'));
print(ord('中'));
print(ord('文'));
print(chr(20013));
#'\u4e2d\u6587' 就是中文对应的Unicode编码的20013和25991的16进制u4e2d和u6587
print('\u4e2d\u6587');
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
byt = b'ABC';
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))
#errors='ignore'可以忽略bytes中部分错误的字节
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore'))
#从下面长度中可以得出1个中文字符经过utf-b编码后占3字节 1个英文字符占1个字符
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

#格式化 我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
#%4d 表示至少显示4位数，不够则空格来凑;%04d 表示至少显示4位数，不够则添0;%.2f 表示保留小数点后2位小数
print('亲爱的%s你好！你%0d月的话费是%.2f元'%('李严',9,123.4))
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('%d%%' %(7))
#format()格式化 它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print('{0},成绩提升了{1:.1f}%'.format('小明',7.86));

#list(相当于数组)
array = ['ab','cd','ef'];
print(array);
print(array[0]);
print(len(array));
#取最后一个索引，带负号取倒数第几个（js不能这样）
print(array[-1]);
#数组末尾追加（相当于js的push）
array.append('gh');
print(array)
#指定位置添加（类似于js的splice(n,0,'a'),js没有直接的方法,可以自己添加,
#Array.prototype.insert = function(index,text) {
#	this.splice(index,0,text)
#}
#这样就可以和python一样有insert方法
array.insert(1,'Jack')
print(array)
#默认删除最后一个索引对应的内容,array.pop(arg)可指定需要删除内容的索引
array.pop()

#tuple 类似list 只是tuple定义后就不能改变，没有append，pop这些方法，只能读取
tup = ('ab','cd','ef')
print(tup)

#条件判断
#使用时需要导入相关模块
import random,math
#input返回的输str所以这里要转换成int类型
# user = int(input('1.石头;2.剪刀;3.布'));
# computer = math.ceil(random.random()*3);
# #1=石头 2=剪刀 3=布
# if user==computer:
# 	result =  '打平'
# elif (user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1):
# 	result =  '你赢了'
# else:
# 	result = '电脑赢了'
# print(result)
# input('exit')
#python没有===
print(1=='1')

#循环 for in 和 while
array_b = [1,2,3,4,5]
for a in array_b:
	print(a)
#生成整数序列(以下会生成一个0-99的数组)
list(range(100))
num = 0;
while num < 10 :
	num = num + 1
	print(num)
#break 跳出循环 continue 跳出当次循环

#字典（js的对象）
maps = {'a':75,'b':88,'c':89}
maps['c'] = 90
print(maps['c'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('as' in maps)
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(maps.get('as','指定的值'))
#删除key
maps.pop('a')
#set set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1,2,3])
s2 = set([1,2,3])
s.add('s')
s.remove(1)
print(s)
print(s & s2)
print(s | s2)