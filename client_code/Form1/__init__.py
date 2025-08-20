from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_2.text = 0
    self.label_4.text = 0
    self.label_6.text = 0 

  def press_me_click(self, **event_args):
    """This method is called when the button is clicked"""
    nbr = 3
    gives = self.label_6.text
    org = self.label_2.text
    new_nbr = org - nbr
    self.label_6.text = new_nbr
    self.label_4.text = nbr
    self.label_2.text = new_nbr

  def down_click(self, **event_args):
    nbr =5
    gives = self.label_6.text
    org = self.label_2.text
    new_nbr = org + nbr
    self.label_6.text = new_nbr
    self.label_4.text = nbr
    self.label_2.text = new_nbr
