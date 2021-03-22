"""
一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。

给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。

接下来会给出一组访问次数和域名组合的列表cpdomains 。要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。

示例 1:
输入:
["9001 discuss.leetcode.com"]
输出:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
说明:
例子中仅包含一个网站域名："discuss.leetcode.com"。按照前文假设，子域名"leetcode.com"和"com"都会被访问，所以它们都被访问了9001次。
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = {}
        for cpdomain in cpdomains:
            count = int(cpdomain.split()[0])
            domains = cpdomain.split()[1]

            domains_split_list = domains.split('.')
            domains_split_list.reverse()

            domains_list = [domains_split_list[0]]
            temp = domains_split_list[0]
            for index in range(1, len(domains_split_list)):
                temp = domains_split_list[index] + '.' + temp
                domains_list.append(temp)

            for domain in domains_list:
                domain_dict[domain] = domain_dict.get(domain, 0) + count

        res = []
        for domain in domain_dict:
            res.append(str(domain_dict[domain]) + ' ' + domain)
        return res
