# a_dict = {"a": 1, "b": 2}
#
# b = a_dict
#
# b["a"] = 3
# print(a_dict)
# print(b)
#
#
# def foo(name, /, **kwds):
#     print(name, kwds)
#     return 'name' in kwds
#
#
# print(foo(1, **{'name': 2}))
#
# a = 123
# b = 123
# print(a is b)

def demo(n1, n2):
    a = {}
    for i in range(n1):

        for j in range(n1, n2):
            a.setdefault(i, []).append(j)

        print(f"demo:{a}")
        yield a
        print(f"demo1:{a}")


def demo1(n1, n2):
    b = {}
    d = demo(n1, n2)
    # print(next(d))
    # print(next(d))
    # next(d)
    for i in d:
        print(i)
        b.update(i)
        i.clear()
    print(b)


a = {9: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}
b = {2: 1}

print(a)
print(b)

b.update(a)
print(a)
print(b)


if __name__ == '__main__':
    # print(demo1(n1=10, n2=20))
    pass
