'''
[编程题] 度度熊回家
时间限制：1秒
空间限制：32768K
一个数轴上共有N个点，第一个点的坐标是度度熊现在位置，第N-1个点是度度熊的家。
现在他需要依次的从0号坐标走到N-1号坐标。
但是除了0号坐标和N-1号坐标，他可以在其余的N-2个坐标中选出一个点，并直接将这个点忽略掉，
问度度熊回家至少走多少距离？ 
输入描述:
输入一个正整数N, N <= 50。

接下来N个整数表示坐标，正数表示X轴的正方向，负数表示X轴的负方向。绝对值小于等于100


输出描述:
输出一个整数表示度度熊最少需要走的距离。

输入例子1:
4
1 4 -1 3

输出例子1:
4
'''

'''
解题思路：简单
  遍历去掉除首尾的任意一个点（利用切片操作），然后用新得到的列表获取距离值，遍历完成后，输出最小的距离值即可
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
cords = [int(each) for each in input().split()]


def get_dis(c):
    length = len(c)
    dis = 0
    for j in range(1, length):
        dis += abs(c[j] - c[j-1])
    return dis

print(min([get_dis(cords[:i]+cords[i+1:]) for i in range(1, n-1)]))
