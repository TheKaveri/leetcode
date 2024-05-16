# Some thoughts:
# 1. In the students array, if students[a] and students[b]'s 
# values are swapped, it is like interchanging two students
# in the queue

# Idea:
# The iterative approach's steps are pretty much given in the
# question itself. The only missing part is when to terminate.
# This happens if all students have received a sandwich or if
# 'none of the queue students want to take the top sandwich'.
# The second stop condition happens if there no person in students
# that prefers sandwich[0] i.e. 'sandwich[0] in students' is false.

def count_students(students: list[int], sandwiches: list[int]) -> int:
    if not students:
        return 0
    elif sandwiches[0] not in students:
        # There's not a single student in the
        # queue who will take the top sandwich
        return len(students)
    
    if sandwiches[0] == students[0]:
        students.pop(0)
        sandwiches.pop(0)
        return count_students(students, sandwiches)
    else:
        first_student = students.pop(0)
        students.append(first_student)
        return count_students(students, sandwiches)
    
# Here's an iterative implementation:

def count_students(students: list[int], sandwiches: list[int]) -> int:

    while students and sandwiches[0] in students:
        if sandwiches[0] == students[0]:
            sandwiches.pop(0)
            students.pop(0)
        else:
            first_student = students.pop(0)
            students.append(first_student)

    return len(students)

# Some further attempts at optimization:
# The iterative solution repeatedly does 'sandwiches[0] in students'
# in each iteration. This can be a little costly as it is O(n). We also
# pop() which is O(n).

# Here is a better method.
def count_students(students: list[int], sandwiches: list[int]) -> int:
    count_pref_0 = students.count(0)
    count_pref_1 = students.count(1)

    for sandwich in sandwiches:
        if sandwich == 0:
            if count_pref_0:
                count_pref_0 -= 1 
            else:
                return count_pref_1
        else: # sandwich == 1:
            if count_pref_1:
                count_pref_1 -= 1 
            else:
                return count_pref_0
    
    return 0