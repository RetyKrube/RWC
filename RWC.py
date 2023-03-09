# Import the modules
import datetime
import tkinter as tk
from tkinter import colorchooser

# Default Values
background_color = "black"
text_color = "lime"
default_font = ("Arial", 15)


# Getting the clock set up
def timing():
    t_now = datetime.datetime.now().strftime('%I:%M:%S:%p')
    t_label.config(text=t_now, background=background_color, foreground=text_color)
    t_label.after(1000, timing)


# Creating the settings window
def settings_page():
    main_window.withdraw()
    settings_window = tk.Toplevel()
    settings_window.title("RWC Settings")
    settings_window.geometry("350x300")
    settings_window.minsize(150, 300)
    settings_window.configure(background=background_color)

    # This makes sure that the program terminates
    def close_window():
        settings_window.destroy()
        main_window.destroy()

    # This closes the settings window but opens back the main
    def close_settings():
        settings_window.destroy()
        main_window.deiconify()

    # Creating the 'Appearance' page
    def appearance_page():
        settings_window.withdraw()
        appearance_window = tk.Toplevel()
        appearance_window.title("Appearance")
        appearance_window.geometry("350x200")
        appearance_window.minsize(200, 250)
        appearance_window.configure(background=background_color)

        def choose_color1():
            global background_color
            color1 = colorchooser.askcolor()
            if color1:
                background_color = color1[1]
                t_label.config(bg=background_color)
                main_window.config(bg=background_color)
                settings_window.config(bg=background_color)

        def choose_color2():
            global text_color
            color2 = colorchooser.askcolor()
            if color2:
                text_color = color2[1]
                main_window.configure(fg=text_color)
                settings_window.configure(fg=text_color)

        def back_appearance():
            appearance_window.withdraw()
            settings_window.deiconify()

        def close_appearance():
            appearance_window.destroy()
            settings_window.destroy()
            main_window.destroy()

        primary_color = tk.Button(appearance_window, text="Background Color", command=choose_color1,
                                  bg=background_color, fg=text_color, font=default_font)
        primary_color.grid(row=0, column=0, pady=20)

        secondary_color = tk.Button(appearance_window, text="Text Color", command=choose_color2,
                                    bg=background_color, fg=text_color, font=default_font)
        secondary_color.grid(row=1, column=0, pady=20)

        back1 = tk.Button(appearance_window, text="Back", command=back_appearance, bg=background_color,
                          fg=text_color, font=default_font)
        back1.grid(row=2, column=0, pady=20)

        appearance_window.grid_columnconfigure(0, weight=1)
        appearance_window.protocol("WM_DELETE_WINDOW", close_appearance)

    # Create the buttons for the settings page
    change_colors = tk.Button(settings_window, text="Appearance", bg=background_color, fg=text_color,
                              font=default_font, command=appearance_page)
    change_colors.grid(row=0, column=0, pady=10)

    setting_alarm = tk.Button(settings_window, text="Set Alarm", bg=background_color, fg=text_color, font=default_font)
    setting_alarm.grid(row=1, column=0, pady=10)

    change_sound = tk.Button(settings_window, text="Alarm Sound", bg=background_color, fg=text_color, font=default_font)
    change_sound.grid(row=2, column=0, pady=10)

    font_settings = tk.Button(settings_window, text="Fonts", bg=background_color, fg=text_color, font=default_font)
    font_settings.grid(row=3, column=0, pady=10)

    close_settings = tk.Button(settings_window, text="Close", command=close_settings,
                               bg=background_color, fg=text_color, font=default_font)
    close_settings.grid(row=4, column=0, pady=10)

    # Center the widgets and allow program to terminate
    settings_window.grid_columnconfigure(0, weight=1)
    settings_window.protocol("WM_DELETE_WINDOW", close_window)

    # Run the settings window infinitely
    settings_window.mainloop()


# Setting up the Main Window
main_window = tk.Tk()
main_window.title("RWC(Remote Work Clock)")
main_window.geometry('350x100')
main_window.minsize(350, 100)
main_window.configure(background=background_color)

# Getting the clock on screen
t_label = tk.Label(main_window, font=("ds-digital", 50))
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
