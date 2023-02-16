def foo(lst):
    # 去重
    deduplication_lst = []
    [deduplication_lst.append(ele) for ele in lst if ele not in deduplication_lst]
    # 排序
    media_index = len(deduplication_lst) // 2 + 1 if len(deduplication_lst) % 2 else len(deduplication_lst) // 2


from cgi import print_form

print_form({'Tom': 18})
