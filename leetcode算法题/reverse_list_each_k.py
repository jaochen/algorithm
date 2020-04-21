# coding: utf-8
'''
给定步长m,每m个节点反转单链表
eg: 
    m=2, a->b->c->d->e->f => b->a->d->c->f->e
    m=3, a->b->c->d->e->f => c->b->a->e->f->d
'''

# ====================
# 数组解法
# 思路：
#     1、判断数组能够反转多少次
#     2、每次将区间内的数组反转即可
# ====================
def reverse_list(s_list, m):
    print 'each ', m
    print 'before: ', s_list
    list_len = len(s_list)
    
    if m <= 0:
        return 

    # print list_len/m
    start = 0
    # 判断需要执行多少次
    for index in range(list_len/m):
        # 执行的数据区间
        end = start + m
        reverse(s_list, start, end)
        start += m

    print 'after: ', s_list

def reverse(s_list, start, end):
    '''
    数组反转函数
    '''
    # print 'start: %s, end: %s' % (start, end) 
    for i in range((end-start)/2):
        s_list[start+i], s_list[end-1-i] = s_list[end-1-i], s_list[start+i]
        

if __name__ == '__main__':

    # 数组测试
    reverse_list(['a', 'b', 'c', 'd', 'e', 'f'], 2)
    reverse_list(['a', 'b', 'c', 'd', 'e', 'f'], 3)
    reverse_list(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    
