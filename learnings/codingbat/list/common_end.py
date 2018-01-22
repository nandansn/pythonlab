def common_end(a=[], b=[]):
    if not a or not b:
        return False
    else:
        if a[0] == b[0] or a.pop() == b.pop():
            return True
        else:
            return False

print(common_end([1,2,3],[3,2,1]))

