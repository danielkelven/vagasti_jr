import pandas as pd
import os
from get_vagas import BuscarVagas

resultado = BuscarVagas('Júnior')

print(resultado)


# if os.path.exists('files/dimensionamento_final.xlsx'):
#     os.remove('files/dimensionamento_final.xlsx')

# with pd.ExcelWriter('files/Resumo vagas Júnior.xlsx') as arquivoFinal:
#     df_plast.to_excel(arquivoFinal, sheet_name='PLAST', index=False)
#     df_full.to_excel(arquivoFinal, sheet_name='FULL', index=False)
#     df_exp.to_excel(arquivoFinal, sheet_name='EXP', index=False)
#     df_f5.to_excel(arquivoFinal, sheet_name='F5', index=False)
#     df_ts.to_excel(arquivoFinal, sheet_name='TS', index=False)