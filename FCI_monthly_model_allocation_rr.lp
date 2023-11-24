\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2241.1 x_frk_('AWB',_'FCSJ') + 1095.5 x_frkcgr_('HKG',_'BGTA')
 + 1441.3 x_frkcgr_('JJKR',_'BGTA') + 1897.2 x_rra_('BRCY',_'HSRA')
Subject To
_C1: x_rra_('BRCY',_'HSRA') <= 1
_C2: x_rra_('BRCY',_'HSRA') >= 1
_C3: x_frk_('AWB',_'FCSJ') <= 1
_C4: x_frk_('AWB',_'FCSJ') >= 1
_C5: x_frkcgr_('JJKR',_'BGTA') <= 1
_C6: x_frkcgr_('HKG',_'BGTA') <= 1
_C7: x_frkcgr_('HKG',_'BGTA') + x_frkcgr_('JJKR',_'BGTA') >= 2
Bounds
 0 <= x_frk_('AWB',_'FCSJ')
 0 <= x_frkcgr_('HKG',_'BGTA')
 0 <= x_frkcgr_('JJKR',_'BGTA')
 0 <= x_rra_('BRCY',_'HSRA')
Generals
x_frk_('AWB',_'FCSJ')
x_frkcgr_('HKG',_'BGTA')
x_frkcgr_('JJKR',_'BGTA')
x_rra_('BRCY',_'HSRA')
End
