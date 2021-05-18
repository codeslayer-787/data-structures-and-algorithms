initial_list = [2,4,6,-8]


def insert_shift_array(lst, item):
  midpoint = len(lst)//2
  new_list = lst[0:midpoint] + [item] + lst[midpoint:]
  return new_list
print(insert_shift_array(initial_list, 5))
