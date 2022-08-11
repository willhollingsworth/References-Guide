import mido
import time


# examples for the library mido, used to interact with midi signals


def monitor_midi():
    # runs forever, logs all midi messages
    while True:
        print(in_port.receive())
    time.sleep(.1)


def blink_lights(loops=4, volocity_limit=2, msgs=['note_on', 'note_off'], channel_limit=15, note_limit=127, sleep=.5):
    # will loop over a large number of settings quickly
    # useful to find how a controller reacts to midi signals
    for loop_count in range(loops):
        for velocity_val in range(volocity_limit):
            for msg in msgs:
                for channel_val in range(channel_limit):
                    for note_val in range(note_limit):
                        out_port.send(mido.Message(
                            msg, channel=channel_val, note=note_val, velocity=velocity_val))
    time.sleep(sleep)


def scroll_lights(loops=6, notes=27, sleep=.001):
    # fun little demo of scrolling lights, works well on the akai midimix
    for z in range(loops):
        for x in range(notes):
            out_port.send(mido.Message('note_on', channel=0,
                                       note=x, velocity=127))
            time.sleep(sleep)
        time.sleep(.1)
        for x in range(notes, 0, -1):
            out_port.send(mido.Message('note_on', channel=0,
                                       note=x, velocity=0))
            time.sleep(sleep)
        for x in range(notes, 0, -1):
            out_port.send(mido.Message('note_on', channel=0,
                                       note=x, velocity=127))
            time.sleep(sleep)
        time.sleep(.1)
        for x in range(notes):
            out_port.send(mido.Message('note_on', channel=0,
                                       note=x, velocity=0))
            time.sleep(sleep)


def define_in_out_midi_ports(target_string):
    # will target a midi port based on a string match
    for device in mido.get_input_names():
        if target_string in device:
            in_port = mido.open_input(device)
    for device in mido.get_output_names():
        if target_string in device:
            out_port = mido.open_output(device)
    return (in_port, out_port)


def print_midi_devices():
    print('input devices:', mido.get_input_names())
    print('out devices:', mido.get_output_names())


print_midi_devices()
in_port, out_port = define_in_out_midi_ports('MIDI Mix')
scroll_lights()

# blink_lights()
# monitor_midi()
