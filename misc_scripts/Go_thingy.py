#0 is empty
#1 is white
#2 is black

length = int(input())
board = [1, 1, 1, 1, 1, 1, 1, 1, 1]

#  [0, 1, 0]
#  SEQ_LEN=1
#  Semi:0
#  Open:1

#  [1, 0, 1, 2, 0, 1, 2, 0, 1, 0]
#  SEQ_LEN=1
#  Semi:3
#  Open:1

#  [0, 1, 1, 1, 0, 0, 2, 1, 2, 1, 1, 2, 0]
#  SEQ_LEN=2
#  Semi:?
#  Open:?
#



#solving for white squares(open seqs, semi-closed seqs)
def solve(in_ar, seq_len): #input row of stones, length of neccesary sequence
  if seq_len == 0:
    raise ValueError
  if seq_len > len(in_ar):
    return (0, 0)

  donotdorest = False

  semiN, openN = 0, 0
  
  i = 0
  while i < len(in_ar):

    donotdorest = False
    
    if in_ar[i] == 1:
      print(i)
      for j in range(i+1, i+seq_len):
        print("J is " + str(j))
        try:
          if in_ar[j] != 1:
            print("NOT EQUAL")
            i=j
            donotdorest = True
            continue
        except IndexError:
          print("EROROR")
          return (semiN, openN)

      print("OUT OF FOR")
      
      try:
        if in_ar[i+seq_len] == 1:
          i+=1
          continue
        if i-1 != -1 and in_ar[i-1] == 1:
          i+=1
          continue
      except IndexError:
        return (semiN, openN)
     
      if donotdorest == False:

        print("REACHED MAIN IF")
        
        numOfBorders = 0
        
        if i-1 == -1:
          numOfBorders+=1
        else:
          if in_ar[i-1] == 2:
            numOfBorders+=1
            
        if i+seq_len > len(in_ar):
          numOfBorders+=1
        else:
          if in_ar[i+seq_len] == 2:
            numOfBorders+=1
            
        if numOfBorders == 1:
          semiN += 1
        elif numOfBorders == 0:
          openN += 1
  
        i+=seq_len-1
    i+=1

  return (semiN, openN)


s, o = solve(board, length)

print(str(s) + " semi-closed seqs and " + str(o) + " open seqs")