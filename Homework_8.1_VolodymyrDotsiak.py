"""Гра Blackjack має дуже прості правила: гравці беруть карти по одній намагаючись зібрати більше ніж опонент,
але не перевищуючи 21. Набір карт містить карти від 2 до 10 включно, які рахуються за їх номіналом, також
Король, Дама, Валет, що коштують по 10 кожна а також Туз, який може бути 1 або 11 в залежності від того що краще.
Вхід програми декілька карт представлені символами: 2, 3, 4, 5, 6, 7, 8, 9;  T, J, Q, K для 10, Валет, Дама, Король;
А - для Туза. Результат роботи кількість очок що не перевищує 21, або слово 'Bust' якщо сума більша за 21
(цей гравець відразу програє).
-----------------------------------------------------------------------------------------------------------------------
--> В програмі реалізований європейський різновид гри BlackJack. В європейському варіанті гри на роздачі круп'є отримує
тільки одну відкриту карту. Гравець отримує по дві карти і приймає рішення до того, як круп'є візьме другу карту. Коли
фінальна комбінація гравця сформована, круп'є добирає другу карту.
-->Якщо перша карта круп'є Туз, тоді гравець може застрахуватися від блэкджека. Для цього потрібно зробити доповнювальну
ставку на бокс, рівну половину початкової ставки. Якщо у круп'є зібрав блэкджек, то гравець отримує виигриш 2:1.
Якщо гравець на роздачі отримав блэкджек, то круп'є пропонує йому «рівні гроші»: отримати виплату відразу за
коефіцієнтом 1:1 до відкриття другої карти круп'є.
-->Якщо перша відкрита карта круп'є не Туз, гра йде за класичними правилами блэкджека.
Якщо початкова комбінація = 9, 10 чи 11 гравець може підняти ставку в два рази. При цьому йому потрібно добрати ще
карту, але тільки одну.
-->Якщо комбінація слабка, гравець може відмовитися від участі в цьому раунді, але це рішення приведе до згорання
половини ставки."""

from random import choice
from colorama import init, Fore, Style

init(autoreset=True)

"""Text styles"""
greeting_text_style = Fore.LIGHTGREEN_EX + Style.BRIGHT
information_text_style = Fore.LIGHTWHITE_EX + Style.BRIGHT
cash_text_style = Fore.LIGHTBLUE_EX + Style.BRIGHT
score_text_style = Fore.LIGHTRED_EX + Style.BRIGHT
black_jack_text_style = Fore.BLACK + Style.BRIGHT
win_text_style = Fore.LIGHTGREEN_EX + Style.BRIGHT
lose_text_style = Fore.BLACK + Style.BRIGHT
bust_text_style = Fore.RED + Style.BRIGHT
error_text_style = Fore.LIGHTRED_EX + Style.BRIGHT


