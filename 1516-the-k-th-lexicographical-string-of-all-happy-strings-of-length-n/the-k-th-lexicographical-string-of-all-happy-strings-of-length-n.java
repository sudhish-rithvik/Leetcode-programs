class Solution {
    public String getHappyString(int n, int k) {
        int total = 3 * (1 << (n - 1));

        if (k > total) {
            return "";
        }

        StringBuilder ans = new StringBuilder();
        char[] letters = {'a', 'b', 'c'};

        for (int i = 0; i < n; i++) {
            int remaining = n - i - 1;
            int groupSize = 1 << remaining;

            for (char c : letters) {
                if (i > 0 && c == ans.charAt(i - 1)) {
                    continue;
                }

                if (k > groupSize) {
                    k -= groupSize;
                } else {
                    ans.append(c);
                    break;
                }
            }
        }

        return ans.toString();
    }
}