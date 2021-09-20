import os
import sys
import logging
from numpy.core.fromnumeric import var
import pandas as pd
from datetime import datetime
from datetime import timedelta
## precisa de xlrd(ler Excel), openpyxl

logging.basicConfig(format='[%(asctime)s] %(levelname)s : %(message)s', level=logging.DEBUG, filename='Codigo.{}.log'.format(datetime.today().strftime('%Y%m%d')), filemode='a+')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def executar():

    try:
        # Descomentar para executar usando o diretorio atual
        nome_dir_entrada = os.path.join(os.getcwd(),'entrada')
        nome_dir_saida = os.path.join(os.getcwd(),'saida')
        data = pd.read_excel( os.path.join(nome_dir_entrada, "Arquivo_Excel.xlsx"), sheet_name='ARQUIVO01' ,
                            dtype={'CPF': str, 'CONTRATO': str, 'NOME': object,'DATA_PAGTO': object,'VALOR_PAGO': object})               
        # Descomentar para executar com parametros
        # arguments = sys.argv[0:]

        logging.debug("--Iniciando--")
        data_now_diretorio = datetime.now().strftime("%d%m%Y%I%M") # Pega data atual.
        logging.debug("--Soma--")
        dataoriginal = data
        data['CPF'] = data['CPF'].apply(str)
        data = data[['CPF', 'VALOR_PAGO']].groupby('CPF').sum() # Soma os valores 'VALOR_PAGO' com o mesmo CPF.
        data = dataoriginal.merge(data, on='CPF')
        data = data.drop(columns=['VALOR_PAGO_x'])
        data = data.rename(columns={"VALOR_PAGO_y":"VALOR_PAGO"})
        data = data.drop_duplicates('CPF', inplace = False)
        os.mkdir(os.path.join(nome_dir_saida,data_now_diretorio))            
        logging.debug("--Escreve Excel--")
        data.to_csv(os.path.join(nome_dir_saida,data_now_diretorio, "Arquivo_Excel_Saida.csv"), sep=';', index=False, header=True)

    except Exception as inst:
        print(inst) 
        logging.debug(f"Erro inesperado durante o processamento dos arquivos: {inst}")
executar()