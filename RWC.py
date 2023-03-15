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
    global background_color, text_color
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
        global background_color, text_color
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
                update_bg_color(main_window)

        def update_bg_color(widget):
            widget.after_idle(lambda: widget.configure(bg=background_color))
            for c in widget.winfo_children():
                update_bg_color(c)

        def choose_color2():
            global text_color
            color2 = colorchooser.askcolor()
            if color2:
                text_color = color2[1]
                update_fg_color(main_window)

        def update_fg_color(widget):
            w_type = widget.winfo_class()
            if w_type in ["Label", "Button", "Entry"]:
                widget.after_idle(lambda: widget.configure(fg=text_color))
            for c in widget.winfo_children():
                update_fg_color(c)

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

    def alarm_page():
        global background_color, text_color
        settings_window.withdraw()
        alarm_window = tk.Toplevel()
        alarm_window.title("Alarm")
        alarm_window.geometry("400x500")
        alarm_window.minsize(200, 250)
        alarm_window.configure(background=background_color)

        def set_alarm():
            hour = hours_listbox.get(hours_listbox.curselection())
            minute = minutes_listbox.get(minutes_listbox.curselection())
            second = seconds_listbox.get(seconds_listbox.curselection())

            total_time = hour * 3600 + minute * 60 + second
            counting_down(total_time)

        def counting_down(time_left):
            if time_left > 0:
                time_label.config(text=str(time_left))
                alarm_window.after(1000, counting_down, time_left-1)
            else:
                time_label.config("Time's up!")

        def back_alarm():
            alarm_window.withdraw()
            settings_window.deiconify()

        def close_alarm():
            alarm_window.destroy()
            settings_window.destroy()
            main_window.destroy()

        # Can close the window by pressing "X" button
        alarm_window.protocol("WM_DELETE_WINDOW", close_alarm)

        # Getting the labels & scrollbar options
        hours_label = tk.Label(alarm_window, text="Hours:", background=background_color, foreground=text_color)
        hours_label.grid(column=0, row=0, sticky='e')
        hours_listbox = tk.Listbox(alarm_window, width=5)
        hours_listbox.grid(column=1, row=0, sticky='we')
        hours_scroll = tk.Scrollbar(alarm_window)
        hours_scroll.grid(column=1, row=0, sticky='ens')
        hours_listbox.config(yscrollcommand=hours_scroll.set)
        for num in range(24):
            hours_listbox.insert(num, str(num).zfill(2))
        hours_scroll.config(command=hours_listbox.yview)

        minutes_label = tk.Label(alarm_window, text="Minutes:", background=background_color, foreground=text_color)
        minutes_label.grid(column=2, row=0, sticky='e')
        minutes_listbox = tk.Listbox(alarm_window, width=5)
        minutes_listbox.grid(column=3, row=0, sticky='we')
        minutes_scroll = tk.Scrollbar(alarm_window)
        minutes_scroll.grid(column=3, row=0, sticky='ens')
        minutes_listbox.config(yscrollcommand=minutes_scroll.set)
        for num in range(60):
            minutes_listbox.insert(num, str(num).zfill(2))
        minutes_scroll.config(command=minutes_listbox.yview)

        seconds_label = tk.Label(alarm_window, text="Seconds:", background=background_color, foreground=text_color)
        seconds_label.grid(column=4, row=0, sticky='e')
        seconds_listbox = tk.Listbox(alarm_window, width=5)
        seconds_listbox.grid(column=5, row=0, sticky='we')
        seconds_scroll = tk.Scrollbar(alarm_window)
        seconds_scroll.grid(column=5, row=0, sticky='ens')
        seconds_listbox.config(yscrollcommand=seconds_scroll.set)
        for num in range(60):
            seconds_listbox.insert(num, str(num).zfill(2))
        seconds_scroll.config(command=seconds_listbox.yview)

        time_label = tk.Label(alarm_window, text="", bg=background_color, fg=text_color)
        time_label.grid(column=1, row=3)

        # Buttons for alarm page
        start_button = tk.Button(alarm_window, text="Start", bg=background_color, fg=text_color,
                                 font=default_font, command=set_alarm)
        start_button.grid(column=1, row=1, pady=20)

        back2 = tk.Button(alarm_window, text="Back", command=back_alarm, bg=background_color,
                          fg=text_color, font=default_font)
        back2.grid(row=2, column=1, pady=20)

    # Create the buttons for the settings page
    change_colors = tk.Button(settings_window, text="Appearance", bg=background_color, fg=text_color,
                              font=default_font, command=appearance_page)
    change_colors.grid(row=0, column=0, pady=10)

    setting_alarm = tk.Button(settings_window, text="Set Alarm", bg=background_color, fg=text_color,
                              font=default_font, command=alarm_page)
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
