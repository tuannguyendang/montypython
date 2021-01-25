def tally():
    score = 0
    while True:
        increment = yield score
        score += increment


white_sox = tally()
blue_jays = tally()

print(next(white_sox))
print(next(blue_jays))

print(white_sox.send(3))
print(blue_jays.send(2))
print(white_sox.send(2))
print(blue_jays.send(4))
