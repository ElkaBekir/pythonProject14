playlist = {
    'title': 'patagonia bus',
    'author': 'Mr.genius',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'ducat'], 'duration': 5.25},
        {'title': 'song3', 'artist': ['garfield'], 'duration': 2.0}

    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)