def card_selection():
    deck_of_cards = ["|2♥|", "|2♠|", "|2♦|", "|2♣|", "|3♥|", "|3♠|", "|3♦|", "|3♣|", "|4♥|", "|4♠|", "|4♦|", "|4♣|",
                     "|5♥|", "|5♠|", "|5♦|", "|5♣|", "|6♥|", "|6♠|", "|6♦|", "|6♣|", "|7♥|", "|7♠|", "|7♦|", "|7♣|",
                     "|8♥|", "|8♠|", "|8♦|", "|8♣|", "|9♥|", "|9♠|", "|9♦|", "|9♣|", "|T♥|", "|T♠|", "|T♦|", "|T♣|",
                     "|J♥|", "|J♠|", "|J♦|", "|J♣|", "|Q♥|", "|Q♠|", "|Q♦|", "|Q♣|", "|K♥|", "|K♠|", "|K♦|", "|K♣|",
                     "|A♥|", "|A♠|", "|A♦|", "|A♣|"]

    cards_values = {"|2♥|": 2, "|2♠|": 2, "|2♦|": 2, "|2♣|": 2, "|3♥|": 3, "|3♠|": 3, "|3♦|": 3, "|3♣|": 3, "|4♥|": 4,
                    "|4♠|": 4, "|4♦|": 4, "|4♣|": 4, "|5♥|": 5, "|5♠|": 5, "|5♦|": 5, "|5♣|": 5, "|6♥|": 6, "|6♠|": 6,
                    "|6♦|": 6, "|6♣|": 6, "|7♥|": 7, "|7♠|": 7, "|7♦|": 7, "|7♣|": 7, "|8♥|": 8, "|8♠|": 8, "|8♦|": 8,
                    "|8♣|": 8, "|9♥|": 9, "|9♠|": 9, "|9♦|": 9, "|9♣|": 9, "|T♥|": 10, "|T♠|": 10, "|T♦|": 10,
                    "|T♣|": 10, "|J♥|": 10, "|J♠|": 10, "|J♦|": 10, "|J♣|": 10, "|Q♥|": 10, "|Q♠|": 10, "|Q♦|": 10,
                    "|Q♣|": 10, "|K♥|": 10, "|K♠|": 10, "|K♦|": 10, "|K♣|": 10, "|A♥|": 11, "|A♠|": 11,
                    "|A♦|": 11, "|A♣|": 11}
    deck_of_cards *= 6  # При роздачі зазвичай використовують 4-6 тасованих колод карт

    selected_card = choice(deck_of_cards)
    selected_card_value = cards_values.get(selected_card)
    return selected_card, selected_card_value


def first_deal_of_cards():
    """Перша роздача карт. Гравець бере дві карти, а круп'є одну"""
    player_deck_power = 0
    print(information_text_style + f"\nГравець отримує карти: ", end="")
    for i in range(2):
        new_card = card_selection()
        print(f"{new_card[0]} ", end="")
        if new_card[1] == 11:
            ace_choice = input(information_text_style + " Виберіть коефіцієнт туза (1 або 11): ")
            while ace_choice != "1" and ace_choice != "11":
                ace_choice = input(information_text_style + " Виберіть коефіцієнт туза (1 або 11): ")
            if ace_choice == "1":
                player_deck_power += 1
            elif ace_choice == "11":
                player_deck_power += 11
        else:
            player_deck_power += new_card[1]
    print(information_text_style + f"Сила колоди:", score_text_style + f"{player_deck_power}")
    new_card = card_selection()
    croupier_deck_power = new_card[1]
    print(information_text_style + "Круп'є отримує карту: ", f"{new_card[0]}", end=" ")
    print(information_text_style + f"Сила колоди:", score_text_style + f"{croupier_deck_power}")
    return player_deck_power, croupier_deck_power


def dealer_takes_the_card(player_blackjack, croupier_deck_power, player_deck_power):
    """Функція, в якій записана 'поведінка' круп'є при випадінні певної карти"""
    if player_blackjack:
        while croupier_deck_power < 21:
            new_card = card_selection()
            print(information_text_style + f"Круп'є випала карта: {new_card[0]}")
            if new_card[1] + croupier_deck_power == 21:
                croupier_deck_power += 11
            else:
                croupier_deck_power += 1
            croupier_deck_power += new_card[1]
    else:
        while croupier_deck_power < player_deck_power:
            new_card = card_selection()
            print(information_text_style + f"Круп'є випала карта: {new_card[0]}")
            croupier_deck_power += new_card[1]
        return croupier_deck_power


