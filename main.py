import PySimpleGUI as sg
from board import Board

sg.theme('DarkAmber')

boardSize = 6
player = Board(False)
enemy = Board()

leftColumn = [[sg.Text('TEXT', key='-TEXT-SHIPS-')]] + [[sg.Button(size=(
    1, 1), key=f'-SHIP{i}{j}-') for j in range(boardSize)] for i in range(boardSize)]
rightColumn = [[sg.Text('TEXT', key='-TEXT-SHOTS-')]] + [[sg.Button(
    size=(1, 1), key=f'-SHOT{i}{j}-') for i in range(boardSize)] for j in range(boardSize)]
layout = [[sg.Column(leftColumn),
           sg.VerticalSeparator(),
           sg.Column(rightColumn)]]

window = sg.Window('battle', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event[:5] == '-SHIP':
        row = int(event[5])
        col = int(event[6])
        shipsAmount = len(player.ships)

        if shipsAmount < 4:
            player.addShip(1, row, col)
            window[event].update(disabled=True, button_color=(
                'black', 'black'))
        elif shipsAmount < 6:
            coordinates = player.addShip(2, row, col)
            for i in range(len(coordinates)):
                window[event[:5] + str(coordinates[i][0]) + str(
                    coordinates[i][1]) + '-'].update(disabled=True, button_color=('black', 'black'))
        elif shipsAmount == 6:
            coordinates = player.addShip(3, row, col)
            for i in range(len(coordinates)):
                window[event[:5] + str(coordinates[i][0]) + str(
                    coordinates[i][1]) + '-'].update(disabled=True, button_color=('black', 'black'))
            for i in range(boardSize):
                for j in range(boardSize):
                    window[f'-SHIP{i}{j}-'].update(disabled=True)

window.close()
