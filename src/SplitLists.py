def split_lists(given_list, requirement_list):
    '''
    Split the given list based on the requirements.
    The requirement list expected to be a list of the length of sub-lists,
        e.g., [3, 5] means get the first 3 elements as the first sub-list, 
        and then the followed 5 as the second sub-list. 
    Returns a list of sub-lists.
    '''

    sub_lists = []
    start = 0 # the index is included
    for len in requirement_list:
        end = start+len # not included
        sub = given_list[start: end] # [)
        sub_lists.append(sub)
        start = end

    return sub_lists

def print_splitted_lists_in_order(sub_lists, order):
    '''
    The order can be: 
        * increase: with the length of the list increased,
        * decrease: with the length of the list decreased.
    '''
    is_reverse = False
    if order == "decrease":
        is_reverse = True

    dict_len = {}
    for i, sub in enumerate(sub_lists):
        dict_len.update({str(i): len(sub)})
    sorted_len = dict(sorted(dict_len.items(), reverse=is_reverse))
    for key in sorted_len.keys():
        print(sub_lists[int(key)])
