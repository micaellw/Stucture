package pkgif;
import java.util.Scanner;

public class IF 
{

    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("  Enter to InFix EX.(A+B/C*D) : ");
        String InFix = input.nextLine();
        StringBuilder RPF = new StringBuilder();
        
        System.out.println("========================PosFix=========================");
        InFixToPosFix.InFixToPosFix(InFix,RPF);
        
        if(RPF.length()!=0){
        String p = RPF.toString();
        System.out.println("\n========================Result=========================\n");
        CalculatePosFix.CalculatePosFix(p);
        }
    }
}

