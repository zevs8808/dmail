from selenium import webdriver #Селениум
from selenium.webdriver.chrome.options import Options #Нужно чтобы ввести опции в селениум (расширения тыр пыр)
from selenium.webdriver.support.ui import WebDriverWait #Нужно чтобы как только страница прогрузилась - выполнить действие
from selenium.webdriver.support import expected_conditions as EC #Не помню)
from selenium.webdriver.common.by import By #Для поиска по хпатху
from selenium.common.exceptions import TimeoutException #Ошибки обрабатывать (вроде..)
from selenium.webdriver.common.keys import Keys #Имитировать кнопки на клаве
from selenium.webdriver.common.action_chains import ActionChains #Имитировать сочитание кнопок на клаве
import csv #Открывать текстовики по особенному
import os #Находить файлы
import json
import random #рандом
import time #Нужно чтобы подождать какое то время
put = os.path.dirname(os.path.abspath(__file__))
putex2 = os.path.join(put, 'mmm.zip')

#указываем путь к текстовикам
seed = os.path.join(put, 'seed.txt')
rasseed = os.path.join(put, 'numseed.txt')
gmails = os.path.join(put, 'gmails.txt')
rasgmails = os.path.join(put, 'numgmails.txt')
msg = os.path.join(put, 'msg.txt')

#Запускаем селениум
options = webdriver.ChromeOptions()
options.add_extension(putex2)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 5)
driver.maximize_window()
#Переходим к расширению, ждем 2 секунды (прогрузка)
driver.get('chrome-extension://hjocpjdeacglfchomobaagbmipeggnjg/options.html')
time.sleep(2)
kk = 0 #Бесполезная переменная, в будущем будет использоваться для того, чтобы понять, нужно ли обновить страничку с метамаском
window_after1 = driver.window_handles[1]
driver.switch_to.window(window_after1)

#Записываем хпатх кнопок в метамаске
path1 = '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input'
path2 = '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button'

#Находим и нажимаем кнопку в мме
while True:
    try:
        kk = kk + 1
        time.sleep(2)
        if kk == 4:
            kk = 0
            driver.refresh()

        driver.find_element(By.XPATH, path1).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, path2).click()
        kk = 0
        break
    except:
        pass


path3 = '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]'
wait.until(EC.visibility_of_element_located((By.XPATH, path3))).click()

#ввести сид фразу
word1 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input'
word2 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div/input'
word3 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[3]/div[1]/div/input'
word4 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[4]/div[1]/div/input'
word5 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[5]/div[1]/div/input'
word6 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[6]/div[1]/div/input'
word7 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[7]/div[1]/div/input'
word8 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[8]/div[1]/div/input'
word9 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[9]/div[1]/div/input'
word10 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[10]/div[1]/div/input'
word11 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[11]/div[1]/div/input'
word12 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[12]/div[1]/div/input'

#гениальная система по взятию некст логина пароля почты
while True:
    try:
        #Открыть rasseed, взять оттуда записанную цифру, засунуть ее в переменную a и добавить к ней +1
        a1 = open(rasseed, 'r')
        a2 = list(a1)
        a3 = int(a2[0])
        a = a3 + 1
        a1.close()

        #Открыть rasseed и заменить имеющуюся цифру на +1
        a4 = open(rasseed, 'w')
        a4.write(str(a))
        a4.close()

        #Достать сидфразу, номер сидфразы = переменная а, взятая цифра из rasseed и засунуть ее в переменную rows
        csvfile = open(seed)
        spamreader = csv.reader(csvfile, delimiter=' ')
        rows = list(spamreader)

        #Разбить сидфразу по словам
        b1 = rows[a][0]
        b2 = rows[a][1]
        b3 = rows[a][2]
        b4 = rows[a][3]
        b5 = rows[a][4]
        b6 = rows[a][5]
        b7 = rows[a][6]
        b8 = rows[a][7]
        b9 = rows[a][8]
        b10 = rows[a][9]
        b11 = rows[a][10]
        b12 = rows[a][11]

        csvfile.close()
        break
    except:
        #если ошибка (закончились сидфразы) - начать заново
        a4 = open(rasseed, 'w')
        a4.write('-1')
        a4.close()

