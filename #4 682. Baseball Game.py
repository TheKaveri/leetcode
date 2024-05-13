# Idea:
# Go through each operation[i], check if the elem is either a
# number, '+', 'D' or 'C'. Then do the required operation for
# for each elem.

# Note:
# "2".isdigit() -> True
# "-2".isdigit() -> False

# So it's better to treat numbers in the else case. This would
# simplify the code as we don't need to give complex conditions

# We will attempt to use a stack to solve the problem due to the 
# nature of the operations we have to perform for each case.

def cal_points(operations: list[str]) -> int:
    records = []

    for operation in operations:
        if operation == '+':
            prev_record = records.pop()
            prev_prev_record = peek(records)
            records.append(prev_record)
            records.append(prev_record + prev_prev_record)
        elif operation == 'D':
            prev_record = peek(records)
            records.append(2 * prev_record)
        elif operation == 'C':
            records.pop()
        else: # operation is a positive/negative number
            record = int(operation)
            records.append(record)

    return sum(records)

def peek(stack):
    return stack[-1]

operations = ["5","2","C","D","+"]
print(cal_points(operations))

# Here is an implementation without using a stack.
# The code is much simpler as well

def cal_points(operations: list[str]) -> int:
    records = []

    for operation in operations:
        if operation == '+':
            records.append(records[-1] + records[-2])
        elif operation == 'D':
            records.append(2 * records[-1])
        elif operation == 'C':
            records.pop()
        else: # operation is a positive/negative number
            records.append(int(operation))
        
    return sum(records)
