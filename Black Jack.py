import time
import random

card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
card_dict = {
    0: "Ace",
    1: "Two",
    2: "Three",
    3: "Four",
    4: "Five",
    5: "Six",
    6: "Seven",
    7: "Eight",
    8: "Nine",
    9: "Ten",
    10: "Jack",
    11: "Queen",
    12: "King",
}
Suit_dict = {
    0: "Hearts",
    1: "Diamonds",
    2: "Clubs",
    3: "Spades",
}

alt_total = 0


def deal():
    suit = random.randint(0, 3)
    face_card = random.randint(0, 12)
    card = [suit, face_card]
    return card


def card_to_string(card):
    suit = Suit_dict.get(card[0])
    face = card_dict.get(card[1])
    return f"{suit} {face}"


def ace_count(hand):
    counter = 0
    for i in current_hand:
        if i == 0:
            counter += 1
    return counter


def total_counter(hand):
    sum = 0
    for i in range(len(hand)):
        if 10 > hand[i] > 0:
            sum += hand[i] + 1
        elif hand[i] > 9:
            sum += 10
        else: sum += 11

    return sum


if __name__ == "__main__":
    print(logo)
    user = input("The dealer looks to you, care to try your luck? (Y/N)")
    wins = 0
    losses = 0
    inner_next_play = "O"


    if user == "Y":
        running = 1
        while running == 1:


            print(f"wins: {wins}")
            print(f"losses: {losses}")

            print("The dealer shuffles and plays the cards")
            current_hand = []
            dealer_hand = []
            time.sleep(2)

            card1 = deal()
            current_hand.append(card1[1])
            card1 = card_to_string(card1)
            card2 = deal()
            current_hand.append(card2[1])
            card2 = card_to_string(card2)


            print(f"You are delt {card1} {card2}")
            total = total_counter(current_hand)
            print(f"Your total is {total}")
            if total == 21:
                print("BLACKJACK! You Win!")
                wins += 1
                user = input("Another round? (Y/N)")
                if user == "Y":
                    continue
                else:
                    break


            aces = ace_count(current_hand)
            if aces >= 1:
                for i in range(1, aces):
                    alt_total = total - 10 * i
                    print(f"Or your total is {alt_total}")
                    alt_total = 0

            dealer1 = deal()
            dealer_hand.append(dealer1[1])
            dealer1 = card_to_string(dealer1)


            print("The Dealer plays")
            dealer_total = total_counter(dealer_hand)
            print(f"The dealer has {dealer1}")
            print(f"The Dealers total is {dealer_total}")
            dealer_aces = ace_count(current_hand)
            if dealer_aces >= 1:
                for i in range(1, len(dealer_aces)):
                    alt_total = dealer_total - 10 * i
                    print(f"Or Their total is {alt_total}")
                    alt_total = 0

            next_play = input("Do you [H]it or [S]tay?")
            if next_play == "H":
                long_play = 1

                while long_play == 1:
                    round_counter = 2
                    card = deal()
                    current_hand.append(card[1])
                    card = card_to_string(card)
                    print(f"You are delt {card}")
                    total = total_counter(current_hand)
                    aces = ace_count(current_hand)

                    if aces >= 1:
                        for i in range(1, aces):
                            alt_total = total - 10 * i
                            if alt_total <= 21 < total:
                                print(f"Your total is {alt_total}")
                            elif total < 21:
                                print(f"Your total is {total} or {alt_total}")
                            elif total > 21 and alt_total > 21:
                                print("Bust!")
                                losses += 1
                                inner_next_play = input("Another round? (Y/N)")
                                if inner_next_play == "Y":
                                    break
                                else:
                                    long_play, running = 0, 0
                    elif total > 21:
                        print(f"Your total is {total} you are BUST!")
                        losses += 1
                        inner_next_play = input("Another round? (Y/N)")
                        if inner_next_play == "Y":
                            break
                        else:
                            long_play, running = 0, 0
                            break

                    print(f"Your total is {total}")
                    inner_next_play = input("Do you [H]it or [S]tay?")
                    if inner_next_play == "H":
                        round_counter += 1
                        continue
                    else:
                        break


            if inner_next_play == "Y":
                continue


            print("The Dealer plays")

            dealer_alive = 1
            while dealer_alive == 1:
                time.sleep(0.5)
                counter = 1
                dealer = deal()
                dealer_hand.append(dealer[1])
                dealer = card_to_string(dealer)
                dealer_total = total_counter(dealer_hand)
                dealer_aces = ace_count(current_hand)
                print(f"The dealer has {dealer}")
                if dealer_aces == 0:
                    print(f"The Dealers total is {dealer_total}")
                elif dealer_aces >= 1 and dealer_total > 21:
                    for i in range(1, dealer_aces):
                        alt_total = dealer_total - 10 * i
                        print(f"The Dealers total is {alt_total}")
                        alt_total = 0
                elif dealer_aces >= 1 and dealer_total < 21:
                    for i in range(1, dealer_aces):
                        alt_total = dealer_total - 10 * i
                        print(f"The Dealers total is {dealer_total}")
                        print(f"Or Their total is {alt_total}")
                        alt_total = 0


                if total <= dealer_total <= 21:
                    print("The Dealer wins")
                    losses += 1
                    inner_next_play = input("Another round? (Y/N)")
                    if inner_next_play == "Y":
                        break
                    else:
                        running = 0
                        break
                elif dealer_total > 21:
                    print("The Dealer is BUST, You Win!")
                    wins += 1
                    inner_next_play = input("Another round? (Y/N)")
                    if inner_next_play == "Y":
                        break
                    else:
                        running = 0
                        break



