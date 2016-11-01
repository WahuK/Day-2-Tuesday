def word_count(str):
  my_string=str.lower().split()
  my_dict={}
  for item in my_string:
    my_dict[item]=my_string.count(item)
  print(my_dict)
  word_count("olly olly in come free")

  