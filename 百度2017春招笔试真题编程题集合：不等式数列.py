'''
[编程题] 不等式数列
时间限制：1秒
空间限制：32768K
度度熊最近对全排列特别感兴趣,对于1到n的一个排列,
度度熊发现可以在中间根据大小关系插入合适的大于和小于符号(即 '>' 和 '<' )使其成为一个合法的不等式数列。
但是现在度度熊手中只有k个小于符号即('<'')和n-k-1个大于符号(即'>'),
度度熊想知道对于1至n任意的排列中有多少个排列可以使用这些符号使其为合法的不等式数列。 
输入描述:
输入包括一行,包含两个整数n和k(k < n ≤ 1000)


输出描述:
输出满足条件的排列数,答案对2017取模。

输入例子1:
5 2

输出例子1:
66
'''

'''
解题思路：动态规划
  用i表示当前有几个数，用j表示在当前i个数构成的全排列中，有j个‘<’号
  dp[i][j]表示：当前i个数中有j个‘<’的全排列有多少种
  例如dp[2][0] = 1, dp[2][1] = 1, 表示当前两个数1,2，在1和2构成的全排列的所有组合中，没有小于号的组合有1种
  即：2>1，有1个小于号的组合有1种，即：1<2
  那么如何获得dp[i][j]呢？
  可以通过四种途径获得dp[i][j]
  一：新增加的数字放在原数列的最左侧：
    如新增加3，原数列为1,2，那么无论原数列怎么排列，在左侧加上3后都相当于新加了一个大于号
  二：新增加的数字放在原数列最右侧：
    如新增加3，原数列为1,2，那么无论原数列怎么排列，在右侧加上3后都相当于新加了一个小于号
  三：新增加的数字放在原数列中小于号的位置
    如新增加3，原数列为1,2，那么无论数列中的其他数字怎么排列，在小于号的位置上放3后都相当于新加了一个大于号
  四：新增加的数字放在原数列中大于号的位置
    如新增加3，原数列为2,1，那么无论数列中的其他数字怎么排列，在大于号的位置上放3后都相当于新加了一个小于号
  上述四种关系换算成对应数学上的关系，可如下表示
  一：dp[i][j] += dp[i-1][j]
  二：dp[i][j] += dp[i-1][j-1]
  三：dp[i][j] += dp[i-1][j] * j
  四：dp[i][j] += dp[i-1][j-1] * (j-1)
  即：dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j] * j + dp[i-1][j-1] * (j-1)
  算法细节不多赘述，具体实现看下面代码
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n, k = [int(each) for each in input().split()]

dp = [1, 0]

for i in range(2, n+1):
    new_dp = [1] + [0] * i
    for j in range(1, i):
        new_dp[j] = dp[j] + dp[j-1] + dp[j]*j + dp[j-1]*(i-j-1)
    dp = new_dp

print(dp[k] % 2017)
