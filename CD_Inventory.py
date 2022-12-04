#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# BStreck, 2022-Dec-03, added functionality to the TODO sections
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD
    
    Properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    
    Methods:
        noAnswer(self) --> (a string)
        __str__(self) --> self.noAnswer (a string)
    """
    
    # Fields
    cd_id = 0
    cd_title = ''
    cd_artist = ''
    
    # Constructor
    def __init__(self, num, cd, art):
    
    # Attributes
        self.__cd_id = num
        self.__cd_title = cd
        self.__cd_artist = art
    
    # Properties
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if str(value).isnumeric():
            self.__cd_id = value
        else:
            raise Exception('The cd_id must be a positive integer')
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
            self.__cd_artist = value
    
    # Methods
    def noAnswer(self):
        return """
# ------------------------------ #
This object has three properties:
  - cd_id
  - cd_title
  - cd_artist
# ------------------------------ #
                """
    
    def __str__(self):
        return self.noAnswer()


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file

    Methods:
        save_inventory(file_name, table): --> None
        load_inventory(file_name, table): --> None
    """
    
    @staticmethod
    def save_inventory(file_name, table):
        """
        Method to manage data writing from the list of dictionaries to a text file.
        It shows the current inventory prior to saving which allows users to verify they are saving the correct data.

        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objects): 2D structure that holds the data during runtime

        Returns:
            None
        """
        with open(file_name, 'w') as file:
            for row in table:
                [d1, d2, d3] = str(row.cd_id), row.cd_title, row.cd_artist
                file.write(','.join([d1, d2, d3]) + '\n')
    
    @staticmethod
    def load_inventory(file_name, table):
        """
        Method to manage data intake from the text file to a list of CD objects.
        The method reads data from the file identified by 'file_name' into a 2D table (list of CD objects).
        One line in the file represents one object in the table.
        
        This also contains error handling if there is a FileNotFoundError.
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objects): 2D structure that holds the data during runtime

        Returns:
            None
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    dum_obj = CD(int(data[0]), data[1], data[2])
                    table.append(dum_obj)
        except FileNotFoundError:
            print('\n{} does not exist...'.format(file_name))
            print('\nCreating the file...')
            file = open(file_name, 'w')
            file.close()
            print('\nThe file, {}, has now been created!'.format(file_name))
        except Exception:
            print('\nThere was a general error...')


# -- PRESENTATION (Input/Output) -- #
class IO:
    """
    Handling Input / Output
    
    Methods:
        print_menu(): --> None
        menu_choice(): --> choice (a string)
        show_inventory(table): --> None
        new_CD_choice(table): --> ID (an integer), strTitle (a string), strArtist (a string)
    """
    
    @staticmethod
    def print_menu():
        """
        Displays a menu of choices to the user

        Args:
            None

        Returns:
            None
        """
        print('\nMenu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to File\n[x] Exit\n')
    
    @staticmethod
    def menu_choice():
        """
        Gets user input for menu selection

        Args:
            None

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(table):
        """
        Displays the current inventory table

        Args:
            table (list of CD objects): 2D structure that holds the data during runtime

        Returns:
            None
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in table:
            print('{}\t{} (by: {})'.format(obj.cd_id, obj.cd_title, obj.cd_artist))
        print('======================================')
    
    @staticmethod
    def new_CD_choice(table):
        """
        Method to accept user inputs for a new CD

        Args:
            table (list of CD objects): 2D structure that holds the data during runtime

        Returns:
            ID (integer): the ID number of the new CD being added to the inventory
            strTitle (string): the title of the new CD being added to the inventory
            strArtist (string): the artist of the new CD being added to the inventory
        """
        ID = len(table) + 1
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return ID, strTitle, strArtist


# -- Main Body of Script -- #

# 1. Load data from the file into a list of CD objects when the script starts
FileIO.load_inventory(strFileName, lstOfCDObjects)

# 2. Start main loop
while True:
    
    # 3. Display menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # 4. Process menu selections
    
        # 4.1 Exit
    if strChoice == 'x':
        print('Goodbye...')
        break
    
        # 4.2 Load Inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost when the Inventory is re-loaded.\n')
        print('Type \'yes\' to continue and reload data from the file. Otherwise reload will be canceled.')
        strYesNo = input('Would you like to continue? ')
        if strYesNo.lower() == 'yes':
            print('\nReloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        continue
    
        # 4.3 Add a CD
    elif strChoice == 'a':
        dum1 = None
        ID, strTitle, strArtist = IO.new_CD_choice(lstOfCDObjects)
        dum1 = CD(ID, strTitle, strArtist)
        lstOfCDObjects.append(dum1)
        continue  # start loop back at top.
    
        # 4.4 Display Current Inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
        # 4.5 Save Inventory to File
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            print('\nSaving updated inventory...')
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('Done')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
        # 4.6 Catch-All Error... Should not be possible because the user's choice gets vetted in IO
    else:
        print('Invalid Input...\n')
        print('Please choose one of the options listed\n')
        continue

