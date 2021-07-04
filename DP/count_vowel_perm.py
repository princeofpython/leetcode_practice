# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3802/
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mo = 10**9+7
        dp = [{} for _ in range(n)]
        def f(n, vowel):
            mo = 10**9+7
            if vowel in dp[n-1].keys():
                return dp[n-1][vowel]
            if n==1:
                dp[0][vowel] = 1
                return dp[0][vowel]
            if vowel =='a':
                dp[n-1][vowel] = (f(n-1, 'e')) % mo
                return dp[n-1][vowel]
            if vowel =='e':
                dp[n-1][vowel] = (f(n-1, 'a') + f(n-1, 'i')) % mo
                return dp[n-1][vowel]
            if vowel == 'i':
                dp[n-1][vowel] =  (f(n-1,'a') + f(n-1,'e') + f(n-1,'o') + f(n-1,'u')) % mo
                return dp[n-1][vowel]
            if vowel == 'o':
                dp[n-1][vowel] =  (f(n-1, 'u') + f(n-1, 'i')) % mo
                return dp[n-1][vowel]
            if vowel == 'u':
                dp[n-1][vowel] = f(n-1,'a') % mo
                return dp[n-1][vowel]
        return (f(n,'a')+f(n,'e')+f(n,'i')+f(n,'o')+f(n,'u')) % mo

  class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # initialize the number of strings ending with a, e, i, o, u
        a_count = e_count = i_count = o_count = u_count = 1
        MOD = 10 ** 9 + 7

        for i in range(1, n):
            a_count_new = (e_count + i_count + u_count) % MOD
            e_count_new = (a_count + i_count) % MOD
            i_count_new = (e_count + o_count) % MOD
            o_count_new = (i_count) % MOD
            u_count_new = (i_count + o_count) % MOD

            # https://docs.python.org/3/reference/expressions.html#evaluation-order
            a_count, e_count, i_count, o_count, u_count = \
                a_count_new, e_count_new, i_count_new, o_count_new, u_count_new

        return (a_count + e_count + i_count + o_count + u_count) % MOD
