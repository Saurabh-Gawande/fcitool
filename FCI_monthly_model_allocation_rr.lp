\* Output\FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 1671.3 x_rice_('ABS',_'ARA') + 1325.5 x_rice_('ABS',_'AY')
 + 1556.6 x_rice_('AJL',_'ARA') + 1095.5 x_rice_('AJL',_'AY')
 + 2866.8 x_wheat_('BHT',_'AAM') + 2708.9 x_wheat_('BHT',_'CMNR')
 + 2866.8 x_wheat_('BXC',_'AAM') + 2708.9 x_wheat_('BXC',_'CMNR')
Subject To
_C1: x_wheat_('BHT',_'AAM') + x_wheat_('BHT',_'CMNR') <= 1
_C2: x_wheat_('BXC',_'AAM') + x_wheat_('BXC',_'CMNR') <= 1
_C3: x_rice_('ABS',_'ARA') + x_rice_('ABS',_'AY') <= 1
_C4: x_rice_('AJL',_'ARA') + x_rice_('AJL',_'AY') <= 1
_C5: x_wheat_('BHT',_'AAM') + x_wheat_('BXC',_'AAM') >= 1
_C6: x_wheat_('BHT',_'CMNR') + x_wheat_('BXC',_'CMNR') >= 1
_C7: x_rice_('ABS',_'ARA') + x_rice_('AJL',_'ARA') >= 1
_C8: x_rice_('ABS',_'AY') + x_rice_('AJL',_'AY') >= 1
End
