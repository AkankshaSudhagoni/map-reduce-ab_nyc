# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 5) : 
    RANK,BRAND,CATEGORIES01,CATEGORIES02,FOLLOWERS,ER,iPOSTS_ON_HASHTAG,MEDIA_POSTED = datalist

    # print intermediate key-value pairs to standard output
    print(FOLLOWERS,"\t",1)
