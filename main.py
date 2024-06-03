test_dict = {1 : {2, 3}, 2 : {}, 3 : {4}, 4 : {5}, 5 : {}, 6 : {}}

is_child = []

def get_childs(page, page_dict):
    if page_dict[page] == {}:
        return {}
        
    childs = {}
    for child in page_dict[page]:
        childs.update({child : get_childs(child, page_dict)})
        is_child.append(child)
        
    return childs
    
def get_childs_with_page(page, page_dict):
    childs = get_childs(page, page_dict)
    return {page : childs}
    
def get_page_struct(page_dict):
    page_struct = {}
    for page in page_dict:
        cilds_w_page = get_childs_with_page(page, page_dict)
    
        if page not in is_child:
            page_struct.update(cilds_w_page)
        
    return page_struct
    
print(get_page_struct(test_dict))
