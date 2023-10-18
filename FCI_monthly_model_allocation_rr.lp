\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2043.2 x_rra_('BGBR',_'VSG')
Subject To
_C1: x_rra_('BGBR',_'VSG') <= 1
_C2: x_rra_('BGBR',_'VSG') >= 1
Bounds
 x_rra_('BGBR',_'VSG') free
Generals
x_rra_('BGBR',_'VSG')
End