def event_player_blackjack(croupier_deck_power):
    """Якщо гравець погодиться на нічийну ставку, то одразу же виграє гроші з коефіцієнтом 1:1
    В іншому випадку гра продовжиться по звичним правилам"""
    print(information_text_style + "Хочете зробити нічийну ставку? Коефіцієнт виграшу 1:1 (Yes/No)")
    player_blackjack_choice = input()
    while player_blackjack_choice != "Yes" and player_blackjack_choice != "No":
        print(error_text_style + "Неправильна команда!")
        player_blackjack_choice = input()
    print(information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
    if player_blackjack_choice == "Yes":
        return "Player Win", 2
    elif player_blackjack_choice == "No":
        croupier_choice = dealer_takes_the_card(True, croupier_deck_power, None)
        if croupier_choice == 21:
            return "Push", 0
        else:
            return "Player Win", 2.5


def do_insurance(player_deck_power, croupier_deck_power):
    """Якщо гравець погодиться на страхівку і круп'є випаде Блекджек, гравець отримає виграш.
     В іншому випадку буде нічия"""
    print(information_text_style + "\nДоступна страхівка від Блекджека. Ціна 50% початкової ставки!  Yes/No")
    player_insurance_choice = input()
    while player_insurance_choice != "Yes" and player_insurance_choice != "No":
        print(error_text_style + "Неправильна команда!")
        player_insurance_choice = input()
    if player_insurance_choice == "Yes":
        new_card = card_selection()
        croupier_deck_power += new_card[1]
        print(information_text_style + f"Круп'є випала карта: {new_card[0]}")
        if croupier_deck_power == 21:
            return "Player Win", 1.50
        else:
            return "Push", 0
    else:
        return do_hit_stand_surrender(player_deck_power, croupier_deck_power)


def do_double_bet(player_deck_power, croupier_deck_power):
    """Якщо сила колоди гравця після першої роздачі == 9, 10 чи 11, він може подвоїти ставку і добрати одну
    додаткову карту"""
    print(information_text_style + "\nДоступне подвоєння ставки. Ціна +100% від початкової ставки!  Yes/No")
    player_double_choice = input()
    while player_double_choice != "Yes" and player_double_choice != "No":
        print(error_text_style + "Неправильна команда!")
        player_double_choice = input()
    if player_double_choice == "Yes":
        new_card = card_selection()
        print(information_text_style + f"Вам випала карта: {new_card[0]}")
        if new_card[1] == 11:
            ace_choice = input(information_text_style + " Виберіть коефіцієнт туза (1 або 11): ")
            while ace_choice != "1" and ace_choice != "11":
                ace_choice = input(information_text_style + " Виберіть коефіцієнт туза (1 або 11): ")
            if ace_choice == "1":
                player_deck_power += 1
            elif ace_choice == "11":
                player_deck_power += 11
        else:
            player_deck_power += new_card[1]
        croupier_deck_power = dealer_takes_the_card(False, croupier_deck_power, player_deck_power)
        print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
              information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
        if croupier_deck_power > 21:
            print(bust_text_style + "Croupier bust!")
            return "Player Win", 4
        elif croupier_deck_power < 21:
            print(bust_text_style + "Player Lose!")
            return "Player Lose", 2
        if croupier_deck_power < player_deck_power:
            return "Player Win", 4
        elif croupier_deck_power > player_deck_power:
            return "Player Lose", 2
        else:
            return "Push", 0
    else:
        return do_hit_stand_surrender(player_deck_power, croupier_deck_power)


def do_hit_stand_surrender(player_deck_power, croupier_deck_power):
    """Hit - взяти додаткову карту, Stand - більше не добирати карт і передати хід круп'є,
    Surrender - здатись і отримати 50% від початкової ставки"""
    print(information_text_style + f"\nВиберіть дію: Hit, Stand, Surrender")
    player_move = input()
    while player_move != "Hit" and player_move != "Stand" and player_move != "Surrender":
        print(error_text_style + "Неправильна команда!")
        player_move = input()
    if player_move == "Hit":
        new_card = card_selection()
        print(information_text_style + f"Вам випала карта: {new_card[0]}")
        if new_card[1] == 11:
            ace_choice = input(information_text_style + " Виберіть коефіцієнт туза (1 або 11): ")
            while ace_choice != "1" and ace_choice != "11":
                ace_choice = input(information_text_style + " Виберіть коефіцієнт туза (1 або 11): ")
            if ace_choice == "1":
                player_deck_power += 1
            elif ace_choice == "11":
                player_deck_power += 11
        else:
            player_deck_power += new_card[1]
        print(information_text_style + f"Сила колоди: {player_deck_power}")
        if player_deck_power > 21:
            print(bust_text_style + "Player bust!")
            return "Player Lose", 1
        else:
            return do_hit_stand_surrender(player_deck_power, croupier_deck_power)
    elif player_move == "Stand":
        croupier_deck_power = dealer_takes_the_card(False, croupier_deck_power, player_deck_power)
        if croupier_deck_power > 21:
            print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
                  information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
            print(bust_text_style + "Croupier bust!")
            return "Player Win", 2
        else:
            print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
                  information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
            return "Player Lose", 1
    elif player_move == "Surrender":
        print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
              information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
        return "Player Lose", 0.5

    if croupier_deck_power > 21:
        print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
              information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
        print(bust_text_style + "Croupier bust!")
        return "Player Win", 2
    elif croupier_deck_power < player_deck_power:
        print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
              information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
        return "Player Win", 2
    elif croupier_deck_power > player_deck_power:
        print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
              information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
        return "Player Lose", 1
    else:
        print(information_text_style + "Сила колоди гравця", score_text_style + f"{player_deck_power}",
              information_text_style + "та круп'є:", score_text_style + f"{croupier_deck_power}")
        return "Push", 0


def determining_the_winner():
    first_cards = first_deal_of_cards()
    player_deck_power = first_cards[0]
    croupier_deck_power = first_cards[1]
    if player_deck_power == 21:
        print(black_jack_text_style + "BlackJack!\n")
        return event_player_blackjack(croupier_deck_power)
    elif croupier_deck_power == 11:
        return do_insurance(player_deck_power, croupier_deck_power)
    elif 12 > player_deck_power > 8:
        return do_double_bet(player_deck_power, croupier_deck_power)
    else:
        return do_hit_stand_surrender(player_deck_power, croupier_deck_power)


def player_doing_bet():
    chip_1 = (Fore.WHITE + "〖𝟏〗")
    chip_5 = (Fore.RED + "〖5〗")
    chip_25 = (Fore.GREEN + "〖25〗")
    chip_50 = (Fore.BLUE + "〖50〗")
    chip_100 = (Fore.BLACK + "〖100〗")
    chip_500 = (Fore.MAGENTA + "〖500〗")
    chip_1000 = (Fore.YELLOW + "〖1000〗")
    print(information_text_style + f"Зробіть свою ставку {chip_1}{chip_5}{chip_25}{chip_50}{chip_100}"
                                   f"{chip_500}{chip_1000}", end="" f":\n")
    bet = input()
    while bet != "1" and bet != "5" and bet != "25" and bet != "50" and bet != "100" and bet != "500" and bet != "1000":
        print(error_text_style + "Неправильна ставка!")
        bet = input()
    bet = int(bet)
    return bet


def announcement_of_results():
    player_cash = 1000
    while player_cash >= 1:
        print(information_text_style + "На вашому рахунку", cash_text_style + f"{player_cash}$")
        player_bet = player_doing_bet()
        score = determining_the_winner()
        if score[0] == "Player Win":
            player_cash += player_bet * score[1]
            print(win_text_style + f"Ви виграли {player_bet * score[1]}$!\n\n")
        elif score[0] == "Player Lose":
            player_cash -= player_bet * score[1]
            print(lose_text_style + f"Ви програли {player_bet * score[1]}$!\n\n")
        elif score[0] == "Push":
            player_cash += player_bet * score[1]
            print(information_text_style + f"Нічия!\n\n")
    else:
        print(score_text_style + f"На вашому рахунку {player_cash}$! Game Over!")


def main():
    print(greeting_text_style + "{:>40}".format("European BlackJack!"))
    print(information_text_style + "-" * 60)
    announcement_of_results()


if __name__ == "__main__":
    main()
