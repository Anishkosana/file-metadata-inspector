import os
def listing_out_methods(module):
    list_of_methods=[]
    for item in dir(module):
        if not (item.startswith('__') and item.endswith('__')):
            list_of_methods.append(item)
    return list_of_methods
print(listing_out_methods(os))
# for method in list_of_methods:
#     print(help(getattr(os,method)))

