import os

FPS = 100

SCREENSIZE = (640, 480)

Imagees = {
    'rabbit': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]dude.png'),
    'grass': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]grass.png'),
    'castle': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]castle.png'),
    'bullet': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]bullet.png'),
    'badguy': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]badguy.png'),
    'healthbar': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]healthbar.png'),
    'health': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]health.png'),
    'gameover': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]gameover.png'),
    'youwin': os.path.join(os.getcwd(), 'resources/images/[SW.BAND]youwin.png')
}

Sounds = {
    'hit': os.path.join(os.getcwd(), 'resources/audio/[SW.BAND]explode.wav'),
    'enemy': os.path.join(os.getcwd(), 'resources/audio/[SW.BAND]enemy.wav'),
    'shoot': os.path.join(os.getcwd(), 'resources/audio/[SW.BAND]shoot.wav'),
    'moonlight': os.path.join(os.getcwd(), 'resources/audio/[SW.BAND]moonlight.wav')
}
