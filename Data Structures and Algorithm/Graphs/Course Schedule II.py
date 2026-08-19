class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        result = []

        # Build graph: course -> prerequisites
        for course, pre in prerequisites:
            graph[course].append(pre)

        def dfs(course):

            # Cycle detected
            if visit[course] == 1:
                return False

            # Already processed
            if visit[course] == -1:
                return True

            # Mark as currently visiting
            visit[course] = 1

            # Visit all prerequisites first
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            # Mark as completed
            visit[course] = -1

            # Add course after prerequisites
            result.append(course)

            return True

        # Run DFS for every course
        for course in range(numCourses):

            if not dfs(course):
                return []

        return result
'''
1. Build a directed graph where each course points to its prerequisites.
2. Use DFS with three states:
   - `0` → not visited
   - `1` → currently visiting
   - `-1` → completely processed
3. If DFS reaches a node with state `1`, a cycle exists.
4. If a node is already `-1`, it is already processed.
5. After visiting all prerequisites of a course, add the course to `result`.
6. Run DFS for every course.
7. If any cycle is found, return `[]`.
8. Otherwise return `result`.

Complexity
Time Complexity: O(V + E)
Space Complexity: O(V + E)

'''