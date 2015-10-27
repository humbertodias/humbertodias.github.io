import java.io.IOException;
import java.util.Scanner;



/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {

    static long divisor_sum( long number ) { 
       long sum = 0, i ; 
       for (i = 1 ; i < number ; i++ ) 
          if ( number % i == 0 ) 
             sum += i ; 
       return sum; 
    }
    public static void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);

        int i, n, num;
        n = scanner.nextInt();
        for(i = 0; i < n; i++){
            num = scanner.nextInt();

            if(divisor_sum(num) == num) System.out.format("%d eh perfeito\n", num);
            else System.out.format("%d nao eh perfeito\n", num);

        }
    }
 
}
