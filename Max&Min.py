def find_max_min(mylist):
	if max(mylist)==min(mylist):
        return [len(mylist)]
    else:
        return [min(mylist),max(mylist)]