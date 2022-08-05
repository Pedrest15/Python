from typing import List, Tuple, TypeVar
pd_DataFrame = TypeVar('pd_DataFrame')
pd_Series = TypeVar('pd_Series')

def data_atual() -> Tuple[str, str]:
    from datetime import datetime

    num_dia = datetime.today().weekday() #segunda é indexada com 0 e assim por diante
    if num_dia == 5 or num_dia == 6: #bolsa não funciona aos sábados e domingos
        exit()
    dia = datetime.today()
    dia = dia.strftime('%m-%d-%Y') #data no padrão americano

    dict = {0: 'segunda-feira', 1: 'terça-feira', 2: 'quarta-feira', 3: 'quinta-feira', 4: 'sexta-feira', 5: 'sábado', 6: 'domingo'}

    nome_dia = dict[num_dia]
    
    return (dia, nome_dia)

def busca_cotacoes(dia: str, indice_codigos: pd_Series) -> pd_DataFrame:
    from pandas_datareader import data as web
    cotacao = pd.DataFrame()

    for codigo in indice_codigos:
        cotacao = pd.concat([cotacao, web.DataReader('{}.SA'.format(codigo), data_source='yahoo', start=dia, end=dia)])

    return cotacao

def variacao_por_papel(valores_abertura: pd_Series, valores_fechamento: pd_Series) -> List[float]:
    variacao = []

    for i in range(valores_abertura.shape[0]):
        variacao.append(100 * ((valores_fechamento[i] - valores_abertura[i]) / valores_abertura[i]))

    return variacao

def texto_email(dia: str, indice_empresas: pd_Series, cotacao: pd_DataFrame, variacao: List[float]) -> str:
    dia = dia.split('-')
    cabecario = '<p>Bom dia, as cotações no dia {}/{}/{}, {}, foram:'.format(dia[1], dia[0], dia[2], nome_dia)

    positivo = 'green'
    negativo = 'red'
    texto_principal = ''
    for i in range(papeis.shape[0]):
        texto_principal += """<h3>{}</h3>
                              <p>-> Valor de Abertura: {:.2f}</p>
                              <p>-> Valor de fechamento: <b>{:.2f}</b></p>""".format(indice_empresas[i], cotacao.Open[i], cotacao.Close[i])
        if variacao[i] > 0: #ação subiu no dia
            texto_principal += '<p>-> Variação no pregão: <font color={}>+{:.2f}%</font></p>'.format(positivo, variacao[i])
        else:
            texto_principal += '<p>-> Variação no pregão: <font color={}>{:.2f}%</font></p>'.format(negativo, variacao[i])
        texto_principal += """<p>-> Máxima no dia: {:.2f}</p> 
                              <p>-> Volume Movimentado: {}</p><hr>""".format(cotacao.High[i], cotacao.Volume[i])
    
    fechamento = '<p>Abraços;</p>'

    return cabecario + texto_principal + fechamento

def enviar_email(corpo_email: str) -> None:
    import smtplib
    import email.message

    msg = email.message.Message()
    msg['Subject'] = 'Cotações do Último Pregão'
    msg['From'] = '<email_remetente>'
    msg['To'] = '<email_destinatario>'
    password = '<senha_remetente>'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    servidor = smtplib.SMTP('smtp.outlook.com: 587')
    servidor.starttls()
    servidor.login(msg['From'], password)
    servidor.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

if __name__ == '__main__':
    import pandas as pd

    dia, nome_dia = data_atual()

    lista_acoes = ['Magalu', 'Vittia', 'Petrobrás', 'BB']
    lista_codigos = ['MGLU3', 'VITT3', 'PETR4', 'BBAS3']
    papeis = pd.DataFrame({'Empresa':lista_acoes, 'Códigos': lista_codigos})

    cotacao = pd.DataFrame()
    cotacao = pd.concat([cotacao, busca_cotacoes(dia, papeis['Códigos'])])

    variacao = variacao_por_papel(cotacao.Open, cotacao.Close)
    
    corpo_email = texto_email(dia, papeis.Empresa, cotacao, variacao)
    enviar_email(corpo_email)
