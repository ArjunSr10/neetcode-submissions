class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
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
            res.append(node)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res[::-1]