class Solution {
public:
    int fib(int N) {
        if (N == 0) return 0;
        if (N == 1) return 1;

        int a = 0;
        int b = 1;
        int result;

        for (int i=2; i<=N; i++){
            result = a+b;
            a = b;
            b = result;
        } //end-for

        return result;
    } //end-fib
};