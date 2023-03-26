# Import the modules
from datetime import datetime
import tkinter as tk
from tkinter import colorchooser

# Default Values
background_color = "black"
text_color = "lime"
default_font = ("Arial", 15)


# Getting the clock set up
def timing():
    """This will get the current local time for the label"""
    t_now = datetime.now().strftime('%I:%M:%S:%p')
    t_label.config(text=t_now, background=background_color, foreground=text_color)
    t_label.after(1000, timing)


# Creating the windows
def settings_page():
    """This will make a new page once the `settings` button is clicked
    and will produce two buttons on screen"""
    global background_color, text_color
    main_window.withdraw()
    settings_window = tk.Toplevel()
    settings_window.title("RWC Settings")
    settings_window.geometry("250x200")
    settings_window.minsize(150, 200)
    settings_window.configure(background=background_color)

    def close_window():
        """This allows the user to press the `X` button in the
        corner of the window to terminate the program"""
        settings_window.destroy()
        main_window.destroy()

    def close_settings():
        """Closes the `settings` window and brings back the `main` window"""
        settings_window.destroy()
        main_window.deiconify()

    def appearance_page():
        """Opens a new page once the `Appearance` button was clicked in the `settings`
        window and will generate 3 buttons on screen"""
        global background_color, text_color
        settings_window.withdraw()
        appearance_window = tk.Toplevel()
        appearance_window.title("Appearance")
        appearance_window.geometry("350x200")
        appearance_window.minsize(200, 250)
        appearance_window.configure(background=background_color)

        def choose_color1():
            """Will let the user choose a color for the `background`"""
            global background_color
            color1 = colorchooser.askcolor()
            if color1:
                background_color = color1[1]
                update_bg_color(main_window)

        def update_bg_color(widget):
            """Makes sure that the `background` color gets upgraded immediately"""
            widget.after_idle(lambda: widget.configure(bg=background_color))
            for c in widget.winfo_children():
                update_bg_color(c)

        def choose_color2():
            """Lets the user choose a color for the `foreground`"""
            global text_color
            color2 = colorchooser.askcolor()
            if color2:
                text_color = color2[1]
                update_fg_color(main_window)

        def update_fg_color(widget):
            """Makes sure that the `foreground` color gets upgraded immediately"""
            w_type = widget.winfo_class()
            if w_type in ["Label", "Button", "Entry"]:
                widget.after_idle(lambda: widget.configure(fg=text_color))
            for c in widget.winfo_children():
                update_fg_color(c)

        def back_appearance():
            """Allows the user to go back to the `settings` window
            from the `appearance` window"""
            appearance_window.withdraw()
            settings_window.deiconify()

        def close_appearance():
            """This allows the user to press the `X` button in the
            corner of the window to terminate the program"""
            appearance_window.destroy()
            settings_window.destroy()
            main_window.destroy()
        
        # Creating the buttons for the `appearance` page
        primary_color = tk.Button(appearance_window, text="Background Color", command=choose_color1,
                                  bg=background_color, fg=text_color, font=default_font)
        primary_color.grid(row=0, column=0, pady=20)

        secondary_color = tk.Button(appearance_window, text="Text Color", command=choose_color2,
                                    bg=background_color, fg=text_color, font=default_font)
        secondary_color.grid(row=1, column=0, pady=20)

        back1 = tk.Button(appearance_window, text="Back", command=back_appearance, bg=background_color,
                          fg=text_color, font=default_font)
        back1.grid(row=2, column=0, pady=20)

        # Center the widgets and allow program to terminate
        appearance_window.grid_columnconfigure(0, weight=1)
        appearance_window.protocol("WM_DELETE_WINDOW", close_appearance)

    # Create the buttons for the settings page
    change_colors = tk.Button(settings_window, text="Appearance", bg=background_color, fg=text_color,
                              font=default_font, command=appearance_page)
    change_colors.grid(row=0, column=0, pady=20)

    close_settings = tk.Button(settings_window, text="Close", command=close_settings,
                               bg=background_color, fg=text_color, font=default_font)
    close_settings.grid(row=1, column=0, pady=10)

    # Center the widgets and allow program to terminate
    settings_window.columnconfigure(0, weight=1)
    settings_window.rowconfigure(0, weight=1)
    settings_window.protocol("WM_DELETE_WINDOW", close_window)

    # Run the settings window infinitely
    settings_window.mainloop()


# Setting up the Main Window
main_window = tk.Tk()
main_window.title("RWC(Remote Work Clock)")
main_window.geometry('500x150')
main_window.minsize(420, 120)
main_window.configure(background=background_color)

# Getting the clock on screen
t_label = tk.Label(main_window, font=("Arial", 50))
t_label.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='news')

# Creating the settings button
settings_button = tk.Button(main_window, text="Settings", command=settings_page, bg=background_color, fg=text_color)
settings_button.grid(row=2, column=0, columnspan=2)

# Center the widgets
main_window.grid_columnconfigure(0, weight=1)

# Calling the function to change the time
timing()

# Run the window forever
main_window.mainloop()
