import pyautogui
import time
import pandas

#cadastrar um produto automaticamente (bot)


#entra no site 
pyautogui.press("win")
pyautogui.PAUSE = 0.7
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.PAUSE = 1
pyautogui.click(x=377, y=87)

#pesquisar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#digitar\clicar

pyautogui.PAUSE = 1
pyautogui.click(x=774, y=464)
pyautogui.write("emaildealguem@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")
pyautogui.PAUSE = 1


#criar variavel para ver uma tabela

tabela = pandas.read_csv

#preencher um item com toda as especificaçoes
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=705, y=322)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll()
