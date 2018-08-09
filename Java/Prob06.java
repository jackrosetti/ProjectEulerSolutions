public class Prob06 {
    public static void main(String[] args) {
        System.out.println(new Prob06().show());
    }

    private int show() {
        int sum = 0;
        for(int i = 0; i <= 100; i++){
            sum += i;
        }
        sum *= sum;
        int mult = 0;
        for(int j = 0; j <= 100; j++){
            mult += j * j;
        }
        return sum - mult;
    }
}
