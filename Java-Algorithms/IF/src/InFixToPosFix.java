
package pkgif;


public class InFixToPosFix {
    
     public static void InFixToPosFix(String InFix,StringBuilder R  ) 
     {

        Linklist x  = new Linklist();
        int N = 0,N1 = 0,N2=0 ,err1 = 0,err2=0;;
        StringBuilder Num = new StringBuilder();
         char Col = 0;
    for (char ch : InFix.toCharArray()) 
    {
        if (Character.isDigit(ch))
        {
            Num.append(ch);
        } 
        else 
        {
          if(Num.length()>1)
          {
            R.append(" "+Num.toString()+" ");
            Num.setLength(0);
          }
          else
          {
            R.append(" "+Num.toString()+" ");
            Num.setLength(0);
          }  
     
         if (Character.isLetter(ch)) 
         {   
            R.append(ch);
         } 
         else 
         {
         if(ch=='+'||ch=='-')     N=1;
         if(ch=='*'||ch=='/')     N=2;
         if(ch == '^')            N=3;  
         if(ch == '('){           N=4;  err1++;}
         if(ch == ')'){           N=0;  err2++;}
         
          if(!x.isEmpty())
           {
             Col=(char)x.pop();
             
             if(Col=='+'||Col=='-') N1=1;
             if(Col=='*'||Col=='/') N1=2;
             if(Col == '^')         N1=3;  
             if(Col == '(')         N1=0;
             
             if(N > N1)
              {
                x.push(Col);  
                x.push(ch);        
              }
             
             if(N<=N1)
              { 
                  if(ch==')')
                  {             
                     while(Col!='(') {
                         R.append(" "+Col);
                         Col=(char)x.pop();
                     }
                  }
                else{
                while(!x.isEmpty())
                 {     
                   R.append(" "+Col);
                   Col=(char)x.pop();
                }
                   R.append(" "+Col);
                   x.push(ch);
              }
              }
           }
          else
           {
             x.push(ch);
           }
        }
      }
    }
    
      if(Num.length()>1)
          {
            R.append(" "+Num.toString()+" ");
            Num.setLength(0);
          }else{
            R.append(" "+Num.toString()+" ");
            Num.setLength(0);
          }
    
    while(!x.isEmpty())
    {
      Col=(char)x.pop();
      R.append(" "+Col);
      
    }  
    String p = R.toString();
    
     if(err1==err2){
        System.out.println("\n               "+p+"  \n");
     }
    else if(err1>err2){
        System.err.println("\n                   :Error to bracket:\n");
        R.setLength(0);
    }
    else{
        System.err.println("\n                   :Error to bracket:\n");
        R.setLength(0);
    }
     
     }
}
