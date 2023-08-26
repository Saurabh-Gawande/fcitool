\* Output\FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 1671.3 x_rice_('HMH',_'ARA') + 2043.2 x_wheat_('KRAR',_'CHA')
Subject To
_C1: x_wheat_('KRAR',_'CHA') <= 1
_C2: x_rice_('HMH',_'ARA') <= 1
_C3: x_wheat_('KRAR',_'CHA') >= 1
_C4: x_rice_('HMH',_'ARA') >= 1
End
