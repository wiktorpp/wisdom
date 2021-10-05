import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib

import random

starSize=90
wisdoms=[
    "Piękne jest lepsze niż brzydkie.",
    "Wyrażone wprost jest lepsze niż domniemane.",
    "Proste jest lepsze niż złożone.",
    "Złożone jest lepsze niż skomplikowane.",
    "Płaskie jest lepsze niż wielopoziomowe.",
    "Rzadkie jest lepsze niż gęste.",
    "Czytelność się liczy.",
    "Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.",
    "Choć praktyczność przeważa nad konsekwencją.",
    "Błędy zawsze powinny być sygnalizowane.",
    "Chyba że zostaną celowo ukryte.",
    "W razie niejasności powstrzymaj pokusę zgadywania.",
    "Powinien być jeden -- i najlepiej tylko jeden -- oczywisty sposób na zrobienie danej rzeczy.",
    "Choć ten sposób może nie być oczywisty jeśli nie jest się Holendrem.",
    "Teraz jest lepsze niż nigdy.",
    "Chociaż nigdy jest często lepsze niż natychmiast.",
    "Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.",
    "Jeśli rozwiązanie jest łatwo wyjaśnić, to może ono być dobrym pomysłem.",
    "Przestrzenie nazw to jeden z niesamowicie genialnych pomysłów -- miejmy ich więcej!",
]
class Handler:
    def __init__(self):
        pass

    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def randomize(*args):
        wisdom = builder.get_object("wisdom")
        wisdom.set_text(random.choice(wisdoms))

    def __getattr__(self, name, *args):
        return lambda *args: print({"name": name, "args": args})

builder = Gtk.Builder()
builder.add_from_file("wisdom.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
button=builder.get_object("buttonid")
widthEntry=builder.get_object("widthEntry")
calc=builder.get_object("calc")

hb = builder.get_object("headerBar")
hb.get_parent().remove(hb)
window.set_titlebar(hb)

window.show_all()
#import pdb; pdb.set_trace()
Gtk.main()