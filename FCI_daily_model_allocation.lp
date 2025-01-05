\* FCI_daily_model_allocation *\
Minimize
OBJ: 1860570 x_frk_br_('FCMA_MOGA_PB',_'GDSG_MANMAD_MH')
 + 6981660 x_rra_('FKA_FEROZEPUR_PB',_'FCSJ_JAMMU_JK')
Subject To
_C1: x_rra_('FKA_FEROZEPUR_PB',_'FCSJ_JAMMU_JK') <= 1
_C2: x_rra_('FKA_FEROZEPUR_PB',_'FCSJ_JAMMU_JK') >= 1
_C3: x_frk_br_('FCMA_MOGA_PB',_'GDSG_MANMAD_MH') <= 1
_C4: x_frk_br_('FCMA_MOGA_PB',_'GDSG_MANMAD_MH') >= 1
Bounds
 0 <= x_frk_br_('FCMA_MOGA_PB',_'GDSG_MANMAD_MH')
 0 <= x_rra_('FKA_FEROZEPUR_PB',_'FCSJ_JAMMU_JK')
Generals
x_frk_br_('FCMA_MOGA_PB',_'GDSG_MANMAD_MH')
x_rra_('FKA_FEROZEPUR_PB',_'FCSJ_JAMMU_JK')
End
