import projeto_mod_1_escolhapersonagem

import time
from termcolor import cprint
import pyfiglet


def jogar1():
    explicacao_missao_vampesley()

def explicacao_biblioteca():
    print('\nNa biblioteca do castelo, você encontra um livro com uma página marcada...')
    time.sleep(1)
    print('quando abre na página encontra um pergaminho dobrado. Abre o pergaminho e lê:')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('\n***ATENÇÃO*** essa é uma conta que você deve fazer de cabeça!')
    time.sleep(1)
    print('Só faça a conta com a calculadora depois para conferir se acertou.\n')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('\nCOMECE COM 1.000, SOME 40 E DEPOIS SOME MAIS 1.000. ADICIONE 30 E DEPOIS SOME MAIS 1.000.')
    time.sleep(1)
    print('AGORA, SOME MAIS 20 E VOLTE A SOMAR MAIS 1.000. PARA FINALIZAR JUNTE MAIS 10 À CONTA.\n')
    cprint('-'* 80, 'red')
    enimga_biblioteca_calculo()


def explicacao_banheiro_escrito_sangue():
    print('\nAo entrar no banheiro, viu uma cortina do boxe escrita com sangue, os seguintes dizeres:\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('INVISÍVEL, PORÉM PRESENTE, MUTÁVEL, MAS SEMPRE CONSTANTE, ME APRESENTO DE VÁRIAS FORMAS,')
    time.sleep(1)
    print('MAS NENHUMA SERÁ BELA, DIGA-ME QUEM SOU...')
    time.sleep(1)
    print('Quem sou eu?')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('\n***Dica*** _ _ _ _ _ ')
    enimga_palavra_banheiro()


def explicacao_encontro_menininha():
    print('\nAndando pelo castelo, você encontra uma menininha pálida e solitária.')
    time.sleep(1)
    print('Boatos que ela sabe as passagens secretas do castelo onde estão as recompensas...\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. tentar conversar com ela')
    time.sleep(1)
    print('2. perguntar se há algum outro enigma para solucionar')
    cprint('-'* 80, 'red')
    interacao_menininha()


def explicacao_missao_vampesley():
    print('\nPoucos são os que notariam o estranho movimento em um castelo abandonado, porém de requinte, em uma área reservada da cidade.')
    time.sleep(1)
    print('Para olhos destreinados, passam despercebidas as figuras pálidas que nele entram movidas a curiosidade...')
    time.sleep(1)
    print('Sedentas por um desaviado e às vezes, até para explorar o local.\n')
    time.sleep(1)

    print('SUA MISSÃO É:')
    time.sleep(1)
    print('decifrar incógnitas e responder o enigma final para receber: sangue e ouro.\n')
    time.sleep(1)
    print('Você está na porta do castelo RedGold, {}, mas parece que a porta tem um enigme para abri-la.'.format(nome_personagem))
    time.sleep(1)
    print('Digite o número correspondente a ação que deseja:')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. Desistir e ir embora (nem combina com você)')
    time.sleep(1)
    print('2. Ver enigma!')
    cprint('-'* 80, 'red')
    resposta_abrir_porta_nao_entrou()

nome_personagem = 'Vampesley'


def jogar_novamente():
    jogar_novamente = input('\nDeseja jogar novamente? [S/N]:')
    if (jogar_novamente.upper().strip() == 'S'):
        projeto_mod_1_escolhapersonagem.escolha_personagem()
    elif(jogar_novamente.upper().strip() == 'N'):
        print('Até a próxima!')



def resp_desistiu_entrar():
    condicao = True
    while condicao:
        resp_desistiu = int(input('Digite sua escolha [1 ou 2]:'))
        if (resp_desistiu == 1) or (resp_desistiu == 2):
                print('\nAo desistir de entrar, você resolveu ficar do lado de fora, embaixo de uma árvore com um galho no canto da boca observando...')
                time.sleep(2)
                print('Porém o galho era de verbena, sua mania de viver mastigando, te levou para outro plano...\n')
                cprint('-'* 80, 'red')
                time.sleep(1)
                cprint('GAME OVER! MORREU TORRADO.', 'yellow', 'on_red', attrs=['bold'])
                time.sleep(1)
                jogar_novamente()
                condicao = False
        else:
            print('Resposta inválida')

def explicacao_resp_enigma_porta():
    cprint('\n----------------*ENIGMA DA PORTA*----------------\n', 'red', attrs=['bold'])
    time.sleep(1)
    cprint('QUANDO O SOL SUBIR PELA MONTANHA, AS AVES IRÃO VOAR PARA CAÇAR AS SERPENTES QUE ESTÃO NO CHÃO\n', attrs=['bold'])
    time.sleep(1)
    print('Qual a sequência de comandos?\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. ↑ ↓ ↑ ↓')
    print('2. ↑ ← ↑ ↓')
    cprint('-'* 80, 'red')
    resp_enigma_porta()

    
def resp_enigma_porta():    
    resp_enigma = int(input('Digite sua resposta [1 ou 2]:'))

    if resp_enigma == 1:
        print('\nA porta é amaldiçoada e quem erra o enigma paga com a vida.')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('GAME OVER!!!', 'yellow', 'on_red', attrs=['bold'])
        time.sleep(1)
        jogar_novamente()
    else:
        if resp_enigma == 2:
            print('\nEssa foi por pouco, hein? Não queria falar nada não, mas quem errou o enigma já não se encontra entre nós.')
            time.sleep(1)
            print('Parabéns, sua coragem e perspicacia te mantiveram vive no jogo.'.format(nome_personagem))
            explicacao_encontro_menininha()
        else:
            print('Resposta inválida!')
            print(resp_enigma_porta())


def resposta_abrir_porta_nao_entrou ():
    resposta_pergunta_abrir_porta = int(input('Digite sua escolha [1 ou 2]:'))
    if (resposta_pergunta_abrir_porta == 1):
        print('\nNenhuma novidade, não é meu caro, {}.\n'.format(nome_personagem))
        time.sleep(1)
        print('Este sua cara de "poucos amigos" diz muito sobre você...')
        time.sleep(1)
        print('Porque você desistiu de entrar?\n')
        cprint('-'* 80, 'red')
        time.sleep(1)
        print('1. Sinto uma estranha ligação com o castelo mas não estou pronto para isso.')
        time.sleep(1)
        print('2. Tô com fome!')
        cprint('-'* 80, 'red')
        resp_desistiu_entrar()
    elif (resposta_pergunta_abrir_porta == 2):
            explicacao_resp_enigma_porta()
    else:
        print('Resposta inválida')
        resposta_abrir_porta_nao_entrou()



def interacao_menininha ():
    resp_pergunta_menininho = int(input('Digite o número correspondente a ação que deseja:'))
    if (resp_pergunta_menininho == 1):
        print('...')
        time.sleep(2)
        print('após um longo período de silêncio,')
        time.sleep(2)
        print('você se lembra que parte dos boatos também diziam que ela não responde perguntas diretas sobre o castelo...')
        interacao_menininha ()
    
    elif (resp_pergunta_menininho == 2):
            cprint('-'* 80, 'red')
            print('\nEla aponta para uma porta aberta, que lembrava um banheiro, mas não diz uma palavra.')
            explicacao_banheiro_escrito_sangue()
    
    else:
        print('Resposta inválida!')
        interacao_menininha()



def enimga_palavra_banheiro():
    resp_enigma_palavra = input('\nDigite sua resposta:')
    if (resp_enigma_palavra.lower().strip() == 'morte'):
        print('\nGenial! A resposta está correta!')
        time.sleep(1)
        print('Impressionate sua perspicácia. Com tamanha inteligência está ficando fácil ganhar o que veio buscar.')
        time.sleep(1)
        explicacao_biblioteca()

    else:
        print('Cué, cué, cué, cuééééé...')
        time.sleep(1)
        cprint('GAME OVER!!!', 'yellow', 'on_red', attrs=['bold'])
        jogar_novamente()


def enimga_biblioteca_calculo ():
    resp_enigma_calculo = int(input('Digite o valor da soma?'))
    if (resp_enigma_calculo == 4100):
        print('\nIHULLLLLLLLL!')
        time.sleep(1)
        print('ACERTOOOOOU, você é mais novo imortal cheio dos recursos do pedaço! Sangue à vontade e ainda barras de ouro?')
        time.sleep(1)
        print('Aproveita e melhora essa cara, né? :P')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('***** FIM DE JOGO *****', 'blue', attrs=['bold'])
        jogar_novamente()
    else:
        print('\nPerder no chefão é triste, né? Mas você pode tentar de novo...')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('GAME OVERRRRRRR!!!', 'yellow', 'on_red', attrs=['bold'])
        cprint('***** FIM DE JOGO *****', 'red', attrs=['bold'])
        jogar_novamente()
    


if __name__ == '__main__':
    jogar1()