def foo(lst):
    # ε»ι
    deduplication_lst = []
    [deduplication_lst.append(ele) for ele in lst if ele not in deduplication_lst]
    # ζεΊ
    media_index = len(deduplication_lst) // 2 + 1 if len(deduplication_lst) % 2 else len(deduplication_lst) // 2


from cgi import print_form

print_form({'Tom': 18})
