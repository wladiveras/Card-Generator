import inquirer

from inquirer.themes import GreenPassion

# ! ########################################################
# ! FIRST STEP                                             #
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

    inquirer.Text('front_inputs',
                  message='Quantos campos contem na frente do cartão?',
                  default='1'),
]

FirstStep = inquirer.prompt(in_first, theme=GreenPassion())

# ! ########################################################
# ! SECOND STEP                                             #
# ! ########################################################

# ? Verify is card contain backside
if(FirstStep['isBack'] == 'sim'):

    in_second = [
        inquirer.Text('back_inputs',
                      message='Quantos campos contem no verso do cartão?',
                      default='1'),
    ]

    SecondStep = inquirer.prompt(in_second, theme=GreenPassion())
# todo: endif

print("Agora, informe o nome que ira conter na FRENTE do cartão")

CurrentFrontInput = 0
CurrentBackInput = 0
FrontInputName = list()
BackInputName = list()

# ? Generate cards by @FirstStep['front_inputs'] value
while CurrentFrontInput < int(FirstStep['front_inputs']):
    FrontInputName.append(
        input("Qual o nome do " + str(CurrentFrontInput + 1) + "° campo?: "))
    CurrentFrontInput += 1
# todo: endwhile

# ? Generate cards by @SecondStep['back_inputs'] value only if FirstStep['isBack'] == sim
if(FirstStep['isBack'] == 'sim'):
    print("Agora, informe o nome que ira conter no VERSO do cartão")

    while CurrentBackInput < int(SecondStep['back_inputs']):
        BackInputName.append(
            input("Qual o nome do " + str(CurrentBackInput + 1) + "° campo?: "))
        CurrentBackInput += 1
# todo: endwhile
# todo: endif

print(FrontInputName)
print(BackInputName)


# ! ########################################################
# !           xxx                                          #
# ! ########################################################
