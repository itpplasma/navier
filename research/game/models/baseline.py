KNOWN={
    'terminal-open': {'terminal_status': 'not-proved', 'unforced_counterexample': 'not-constructed'},
    'positive-consumer': {'needs': 'input-only arbitrary-data critical producer', 'consumer': 'finite L^{3,q} or equivalent continuation bound'},
    'finite-inverse-scope': {'finite_horizon_inverse': True, 'endpoint_uniformity': False, 'common_trace': False, 'arbitrary_data_critical_producer': False},
    'pressure-curvature-transfer': {'uniform_global_sqrtK_budget_can_drive_blowup': False, 'local_directional_constraints_excluded': False},
    'viscous-action-coercivity': {'pressure_only_semibounded_nonzero_background': False, 'zero_background_exception': True},
    'separated-pulse-start': {'separated_zero_pulses_start_autonomously': False},
    'numerics-not-certificate': {'numerical_orbit_proves_blowup': False, 'numerical_orbit_proves_regularity': False},
    'clock-action-obstruction': {'fixed_action_requires': 'S/N^2 >= c0', 'slow_purifier_requires': 'lambda*b >= eta0', 'bounded_fast_parent_requires': 'lambda*sqrt(S) <= C0', 'all_three_with_N_over_b_to_infinity': False},
    'old-strong-scaling-action': {'integrated_clean_action_limit': 0, 'sufficient_for_fixed_positive_filter_action': False},
}
def predict(control): return KNOWN[control['id']]