#Дождаться появления места для ввода сидфразы и ввести
wait.until(EC.visibility_of_element_located((By.XPATH, word1))).send_keys(b1)
driver.find_element(By.XPATH, word2).send_keys(b2)
driver.find_element(By.XPATH, word3).send_keys(b3)
driver.find_element(By.XPATH, word4).send_keys(b4)
driver.find_element(By.XPATH, word5).send_keys(b5)
driver.find_element(By.XPATH, word6).send_keys(b6)
driver.find_element(By.XPATH, word7).send_keys(b7)
driver.find_element(By.XPATH, word8).send_keys(b8)
driver.find_element(By.XPATH, word9).send_keys(b9)
driver.find_element(By.XPATH, word10).send_keys(b10)
driver.find_element(By.XPATH, word11).send_keys(b11)
driver.find_element(By.XPATH, word12).send_keys(b12)

#нажать далее
path4 = '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button'
#driver.find_element(By.XPATH, path4).click()
wait.until(EC.visibility_of_element_located((By.XPATH, path4)))
time.sleep(0.2)
driver.find_element(By.XPATH, path4).click()

#ввести и повторить пароль
path5 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input'
wait.until(EC.visibility_of_element_located((By.XPATH, path5))).send_keys('1234567890')
path6 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input'
wait.until(EC.visibility_of_element_located((By.XPATH, path6))).send_keys('1234567890')

#принять правила и нажать далее далее далее далее
path7 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input'
wait.until(EC.visibility_of_element_located((By.XPATH, path7))).click()
path8 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button'
wait.until(EC.visibility_of_element_located((By.XPATH, path8))).click()

#Тут может багнуть, надо сделать так, чтоб не крашилось
while True:
    try:
        path9 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'
        driver.find_element(By.XPATH, path9).click()
        break
    except:
        pass

#тыкаем далее далее, ждем 1 сек
path10 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'
wait.until(EC.visibility_of_element_located((By.XPATH, path10))).click()
path11 = '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'
wait.until(EC.visibility_of_element_located((By.XPATH, path11))).click()
time.sleep(1)

#Сохраняем ссылку на метамаск (она меняется) и делаем из нее ссылку на ЗАБЫЛ ПАРОЛЬ, в будущем так мы будем менять аккаунт на некст
mm = driver.current_url
metamask = mm.replace("home.html#", "home.html#restore-vault")
#Делаем ссылку на добавление сети
metamaskchain = mm.replace("home.html#", "home.html#settings/networks/add-network")
print('mm = ', mm)
print('metamask = ', metamask)

driver.get(metamaskchain)
#Хпатхи метамаска для добавления новой сети
chainname = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input'
urlrpc = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input'
id = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input'
symb = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input'
urlblock = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input'
save = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]'
#Дождаться прогрузки и ввести данные от зксинк сети
wait.until(EC.visibility_of_element_located((By.XPATH, chainname))).send_keys('zkSync Era Mainnet')
driver.find_element(By.XPATH, urlrpc).send_keys('https://mainnet.era.zksync.io')
time.sleep(0.5)
driver.find_element(By.XPATH, id).send_keys('324')
time.sleep(0.5)
driver.find_element(By.XPATH, symb).send_keys('ETH')
driver.find_element(By.XPATH, urlblock).send_keys('https://explorer.zksync.io/')
time.sleep(2)
while True:
    try:
        driver.find_element(By.XPATH, save).click()
    except:
        pass
        #переключиться на сеть зксинк
        path = '/html/body/div[2]/div/div/section/div/div/button[1]'

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, path))).click()
        break
    except:
        pass
