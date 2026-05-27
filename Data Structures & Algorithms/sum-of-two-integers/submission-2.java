class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1; // shift LEFT, not right
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
}