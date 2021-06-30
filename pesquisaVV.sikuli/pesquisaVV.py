url = "http://www.lourencodemonaco.com.br/vvtest/"
nome = "Luiz"
sobrenome = "Piva"
email = "tazlfdp@gmail.com"
email_confirm = "tazlfdp@gmail.com"
tel = "11980237384"
linguagem = "Python"
plano = ("Melhorar meu skill com testes automatizados e buscar um cargo de lider")

def abreSite():
    app = App("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    if (app.isRunning()):
        App.open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        type("n", Key.CTRL)
    else:    
        App.open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    #maximiza a janela 
    sleep(3)   
    type(Key.SPACE + "x", KeyModifier.ALT)
    paste(url)
    sleep(1)
    type(Key.ENTER)
    wait("1625064235013.png",15)
    #abre pagina da pesquisa
    click("1625067511717.png")
    #valida pagina
    wait("1625067566990.png",15)

def preencheForm():
   
    wheel(WHEEL_DOWN,3)
    click(Pattern("1625067661840.png").targetOffset(-3,23))
    type(nome)
    type(Key.TAB)
    type(sobrenome)
    type(Key.TAB)
    type(email)
    type(Key.TAB)
    type(email_confirm)
    type(Key.TAB)
    type(tel)
    type(Key.TAB)
    #seleciona idade
    click(Pattern("1625068250448.png").targetOffset(-27,-1))
    type(Key.TAB)
    type("mais")
    type(Key.TAB)
    type("sou")
    type(Key.TAB)
    click(Pattern("1625069364664.png").targetOffset(-38,0))
    type(Key.TAB)
    type(linguagem)
    type(Key.TAB)
    type(plano)
    type(Key.TAB)
    click("1625069492135.png")
    wait("1625074530663.png",30)
    print("Formulario enviado") 
   
#chamada dos defs
abreSite()
preencheForm()