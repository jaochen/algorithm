# -*- coding: utf-8 -*-


class Primes():
    """ 参考廖雪峰老师的filter教程
        用这个例子理解流式惰性计算
    """
    def _odd_iter(self):
        n = 1
        while True:
            n += 2
            print(f'odd iter {n} ')
            yield n

    def _not_divisible(self, n):
        # print(f'n: {n}')
        def t(x):
            print(f'divisible {x} {n}')
            return x % n > 0
        return t
    
    def __iter__(self):
        return self.__next__()
    
    def __next__(self):
        yield 2
        it = self._odd_iter()
        while True:
            n = next(it)
            yield n
            # 7 为啥会被3和5整除，而不是只被5整除
            # 关键在self.it，self.it是满足之前运算的素数集。下面可以看出
            # 有点像递归了，比较难理解
            if n > 50:
                print('================ it start')
                for i in it:
                    if i < 100:
                        print(i)
                    else:
                        break
                print('===============it end')
            it = filter(self._not_divisible(n), it)


if __name__ == '__main__':
    primes = Primes()
    for n in primes:
        if n < 100:
            print(n)
        else:
            break

    for n in primes:
        if n < 10:
            print(n)
        else:
            break
