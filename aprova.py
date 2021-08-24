import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException        

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def aprova_tickets(usuario, senha, barra):

    opcoes = webdriver.ChromeOptions()
    #opcoes.add_argument("--headless")

    navegador = webdriver.Chrome(options=opcoes)
    navegador.get("http://newmonitor/user/login_old.php#")

    sleep(2)
    #problema de seguranca do http
    #navegador.find_element_by_xpath('//*[@id="details-button"]').click()
    #navegador.find_element_by_xpath('//*[@id="proceed-link"]').click()

    #clicando no aviso do newmonitor
    navegador.find_element_by_xpath('//*[@id="comunicado"]/center/strong/a').click()

    #tela de login
    wlogin = navegador.find_element_by_xpath('//*[@id="divLogin"]/form/table/tbody/tr[2]/td[2]/input')
    wlogin.clear()
    wlogin.send_keys(usuario)
    wsenha = navegador.find_element_by_xpath('//*[@id="divLogin"]/form/table/tbody/tr[3]/td[2]/input')
    wsenha.clear()
    wsenha.send_keys(senha)
    navegador.find_element_by_xpath('//*[@id="divLogin"]/form/table/tbody/tr[4]/td/input[2]').click()
    sleep(2)

    senhaIncorreta = check_exists_by_xpath(navegador,'//*[@id="divLogin"]/h4')
    if senhaIncorreta:
        navegador.close()
        return -1
    

    #entrando na fila de aprovacoes
    navegador.get("http://newmonitor/user/aprov/aprov.php")
    sleep(1)

    tabela = navegador.find_elements_by_xpath('//*[@id="divTicket"]/table/tbody/tr/td[1]')
    tamanhoTabela = len(tabela)
    ticketsAprovados = 0
    undProgresso = float(100/tamanhoTabela)

    while tamanhoTabela > 1:
        for numTicket in tabela:
            barra.setValue(barra.value() + undProgresso)
            if (numTicket.text != 'Ticket') and (numTicket.text != 'Nenhum ticket encontrado'):
                url = 'http://newmonitor/user/gi/gi_view.php?idTicket='+numTicket.text+'&aprov=1'
                navegador.execute_script("window.open();")
                navegador.switch_to.window(navegador.window_handles[1])
                navegador.get(url)
                sleep(1)
                navegador.find_element_by_xpath('//*[@id="divDados"]/table/tbody/tr[1]/td[1]/a/img').click()
                sleep(1)
                navegador.close()
                navegador.switch_to.window(navegador.window_handles[0])
                ticketsAprovados += 1
                
        
        navegador.refresh()
        sleep(1)

        tabela = navegador.find_elements_by_xpath('//*[@id="divTicket"]/table/tbody/tr/td[1]')
        tamanhoTabela = len(tabela)
        undProgresso = float(100/tamanhoTabela)

        if tabela[1].text == 'Nenhum ticket encontrado':
            break


    sleep(2)
    navegador.close()

    return ticketsAprovados




