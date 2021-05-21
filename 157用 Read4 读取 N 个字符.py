"""
给你一个文件，并且该文件只能通过给定的 read4 方法来读取，请实现一个方法使其能够读取 n 个字符。

read4 方法：

API read4 可以从文件中读取 4 个连续的字符，并且将它们写入缓存数组 buf 中。

返回值为实际读取的字符个数。

注意 read4() 自身拥有文件指针，很类似于 C 语言中的 FILE *fp 。

read4 的定义：

参数类型: char[] buf4
返回类型: int

注意: buf4[] 是目标缓存区不是源缓存区，read4 的返回结果将会复制到 buf4[] 当中。
下列是一些使用 read4 的例子：


File file("abcde"); // 文件名为 "abcde"， 初始文件指针 (fp) 指向 'a'
char[] buf4 = new char[4]; // 创建一个缓存区使其能容纳足够的字符
read4(buf4); // read4 返回 4。现在 buf4 = "abcd"，fp 指向 'e'
read4(buf4); // read4 返回 1。现在 buf4 = "e"，fp 指向文件末尾
read4(buf4); // read4 返回 0。现在 buf = ""，fp 指向文件末尾
read 方法：

通过使用read4方法，实现read方法。该方法可以从文件中读取 n 个字符并将其存储到缓存数组buf 中。您不能直接操作文件。

返回值为实际读取的字符。

read的定义：
参数类型:   char[] buf, int n
返回类型:   int

注意: buf[] 是目标缓存区不是源缓存区，你需要将结果写入 buf[] 中。

示例 1：
输入： file = "abc", n = 4
输出： 3
解释： 当执行你的 read 方法后，buf 需要包含 "abc"。 文件一共 3 个字符，因此返回 3。 注意 "abc" 是文件的内容，不是 buf 的内容，buf 是你需要写入结果的目标缓存区。

示例 2：
输入： file = "abcde", n = 5
输出： 5
解释： 当执行你的 read 方法后，buf 需要包含 "abcde"。文件共 5 个字符，因此返回 5。

示例 3:
输入： file = "abcdABCD1234", n = 12
输出： 12
解释： 当执行你的 read 方法后，buf 需要包含 "abcdABCD1234"。文件一共 12 个字符，因此返回 12。

示例 4:
输入： file = "leetcode", n = 5
输出： 5
解释： 当执行你的 read 方法后，buf 需要包含 "leetc"。文件中一共 5 个字符，因此返回 5。

提示：
你不能直接操作该文件，文件只能通过 read4获取而不能通过 read。
read函数只在每个测试用例调用一次。
你可以假定目标缓存数组buf 保证有足够的空间存下 n 个字符。
"""


"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        real_n = 0
        cache = [' '] * 4

        while n > real_n:
            if n - real_n >= 4:
                cache_len = read4(cache)
                buf[real_n:real_n+cache_len] = cache[:cache_len]
                real_n += cache_len
                if cache_len < 4 or real_n == n:
                    return real_n
            else:
                cache_len = read4(cache)
                if cache_len < n - real_n:
                    buf[real_n:real_n+cache_len] = cache[:cache_len]
                    real_n += cache_len
                    return real_n
                else:
                    buf[real_n:n] = cache[:n-real_n]
                    return n


def read4(cache):
    """

    :param cache:
    :return:
    """
    cache_len = 0
    return cache_len
