import csv
import os 
import PySimpleGUI as sg

#janela1
def Janela_Login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Bem vindo(a),')],
        [sg.Text('Digite seu E-mail')],
        [sg.Input(key="Email")],
        [sg.Button('Continuar'),sg.Button('Voltar')],
    ]
    return sg.Window('Login', layout=layout,finalize=True)
#janela2
def Janela_Estoque():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Seu estoque atual')],
        [sg.Output(size=(65, 15),font='Courier 10')],
        [sg.Button('Adicionar'),sg.Button('Atualizar'),sg.Button('Retornar')],
    ]
    return sg.Window('Area Estoque',layout=layout,finalize=True)
#janela3
def Janela_Adicionar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Adicionar Produto')],
        [sg.Text('Produto')],
        [sg.Input(key="Produto")],
        [sg.Text('Quantidade')],
        [sg.Input(key="quantidade",size=(5,4))],
        [sg.Text('Codigo')],
        [sg.Input(key="Codigo")],
        [sg.Button('Confirmar'),sg.Button('Voltar')],
    ]
    return sg.Window('Area de Cadastro',layout=layout,finalize=True)

    
janela1,janela2,janela3 = Janela_Login(), None, None,
while True:
    window, event,value = sg.read_all_windows()
    if janela1 and  event == sg.WIN_CLOSED:
        break
    if janela2 and event == sg.WIN_CLOSED:
        break
    if janela3 and event == sg.WIN_CLOSED:
        break
# Eventos janela1 
    if window == janela1 and event == 'Continuar':
        f = open('usuario.csv','w', newline='', encoding='UTF-8')
        writer = csv.writer(f)
        writer.writerow([value])
        f.close()
        janela2 = Janela_Estoque()
        janela1.hide()
        janela2.un_hide()
        
    if window == janela1 and event == 'Voltar':
        break
# Eventos janela2
    if window == janela2 and event == 'Retornar':
        janela1 = Janela_Login()
        janela2.hide()
        
    if janela2 and event =='Atualizar':
        with open("Produto.csv", "r") as arquivos:
            Estoque = arquivos.read()
            print(Estoque)
                   
    if janela2 and event == 'Adicionar':
       janela3 = Janela_Adicionar()
       janela2.hide()
                
# Eventos janela3

    if window == janela3 and event == 'Confirmar':
        produto = open('Produto.csv','w', newline='', encoding='UTF-8')
        writer = csv.writer(produto)
        writer.writerow([value])
        produto.close()
        janela2 = Janela_Estoque()
        janela3.hide()
        janela2.un_hide()
        sg.popup('Produto adicionado com sucesso')
    if window == janela3 and event == 'Voltar':
        janela2 = Janela_Estoque()
        janela3.hide()
         