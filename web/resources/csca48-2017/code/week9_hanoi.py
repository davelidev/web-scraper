def hanoi(n, from_tower="Tower A", to_tower="Tower B", spare_tower="Tower C"):
    '''(int, str, str, str) -> NoneType

    Print the moves for the Tower of Hanoi puzzle, starting with n levels on
    from_tower, and moving them to to_tower with spare_tower as the third
    available tower slot.
    '''
    if(n == 1):
        print(from_tower, " -> ", to_tower)
    else:
        hanoi(n-1, from_tower, spare_tower, to_tower)
        print(from_tower, " -> ", to_tower)
        hanoi(n-1, spare_tower, to_tower, from_tower)

if(__name__ == "__main__"):
    hanoi(3)
