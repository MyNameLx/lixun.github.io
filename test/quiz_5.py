# Written by *** for COMP9021
#
# Prompts the user for two capitalised strings of letters, #提示用户输入两个大写的字母字符串，
# say s1 and s2, then for two years in the range 1947--2021, #比如说 S1 和 S2，然后在 1947--2021 范围内两年，
# say Y1 and Y2, with s1 and s2 and with Y1 and Y2 being separated #假设 Y1 和 Y2，其中 s1 和 s2 以及 Y1 和 Y2 分开
# by at least one space, and with possibly any extra spaces #至少一个空格，并且可能带有任何额外的空格
# beween s1 and s2, between Y1 and Y2, at the start of either input, #在 S1 和 S2 之间，在 Y1 和 Y2 之间，在任一输入的开头，
# and at the end of either input. #并在任一输入的末尾。
# - s1 can be lexicographically smaller than or equal to s2 #S1 在字典上可以小于或等于 S2或者相反
#   or the other way around;
# - Y1 can be smaller than or equal to Y2 or the other way around. #Y1 可以小于或等于 Y2，或者相反。
#
# Outputs an error message if input is incorrect. #如果输入不正确，则输出错误消息。
# Otherwise, finds out amongst the first name that starts with s1 #否则，在以 s1 开头的名字中找出
# and the last name that starts with s2, which name has been given #以及以 S2 开头的姓氏，该名称已被赋予
# as both a female name and a male name in a year between Y1 and Y2 #在Y1和Y2之间的一年中同时包括女性名字和男性名字
# included. If there is such a name and year, then outputs all such #如果有这样的名称和年份，则输出所有此类名称和年份的绝对值之差
# names and years for which the absolute value of the difference
# between
# - the ratio defined as the count of the name as a female name
#   in that year over the count of all female names in that year,
# - the ratio defined as the count of the name as a male name
#   in that year over the count of all male names in that year,
# is minimal (so essentially, the popularities in that year
# of the name as a female name and of the name as a male name
# are as close as possible).
# Outputs the name, the year, and both ratios as percentages
# printed out with 5 digits after the decimal point.
# In case there are many solutions (that is, same minimal
# difference in popularities), then outputs all solutions
# in increasing lexicographic order of names, and for
# a given name, in increasing lexicographic order of years.
#
# The directory named names is stored in the working directory.
#
# IF YOU USE ABSOLUTE PATHS, YOUR PROGRAM CAN ONLY FAIL TO RUN PROPERLY
# ON MY MACHINE AND YOU WILL SCORE 0 TO THE QUIZ, WITH NO CHANCE FOR YOU
# TO FIX THIS MISTAKE AFTER RESULTS HAVE BEEN RELEASED.
#
# YOU CANNOT USE pandas FOR THIS QUIZ; IF YOU DO, YOU WILL SCORE 0
# TO THE QUIZ.
# 提示用户输入两个大写字母字符串，例如 s1 和 s2，然后输入 1947--2021 范围内的两年，例如 Y1 和 Y2，
# 其中 s1 和 s2 并且 Y1 和 Y2 至少由一个空格分隔，并且s1 和 s2 之间、Y1 和 Y2 之间、任一输入的开头以及任一输入的末尾可能有任何额外空格。
# - s1 按字典顺序可以小于或等于 s2，反之亦然；
# - Y1 可以小于或等于 Y2，反之亦然。
# 如果输入不正确则输出错误信息。
# 否则，找出以 s1 开头的名字和以 s2 开头的姓氏中，在 Y1 和 Y2 之间的一年中，哪个名字同时被指定为女性名字和男性名字。如果存在这样的名称和年份，则输出所有这样的名称和年份，其差值的绝对值
# - 定义为当年女性姓名数量与当年所有女性姓名数量的比率，
# - 定义为当年男性名字的数量与当年所有男性名字的数量的比率是最小的（所以本质上，该年女性名字的受欢迎程度和名字尽可能接近男性名字）。
# 以百分比形式输出名称、年份和两个比率
# 打印出小数点后 5 位数字。
# 如果有许多解决方案（即流行度差异最小），则按名称的字典顺序递增输出所有解决方案，对于给定的名称，按年份的字典顺序递增输出所有解决方案。
# 工作目录中存放名为names的目录。
# 如果您使用绝对路径，您的进程只能无法在我的机器上正常运行，您的测验得分为 0，并且在结果发布后您没有机会修复此错误。


from collections import defaultdict
from pathlib import Path
import csv
import os


