"""
Author: Darien Tsai
Date Created: 12/30/18
Description: Contains general functions
"""
import os, sys
sys.path.append("modules")

import status_log as sl

def clear_win():
  """
  Clear the cmd or terminal window
  """
  os.system('cls' if os.name == 'nt' else 'clear')

def display_status( status_message ):
  """
  displays a message before moving on
  """
  clear_win()
  print( status_message )
  input( sl.continue_message )

def exit_app( exit_message ):
  """
  exits the app with some message
  """
  #Display message
  clear_win()
  print( exit_message )
  input( sl.continue_message )

  #Exit
  try:
    sys.exit()
  except SystemExit:
    os._exit( 1 )