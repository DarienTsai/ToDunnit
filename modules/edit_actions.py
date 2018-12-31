"""
Author: Darien Tsai
Date Created: 12/30/18
Description: Contains edit functions
"""
import os, sys
sys.path.append( "modules" )

import gen_actions
import status_log as sl
import error_log as el

def add( file ):
  """
  Adds an item to a todo list
  """
  with open( file, mode = "a", encoding = "utf-8" ) as list:
    addition = input( sl.new_todo )
    if len( addition ) == 0:
      gen_actions.display_status( el.bad_general_input )
    else:
      list.write( addition + "\n" )

def rem( file ):
  """
  Removes a line in a todo list
  """
  try:
    text = []
    #Get each line in the file
    with open( file, mode = "r", encoding = "utf-8" ) as list:
      for lines in list:
        text.append( lines )
    #Test if there are items in file
    if len( text ) == 0:
      gen_actions.display_status( el.no_items )
    else:
      #Get input
      removal_index = int( input( sl.remove_item ) )
      
      #Test if input is within range
      if removal_index < len( text ):
        #Overwrite file, omit line to remove
        with open( file, mode = "w", encoding = "utf-8" ) as list:
          for i in range( len(text) ):
            if i != removal_index:
              list.write( text[i] )
      else:
        gen_actions.display_status( el.does_not_exist )

  except ValueError:
    gen_actions.display_status( el.bad_general_input )

def wipe( file ):
  with open( file, mode = "w", encoding = "utf-8" ) as list:
    return None

def edit( file, index ):
  #Get input
  try:
    text = []
    new_item = input( sl.edit_item)

    #test there is an input
    if len( new_item ) != 0:
      #Get each line in the file
      with open( file, mode = "r", encoding = "utf-8" ) as list:
        for lines in list:
          text.append( lines )

      #Test if input is within range
      if index < len( text ):
        #Overwrite file, replace item
        with open( file, mode = "w", encoding = "utf-8" ) as list:
          for i in range( len(text) ):
            if i != index:
              list.write( text[i] )
            else:
              list.write( new_item + "\n" )
      else:
        gen_actions.display_status( el.does_not_exist )

    else:
      #No input
      gen_actions.display_status( el.bad_general_input )

  except ValueError:
    gen_actions.display_status( el.bad_general_input )
