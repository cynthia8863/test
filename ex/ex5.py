#coding=UTF-8

my_name = u'提拉米苏'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = u'蓝色'
my_teeth = u'白色'
my_hair = u'棕色'

print "Let's talk about %s." %my_name
print "她有 %d 英尺高。" %my_height
print "He's %d pounds heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
'''
Result:
Let's talk about 提拉米苏.
她有 74 英尺高。
He's 180 pounds heavy.
Actually that's not too heavy.
He's got 蓝色 eyes and 棕色 hair.
His teeth are usually 白色 depending on the coffee.
If I add 35, 74, and 180 I get 289.

'''