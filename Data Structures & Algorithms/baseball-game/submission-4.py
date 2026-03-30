class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # 'top' represents the index where the NEXT value will be written
        top = 0 
        
        for op in operations:
            if op == "+":
                # Use the two values immediately before the current 'top'
                val = int(operations[top - 1]) + int(operations[top - 2])
                operations[top] = val
                top += 1
            elif op == "D":
                # Double the value at top - 1
                val = 2 * int(operations[top - 1])
                operations[top] = val
                top += 1
            elif op == "C":
                # Simply move the pointer back; the value is "deleted"
                top -= 1
            else:
                # It's a number; write it at the current top
                operations[top] = int(op)
                top += 1
        
        # We only sum up to the 'top' pointer
        total = 0
        for i in range(top):
            total += int(operations[i])
            
        return total