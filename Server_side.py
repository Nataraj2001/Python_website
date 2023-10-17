@anvil.server.callable
def submit(name,weight, address, personal):
  app_tables.gym.add_row(name=name, address=address, personal=personal, weight=weight)
  anvil.email.send(to="veereshachar385@gmail.com", subject="Response from anvil app",
                   text=f"Feedback from {name} : weight is{weight} and they live at:{address}.Personal Training required :{personal}")
