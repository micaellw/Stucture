
package gcd;

/**
 *
 * @author Treeraphat
 */
import java.util.Arrays;
import java.util.Scanner;

public class GCD{
    public static void main(String[] args) {


        Scanner input = new Scanner(System.in);

        System.out.print("Enter number for a: ");
        int a = input.nextInt();
      
        System.out.print("Enter number for b: ");
        int b = input.nextInt();
      
        System.out.print("Enter number for c: ");
        int c = input.nextInt();
        System.out.println("===============================================");



        int x0, y0;
        int gst[];
        
        gst = Ex_Euclid(a,b);
        System.out.println(Arrays.toString(gst));
        
        System.out.println("===============================================");

        if(c%gst[0]==0){

            x0 = gst[1] * c / gst[0];
            y0 = gst[2] * c / gst[0];
            System.out.println("X0 =" +  x0);
            System.out.println("Y0 =" +  y0);

            System.out.println("X =" +  x0 + " + " + b/gst[0] + "n");
            System.out.println("Y =" +  y0 + " - " + a/gst[0] + "n");
            
            System.out.println("===============================================");

            int n1,n2;
            int nX = b/gst[0];
            int nY = -a/gst[0];

            n1 = -x0 / nX;
            n2 = -y0 / nY;
            int x , y ;

            if(-x0 % nX != 0 && -y0 % nY != 0){

                 System.out.println(n1+"<n<"+n2); 
                 System.out.println("===============================================");


                 for(int i=n1+1; i<n2  ;i++)
                 {
                    System.out.println("n = "+i);
                    x = x0 + nX*(i);
                    y = y0 - nY*(-i);
                    System.out.println("x = " + x + " ,  y = " + y);
                 }

            }else if (-x0 % nX == 0 && -y0 % nY == 0) {

                System.out.println(n1+"<=n<="+n2);
                System.out.println("===============================================");


                for(int i=n1; i<=n2 ;i++)
                 {
                    System.out.println("n = "+i);
                    x = x0 + nX*i;
                    y = y0 - nY*(-i);
                    System.out.println("x = " + x + " ,  y = " + y);
                 }

            }else if(-x0 % nX != 0 && -y0 % nY == 0){

                System.out.println(n1+"<n<="+n2);
                System.out.println("===============================================");

                for(int i=n1+1; i<=n2 ; i++)
                 {
                    System.out.println("n = "+i);
                    x = x0 + nX*(i);
                    y = y0 - nY*(-i);
                    System.out.println("x = " + x + " ,  y = " + y);
                 }

            }else if(-x0 % nX == 0 && -y0 % nY != 0){

                System.out.println(n1+"<=n<"+n2);
                System.out.println("===============================================");

                for(int i=n1; i<n2  ;i++)
                 {
                    System.out.println("n = "+i);
                    x = x0 + nX*(i);
                    y = y0 - nY*(-i);
                    System.out.println("x = " + x + " ,  y = " + y);
                 } 
            }

           
        } else{
            System.out.println("No result!");
        }


    }


    static int[] Ex_Euclid(int a, int b) {
        int[] r = {b,0,1};
        if(a == 0){
            return r;
        } else{
            int s,t;
            r = Ex_Euclid(b%a,a);
            s = r[1];
            t = r[2];
            r[2] = s;
            r[1] = t-((b/a)*s);
            return r;
        }
    }
}