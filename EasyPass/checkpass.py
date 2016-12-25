#coding=utf-8
import re

#编译正则表达式
NUMBER = re.compile(r'[0-9]')
LOWER_CASE = re.compile(r'[a-z]')
UPPER_CASE = re.compile(r'[A-Z]')
OTHERS = re.compile(r'[^0-9a-zA-Z]')

#加载常见的密码
def load_common_password():
    words = []
    with open('password.txt', 'rb') as f:
        for word in f.readlines():
            words.append(word.strip())
    return words

COMMON_WORDS = load_common_password()

#定义类输出信息
class Strength:
    def __init__(self, valid, strength, message):
        self.valid = valid
        self.strength = strength
        self.message = message
	print "["+self.strength+":"+self.message+"]"

#封装一个密码类
class Password:
    #密码等级	
    TERRIBLE = 0
    SIMPLE = 1
    MEDIUM = 2
    STRONG = 3
    
    #是否是相邻按键
    @staticmethod
    def is_regular(input):
        reverse = input[::-1]
        regular = ''.join(['qwertyuio', 'asdfghjkl', 'zxcvbnm'])
        return input in regular or reverse in regular
   
    #是否是相邻字母
    @staticmethod
    def is_by_step(input):
        delta = ord(input[1]) - ord(input[0])

        for i in range(2, len(input)):
            if ord(input[i]) - ord(input[i-1]) != delta:
                return False

        return True

    #是否在常见列表
    @staticmethod
    def is_common(input):
        return input in COMMON_WORDS

    #魔术方法方便调用
    def __call__(self, input, min_length=6, min_types=3, level=STRONG):
	
	#密码过于简单未通过
        if len(input) < min_length:
            return Strength(False, 'terrible', '密码太短了')

        if self.is_regular(input) or self.is_by_step(input):
            return Strength(False, 'simple', '密码有规则')

        if self.is_common(input):
            return Strength(False, 'simple', '密码很常见')
	
	#密码强度通过划分等级
        types = 0

        if NUMBER.search(input):
            types += 1

        if LOWER_CASE.search(input):
            types += 1

        if UPPER_CASE.search(input):
            types += 1

        if OTHERS.search(input):
            types += 1

        if types < 2:
            return Strength(level <= self.SIMPLE, 'simple', '密码太简单了')

        if types < min_types:
            return Strength(level <= self.MEDIUM, 'medium', '密码不错，但还不够强')

        return Strength(True, 'strong', '完美的密码')

password = Password()
