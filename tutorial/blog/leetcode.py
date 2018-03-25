class Solution:
    def numJewelsInStones(self, J, S):
        dic = dict()
        for i in J:
            dic[i] = True
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count

    def findRepeatedDnaSequences(self, s):
        """

        :param s:str
        :return: List[str]
        """
        LENGTH = 10
        mapInfo = dict()
        arr = []
        for i in range(0, len(s) - LENGTH + 1):
            si = s[i:i + LENGTH]
            if si in mapInfo:
                if mapInfo[si] == 0:
                    arr.append(si)
                mapInfo[si] += 1
            else:
                mapInfo[si] = 0
        return arr

    def isInterleave(self, s1, s2, s3):
        """
        https://leetcode.com/problems/interleaving-string/description/
        :param s1: str
        :param s2: str
        :param s3: str
        :return: bool
        """

        def lastchar(str):
            lenstr = len(str)
            return str[lenstr - 1:lenstr]

        def forwardchar(str):
            return str[:len(str) - 1]

        s3end = lastchar(s3)
        s2end = lastchar(s2)
        s1end = lastchar(s1)

        s3forward = forwardchar(s3)
        s2forward = forwardchar(s2)
        s1forward = forwardchar(s1)
        lens3e = len(s3end)
        lens2e = len(s2end)
        lens1e = len(s1end)
        print(len(s3),s3,s2,s1)
        if lens3e > 0 and s3end == s2end and s3end == s1end:
            rt = self.isInterleave(s1, s2forward, s3forward)
            if rt == False:
                return  self.isInterleave(s1forward, s2, s3forward)
            else:
                return True
        elif lens3e > 0 and s3end == s2end:
            return self.isInterleave(s1, s2forward, s3forward)
        elif lens3e > 0 and s3end == s1end:
            return self.isInterleave(s1forward, s2, s3forward)
        elif lens1e == lens2e == lens3e == 0:
            return True
        else:
            return False


class SolutionTest:
    def __init__(self):
        self.solution = Solution()

    def testNumJewelsInStones(self):
        J = "aA"
        S = "aaaAAAvv"
        count = self.solution.numJewelsInStones(J=J, S=S)
        print(J, S, count)

    def testFindRepeatedDnaSequences(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        print(s, self.solution.findRepeatedDnaSequences(s))

    def testIsInterleave(self):
        s1 = "ab"
        s2 = "bc"
        s3 = "babc"
        print(s1, s2, s3, self.solution.isInterleave(s1, s2, s3))


solutionTest = SolutionTest()
solutionTest.testIsInterleave()
