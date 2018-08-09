public class Prob02 {

    public static void main(String args[]){
        System.out.println(new Prob02().solve());
    }

    public int solve(){
        int total = 0;
        int a = 1;
        int b = 2;

        while (a <= 4000000) {
            if (a % 2 == 0)
                total += a;
            int c = b + a;
            a = b;
            b = c;
        }
        return total;
    }
}
