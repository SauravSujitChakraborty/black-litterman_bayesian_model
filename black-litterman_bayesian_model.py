import numpy as np
import pandas as pd

def black_litterman_blend(w_mkt, cov, views, confidences, tau=0.05):
    """Blends Market Equilibrium with Investor Views."""
    # 1. Reverse Optimization: Find implied equilibrium returns (Pi)
    # Risk aversion coefficient (lambda) assumed at 3.0 (standard)
    lmbda = 3.0
    pi = lmbda * (cov @ w_mkt)
    
    # 2. The 'P' matrix (Identifies which assets we have views on)
    # 3. The 'Q' vector (The expected return of those views)
    P = np.eye(len(w_mkt))
    Q = views
    
    # 4. Omega (Uncertainty of views)
    omega = np.diag(np.diag(P @ (tau * cov) @ P.T)) / confidences
    
    # 5. Black-Litterman Formula (The Bayesian Blend)
    # New Returns = [(tau*Cov)^-1 + P'*Omega^-1*P]^-1 * [(tau*Cov)^-1*Pi + P'*Omega^-1*Q]
    term1 = np.linalg.inv(np.linalg.inv(tau * cov) + P.T @ np.linalg.inv(omega) @ P)
    term2 = (np.linalg.inv(tau * cov) @ pi) + (P.T @ np.linalg.inv(omega) @ Q)
    
    bl_returns = term1 @ term2
    return bl_returns

# --- SCENARIO ---
assets = ['Tech', 'Energy', 'Bonds']
mkt_weights = np.array([0.5, 0.2, 0.3])
covariance = np.array([
    [0.04, 0.01, 0.00],
    [0.01, 0.09, 0.00],
    [0.00, 0.00, 0.01]
])

# My View: Tech will do 8% (High confidence), Energy 2% (Low confidence)
my_views = np.array([0.08, 0.02, 0.03])
my_conf = np.array([10.0, 1.0, 10.0]) # Higher number = more confidence

adjusted_returns = black_litterman_blend(mkt_weights, covariance, my_views, my_conf)

print(f"--- 📐 BLACK-LITTERMAN BAYESIAN ENGINE ---")
print(f"{'Asset':<10} | {'Mkt Implied Ret':<15} | {'BL Adjusted Ret'}")
print("-" * 50)
lmbda = 3.0
pi = lmbda * (covariance @ mkt_weights)

for i, asset in enumerate(assets):
    print(f"{asset:<10} | {pi[i]:<15.2%} | {adjusted_returns[i]:.2%}")

print("-" * 50)
print("Quant Note: BL prevents extreme 'All-or-Nothing' weights")
print("by anchoring the optimization to the Market Equilibrium.")
