from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By

from time import sleep


# Abre o driver 
browser = Chrome(executable_path="/usr/local/share/chromedriver")


def clickSeasonDiv():
    class_parent_div = 'Zz99o'
    class_season_divs = 'bSmy5'

    try :
        wait_parent_div = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_season_divs))
        )  
        
        season_divs = browser.find_elements_by_class_name(class_season_divs)
        if ( len (season_divs) == 0 ):
            raise NameError('Recarregar mapeamento de divs')

        return season_divs

    except:
        print ("Algo deu errado ao coletar todas as divs das temporadas, tentando novamente...")
        clickSeasonDiv()


def mainIteration():
 
    # Faz um request pra página do google drive
    browser.get("https://drive.google.com/drive/folders/1m5aDI0SjgvADgo6oF2VjnUP4XdX-lCq-?fbclid=IwAR3mlT44AfLg1OWOcCyYGUC7R7KXe_yxetUymoFsmxpoQkSWdg_vb2weLio")

    print('Buscando todas as divs das temporadas...')
    print('-----------------------------------------')
    # Acha todos as divs clicáveis das temporadas
    season_divs = clickSeasonDiv();

    print('Busquei todas as divs das temporadas')
    print('-----------------------------------------')

    print(len(season_divs))

    print('Divs existem... começando a clicar!')
    print('-----------------------------------------')
    # Se existir divs, vamos iterar sobre elas
    for index_div, div in enumerate(season_divs):

        season_divs = browser.find_elements_by_class_name('bSmy5')

        
        # Efetuar o click
        season_divs[index_div].click()
    
        print(f'Cliquei na div e estou dentro da {index_div}a div')
        print('-----------------------------------------')

        # Dentro da div, iremos buscar os elements cujo nome da classe é akerZd

        print(f'Buscando todos os botões da {index_div}a div')
        print('-----------------------------------------')
        download_modal_button_episode = browser.find_elements_by_class_name('akerZd')

        print(len(download_modal_button_episode))
        return 1


        sleep(2);

        print("Encontrei os botões, vamos começar a clicar")
        print('-----------------------------------------')
        for index_btn, modal_button in enumerate(download_modal_button_episode):

            sleep(2);
            modal_button.click()
            print(f"Cliquei no {index_btn} botão da {index_div}a div")
            print('-----------------------------------------')

            sleep(2);
            download_button = browser.find_elements_by_class_name('h-De-Vb')[0]
            print("Encontrei o botão de download principal")
            print('-----------------------------------------')

            #download_button.click()
            print("Cliquei no botão de download principal")
            print('-----------------------------------------')

            sleep(2)

            print(f"Baixando episódio {index_btn}!")

        browser.execute_script("window.history.go(-1)")



            


    # bSmy5
    # browser.find_element_by_xpath('/html/body/div[1]/div/md-content/navbar/md-toolbar/div/div[2]/nav[3]/button').click()

    # login_username_input = browser.find_element_by_id('login-username')
    # password_input = browser.find_element_by_id('password-input')

    # login_username_input.send_keys('lilcashsaitama')
    # password_input.send_keys('luosd2008')
    # password_input.send_keys(Keys.ENTER)

    # browser.execute_script("window.open('');")
    # browser.switch_to.window(browser.window_handles[1])
    # browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1593290591&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d96dda0ec-1b8d-0378-23bf-812efa58de90&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')


    # email_input = browser.find_element_by_id('i0116')
    # email_input.send_keys('starminebrgames@hotmail.com')
    # email_input.send_keys(Keys.ENTER)

    # sleep(2)

    # password_input = browser.find_element_by_id('i0118')
    # password_input.send_keys('Luosd2008')
    # password_input.send_keys(Keys.ENTER)

    # sleep(10)

    # span = browser.find_elements_by_tag_name('span')

    # for palavra in span:
    #     if palavra.text == 'Seu código de verificação de login da Twitch':
    #         palavra.click()
    #         break

    # sleep(5)

    # identify_number = browser.find_element_by_css_selector("div.x_text-center > p:nth-child(1)")
    # code = identify_number.text 
    # browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
    # browser.close()
    # browser.switch_to.window(browser.window_handles[0])

    # pos1 = browser.find_element_by_css_selector("div.tw-pd-r-1:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    # pos2 = browser.find_element_by_css_selector("div.tw-pd-r-1:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
    # pos3 = browser.find_element_by_css_selector("div.tw-pd-r-1:nth-child(3) > div:nth-child(1) > input:nth-child(1)")
    # pos4 = browser.find_element_by_css_selector("div.tw-pd-r-1:nth-child(4) > div:nth-child(1) > input:nth-child(1)")
    # pos5 = browser.find_element_by_css_selector("div.tw-pd-r-1:nth-child(5) > div:nth-child(1) > input:nth-child(1)")
    # pos6 = browser.find_element_by_css_selector(".tw-pd-r-0 > div:nth-child(1) > input:nth-child(1)")


    # pos1.send_keys(code[0])
    # sleep(0.5)
    # pos2.send_keys(code[1])
    # sleep(0.5)
    # pos3.send_keys(code[2])
    # sleep(0.5)
    # pos4.send_keys(code[3])
    # sleep(0.5)
    # pos5.send_keys(code[4])
    # sleep(0.5)
    # pos6.send_keys(code[5])

    # sleep(5)

    # browser.get("https://streamelements.com/gaules/store")

    # sleep(5)

    # reedem_msg = browser.find_element_by_css_selector("md-card.stream-store-list-item:nth-child(2) > div:nth-child(3) > button:nth-child(1)")
    # reedem_msg.click()

    # sleep(2)


    # input_box = browser.find_element_by_css_selector("html.wf-proximanova-n9-active.wf-proximanova-n7-active.wf-proximanova-i7-active.wf-proximanova-n8-active.wf-proximanova-n6-active.wf-proximanova-n4-active.wf-proximanova-i4-active.wf-proximanova-n3-active.wf-proximanova-n5-active.wf-active body.md-dialog-is-showing div.md-dialog-container md-dialog.store-buy._md.md-default-theme.md-transition-in form.ng-pristine.ng-valid.ng-valid-md-maxlength md-dialog-content#dialogContent_35.md-dialog-content div.slides.layout-column.layout-align-start-center.flex-100 div.layout-column.layout-align-start-start.element-100pw md-input-container.element-100pw.margin-bottom-0.md-default-theme div.md-resize-wrapper textarea#input_36.ng-pristine.ng-untouched.ng-valid.md-input.ng-empty.ng-valid-md-maxlength")
    # p = browser.find_element_by_css_selector("p.md-body-1:nth-child(3)")
    # if p.text == "You do not have enough points to redeem this item":
    #     print("You do not have enough points to redeem a message to Gaules! ")
    # else:
    #     your_message = input("Enter your message to send to Gaules: \n>:")
    #     input_box.send_keys(your_message)


    # print("Tá feito!")


mainIteration()