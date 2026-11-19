class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = defaultdict(list)

        for course, prereq in prerequisites:
            hashMap[prereq].append(course)

        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False

            if node in visited:
                return True

            path.add(node)

            for course in hashMap[node]:
                if not dfs(course):
                    return False

            path.remove(node)
            visited.add(node)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True