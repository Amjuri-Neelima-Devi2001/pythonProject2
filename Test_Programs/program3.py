def index_list1(l):
    search=int(input("enter elemnet in list:"))
    for i in range(len(l)):
        if l[i] == search:
            return i

