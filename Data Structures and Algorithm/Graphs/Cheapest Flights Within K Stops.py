class Solution:
    def findCheapestPrice(self,n: int,flights: List[List[int]],src: int,dst: int,K: int) -> int:

        # dp[i][city] = minimum cost to reach city
        # using at most i flights
        dp = [
            [float("inf")] * n
            for _ in range(K + 2)
        ]

        # Starting city costs 0
        dp[0][src] = 0

        # At most K stops = at most K + 1 flights
        for i in range(1, K + 2):

            # We can always remain at source with cost 0
            dp[i][src] = 0

            # Relax every flight
            for u, v, cost in flights:

                # Reach u using previous number of flights,
                # then take flight u -> v
                dp[i][v] = min(
                    dp[i][v],
                    dp[i - 1][u] + cost
                )

        # Destination unreachable
        if dp[K + 1][dst] == float("inf"):
            return -1

        return dp[K + 1][dst]
'''
1. Use **Dynamic Programming / Bellman-Ford style relaxation**.
2. Since at most `K` stops means at most `K + 1` flights, create `K + 2` DP rows.
3. Let:

   `dp[i][city]` = cheapest cost to reach `city` using at most `i` flights.

4. Initialize:

   `dp[0][src] = 0`

5. For each number of flights from `1` to `K + 1`:
   - Keep source cost as `0`.
   - Relax every flight `[u, v, cost]`.
6. Update:

   `dp[i][v] = min(dp[i][v], dp[i-1][u] + cost)`

7. Return `dp[K+1][dst]`.
8. If it is still infinity, return `-1`.

Complexity
Time Complexity: O(K × E)
Space Complexity: O(K × V)

Where E = flights and V = cities.
'''