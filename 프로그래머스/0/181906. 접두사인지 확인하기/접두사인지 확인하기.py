#$def solution(my_string, is_prefix):
    #if len(is_prefix)>len(my_string):
       # return 0
    #for i in my_string:
        #for j in is_prefix:
            #if i == j:
              #  return 1
            #else:
                #return 0
            
            
def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix):
        return 1
    else:
        return 0