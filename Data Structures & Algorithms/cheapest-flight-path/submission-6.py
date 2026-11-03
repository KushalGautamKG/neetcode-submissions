class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        prices = [float("infinity")for i in range(n)]
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()

            for s, e, w in flights:
                if prices[s] == float("inf"):
                    continue

                if prices[s] + w < temp[e]:
                    temp[e] = prices[s] + w


            

            prices = temp

        return -1 if prices[dst] == float("inf") else prices[dst]