full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):

    Name=character_name(name)
    stats=The_stats(strength,intelligence,charisma)

    STR=''
    INT=''
    CHA=''

    if(Name != None):
        return Name
    elif(stats != None):
        return stats  
    else:
        for i in range(0,10):
            if i < strength:
                STR += full_dot
            else:
                STR += empty_dot

        for i in range(0,10):
            if i < intelligence:
                INT += full_dot
            else:
                INT += empty_dot

        for i in range(0,10):
            if i < charisma:
                CHA += full_dot
            else:
                CHA += empty_dot                    
         
    return f'{name}\nSTR {STR}\nINT {INT}\nCHA {CHA}'  

def character_name(name):

    if (not isinstance(name,str)):
        return 'The character name should be a string'
    
    elif (name==None or name==''):
        return 'The character should have a name'
    
    elif (len(name)>10):
        return 'The character name is too long'    
    
    elif (" " in name):
        return 'The character name should not contain spaces'
     
def The_stats(strength,intelligence,charisma):
    
    if ( (not isinstance(strength,int)) or (not isinstance(intelligence,int)) or (not isinstance(charisma,int)) ):
        return 'All stats should be integers'  
    
    elif( strength<1 or intelligence<1 or charisma<1):
        return 'All stats should be no less than 1'
    
    elif(strength>4 or intelligence>4 or charisma>4):
        return 'All stats should be no more than 4'    
    
    elif( (strength + intelligence + charisma) != 7):
        return 'The character should start with 7 points'          