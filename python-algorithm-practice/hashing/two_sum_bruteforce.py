def find_target(arr, target):

    try :
        tar=int(target)

    except ValueError as e:
        return("Value Typ Error Must Be Integer")

    except Exception as e:
        return "Unknown Error" 

    else:
        ar=[]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)): 
                if arr[i] + arr[j] == tar:
                    return [i, j]            
           
        if ar == []:
            return "Target not found"  