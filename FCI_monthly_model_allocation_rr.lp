\* FCI_monthly_model_allocation_rr *\
Minimize
OBJ: 2418.5 x_frkrra_('BIDR',_'BBMN') + 2263.7 x_frkrra_('BIDR',_'BRW')
 + 2043.2 x_frkrra_('BIDR',_'HZBN') + 1325.5 x_frkrra_('BUDI',_'BBMN')
 + 1038.2 x_frkrra_('BUDI',_'BRW') + 1671.3 x_frkrra_('BUDI',_'HZBN')
 + 1785.9 x_frkrra_('CHD',_'BBMN') + 1556.6 x_frkrra_('CHD',_'BRW')
 + 980.6 x_frkrra_('CHD',_'HZBN')
Subject To
_C1: x_frkrra_('BIDR',_'BBMN') + x_frkrra_('BIDR',_'BRW')
 + x_frkrra_('BIDR',_'HZBN') <= 1
_C2: x_frkrra_('BUDI',_'BBMN') + x_frkrra_('BUDI',_'BRW')
 + x_frkrra_('BUDI',_'HZBN') <= 1
_C3: x_frkrra_('CHD',_'BBMN') + x_frkrra_('CHD',_'BRW')
 + x_frkrra_('CHD',_'HZBN') <= 1
_C4: x_frkrra_('BIDR',_'BRW') + x_frkrra_('BUDI',_'BRW')
 + x_frkrra_('CHD',_'BRW') >= 1
_C5: x_frkrra_('BIDR',_'BBMN') + x_frkrra_('BUDI',_'BBMN')
 + x_frkrra_('CHD',_'BBMN') >= 1
_C6: x_frkrra_('BIDR',_'HZBN') + x_frkrra_('BUDI',_'HZBN')
 + x_frkrra_('CHD',_'HZBN') >= 1
Bounds
 x_frkrra_('BIDR',_'BBMN') free
 x_frkrra_('BIDR',_'BRW') free
 x_frkrra_('BIDR',_'HZBN') free
 x_frkrra_('BUDI',_'BBMN') free
 x_frkrra_('BUDI',_'BRW') free
 x_frkrra_('BUDI',_'HZBN') free
 x_frkrra_('CHD',_'BBMN') free
 x_frkrra_('CHD',_'BRW') free
 x_frkrra_('CHD',_'HZBN') free
Generals
x_frkrra_('BIDR',_'BBMN')
x_frkrra_('BIDR',_'BRW')
x_frkrra_('BIDR',_'HZBN')
x_frkrra_('BUDI',_'BBMN')
x_frkrra_('BUDI',_'BRW')
x_frkrra_('BUDI',_'HZBN')
x_frkrra_('CHD',_'BBMN')
x_frkrra_('CHD',_'BRW')
x_frkrra_('CHD',_'HZBN')
End
