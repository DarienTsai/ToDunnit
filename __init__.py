"""
Author: Darien Tsai
Date Created: 12/30/18
Description: Contains the functions and definitions for this application.
"""
import os, sys

from modules import gen_actions
from modules import list_actions
from modules import edit_actions
from modules import ui_strings as ui
from modules import status_log as sl
from modules import error_log as el

########## FUNCTIONS ##########

def check_folder( parent ):
  """
  Checks if todo directories exist
  Asks for creation if not, exits
  Goes to todo list interface
  """
  gen_actions.clear_win()
  try:
    #Attempt to locate todo folder
    os.chdir( parent + todo_path_str )
    
  except FileNotFoundError:
    #If nonexistant, ask for creation. Exits if no creation
    global response
    response = input( el.no_file ).lower()
    print(len(response))

    #Handles todo folder creation
    if response[0] == "y":
      os.mkdir( todo_directory_name )
      gen_actions.clear_win()
      print( sl.todo_create_success )
      os.chdir( parent + todo_path_str )
      input( sl.continue_message )

    elif response[0] == "n":
      gen_actions.exit_app( el.no_create )

    else:
      gen_actions.exit_app( el.bad_input )

  except:
    #general error
    gen_actions.exit_app( el.general_error )

  finally:
    if len(response) == 0:
      gen_actions.exit_app( el.bad_input )
    global todo_lists
    todo_lists = os.listdir(os.getcwd())
    list_interface()

def list_interface():
  """
  Interface for lists
  """
  global todo_lists
  #print the interface
  gen_actions.clear_win()
  print( ui.ToDunnit )
  print( ui.current_lists )

  for i in range( len( todo_lists ) ):
    print( i, "| " + todo_lists[i].replace( ".txt", "" ) )


  for i in range( len( ui.todo_list_options) ):
    print( ui.todo_list_options[i] )

  #listens for input, process input
  try:
    global response
    response = input().lower()

    if response == "a":
      list_actions.add()

    elif response == "d":
      list_actions.rem( todo_lists )

    elif response == "c" or response == "clear":
      list_actions.wipe( todo_lists )

    elif response =="x":
      gen_actions.exit_app( sl.farewell_message )

    elif int(response) < len( todo_lists ):
        edit_interface( int(response) )

    elif len( response ) == 0:
      gen_actions.display_status( el.bad_general_input )

    else:
      gen_actions.display_status( el.bad_general_input )
      list_interface()

  except ValueError:
    gen_actions.display_status( el.bad_general_input )

  except UnboundLocalError:
    pass
      
  except:
    print( sys.exc_info()[0], "listInterface" )
    input()
    gen_actions.exit_app( el.general_error )

  finally:
    #Updates the todo lists and recalls this interface
    todo_lists = os.listdir( os.getcwd() )
    list_interface()

def edit_interface( index ):
  """
  interface for editing todo list
  """
  global todo_lists
  gen_actions.clear_win()
  #load file
  edit = open( todo_lists[index], mode = "r", encoding = "utf-8" )
  #print interface
  print( ui.current_items )
  count = 0
  for line in edit:
    print( count, "| " + line, end = '' )
    count += 1
  for i in range( len( ui.edit_options ) ):
    print( ui.edit_options[i] )

  #Listen for input
  try:
    global response
    response = input().lower()

    #Handle input
    if len( response ) == 0:
      gen_actions.display_status( el.bad_general_input )
    
    elif response == "a":
      edit_actions.add( todo_lists[index] )
    
    elif response == "d":
      edit_actions.rem( todo_lists[index] )

    elif response == "c":
      edit_actions.wipe( todo_lists[index] )

    elif int( response ) < count:
      edit_actions.edit( todo_lists[index], int(response) )

    elif response != "x":
      gen_actions.display_status( el.bad_general_input )
      edit_interface( index )

  except ValueError:
    if response == "x":
      pass
    else:
      gen_actions.display_status( el.bad_general_input )

  except:
    print( sys.exc_info()[0], "edit" )
    input()
  finally:
    if response == "x":
      return 1
    else:
      edit_interface( index )

#The todo folder name
todo_directory_name = "todo"

#The todo folder path
todo_path_str = "\\todo"

#holds all todo list filenames
todo_lists = []

########## INITIALIZATION ##########

#create a string for holding responses
response = "x"

#Wipe the window, get the parent directory
parent_directory = os.getcwd()

#Check if todo directory exists, prints todo lists              
check_folder( parent_directory )