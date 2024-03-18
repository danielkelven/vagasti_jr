import pandas as pd
import os
from get_vagas import BuscarVagas

resultado = BuscarVagas('Júnior')

dfAcre = resultado[resultado['Local'].str.contains('AC', case=False)]

dfAlagoas = resultado[resultado['Local'].str.contains('AL', case=False)]

dfAmapa=resultado[resultado['Local'].str.contains('AP', case=False)]

dfAmazonas=resultado[resultado['Local'].str.contains('AM', case=False)]

dfBahia=resultado[resultado['Local'].str.contains('BA', case=False)]

dfCeara=resultado[resultado['Local'].str.contains('CE', case=False)]

dfEspiritoSanto=resultado[resultado['Local'].str.contains('ES', case=False)]

dfGoias=resultado[resultado['Local'].str.contains('GO', case=False)]

dfMaranhao=resultado[resultado['Local'].str.contains('MA', case=False)]

dfMatoGrosso=resultado[resultado['Local'].str.contains('MT', case=False)]

dfMGSul=resultado[resultado['Local'].str.contains('MS', case=False)]

dfMinasGerais=resultado[resultado['Local'].str.contains('MG', case=False)]

dfPara=resultado[resultado['Local'].str.contains('PA', case=False)]

dfParaiba=resultado[resultado['Local'].str.contains('PB', case=False)]

dfParana=resultado[resultado['Local'].str.contains('PR', case=False)]

dfPernambuco=resultado[resultado['Local'].str.contains('PE', case=False)]

dfPiaui=resultado[resultado['Local'].str.contains('PI', case=False)]

dfRioJaneiro=resultado[resultado['Local'].str.contains('RJ', case=False)]

dfRGNorte=resultado[resultado['Local'].str.contains('RN', case=False)]

dfGSul=resultado[resultado['Local'].str.contains('RS', case=False)]

dfRondonia=resultado[resultado['Local'].str.contains('RO', case=False)]

dfRoraima=resultado[resultado['Local'].str.contains('RR', case=False)]

dfSantaCatarina=resultado[resultado['Local'].str.contains('SC', case=False)]

dfSaoPaulo=resultado[resultado['Local'].str.contains('SP', case=False)]

dfSergipe=resultado[resultado['Local'].str.contains('SE', case=False)]

dfTocantins=resultado[resultado['Local'].str.contains('TO', case=False)]

dfDistritoFederal=resultado[resultado['Local'].str.contains('DF', case=False)]


# if os.path.exists('files/dimensionamento_final.xlsx'):
#     os.remove('files/dimensionamento_final.xlsx')

# with pd.ExcelWriter('files/Resumo vagas Júnior.xlsx') as arquivoFinal:
#     df_plast.to_excel(arquivoFinal, sheet_name='PLAST', index=False)
#     df_full.to_excel(arquivoFinal, sheet_name='FULL', index=False)
#     df_exp.to_excel(arquivoFinal, sheet_name='EXP', index=False)
#     df_f5.to_excel(arquivoFinal, sheet_name='F5', index=False)
#     df_ts.to_excel(arquivoFinal, sheet_name='TS', index=False)