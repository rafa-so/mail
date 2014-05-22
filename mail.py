import smtplib
from datetime import date, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ME = 'rafaoliveira@mestrainfo.com.br'
YOU = 'leandrogomes@mestrainfo.com.br'

def enviaEmail():
	
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Horario de Saida'
    msg['From'] = ME
    msg['To'] = YOU
    msg.attach(retornaHTMLMensagem())
    s = smtplib.SMTP('192.100.100.55','25')
    s.sendmail(ME, YOU, msg.as_string())
    s.quit()

def retornaHTMLMensagem():
    hora_saida = retornaHoraSaida()
    data_saida = retornaDataSaida()
    htmlText = '''	<html>
                        <head></head>
                        <body>
                            <p>Bom dia!<br>
                            Horario de saida: ''' + hora_saida +'''<br>
                            Data de saida: ''' + data_saida + '''
                        </body>
                    </html>'''
    partHTML = MIMEText(htmlText, 'html')
    return partHTML
    
def retornaDataSaida():
    hj = date.today()
    return str(hj.day) + '/' + str(hj.month) + '/' + str(hj.year)
    
def retornaHoraSaida():
    agora = datetime.now()
    return str(agora.hour) + ':' + str(agora.minute)
    
if __name__ == '__main__':
    enviaEmail()