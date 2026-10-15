tag = input('what is your gamer tag?')
fav_game = input('what is your favorite game?')
hours = float(input('how many hours do you play per day'))
weeks = int(input('how many weeks do you play'))
days = int(input('how many days a week do you play? '))
weekly_hours = hours * days
yearly_hours = weekly_hours * 52

print('hello', tag, "you play", fav_game, "and you spend", hours, "hours on", fav_game, "and your yearly hours are", yearly_hours)
