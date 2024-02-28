num = 1
num2 = 20
num3 = 3000
num4 = 40
num5 = 50
num6 = 60
num7 = 70


class pronson(object):
    def __init__(self):
        self._num = 1

    @property
    def num(self):
        return self._num


# 使用property装饰器，为实例的attribute 增加（除访问与修改之外的）其他处理逻辑
class Person:
    """
    https://blog.csdn.net/cnds123/article/details/129420059
    https://docs.python.org/zh-cn/3/index.html ->Python 3.12.2 文档
    """
    def __init__(self, first_name):
        self.first_name = first_name

    # 定义相关联的函数（方法），这里是三个，名字都必须一样。
    # 定义Getter函数
    @property
    def first_name(self):
        return self._first_name

    # 定义Setter装饰器函数
    @first_name.setter
    def first_name(self, value):
        # isinstance() 函数，用来判断一个函数是否是一个已知的类型
        if not isinstance(value, str):
            raise TypeError('应为字符串')
        self._first_name = value

    # 定义Deleter装饰器函数——可选
    @first_name.deleter
    def first_name(self):
        raise AttributeError("不能删除")


if __name__ == '__main__':
    # pronson1 = pronson()
    # print(pronson1.num)
    a = Person('Jack')
    print(a.first_name)  # 调用getter，输出：Jack

    # a.first_name = 42  #【注1】不允许，否则报错 TypeError: 应为字符串
    print(a.first_name)

    # del a.first_name  #【注2】不允许，否则报错 AttributeError: 不能删除