from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

# Set up the listener
with mouse.Listener(on_move=on_move) as listener:
    listener.join()
