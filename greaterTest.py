def greaterTest(st):
    for i in range(len(st)-1):
        if int(st[i]) <= int(st[i+1]):
            return False
    return True

if __name__ == '__main__':
    count = 0
    for r in range(43210, 98766):
        st = str(r)
        if greaterTest(st):
            print(st)
            count += 1

    print(count)
