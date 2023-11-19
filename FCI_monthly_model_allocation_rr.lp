\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2903.7 x_rra_('BBMN',_'DPJ')
Subject To
_C1: x_rra_('BBMN',_'DPJ') <= 1
_C2: x_rra_('BBMN',_'DPJ') >= 1
Bounds
 x_rra_('BBMN',_'DPJ') free
Generals
x_rra_('BBMN',_'DPJ')
End
