"""
Author: Darien Tsai
Date Created: 12/30/18
Description: Contains Error, Handling, and Exit definitions.
-Print when catching exceptions
-Print when receiving bad input
"""

#General error exit message
general_error = "An error has occured. Closing application\n"

#Message when there is no todo directory
no_file = "Couldn't find a todo list folder. Would you like to make one? (Y/N)\n"

#Exit message when user does not want to create directory
no_create = "This application cannot work without a todo directory. Will exit.\n"

#Bad input message when user creates a list with an existing name
already_exists = "Unable to create new todo list. Name already exists.\n"

#Bad request message when user tries to delete a list when none exist
no_lists = "There are no lists to delete\n"

#Bad request message when user tries to delete an item when none exist
no_items = "There are no items to delete\n"

#Bad input message when user enters a file that does not exist
does_not_exist = "Does not exist\n"

#Operation failure message
incomplete = "Could not complete operation"

#Bad input message when user does not enter acceptable (Y/N?) input
bad_input = "Not recognized as (Y/N) input. Will exit.\n"

#Bad input message when user does not enter acceptable input
bad_general_input = "Could not recognize input.\n"