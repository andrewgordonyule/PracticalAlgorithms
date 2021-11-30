class Stack:
    def __init__(self, size=0):
        self.arr = [0] * size
        self.top = -1

    # check for overflow
    # Increment top, insert value at new top of stack
    def push(self, val):
        if self.top == len(self.arr) - 1:
            print('Overflow Error')
        else:
            self.top += 1
            self.arr[self.top] = val

    # Check for underflow
    # Decrement top, return previous top
    def pop(self):
        if self.top == -1:
            print('Underflow Error')
        else:
            self.top -= 1
            return self.arr[self.top + 1]

    # Return item at top of stack without removing
    def peek(self):
        return self.arr[self.top]

    def stack_size(self):
        return self.top + 1

    def stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False


stack = Stack(10)

while True:
    current_url = stack.peek()
    if stack.stack_empty():
        url = input("You are on your home page. Enter the url you wish to visit next (or 'q' to quit). :")
    else:
        prompt = "You are currently visiting the webpage at this url: " + str(current_url) + \
             "\nEnter the url you wish to visit next (or 'q' to quit, 'b' to go back to previous url)."
        url = input(prompt)

    if url.lower() == 'q':
        break
    elif url.lower() == 'b':
        stack.pop()
    else:
        stack.push(url)


print('Browser closed.')


