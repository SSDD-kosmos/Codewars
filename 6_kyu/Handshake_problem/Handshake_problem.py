def test():
    handshakes = 7
    get_participants(handshakes)


def get_participants(handshakes):
    participants = 0
    while handshakes > 0:
        handshakes -= participants
        participants += 1
    print(participants)
    return participants


test()
