# black-litterman_bayesian_model  

NOTE : 

This project was made by me during Oct'25, preserved and finally published on Apr 7, 2026 

In this implementation, the Market Equilibrium acts as the Prior Distribution. The Investor Views represent the Likelihood, and the resulting Black-Litterman returns are the Posterior Distribution. This framework mathematically prevents the 'corner solutions' (extreme weights) common in standard mean-variance optimization.

THEORY :

1. The Core Problem: The 'MVO Sensitivity' Trap
   
==> ​Traditional Markowitz optimization (Mean-Variance) is notorious for being 'Estimation-Error Maximizers'. Small changes in expected return inputs lead to massive, unrealistic 'all-or-nothing' swings in portfolio weights. In a production HFT or Asset Management environment, this is unacceptable.

​2. The Solution: Black-Litterman Bayesian Blending

==> ​The Black-Litterman model solves this by using Bayesian Inference. It starts with a 'Prior' (the Market Equilibrium) and updates it with 'Investor Views' (the Alpha) based on the Confidence of those views.

​Mathematical Framework

​A. Reverse Optimization (The Prior)

==> ​Instead of guessing returns, we assume the current Market Cap weights ($w_{mkt}$) are optimal. We solve for the Implied Equilibrium Returns (Π):

 $$ \Pi = \lambda \Sigma w_{mkt} $$
 
where, we have,

λ: Risk Aversion Coefficient,

Σ: Covariance Matrix.
 
Variable Breakdown:

==> $​\Pi$ (Pi): An $(N \times 1)$ vector of Implied Equilibrium Returns. This represents what the market 'thinks' the returns should be to justify current prices.

==> $​\lambda$ (Lambda): A Risk Aversion Coefficient (Scalar). It represents the market's 'Risk-Reward' trade-off. A standard institutional value is 3.0.

==>​ $\Sigma$ (Sigma): An $(N \times N)$ Covariance Matrix. This captures the volatility of each asset and the correlations between them.

==> $​w_{mkt}$: An $(N \times 1)$ vector of Market Capitalization Weights.

B. The Bayesian Formula (The Blend)

==>The model calculates the new adjusted returns $(\mu_{BL})$ by blending the Market Prior with Investor Views (Q):

 $$ \mu_{BL} = [(\tau\Sigma)^{-1} + P^T\Omega^{-1}P]^{-1} [(\tau\Sigma)^{-1}\Pi + P^T\Omega^{-1}Q] $$

==> $​P$ (Pick Matrix): Maps our views to specific assets.

==> $​\Omega$ (Uncertainty): A diagonal matrix representing the variance of each view (Confidence).

==> $\tau$ (Scalar): Determines the weight given to the market prior versus the views.

Computational Complexity 

​1. Complexity: $O(A^3)$
​where $A$ is the number of assets.

i) ​The Bottleneck: The matrix inversions $(np.linalg.inv)$ for $(\tau\Sigma)$ and $\Omega$.

ii) ​HFT Optimization: For 500+ assets (S&P 500), we would replace inv with Cholesky Decomposition or LU Factorization to reduce floating-point errors and latency.

​2. Advantage :

​i) Stability: BL produces intuitive, diversified portfolios. If you have no view on an asset, the model defaults to the Market Weight.

ii) ​Confidence Weighting: Unlike standard models, BL allows us to mathematically state: "We are 90% sure about Tech, but only 10% sure about Energy."

Packages required :

==> This project requires Python 3.x and the following scientific computing libraries:

==> NumPy :- (>= 1.20.0): For vectorization and linear algebra operations.

==> Pandas :- (>= 1.3.0): For data structuring and financial time-series management.

Installation :

==> We can install the required dependencies via `pip`:

```bash
pip install numpy pandas



