#DSA assignment 1
#Siddharth Singh Kathait
#Roll no.-2501730215

from datetime import datetime

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def tower(n, source='A', target='C', aux='B', trace=None):
    if trace == None:
        trace = []
    if n == 1:
        trace.append(f"Move disk 1 from {source} to {target}")
        return trace
    tower(n - 1, source, aux, target, trace)
    trace.append(f"Move disk {n} from {source} to {target}")
    tower(n - 1, aux, target, source, trace)
    return trace

def binarySearch(arr, target, left=0, right=None):
    if right == None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binarySearch(arr, target, left, mid - 1)
    return binarySearch(arr, target, mid + 1, right)

def runTests():
    output = []
    output.append("=" * 50)
    output.append("AERT TOOLKIT TEST RESULTS")
    output.append("=" * 50)
    output.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("")
    
    output.append("1. STACK TESTS")
    output.append("-" * 20)
    s = Stack()
    for val in [1,2,3,4,5]:
        s.push(val)
    output.append(f"Stack size: {s.size()}")
    
    popped = []
    while not s.isEmpty():
        popped.append(s.pop())
    output.append(f"Popped: {popped}")
    output.append("")
    
    output.append("2. FACTORIAL TESTS")
    output.append("-" * 20)
    for n in [0,1,5,10]:
        output.append(f"fact({n}) = {factorial(n)}")
    output.append("")
    
    output.append("3. FIBONACCI TESTS")
    output.append("-" * 20)
    for n in [0,1,5,8]:
        output.append(f"fib({n}) = {fib(n)}")
    output.append("")
    
    output.append("4. TOWER OF HANOI n=3")
    output.append("-" * 20)
    moves = tower(3)
    for i, move in enumerate(moves, 1):
        output.append(f"{i}. {move}")
    output.append("")
    
    output.append("5. BINARY SEARCH")
    output.append("-" * 20)
    arr = list(range(1,21))
    for target in [7,15,20,0]:
        pos = binarySearch(arr, target)
        found = "FOUND" if pos != -1 else "NOT FOUND"
        output.append(f"{target}: index {pos} {found}")
    
    output.append("")
    output.append("COMPLEXITY:")
    output.append("Stack: O(1)")
    output.append("Factorial: O(n)")
    output.append("Fib: O(2^n) - SLOW!")
    output.append("Tower: O(2^n)")
    output.append("Binary Search: O(log n) - BEST!")
    
    with open("output.txt", "w") as f:
        f.write("\n".join(output))
    
    print("Tests done! Check output.txt")

if __name__ == "__main__":
    print("AERT Toolkit - All Recursive!")
    runTests()
