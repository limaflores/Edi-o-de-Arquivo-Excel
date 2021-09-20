# Edicao-de-Arquivo-Excel
Script python para edição de campos de arquivo em Excel utilizando a biblioteca Pandas

É necessário crir duas pastas ('Entrada' e 'Saida') no mesmo diretório ou indicar o caminho.
Na pasta de entrada precisa ter um documento Excel chamado "Arquivo_Excel.xlsx".
Com a primeira aba chamada 'ARQUIVO01'.
E com os seguintes campos no header: 'CPF', 'CONTRATO', 'NOME','DATA_PAGTO','VALOR_PAGO'.
A aplicação realiza a soma das linhas de mesmo CPF no campo 'VALOR_PAGO'.
