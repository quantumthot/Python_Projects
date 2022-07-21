import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import os
import time
from datetime import datetime, timedelta


class ParentWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self)
        # Sets title of GUI window
        self.master.title("File Transfer")
        self.hours = 24

        # Creates button to select files from source directory
        self.sourceDir_btn = Button(
            text="Select Source", width=20, command=self.sourceDir)
        # Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry into GUI using tkinter grid() padx and pady are
        # the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2,
                             padx=(20, 10), pady=(30, 0))

        # Creates button to select destination of files from destination
        # directory
        self.destDir_btn = Button(
            text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry into GUI using tkinter grid() padx and pady are
        # the same as the button to ensure they will line up
        self.destination_dir.grid(
            row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # Creates button to transfer files
        self.transfer_btn = Button(
            text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # Creates an exit button
        self.exit_btn = Button(text="Exit", width=20,
                               command=self.exit_program)
        # position the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

        # Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir
        # Entry widget
        self.source_dir.insert(0, selectSourceDir)

        # Creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        # The .insert method will insert the user selection to the
        # destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)

        # Creates function to transfer files from one directory to another
    def transferFiles(self):

        # Get timestamp of 24 hours ago
        hours_ago = datetime.timestamp(
            datetime.now() - timedelta(hours=self.hours)
        )

        # Gets source directory
        source = self.source_dir.get()
        # Gets destination directory
        destination = self.destination_dir.get()
        # Gets a list of files in the source directory
        source_files = os.listdir(source)


        # Iterate through files in source folder
        for file in source_files:
            src_path = source + '/' + file
            dest_path = destination + '/' + file

            # skip any folders
            if not os.path.isfile(src_path):
                continue

            # Get the file timestamp
            file_ts = os.path.getmtime(src_path)

            # Check if file timestamp is greater than 24 (default) hours
            if file_ts > hours_ago:
                try:
                    # Move the file to new destination folder
                    # os.rename(src_path, dest_path)
                    shutil.move(src_path, dest_path)

                    message = 'Successfully moved {} from {} to {} folder'.format(
                        file, source, destination
                    )
                    print(message)
                except Exception as e:
                    # Let us know if the moving the file failed
                    message = 'Failed to move {} from {} to {} folder. Error: {}'
                    message = message.format(
                        file, source, destination, e
                    )
                    print(message)
            else:
                # Skip if file is older than 24 hours
                print('Skipping. {} file older than {} hours.'.format(
                    file, self.hours))

        

        # Creates function to exit program
    def exit_program(self):
        # root is the main GIU window, the Tkinter destroy method
        # tells Python to terminate root.mainloop and all widgets in the GUI
        # window
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
