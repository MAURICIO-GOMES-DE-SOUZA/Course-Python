# repetiçoes
print("Start")

count = 0
while count < 10:
    count += 1
    print(count)
    
print("End")

musics = [ "Time", "Bateu 20h", "Clocks", "Menina Veneno", "Morango do nordeste" ]

index_music = 0
while index_music < len(musics) - 1:
    print(musics[index_music])
    index_music += 1


for i in range(0, 11):
    print(i)

for music in musics:
    print(music)

letters = [
           ["A", "B", "C"],
           ["A", "B", "C"]
           ]

for arrey in letters:
    for letter in arrey:
        print(letter)