time.sleep(0.5)
#перейти на сайт дмайла
driver.get('https://mail.dmail.ai/login?path=%2Fcompose')
#Выбрать подключение метамаска
#тут запускаем бесконечный цикл отправить сообщение - поменять акк - отправить сообщение - ....
while True:
    try:
        print('вот тут11!!')
        mmpath = '/html/body/div/div/div/div/div[2]/div[2]/div[2]/div[2]/ul/li[1]'
        print('пробуем111')
        wait.until(EC.visibility_of_element_located((By.XPATH, mmpath)))
        print('попробовал успешно')
        time.sleep(1)
        driver.find_element(By.XPATH, mmpath).click()

        #переключиться на окно метамаска как только появится
        while True:
            try:
                window_after1 = driver.window_handles[2]
                driver.switch_to.window(window_after1)
                break
            except:
                pass

        #нажать далее подключиться подписать

        dalee = '/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]'


        podkl = '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/footer/button[2]'
        while True:
            try:
                driver.find_element(By.XPATH, dalee).click()
                break
            except:
                pass
        wait.until(EC.visibility_of_element_located((By.XPATH, podkl))).click()

        podpisat = '/html/body/div[1]/div/div/div/div[4]/footer/button[2]'
        while True:
            try:
                driver.find_element(By.XPATH, podpisat).click()
                break
            except:
                pass
        #переключиться на окно дмайла
        window_after1 = driver.window_handles[1]
        driver.switch_to.window(window_after1)


        time.sleep(1)
        #ВОТ ГДЕ ТО ТУТ ВСПЛЫВАЮЩИЕ ХУЙНИ ОТ ДМАЙЛА

        #ввести получателя, если есть всплывающие окна - прокликать их
        to = '/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/input'

        vspl1 = '/html/body/div/div/div[2]/div[3]/div/div/div[4]/a'
        while True:
            try:
                # Открыть rasseed, взять оттуда записанную цифру, засунуть ее в переменную a и добавить к ней +1
                a1 = open(rasgmails, 'r')
                a2 = list(a1)
                a3 = int(a2[0])
                a = a3 + 1
                a1.close()

                # Открыть rasseed и заменить имеющуюся цифру на +1
                a4 = open(rasgmails, 'w')
                a4.write(str(a))
                a4.close()

                # Достать адрес для отправки
                csvfile = open(gmails)
                spamreader = csv.reader(csvfile, delimiter=' ')
                gmail = list(spamreader)
                print('почта = ', gmail[a])

                while True:
                    try:
                        driver.find_element(By.XPATH, vspl1).click() #тыкаем на всплывающую штуку
                    except:
                        pass

                    try:

                        driver.find_element(By.XPATH, to).send_keys(gmail[a]) #вводим почту
                        break
                    except:
                        pass

                #ввести сабджект
                subject = '/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div[1]/input'
                # Открываем файл на чтение
                with open('msg.txt', 'r') as file:
                    lines = file.readlines()
                # Получаем случайную строчку из списка lines
                random_line1 = random.choice(lines)
                driver.find_element(By.XPATH, subject).send_keys(random_line1)
                #ввести текст
                text = '/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[5]/div/div/div/div[2]/div[1]/p[1]'
                # Открываем файл на чтение
                with open('msg.txt', 'r') as file:
                    lines = file.readlines()
                # Получаем случайную строчку из списка lines
                random_line2 = random.choice(lines)
                driver.find_element(By.XPATH, text).send_keys(random_line2)
                time.sleep(2)

                #нажать отправку сообщения, если есть всплывающие окна - прокликать
                #Тут прикол в том, что если сделать это слишком быстро - выдаст ошибку
                send = '/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/a[1]'


                error = 0  # бесполезная переменная, с ее помощью буду дектить произошло ли действие
                try:
                    driver.find_element(By.XPATH, vspl1).click() #Прокликать всплывающее сообщение если оно есть
                except:
                    pass
                try:
                    driver.find_element(By.XPATH, vspl1).click() #Прокликать всплывающее сообщение если оно есть
                except:
                    pass
                try:
                    driver.find_element(By.XPATH, vspl1).click() #Прокликать всплывающее сообщение если оно есть
                except:
                    pass
                try:
                    wait = WebDriverWait(driver, 1) #Изменение таймера wait, ждем до 1 секунды
                    print('Пробуем')
                    wait.until(EC.element_to_be_clickable((By.XPATH, send))) #Дождаться пока кнопка отправки письма станет кликабельной
                    print('Кликабельный')
                    time.sleep(5)
                    driver.find_element(By.XPATH, send).click() #Отправить письмо
                    print('Нажал')
                    wait = WebDriverWait(driver, 5) #Возвращаем значение обратно, ждем появление кнопки до 5 секунд
                    time.sleep(1)
                    try:
                        #если вылезла ошибка - закрыть ее и написать письмо заново
                        close = '/html/body/div[3]/div[3]/div/h2/span[2]'
                        driver.find_element(By.XPATH, close).click()
                        compose = '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/span[1]'
                        wait.until(EC.visibility_of_element_located((By.XPATH, compose))).click()
                        error = 1

                        print('заново')
                    except:
                        pass
                    try:
                        #если предложит сохранить содержимое письма при ошибке - прокликать
                        savemail = '/html/body/div[4]/div[3]/div/div[2]/span[1]/a'
                        driver.find_element(By.XPATH, savemail).click()
                    except:
                        pass
                    if error == 0:
                        break
                except:
                    pass
            except:
                pass

        # #переключиться на окно метамаска
        while True:
            try:
                window_after1 = driver.window_handles[2]
                driver.switch_to.window(window_after1)
                break
            except:
                pass



        print('во тут')
        # time.sleep(2000)
        money = 0 #Бесполезная переменная для детекта
        #Прокликать в метамаске, подтвердить транзу, сменить окно обратно
        while True:
            try:
                money = money + 1
                #Если недостаточно денег - скипнуть акк
                if money == 4:
                    print('недостаточно денег')
                    money = 0
                    otkl = '/html/body/div[1]/div/div/div/div[3]/div[4]/footer/button[1]'
                    driver.find_element(By.XPATH, otkl).click()
                    window_after1 = driver.window_handles[1]
                    driver.switch_to.window(window_after1)
                    break
                podtv = '/html/body/div[1]/div/div/div/div[3]/div[3]/footer/button[2]'
                wait.until(EC.element_to_be_clickable((By.XPATH, podtv)))
                time.sleep(2)
                driver.find_element(By.XPATH, podtv).click()
                time.sleep(1)
                window_after1 = driver.window_handles[1]
                driver.switch_to.window(window_after1)
                break
            except:
                pass

        print('ГОТОВО!!!')


        # поменять аккаунт
        driver.get(metamask)




        try:
            print('пробуем прокликать всплывающее')
            alert = driver.switch_to.alert
            print('текст', alert.text)
            alert.accept()
            print('прокликал всплывающее')
        except:
            pass
        time.sleep(1)
        # ввести сид фразу
        word1 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[1]/div[1]/div/input'
        word2 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[2]/div[1]/div/input'
        word3 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[3]/div[1]/div/input'
        word4 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[4]/div[1]/div/input'
        word5 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[5]/div[1]/div/input'
        word6 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[6]/div[1]/div/input'
        word7 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[7]/div[1]/div/input'
        word8 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[8]/div[1]/div/input'
        word9 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[9]/div[1]/div/input'
        word10 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[10]/div[1]/div/input'
        word11 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[11]/div[1]/div/input'
        word12 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div[3]/div[12]/div[1]/div/input'
        # driver.find_element(By.XPATH, word1).send_keys('play')
        while True:
            try:
                #Открыть rasseed, взять оттуда записанную цифру, засунуть ее в переменную a и добавить к ней +1
                a1 = open(rasseed, 'r')
                a2 = list(a1)
                a3 = int(a2[0])
                a = a3 + 1
                a1.close()

                #Открыть rasseed и заменить имеющуюся цифру на +1
                a4 = open(rasseed, 'w')
                a4.write(str(a))
                a4.close()

                #Достать сидфразу, номер сидфразы = переменная а, взятая цифра из rasseed и засунуть ее в переменную rows
                csvfile = open(seed)
                spamreader = csv.reader(csvfile, delimiter=' ')
                rows = list(spamreader)


                b1 = rows[a][0]
                b2 = rows[a][1]
                b3 = rows[a][2]
                b4 = rows[a][3]
                b5 = rows[a][4]
                b6 = rows[a][5]
                b7 = rows[a][6]
                b8 = rows[a][7]
                b9 = rows[a][8]
                b10 = rows[a][9]
                b11 = rows[a][10]
                b12 = rows[a][11]

                csvfile.close()
                break
            except:
                # если ошибка - начать с первой сидфразы
                a4 = open(rasseed, 'w')
                a4.write('-1')
                a4.close()


        while True:
            try:
                print('пробуем222')
                alert = Alert(driver)
                apert.accept()
                print('норм222')
            except:
                pass
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, word1))).send_keys(b1)
                driver.find_element(By.XPATH, word2).send_keys(b2)
                driver.find_element(By.XPATH, word3).send_keys(b3)
                driver.find_element(By.XPATH, word4).send_keys(b4)
                driver.find_element(By.XPATH, word5).send_keys(b5)
                driver.find_element(By.XPATH, word6).send_keys(b6)
                driver.find_element(By.XPATH, word7).send_keys(b7)
                driver.find_element(By.XPATH, word8).send_keys(b8)
                driver.find_element(By.XPATH, word9).send_keys(b9)
                driver.find_element(By.XPATH, word10).send_keys(b10)
                driver.find_element(By.XPATH, word11).send_keys(b11)
                driver.find_element(By.XPATH, word12).send_keys(b12)
                time.sleep(0.3)
                break
            except:
                pass
        # ввести и повторить пароль
        path5 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[2]/div[1]/div/input'
        wait.until(EC.visibility_of_element_located((By.XPATH, path5))).send_keys('1234567890')
        path6 = '/html/body/div[1]/div/div[3]/div/div/div/form/div[2]/div[2]/div/input'
        wait.until(EC.visibility_of_element_located((By.XPATH, path6))).send_keys('1234567890')
        time.sleep(0.3)
        path18 = '/html/body/div[1]/div/div[3]/div/div/div/form/button'
        wait.until(EC.visibility_of_element_located((By.XPATH, path18))).click()
        time.sleep(2)
        driver.get('https://mail.dmail.ai/login?path=%2Fcompose')
        print('ГОТОВ ЕБАШИТЬ')
    except:
        pass

