package prime0;

 public class LinkNode 
 {
    public int data;                
    public LinkNode next;
  
    public LinkNode (int e, LinkNode next)
      {
         this.data = e;
         this.next = next;    
      }
   public static LinkNode Del (LinkNode x, int y)
      {
        LinkNode z;
        if(x.data == y)
        {
           x=x.next;
           return x;
        }
        z=x;
        while(z.next != null)
        {
           if(z.next.data == y)
           {
              if(z.next.next != null)
               {
                 z.next = z.next.next;
               }
              else
               {
                 z.next = null;
                 return x;
               }
            }
            z=z.next;
        }
        return x;
      }
 }

