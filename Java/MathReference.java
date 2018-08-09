import java.math.BigInteger;

final class MathReference {

    static boolean isPal(int n)
    {
        int palindrome = n;
        int reverse = 0;

        while (palindrome != 0) {
            int remainder = palindrome % 10;
            reverse = reverse * 10 + remainder;
            palindrome = palindrome / 10;
        }

        return n == reverse;
    }

     static boolean[] listPrimality(int n) {
        boolean[] result = new boolean[n + 1];

        if (n >= 2) result[2] = true;
        
        for (int i = 3; i <= n; i += 2)
            result[i] = true;

        // Sieve of Eratosthenes
        for (int i = 3, end = (n * n); i <= end; i += 2) {
            if (result[i]) {
                for (int j = i * i, inc = i * 2; j <= n; j += inc)
                    result[j] = false;
            }
        }
        return result;
    }


     static int[] listPrimes(int n) {
        boolean[] isPrime = listPrimality(n);
        int count = 0;
        for (boolean b : isPrime) {
            if (b)
                count++;
        }

        int[] result = new int[count];
        for (int i = 0, j = 0; i < isPrime.length; i++) {
            if (isPrime[i]) {
                result[j] = i;
                j++;
            }
        }
        return result;
    }

    static boolean isPrime(int n) {
        if(n <= 1) return false;
        if(n <= 3) return true;

        if(n % 2 == 0 || n % 3 == 0) return false;

        for(int i = 5; i * i <= n; i += 6){
            if(n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    public static int getGCD(int a, int b) {
        BigInteger b1 = BigInteger.valueOf(a);
        BigInteger b2 = BigInteger.valueOf(b);
        BigInteger gcd = b1.gcd(b2);
        return gcd.intValue();
    }


}