# r_delta_calculator.py
# V14 Delta Paññā-shī Engine: Core Dharma-Resilience Index (R_Delta) Calculator

# The V14 engine computes the potential for success and recovery using the 
# Dharma-Resilience Index (R_Delta), which mathematically integrates the 
# astrological risk (N_Risk) with the ethical and spiritual effort (V_0).

def calculate_r_delta(n_risk: float, v_0: float) -> tuple[float, str]:
    """
    Calculates the Dharma-Resilience Index (R_Delta) and determines the Mandate.

    Args:
        n_risk (float): Natal Conflict Score (N_Risk). Range 1.0 to 3.0.
        v_0 (float): Ethical and Spiritual Value (V_0). Range 1.0 to 4.0.

    Returns:
        tuple[float, str]: The R_Delta value and the corresponding Mandate.
    """
    
    # CONFIDENTIAL WEIGHTING FACTORS - (Proprietary values based on V14 Calibration)
    # These values are set as constants for the calculation but are derived 
    # from empirical testing and philosophical weighting (W_P, W_A).
    # Current test values are used for demonstration based on the Master Architect's
    # framework favoring spiritual/ethical weight (0.6) over physical/planetary weight (0.4).
    WEIGHT_PLANETARY = 0.4  # W_P
    WEIGHT_APPELLATION = 0.6 # W_A
    NORMALIZATION_CONSTANT = 3.0
    MANDATE_THRESHOLD = 1.9

    # The Timeless Equation (R_Delta)
    # R_Delta = [ (W_P * (4 - N_Risk)) + (W_A * V_0) ] / 3
    r_delta = (
        (WEIGHT_PLANETARY * (4.0 - n_risk)) + 
        (WEIGHT_APPELLATION * v_0)
    ) / NORMALIZATION_CONSTANT

    # Mandate Generation Function (P = Mandate(R_Delta))
    if r_delta <= MANDATE_THRESHOLD:
        mandate = "Amā Mandate: Tough Spirit / Inner Fortitude"
    else:
        mandate = "Mettā Mandate: Loving-Kindness / Positive Action"

    return r_delta, mandate

# Example Usage (Using the Master Architect's test values)
# N_Risk = 3.0 (Maximum Crisis)
# V_0    = 4.0 (Highest Ethical Effort)
# result_r_delta, result_mandate = calculate_r_delta(3.0, 4.0)

# print(f"Calculated R_Delta: {result_r_delta:.3f}")
# print(f"Generated Mandate: {result_mandate}")
# Output: Calculated R_Delta: 0.933, Generated Mandate: Amā Mandate...
