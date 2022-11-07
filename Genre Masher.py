import random

#List of Subgenres
genres=["Alternate History Fantasy", "Children's Story Fantasy", "Fantasy Comedy", "Contemporary Fantasy", "Dark Fantasy",
        "Fairy Tale Fantasy", "Fantasy of Manners", "Heroic Fantasy", "High Fantasy", "Historical Fantasy", "Low Fantasy",
        "Magical Realism", "Mythic Fantasy", "Superhero Fantasy", "Sword and Sorcery Fantasy", "Urban Fantasy",
        "Young Adult Fantasy", "Body Horror", "Horror Comedy", "Creepy Kids Horror", "Extreme Horror", "Gothic Horror",
        "Hauntings Horror", "Historical Horror", "Cosmic Horror", "Man-Made Horror", "Monster Horror", "Mythic Horror",
        "Occult Horror", "Psychic Abilities Horror", "Psychological Horror", "Quiet Horror", "Young Adult Horror",
        "Amateur Sleuth Mystery", "Bumbling Detective Mystery", "Caper Mystery", "Child in Peril Mystery",
        "Children's Story Mystery", "Cozy Mystery", "Culinary Mystery", "Disabled Mystery", "Doctor Detective Mystery",
        "Furry Sleuth Mystery", "Hardboiled Mystery", "Historical Mystery", "Howdunit Mystery", "Legal Mystery",
        "Locked Room Mystery", "Culturally Diverse Mystery", "Paranormal Mystery", "Police Procedural Mystery",
        "Private Detective Mystery", "Whodunit Mystery", "Woman in Peril Mystery", "Young Adult Mystery",
        "Billionaires Romance", "Romance Comedy", "Contemporary Romance", "Fantasy Romance", "Gothic Romance",
        "Historical Romance", "Holidays Romance", "Inspirational Romance", "Military Romance", "Paranormal Romance",
        "Regency Romance", "Romantic Suspense", "Science Fiction Romance", "Sports Romance", "Time Travel Romance",
        "Western Romance", "Young Adult Romance", "Aliens Science Fiction", "Alternate History Science Fiction",
        "Alternate/Parallel Universe Science Fiction", "Apocalyptic/Post-Apocalpytic Science Fiction",
        "Biopunk Science Fiction", "Children's Story Science Fiction", "Colonization Science Fiction",
        "Science Fiction Comedy", "Cyberpunk Science Fiction", "Dying Earth Science Fiction", "Dystopia Science Fiction",
        "Galactic Empire Science Fiction", "Generation Ship Science Fiction", "Hard Science Fiction",
        "Immortality Science Fiction", "Lost Worlds Science Fiction", "Military Science Fiction",
        "Mind Transfer Science Fiction", "Mundance Science Fiction", "Mythic Science Fiction", "Nanopunk Science Fiction",
        "Robots/A.I. Science Fiction", "Science Fantasy", "Slipstream Science Fiction", "Soft Science Fiction",
        "Space Exploration Science Fiction", "Space Opera Science Fiction", "SpyFi Science Fiction",
        "Steampunk Science Fiction", "Time Travel Science Fiction", "Utopia Science Fiction", "Young Adult", "Action Thriller", "Thriller Comedy", "Conspiracy Thriller", "Crime Thriller", "Disaster Thriller", "Espionage Thriller", "Forensic Thriller", "Historical Thriller", "Legal Thriller", "Medical Thriller", "Military Thriller", "Mystery Thriller", "Paranormal Thriller", "Political Thriller", "Psychological Thriller", "Religious Thriller", "Techno Thriller", "Young Adult Thriller", "Bounty Hunters Western", "Cattle Drive Western", "Children's Story Western", "Western Comedy", "Gold Rush Western", "Gunfighters Western", "Land Rush Western", "Lawmen Western", "Mountain Men Western",
        "Outlaws Western", "Prairie Settlement Western", "Revenge Western", "Wagon Train Western", "Young Adult Western"]

#Masher Function
def masher():
    print("How many mashups do you want?: ")
    x = int(input())
    seq = [i+1 for i in range(x)]
    for j in seq:
        pair=random.sample(genres, 2)
        print(pair[0] + ' + ' + pair[1]+ '\n')
