public class Prob03{

    public static void main(String[] args){
        System.out.println(new Prob03().solve());
        System.out.println(MathReference.isPrime(11));
    }

    public long solve(){
        long num = 600851475143L;
        int i = 2;
        while(i * i < num){
            while(num % i == 0){
                num /= i;
            }
            i++;
        }
        return num;
    }



}
