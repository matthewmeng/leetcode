class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        countera = 0
        counterb = 0
        counter = 0
        total = []
        for i in nums1:
            for j in nums2:
                print("i "+str(i))
                print("j "+str(j))
                if i < j:
                    total.append(i)
                    nums1.remove(i)
                    counter += 1
                    countera += 1
                    break
                else:
                    total.append(j)
                    nums2.remove(j)
                    counter += 1
                    counterb += 1
            if nums2 == []:
                total.append(i)
            print("nums1:    "+str(nums1))
            print("nums2:    "+str(nums2))
        print(total)
def stringToIntegerList(input):
    return json.loads(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums1 = stringToIntegerList(line)
            line = lines.next()
            nums2 = stringToIntegerList(line)
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = doubleToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()