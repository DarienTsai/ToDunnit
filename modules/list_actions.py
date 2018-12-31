"""
Author: Darien Tsai
Date Created: 12/30/18
Description: Contains list functions
"""
import os, sys
sys.path.append( "modules" )

import gen_actions
import status_log as sl
import error_log as el

def add():
  """
  Creates a new todo list
  """
  gen_actions.clear_win()
  try:
    #Listen for input
    name = input( sl.name_prompt )
    if len( name ) == 0:
      gen_actions.display_status( el.bad_general_input )
    else:
      new = open( name + ".txt", "x" )
  except FileExistsError:
    #When the todo list already exists
    gen_actions.display_status( el.already_exists )
  except:
    #General error
    gen_actions.exit_app( el.general_error )
  finally:
    new.close()

def rem( lists ):
  """
  Removes a todo list
  """
  if len( lists ) == 0:
    gen_actions.display_status( el.no_lists )
  else:
    try:
      num = input( sl.remove_prompt )
      if len( num ) == 0:
        gen_actions.display_status( el.bad_general_input )
      else:
        os.remove( lists[int( num )] )
    except FileNotFoundError:
      gen_actions.display_status( el.does_not_exist )
    except IndexError:
      gen_actions.display_status( el.does_not_exist )
    except ValueError:
      gen_actions.display_status( el.bad_general_input )

def wipe( lists ):
  """
  deletes all todo lists
  """
  try:
    for i in range(len(lists)):
      os.remove( lists[i] )
  except:
    print( sys.exc_info()[0] )
    input()
    gen_actions.display_status( el.incomplete )