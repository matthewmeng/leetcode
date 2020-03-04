class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        str_list = []
        for i in range(len(s)):
            the_char = s[i]
            print("this char is "+the_char)
            print(s[i] in str_list)
            
            if (s[i] in str_list) == True:
                print("duplicate")
                dic[len(str_list)] = str_list
                if i+1 >= len(s):
                    str_list = []
                
            else:
                print("not duplicate")
                str_list.append(s[i])
                print(str_list)
              
        print(dic)
        return(max(dic.keys()))

def stringToString(input):
    return input[1:-1].encode().decode('unicode_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            s = stringToString(line)
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()