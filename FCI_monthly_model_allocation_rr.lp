\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 1441.3 x_frkrra_('ABS',_'GMUV') + 1441.3 x_wheat_('FCP',_'BNF')
Subject To
_C1: x_wheat_('FCP',_'BNF') <= 1
_C2: x_wheat_('FCP',_'BNF') >= 1
_C3: x_frkrra_('ABS',_'GMUV') <= 1
_C4: x_frkrra_('ABS',_'GMUV') >= 1
Bounds
 x_frkrra_('ABS',_'GMUV') free
 x_wheat_('FCP',_'BNF') free
Generals
x_frkrra_('ABS',_'GMUV')
x_wheat_('FCP',_'BNF')
End
