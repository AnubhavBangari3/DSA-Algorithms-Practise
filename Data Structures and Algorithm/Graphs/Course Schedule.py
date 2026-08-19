
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses

        # Build graph: course -> prerequisites
        for course, pre in prerequisites:
            graph[course].append(pre)

        def dfs(course):
            # Cycle detected
            if visit[course] == -1:
                return False

            # Already completely processed
            if visit[course] == 1:
                return True

            # Mark as currently visiting
            visit[course] = -1

            # Check all prerequisites
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            # Mark as completely visited
            visit[course] = 1
            return True

        # Check every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
'''
1. Build a directed graph from each course to its prerequisites.
2. Use DFS to detect a cycle.
3. Maintain three states:
   - `0` → not visited
   - `-1` → currently visiting
   - `1` → completely visited
4. If DFS reaches a node with state `-1`, a cycle exists → return `False`.
5. If a node is already fully visited (`1`), return `True`.
6. After checking all prerequisites of a course, mark it as `1`.
7. Run DFS for every course.
8. If no cycle is found, return `True`.


Complexity
Time Complexity: O(V + E)
Space Complexity: O(V + E)

Where V = courses and E = prerequisites.
'''