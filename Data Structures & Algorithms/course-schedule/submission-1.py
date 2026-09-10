class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Here, b is the pre-requisite to taking course a. So, a -> b. The only case where it's not possible to take a course is when there's a cycle in the graph.
        # So, we build the graph one-by-one from the edges, hashmap + list to build out the graph. Then we run a dfs and keep track of visit, in case we run the dfs and encounter a vertex we have already seen before, we just return False.
        course_graph = defaultdict(list)
        
        for course, prereq in prerequisites: # Builds the graph in O(edges)
            course_graph[course].append(prereq)

        # We'll use a recursive dfs approach here as it's more natural    
        visiting = set() # detection of cycle in the current path
        visited = set()  # set of all visited nodes to avoid repeated work

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

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True  


            






