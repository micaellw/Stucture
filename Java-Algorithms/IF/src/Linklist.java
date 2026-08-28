package pkgif;

public class Linklist {


    class LData
    {
        double data;
        LData link;
    }
    
    public LData head, tail, tem;
    
    public int len = 0;
    
    public boolean isEmpty()
    {
        if(len > 0)
            return false;
        else 
            return true;        
    }
    
    public int lengh()
    {
        return len;
    }
    
    public void push(double x)
    {
        if(len < 1)
        {
            head = new LData();
            tail = head;
            head.data = x;
            len = 1;
        }
        else{
            tem = new LData();
            tem.data = x;
            tem.link = tail;
            tail =  tem;
            len++;
        }
    }
    
    public double  pop()
    {
        if(len < 1)
        { 
            return -1;
        }
        else
        {
          double x;
          x = tail.data;
          tail = tail.link;
          len--;
          return x;
        }
    }  
}
