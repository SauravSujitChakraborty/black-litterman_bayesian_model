# black-litterman_bayesian_model

This project was made by me duribg Oct'25, preserved and finally published on Apr 7, 2026 

THEORY :

The Core Problem: The "MVO Sensitivity" Trap
​Traditional Markowitz optimization (Mean-Variance) is notorious for being "Estimation-Error Maximizers." Small changes in expected return inputs lead to massive, unrealistic "all-or-nothing" swings in portfolio weights. In a production HFT or Asset Management environment, this is unacceptable.
​2. The Solution: Black-Litterman Bayesian Blending
​The Black-Litterman model solves this by using Bayesian Inference. It starts with a "Prior" (the Market Equilibrium) and updates it with "Investor Views" (Your Alpha) based on the Confidence of those views.
​🔬 Mathematical Framework
​A. Reverse Optimization (The Prior)
​Instead of guessing returns, we assume the current Market Cap weights ($w_{mkt}$) are optimal. We solve for the Implied Equilibrium Returns (Π):
       
       Π = λΣ$w_{mkt}$
       $\Pi = \lambda \Sigma w_{mkt}$

 where, we have,

λ: Risk Aversion Coefficient,
Σ: Covariance Matrix.
 
