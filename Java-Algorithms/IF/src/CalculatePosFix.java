
package pkgif;


public class CalculatePosFix {
     public static void CalculatePosFix(String p) {
           Linklist x = new Linklist();
        StringBuilder Num = new StringBuilder();

        for (char Ch : p.toCharArray()) {
            if (Character.isDigit(Ch)) {
                Num.append(Ch);
            } else {
                if (Num.length() > 0) {
                    x.push(Integer.parseInt(Num.toString()));
                    Num.setLength(0); 
                }

                if (Character.isLetter(Ch)) {
                    System.err.println("                 Error::Unable to calculate:");
                    return;
                } else {
                    if (Ch == ' ') continue;
                    double B = x.pop();
                        if (x.isEmpty()){
                        System.err.println("     :Error::The number set entered is invalid:");
                        return;
                    } 
                    double A = x.pop();
                    double C = 0;
                    switch (Ch) {
                        case '+': C = A + B; break;
                        case '-': C = A - B; break;
                        case '*': C = A * B; break;
                        case '/': C = A / B; break;
                        case '^': C = (int) Math.pow(A, B); break;
                    }

                    x.push(C);
                }
            }
        }
        
        if (Num.length() > 0) {
            x.push(Integer.parseInt(Num.toString()));
        }
        double Ca = x.pop();
        
        if(!x.isEmpty() || Ca<=-1){
            System.err.println("     :Error::The number set entered is invalid:\n");
        }else{
             System.out.printf("                        "+"%.2f\n",Ca);
        
        }
    }
}
