class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # If we detect a cycle with the courses that is given to us, we will return [], otherwise if it's possible to take those courses, I return the order. I can just maintain a new array which contains ordering information alongside with other info.
        course_graph = defaultdict(list)
        
        for course, prereq in prerequisites: # Builds the graph in O(edges)
            course_graph[course].append(prereq)

        # We'll use a recursive dfs approach here as it's more natural    
        visiting = set() # detection of cycle in the current path
        visited = set()  # set of all visited nodes to avoid repeated work
        ordering = []    # ordering of the courses to take

        def dfs(node):
            if node in visiting:
                return False

            if node in visited:
                return True
            
            visiting.add(node)

            for prereq in course_graph[node]: # Exploring the current path
                if not dfs(prereq):
                    return False

            visiting.remove(node)
            visited.add(node)
            ordering.append(node)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return ordering 