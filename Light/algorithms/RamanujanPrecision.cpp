/*
  This algorithm computes the value of π using Ramanujan’s rapidly convergent series for 
1/π
1/π. Instead of approximating π directly, it evaluates an infinite series whose sum equals the reciprocal of π, and then inverts the result.

At each iteration 
k
k, the algorithm calculates a term involving factorials, powers, and a linear expression 
(26390k+1103)
(26390k+1103). These terms decrease extremely fast, so only a small number of iterations (typically 5–10) are needed to achieve high precision.

Factorials are computed using the gamma function, since 
n!=Γ(n+1)
n!=Γ(n+1). After summing the desired number of terms, the result is multiplied by a constant factor 
22992
99²
 to obtain 
1/π
1/π. The final step is to invert this value to produce an approximation of π.

Because of its very fast convergence, this algorithm is much more efficient than classical series for π and historically influenced modern high-precision π algorithms such as the Chudnovsky method.
*/
	​

	​

#include <iostream>
#include <cmath>

long double cal_pi_ramanujan(int terms) {
    long double sum = 0.0L;

    for (int k = 0; k < teros; k++) {
        long double numerador =
            tgammal(4 * k + 1) * (26390.0L * k + 1103.0L);

        long double denominador =
            powl(tgammal(k + 1), 4) * powl(396.0L, 4 * k);

        som += numerador / denominador;
    }

    long double fator = (2.0L * sqrtl(2.0L)) / (99.0L * 99.0L);
    long double inv_pi = fator * som;

    return 1.0L / inv_pi;
}

int main() {
    int terms = 5; // 5 já é bastante!
    long double pi = calcular_pi_ramanujan(terms);

    std::cout.precision(20);
    std::cout << "Pi ≈ " << pi << std::endl;

    return 0;
}
