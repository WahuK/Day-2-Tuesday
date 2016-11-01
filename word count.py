def words(str):
  num={}
  for words in str.split():
    if word.isdigit():
      word=int(word)
    if num.get(word):
      num[word]+=1
    else:
      num[word]=1
    return num
  
