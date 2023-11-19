\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2866.8 x_rra_('SMBX',_'DPJ')
Subject To
_C1: x_rra_('SMBX',_'DPJ') <= 1
_C2: x_rra_('SMBX',_'DPJ') >= 1
Bounds
 x_rra_('SMBX',_'DPJ') free
Generals
x_rra_('SMBX',_'DPJ')
End
