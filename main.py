from numpy import number
import wx
from random import randint

# -- constants

RESOLUTION = [400, 300]
WINDOW_STYLE = style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX
FRAME_STYLE = wx.SUNKEN_BORDER
FIELD_SIZE = [50, 20]
FIELD_POSITION = [RESOLUTION[0] // 2 - FIELD_SIZE[0] // 2, 10]

BUTTON_SIZE = [50, 20]
BUTTON_POSITION = [RESOLUTION[0]//2 - BUTTON_SIZE[0]//2, 40]

# -- variable globale
computer_number = randint(1, 10)

# -- functions


def on_button_click(event):
    text = user_number = field.GetLineText(0)

    try:
        number = int(text)
    except:
        dialog = wx.MessageDialog(None, message="Veuillez entrer un nombre valide.",
                                  caption="Erreur", style=wx.ICON_ERROR)
        dialog.ShowModal()
        return

    if number < 1 or number > 10:
        dialog = wx.MessageDialog(None, message="Veuillez entrer un nombre entre 1 et 10.",
                                  caption="Erreur", style=wx.ICON_ERROR)
        dialog.ShowModal()
        return

    if number > computer_number:
        dialog = wx.MessageDialog(None, message="Votre nombre est trop grand",
                                  caption="Nombre trop grand", style=wx.ICON_INFORMATION)
        dialog.ShowModal()
    elif number < computer_number:
        dialog = wx.MessageDialog(None, message="Votre nombre est trop petit",
                                  caption="Nombre trop petit", style=wx.ICON_INFORMATION)
        dialog.ShowModal()
    else:
        dialog = wx.MessageDialog(None, message="Vous avez devinez",
                                  caption="Victoire", style=wx.ICON_ASTERISK)
        dialog.ShowModal()

        # -- Application creation


app = wx.App()

frame = wx.Frame(None, title="Guess the Number v2.0",
                 size=RESOLUTION, style=WINDOW_STYLE)
panel = wx.Panel(frame, style=FRAME_STYLE)

field = wx.TextCtrl(panel, pos=FIELD_POSITION, size=FIELD_SIZE)
okButton = wx.Button(panel, id=wx.OK, label="Ok",
                     pos=BUTTON_POSITION, size=BUTTON_SIZE)
okButton.Bind(wx.EVT_BUTTON, on_button_click)

# -- main programme

frame.Show()
app.MainLoop()