# INSERT YOUR CODE HERE
def panduan_zifu(letters):
    if len(letters) !=2:
        return False
    s1,s2 = letters[0],letters[1]
    if (len(letters) == 2 and s1[0].isupper() and s1[1:].islower() and s1.isalpha()):
#长度为2且第一个字符串的首字母为大写，第一个字符串以后的字母为小写
        return True
    if (len(letters) == 2 and s2[0].isupper() and s2[1:].islower() and s2.isalpha()):
        return True
#长度为2且第二个字符串的首字母为大写，第二个字符串以后的字母为小写
    return False

def shuru_panduan():
    letters = input("Enter two capitalised strings of letters:").split()
    if not panduan_zifu(letters):
        print("Incorrect input, leaving it there.")
        return None
#判断是否满足前面判断字符的def，不满足的话输出报错信息
    years = input("Enter two integers between 1947 and 2021:").split()
    Y1, Y2 = int(years[0]), int(years[1])
    s1,s2 = letters[0],letters[1]
    if (len(years) !=2 or Y1 < 1946 or Y2 >2020):
        print("Incorrect input, leaving it there.")
        return False
    
    if s1 == s2:
        print("No name was given as both female and male names.")
        return

    if s2 < s1:
        s1,s2 = s2,s1
    if Y2 < Y1:
        Y1,Y2 = Y2,Y1

#eg.s1=Pau s2=Carr,s1s2 change
    min_dic = 1
    final = []
    my_dic_shaixuan = {}
    for year in range(Y1,Y2 + 1):
    #Y2是被包含的，所以要+1包括在内，设置循环结构
        male,female =0,0
        my_dic = {}
        folder_name, file_name = "names", "yob" + str(year) +".txt"
        if not os.path.exists((os.path.join(folder_name, file_name))):
        #检查文件是否存在，os.path.join(folder_name, file_name)先将文件夹名称和文件名连接起来，以创建完整的文件路径
        #os.path.join()合并路径，确保生成正确的路径
        #os.path.exists(）接受一个文件路径作为参数，如果该文件存在，返回True
            print(f"Incorrect input, leaving it there.")
            return
        male, female = 0, 0
        my_dic = {}
        with open(folder_name + "/" + file_name) as file:
            data = file.read().split("\n")
        for read in data:
            read_data = read.split(",")
            if len(read_data) >= 3:
                name, gender, number = read_data[0], read_data[1], read_data[2]
                if len(read_data) !=3 or read_data[2] == "":
                    continue
                if gender == "M":
                    male = int(number) + male
                elif gender == "F":
                    female = int(number) + female
                if (s1 <= name <= s2) or name.startswith(s2):
                    my_dic[(name,year)] = my_dic.get((name,year), []) + [int(read_data[2])] #赋值到my_dic
        for shaixuan in my_dic.keys():
            if len(my_dic[shaixuan]) == 2:
                female_ratio = my_dic[shaixuan][0] / female
                male_ratio = my_dic[shaixuan][1] / male
                my_dic_shaixuan[shaixuan] = [female_ratio, male_ratio]
                #my_dic_shaixuan[shaixuan] = [my_dic[shaixuan][0] / female, my_dic[shaixuan][1] / male]
                #count for boys and girls(在该年份（由 shaixuan 键表示）中，与当前名称相关的女性名字的数量除以所有女性名字的数量。)
        #print(my_dic_shaixuan)
        min_dic = 1
        for shaixuan in my_dic_shaixuan:
            differences = abs(my_dic_shaixuan[shaixuan][0] - my_dic_shaixuan[shaixuan][1])  # 求绝对值
            if differences < min_dic:
                min_dic = differences
                final = [(shaixuan, my_dic_shaixuan[shaixuan])]
            elif differences == min_dic:
                final.append((shaixuan, my_dic_shaixuan[shaixuan]))

    if len(final) == 0:
        print(f"No name was given as both female and male names.")
    else:
        for result in final:
            name = result[0][0]
            year = result[0][1]
            female_ratio = result[1][0]
            male_ratio = result[1][1]
            print(f"Here are the names that were given as both")
            print(f"female and male names, for the smallest difference")
            print(f"of ratio as a female name over all female names")
            print(f"and ratio as a male name over all male names,")
            print(f"for the years when that happened:")
            print(f"  {name} in {year}, for ratios of")
            print(f"    - {female_ratio:.5%} as a female name")
            print(f"    - {male_ratio:.5%} as a male name.")
                #print(Y1,Y2)
shuru_panduan()