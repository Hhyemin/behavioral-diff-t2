import random


def split_lists(given_list, requirement_list):
    '''
    Split the given list based on the requirements.
    The requirement list expected to be a list of the length of sub-lists,
        e.g., [3, 5] means get the first 3 elements as the first sub-list, 
        and then the followed 5 as the second sub-list. 
    Returns a list of sub-lists.
    ''' 

    sub_lists = []
    for num in requirement_list: # change the variable name to solve a conflict from above lines.
        sub = given_list[0:num]
        if not sub:
            print("The split process stops as all elements in the list have been processed.")
            break
        else:
            sub_lists.append(sub)
            given_list = given_list[num:]
        
    return sub_lists

def print_splitted_lists_in_order(sub_lists, order):
    '''
    The order can be: 
        * increase: with the length of the list increased,
        * decrease: with the length of the list decreased,
        * random:  with the length of the list in a random order.
    '''
    order_to_print = []
    if order == "random":
        sub_num = len(sub_lists)
        random.seed(10)
        order_to_print = random.sample(range(sub_num), sub_num)
    else:
        is_reverse = None
        if order == "decrease":
            is_reverse = True
        elif order == "increase":
            is_reverse = False
        else:
            print("Please give a supported order ('increase', 'decrease', and 'random').")
            return

        dict_len = {}
        for i, sub in enumerate(sub_lists):
            dict_len.update({str(i): len(sub)})
        sorted_len = dict(sorted(dict_len.items(), reverse=is_reverse))
        order_to_print = [int(key) for key in sorted_len.keys()]
        
    for idx in order_to_print:
        print(sub_lists[idx])
