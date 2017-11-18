from week9_stacks import PrintableStack as Stack

# tower of hanoi done using actual stacks for the towers


def hanoi_stacks(n, from_stack, to_stack, spare_stack):
    if(n == 1):
        to_stack.push(from_stack.pop())
        # This is the easy way, print when we move
        # print(from_stack,"->",to_stack,"|",spare_stack)

        # get really fancy and alawys print in sorted order (makes it
        # easier to read)
        my_stacks = []
        my_stacks.append(str(from_stack))
        my_stacks.append(str(to_stack))
        my_stacks.append(str(spare_stack))
        my_stacks.sort()
        for next_stack in my_stacks:
            print(next_stack.ljust(20), end="")
        print("")

    else:
        hanoi_stacks(n-1, from_stack, spare_stack, to_stack)
        hanoi_stacks(1, from_stack, to_stack, spare_stack)
        hanoi_stacks(n-1, spare_stack, to_stack, from_stack)

if(__name__ == "__main__"):
    start = Stack("A")
    spare = Stack("B")
    end = Stack("C")

    start.push(5)
    start.push(4)
    start.push(3)
    start.push(2)
    start.push(1)
    hanoi_stacks(5, start, end, spare)
