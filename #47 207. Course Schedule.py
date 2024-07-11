# Given:
# If [a, b] is in prerequisites array it means
# that 'b' is a prereq for 'a'. We can represent
# this as an edge of a directed graph as follows:
# a->b i.e. to take a we have to take b

# Let's first model prerequisites as an adjacency list
# to represent the graph.

# adj_list maps a course to it's pre-reqs.

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    
    adj_list = {i : [] for i in range(num_courses)}
    # initializes adj_list but all
    # courses have no pre-reqs.

    for course, prereq in prerequisites:
        adj_list[course].append(prereq)
    
    for course in range(num_courses):
        if not can_take(course, adj_list, set()):
            return False
    
    return True

# 'can_take' returns True if we 'course' which is
# a part of the adj_list that represents courses
# and their pre-reqs can be taken.
def can_take(course, adj_list, visited) -> bool:
    if adj_list[course] == []:
        # i.e. course has no pre-reqs
        return True
    elif course in visited:
        # we have found a cycle
        return False
    
    visited.add(course)
    for prereq in adj_list[course]:
        if not can_take(prereq, adj_list, visited):
            return False
        
    visited.remove(course)
    adj_list[course] = [] # we know 'course' can be
    # taken, so we do this that way don't have to
    # recurse again.
    return True