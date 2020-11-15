def advance_array(lst):
    max_reach = 0
    for i in range(len(lst)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + lst[i])
    return True

def main():
    a1 = [3, 3, 1, 0, 2, 0, 1]
    a2 = [3, 2, 0, 0, 2, 0, 1]
    print(advance_array(a1))
    print(advance_array(a2))

if __name__ == "__main__":
    main()