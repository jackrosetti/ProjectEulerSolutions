public class Prob05 {
    public static void main(String[] args) {
        System.out.println(new Prob05().solve());
    }

    public int solve(){
        int mult = 1;
        for(int i = 1; i < 21; i++){
            mult *= i / MathReference.getGCD(i, mult);
        }
        return mult;
    }
}
