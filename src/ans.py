""" 
Practice Question 2: List of Dictionaries - Key Filtering

Task:

Create a function filter_dict_list that takes a list of dictionaries 
and a key name. The function should return a new list of dictionaries, 
each missing the specified key.
"""

def filter_dict_list(input_list, key_to_remove):
    # ans = []
    # for indiv_map in input_list:
    #     new_map = {}
    #     for key, value in indiv_map.items():
    #         if key != key_to_remove:
    #             new_map[key] = value
    #     ans.append(new_map)
    # return ans

    return [{key: value for key, value in indiv_map.items() if key != key_to_remove} for indiv_map in input_list]

