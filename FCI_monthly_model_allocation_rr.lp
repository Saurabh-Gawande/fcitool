\* Output\FCI_monthly_model_allocation_rr *\
Minimize
OBJ: nan x_rice_('GADJ',_'AJIT') + 1556.6 x_rice_('GADJ',_'BLSN')
 + 571 x_wheat_('BSPR',_'BLSN') + 2263.7 x_wheat_('BSPR',_'VSG')
Subject To
_C1: x_wheat_('BSPR',_'BLSN') + x_wheat_('BSPR',_'VSG') <= 1
_C2: x_rice_('GADJ',_'AJIT') + x_rice_('GADJ',_'BLSN') <= 1
_C3: x_wheat_('BSPR',_'BLSN') >= 1
_C4: x_wheat_('BSPR',_'VSG') >= 1
_C5: x_rice_('GADJ',_'BLSN') >= 1
_C6: x_rice_('GADJ',_'AJIT') >= 1
End
