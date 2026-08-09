class Fancy {
    static const long long MOD = 1000000007;

    vector<long long> a;
    long long mul = 1;
    long long add = 0;

    long long power(long long x, long long n) {
        long long res = 1;

        while (n > 0) {
            if (n & 1)
                res = res * x % MOD;

            x = x * x % MOD;
            n >>= 1;
        }

        return res;
    }

    long long inv(long long x) {
        return power(x, MOD - 2);
    }

public:
    Fancy() {
    }

    void append(int val) {
        // Store the value after reversing the current transformation:
        // actual = stored * mul + add
        long long x = (val - add + MOD) % MOD;
        x = x * inv(mul) % MOD;

        a.push_back(x);
    }

    void addAll(int inc) {
        add = (add + inc) % MOD;
    }

    void multAll(int m) {
        mul = mul * m % MOD;
        add = add * m % MOD;
    }

    int getIndex(int idx) {
        if (idx < 0 || idx >= (int)a.size())
            return -1;

        return (a[idx] * mul + add) % MOD;
    }
};