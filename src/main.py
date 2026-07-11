import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class MintCrossHairApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.nicopekdk.mintcrosshair")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("MintCrossHair")
        window.set_default_size(800, 500)

        label = Gtk.Label(label="¡Bienvenido a MintCrossHair!")
        window.set_child(label)

        window.present()


app = MintCrossHairApp()
app.run()