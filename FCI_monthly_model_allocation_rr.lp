\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 1556.6 x_wheat_('BH',_'BTI') + 1897.2 x_wheat_('BH',_'FCSJ')
 + 1785.9 x_wheat_('BSP',_'BTI') + 2043.2 x_wheat_('BSP',_'FCSJ')
Subject To
_C1: x_wheat_('BSP',_'BTI') + x_wheat_('BSP',_'FCSJ') <= 1
_C2: x_wheat_('BH',_'BTI') + x_wheat_('BH',_'FCSJ') <= 1
_C3: x_wheat_('BH',_'BTI') + x_wheat_('BSP',_'BTI') >= 1
_C4: x_wheat_('BH',_'FCSJ') + x_wheat_('BSP',_'FCSJ') >= 1
Bounds
 x_wheat_('BH',_'BTI') free
 x_wheat_('BH',_'FCSJ') free
 x_wheat_('BSP',_'BTI') free
 x_wheat_('BSP',_'FCSJ') free
Generals
x_wheat_('BH',_'BTI')
x_wheat_('BH',_'FCSJ')
x_wheat_('BSP',_'BTI')
x_wheat_('BSP',_'FCSJ')
End
