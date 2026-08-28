package prime0;

import java.util.Scanner;
import static prime0.LinkNode.Del;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Prime0 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in); 
        System.out.print("  Enter number:");
        int p;
        p= input.nextInt();
        double root = Math.sqrt(p);
        LinkNode y = new LinkNode(p,null);
        LinkNode x,z,e;
        x = y;  
        for(int i=p;i>1;i--)
        {
          x = new LinkNode(i,x);
        }     
        
        z = x; 
        int n;
        e = x;
        while(e.next != null && e.data < root)
        {
            while(z.next != null)
            {           
                if(z.data % e.data == 0)
                {
                   if(z.data != e.data)
                   {
                      n = z.data;
                      x =  Del(x,n);                   
                   }                            
                } 
               z = z.next;              
            }
            z = x;          
            e = e.next; 
        }      
       StringBuilder r = new StringBuilder();
       
       while(x.next != null)
       {
       r.append("\t"+x.data).append("\n");
          x = x.next;
       }
       String prime= r.toString();
        openNotepadWithMessage(" Received Value : "+ p + "\n\n" + 
                               "   PrimeNumber" +"\n" + prime );          
    }

     public static void openNotepadWithMessage(String message) {
        try {
          
            String filePath = "output.txt";
  
            BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
            writer.write(message);
            writer.close();
 
            Runtime.getRuntime().exec("notepad.exe " + filePath);
            
        } 
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    
}