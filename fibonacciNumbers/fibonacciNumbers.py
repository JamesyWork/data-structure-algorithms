def create_fibonacci_numbers_by_using_loop():
    prev_node1 = 0
    prev_node2 = 1

    print(prev_node1)
    print(prev_node2)
    for fibo in range(18):
        new_node = prev_node1 + prev_node2
        print(new_node)
        prev_node1 = prev_node2
        prev_node2 = new_node


def create_fibonacci_numbers_by_recursion(prev_node1=0, prev_node2=1, counter=2):
    print(prev_node1)
    print(prev_node2)
    if counter <= 19:
        new_node = prev_node1 + prev_node2
        prev_node1 = prev_node2
        prev_node2 = new_node
        counter += 1
        print(counter)
        create_fibonacci_numbers_by_recursion(prev_node1, prev_node2, counter)
    else:
        return


def create_fibonacci_numbers_by_nth_recursion(node=19):
    if node <= 1:
        return node
    else:
        return create_fibonacci_numbers_by_nth_recursion(node - 1) + create_fibonacci_numbers_by_nth_recursion(node - 2)
