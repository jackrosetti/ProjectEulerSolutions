public class Prob04 {
    public static void main(String[] args){
        System.out.print(new Prob04().solve());
    }

    public int solve(){
        int ans = 0;
        for(int i = 100; i < 1000; i++){
            for(int j = 100; j < 1000; j++){
                int temp = j * i;
                if(MathReference.isPal(temp) && temp > ans)
                    ans = temp;
            }
        }
        return ans;
    }

}
