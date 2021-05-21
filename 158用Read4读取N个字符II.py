"""
给你一个文件，并且该文件只能通过给定的 read4 方法来读取，请实现一个方法使其能够读取 n 个字符。注意：你的 read 方法可能会被调用多次。

read4 的定义：

read4 API 从文件中读取 4 个连续的字符，然后将这些字符写入缓冲区数组 buf4 。

返回值是读取的实际字符数。

请注意，read4() 有其自己的文件指针，类似于 C 中的 FILE * fp 。

参数类型: char[] buf4
返回类型: int

注意: buf4[] 是目标缓存区不是源缓存区，read4 的返回结果将会复制到 buf4[] 当中。
下列是一些使用 read4 的例子：



File file("abcde"); // 文件名为 "abcde"， 初始文件指针 (fp) 指向 'a'
char[] buf4 = new char[4]; // 创建一个缓存区使其能容纳足够的字符
read4(buf4); // read4 返回 4。现在 buf4 = "abcd"，fp 指向 'e'
read4(buf4); // read4 返回 1。现在 buf4 = "e"，fp 指向文件末尾
read4(buf4); // read4 返回 0。现在 buf4 = ""，fp 指向文件末尾
read 方法：

通过使用 read4 方法，实现 read 方法。该方法可以从文件中读取 n 个字符并将其存储到缓存数组 buf 中。您 不能 直接操作文件。

返回值为实际读取的字符。

read 的定义：

参数:   char[] buf, int n
返回值: int

注意: buf[] 是目标缓存区不是源缓存区，你需要将结果写入 buf[] 中。
 

示例 1：

File file("abc");
Solution sol;
// 假定 buf 已经被分配了内存，并且有足够的空间来存储文件中的所有字符。
sol.read(buf, 1); // 当调用了您的 read 方法后，buf 需要包含 "a"。 一共读取 1 个字符，因此返回 1。
sol.read(buf, 2); // 现在 buf 需要包含 "bc"。一共读取 2 个字符，因此返回 2。
sol.read(buf, 1); // 由于已经到达了文件末尾，没有更多的字符可以读取，因此返回 0。
示例 2：

File file("abc");
Solution sol;
sol.read(buf, 4); // 当调用了您的 read 方法后，buf 需要包含 "abc"。 一共只能读取 3 个字符，因此返回 3。
sol.read(buf, 1); // 由于已经到达了文件末尾，没有更多的字符可以读取，因此返回 0。
 

提示：

你 不能 直接操作该文件，文件只能通过 read4 获取而 不能 通过 read。
read  函数可以被调用 多次。
请记得 重置 在 Solution 中声明的类变量（静态变量），因为类变量会 在多个测试用例中保持不变，影响判题准确。请 查阅 这里。
你可以假定目标缓存数组 buf 保证有足够的空间存下 n 个字符。 
保证在一个给定测试用例中，read 函数使用的是同一个 buf。


思路：假设 read4本次读取4个 但本次read只需要1个 那么剩下的字符需要缓冲存储起来
"""


# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.cache = [' '] * 4
        self.cache_len = 0

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        current_index = 0
        if n == 0:
            return 0

        if n <= self.cache_len:
            buf[current_index:current_index + n] = self.cache[:n]
            current_index += n
            self.cache[:self.cache_len - n] = self.cache[n:]
            self.cache_len = self.cache_len - n
            return current_index
        else:
            if self.cache_len > 0:
                buf[current_index:current_index + self.cache_len] = self.cache[:self.cache_len]
                current_index += self.cache_len
                n -= self.cache_len
                self.cache_len = 0
                self.cache = [' '] * 4

            while n > 0:
                read4_cache = [' '] * 4
                read4_cache_len = read4(read4_cache)

                if read4_cache_len == 0:
                    return current_index

                if read4_cache_len < 4 and n >= read4_cache_len:
                    buf[current_index:current_index + read4_cache_len] = read4_cache[:read4_cache_len]
                    current_index += read4_cache_len
                    n -= read4_cache_len
                    return current_index

                if n < read4_cache_len < 4:
                    buf[current_index:current_index + n] = read4_cache[:n]
                    self.cache[:read4_cache_len - n] = read4_cache[n:]
                    self.cache_len = read4_cache_len - n
                    current_index += n
                    n -= n

                    return current_index

                if read4_cache_len == 4 and n >= 4:
                    buf[current_index:current_index + 4] = read4_cache[:]
                    current_index += 4
                    n -= 4
                    continue

                if read4_cache_len == 4 and n < 4:
                    buf[current_index:current_index + n] = read4_cache[:n]
                    self.cache[:4 - n] = read4_cache[n:]
                    self.cache_len = 4 - n
                    current_index += n
                    n -= n
                    return current_index

            return current_index
