
from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
   
    self.init_components(**properties)

   

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name=self.text_box_1.text
    weight=int(self.text_box_2.text)
    address=self.text_box_4.text
    personal=self.check_box_1.checked
    anvil.server.call('submit',name=name, weight=weight, address=address, personal=personal)
    Notification("Your Response has been recorded").show()
