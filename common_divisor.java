public class main {

  public static void main(String[] args){

 int a = 108;
   int b = 48;
   System.out.println("GCD of a and b is" + calcGcd(a, b));
  }
  //method to calculate the GCD
  public static long calcGcd(int a, int b) {
   if(b != 0) {
    print(b, a%b)
    return calcGcd(b, a%b)
   } else {
    return a;
   }
  }
}