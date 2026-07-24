import bisect
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        products.sort()
        result = []

        for i in range(1,len(searchWord) + 1):
            I_result = []
            j = bisect.bisect_left(products,searchWord[:i])
            for k in range(j, j + 3):
                if k < len(products) and products[k][:i] == searchWord[:i]:
                    I_result.append(products[k])

            result.append(I_result)

        return result




        