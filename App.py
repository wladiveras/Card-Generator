import inquirer
import template.ReturnTemplate as T
from inquirer.themes import GreenPassion

# ! ########################################################
# ! FIRST STEP :: Questions setup                          #
# ! ########################################################

in_first = [
    inquirer.Text('id',
                  message='Digite um ID para o cartão (ex: 15)',
                  ),

    inquirer.List('isBack',
                  message='O cartão contém frente e verso?',
                  choices=['sim', 'nao'],
                  default='nao'),

    inquirer.List('isPhoto',
                  message='O cartão contem foto?',
                  choices=['sim', 'nao'],
                  default='sim'),

    inquirer.Text('FrontInput',
                  message='Quantos campos contem na frente do cartão?',
                  default='1'),
]

FirstStep = inquirer.prompt(in_first, theme=GreenPassion())

# ! ########################################################
# ! SECOND STEP :: Only if exist Card Backside             #
# ! ########################################################

# ? Verify is card contain backside
if(FirstStep['isBack'] == 'sim'):

    in_second = [
        inquirer.Text('BackInput',
                      message='Quantos campos contem no verso do cartão?',
                      default='1'),
    ]

    SecondStep = inquirer.prompt(in_second, theme=GreenPassion())
# todo: endif

# ! ########################################################
# ! While Input :: While asking input name                 #
# ! ########################################################

print("\n\n >> Agora, informe o nome de cada campo que ira conter na FRENTE do cartão")

# ? Define vars to While Function and Input ask list
CurrentFrontInput = 0
CurrentBackInput = 0
FrontInputName = list()
BackInputName = list()

# ? Generate cards by @FirstStep['FrontInput'] value
while CurrentFrontInput < int(FirstStep['FrontInput']):

    FrontInputName.append(
        input(" > Qual o nome do " + str(CurrentFrontInput + 1) + "° campo?: "))
    CurrentFrontInput += 1
# todo: endwhile

# ? Generate cards by @SecondStep['BackInput'] value only if FirstStep['isBack'] == sim
if(FirstStep['isBack'] == 'sim'):
    print("\n\n >> Maravilha, agora informe o nome de cada campo que ira conter no VERSO do cartão")

    while CurrentBackInput < int(SecondStep['BackInput']):
        BackInputName.append(
            input(" > Qual o nome do " + str(CurrentBackInput + 1) + "° campo?: "))
        CurrentBackInput += 1
    # todo: endwhile
# todo: endif

# ! ########################################################
# !           xxx                                          #
# ! ########################################################
