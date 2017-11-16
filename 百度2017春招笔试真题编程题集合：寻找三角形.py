'''
[编程题] 寻找三角形
时间限制：1秒
空间限制：32768K
三维空间中有N个点，每个点可能是三种颜色的其中之一，三种颜色分别是红绿蓝，分别用'R', 'G', 'B'表示。 
现在要找出三个点，并组成一个三角形，使得这个三角形的面积最大。
但是三角形必须满足：三个点的颜色要么全部相同，要么全部不同。 
输入描述:
首先输入一个正整数N三维坐标系内的点的个数.(N <= 50) 

接下来N行，每一行输入 c x y z，c为'R', 'G', 'B' 的其中一个。x，y，z是该点的坐标。(坐标均是0到999之间的整数)


输出描述:
输出一个数表示最大的三角形面积，保留5位小数。

输入例子1:
5
R 0 0 0
R 0 4 0
R 0 0 3
G 92 14 7
G 12 16 8

输出例子1:
6.00000
'''

'''
解题思路：三角形知识
  在处理几何问题时一定要仔细小心，比如三角形三条边中的最大边一定要小于另外两边之和，否则构不成三角形
  计算面积时候可以使用秦九韶公式可以极大简化代码，使代码更加优雅
  这道题数据量比较少，如果数据量大的话，本方法O(n^3)次方的复杂度很难全部通过测试
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

import math

n = int(input())

c_cords = []
for i in range(n):
    temp = input().split()
    c_cords.append([temp[0]])
    c_cords[i].extend([int(temp[j]) for j in range(1, 4)])


def get_dis(p1, p2):
    return math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 + (p1[3]-p2[3])**2)


def get_area(p1, p2, p3):
    a = get_dis(p1, p2)
    b = get_dis(p2, p3)
    c = get_dis(p1, p3)
    p = (a + b + c) / 2
    t = p*(p-a)*(p-b)*(p-c)
    if t > 0:
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return 0

R = []
G = []
B = []
for each in c_cords:
    if each[0] == 'R':
        R.append(each)
    elif each[0] == 'G':
        G.append(each)
    else:
        B.append(each)


def get_same_color_tri(color):
    temp_area = []
    length_c = len(color)
    for x in range(n-2):
        for y in range(x+1, n-1):
            for z in range(y+1, length_c):
                temp_area.append(get_area(color[x], color[y], color[z]))
    return temp_area


def get_diff_color_tri(c1, c2, c3):
    temp_area = []
    for each1 in c1:
        for each2 in c2:
            for each3 in c3:
                temp_area.append(get_area(each1, each2, each3))
    return temp_area

area = [0]
if len(R) > 2:
    area.extend(get_same_color_tri(R))
if len(G) > 2:
    area.extend(get_same_color_tri(G))
if len(B) > 2:
    area.extend(get_same_color_tri(B))

if R and G and B:
    area.extend(get_diff_color_tri(R, G, B))

print('%.5f' % max(area))
