# Import the modules
from datetime import datetime
import tkinter as tk
from tkinter import colorchooser
import tkinter.messagebox
import time
import random

# Default Values
background_color = "black"
text_color = "lime"
default_font = ("Arial", 15)
default_alarm = "Time's up!"
timer_active = False
alarm_messages = []


# Getting the clock set up
def timing():
    """This will get the current local time for the label"""
    t_now = datetime.now().strftime('%I:%M:%S:%p')
    t_label.config(text=t_now, background=background_color, foreground=text_color)
    t_label.after(1000, timing)


# Creating the settings window
def settings_page():
    """This will make a new page once the `Settings` button is clicked
    and will produce two buttons on screen"""
    global background_color, text_color
    main_window.withdraw()
    settings_window = tk.Toplevel()
    settings_window.title("RWC Settings")
    settings_window.geometry("350x300")
    settings_window.minsize(150, 300)
    settings_window.configure(background=background_color)

    def close_window():
        """This allows the user to press the `X` button in the
        top right corner of the `settings` window to terminate the program"""
        settings_window.destroy()
        main_window.destroy()

    def close_settings():
        """Closes the `settings` window and brings back the
        `main` window when the `Close` button is clicked"""
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

        def back_appearance():
            """Allows the user to go back to the `settings` window
            from the `appearance` window after the `Back` button is clicked"""
            appearance_window.withdraw()
            settings_window.deiconify()

        def close_appearance():
            """This allows the user to press the `X` button in the
            top right corner of the `appearance` window to terminate the program"""
            appearance_window.destroy()
            settings_window.destroy()
            main_window.destroy()

        def choose_color1():
            """Will let the user choose a color for the `background`
            when the `Background Color` button is clicked"""
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
            """Lets the user choose a color for the `foreground`
            when the `Text Color` button is clicked"""
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

    def alarm_page():
        """Opens a new page once the `Set Alarm` button is clicked and
        will produce 3 list boxes and 4 buttons"""
        global background_color, text_color
        settings_window.withdraw()
        alarm_window = tk.Toplevel()
        alarm_window.title("Alarm")
        alarm_window.geometry("400x500")
        alarm_window.minsize(400, 350)
        alarm_window.configure(background=background_color)

        def back_alarm():
            """Allows the user to go back to the `settings` window
            from the `alarm` window after the `Back` button is clicked"""
            alarm_window.withdraw()
            settings_window.deiconify()

        def close_alarm():
            """This allows the user to press the `X` button in the
            top right corner of the `alarm` window to terminate the program"""
            global timer_active
            timer_active = False
            alarm_window.destroy()
            settings_window.destroy()
            main_window.destroy()

        def messages_page():
            """Opens a new page once the `Manage Messages` button is clicked and
            will produce an entry widget, a list box and 4 buttons"""
            global background_color, text_color
            alarm_window.withdraw()
            messages_window = tk.Toplevel()
            messages_window.title("Manage Messages")
            messages_window.geometry("430x400")
            messages_window.minsize(380, 350)
            messages_window.configure(background=background_color)

            def back_messages():
                """Allows the user to go back to the `alarm` window
                from the `manage messages` window after the `Back` button is clicked"""
                messages_window.withdraw()
                alarm_window.deiconify()

            def close_messages():
                """This allows the user to press the `X` button in the
                top right corner of the `manage messages` window to terminate the program"""
                messages_window.destroy()
                alarm_window.destroy()
                settings_window.destroy()
                main_window.destroy()

            def add_message():
                """This allows any text prompt entered into the entry widget
                to be added to a list box with a click of a button"""
                message = message_entry.get()
                if message:
                    alarm_messages.append(message)
                    messages_listbox.insert(tk.END, "- " + message)
                    message_entry.delete(0, tk.END)

            def remove_message():
                """Removes a selected message from the listbox"""
                selected_index = messages_listbox.curselection()
                if selected_index:
                    alarm_messages.pop(selected_index[0])
                    messages_listbox.delete(selected_index)

            def edit_message():
                """Puts selected message back into entry widget to make changes"""
                selected_index = messages_listbox.curselection()
                if selected_index:
                    message = messages_listbox.get(selected_index)
                    message_entry.insert(0, message[2:])
                    remove_message()

            # Creating the widgets and buttons for the `manage messages` page
            message_entry = tk.Entry(messages_window, bg=background_color, fg=text_color, insertbackground=text_color,
                                     font=default_font, width=20)
            message_entry.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky='ew')

            message_label = tk.Label(messages_window, text="<-- Enter your message here", bg=background_color,
                                     fg=text_color)
            message_label.grid(row=0, column=2, sticky='w')

            add_message_button = tk.Button(messages_window, text="Add", command=add_message, bg=background_color,
                                           fg=text_color, font=default_font)
            add_message_button.grid(row=1, column=2, padx=20)

            remove_message_button = tk.Button(messages_window, text="Remove", command=remove_message,
                                              bg=background_color, fg=text_color, font=default_font)
            remove_message_button.grid(row=2, column=2, padx=20)

            edit_message_button = tk.Button(messages_window, text="Edit", command=edit_message, bg=background_color,
                                            fg=text_color, font=default_font)
            edit_message_button.grid(row=3, column=2, padx=20)

            back3 = tk.Button(messages_window, text="Back", command=back_messages, bg=background_color,
                              fg=text_color, font=default_font)
            back3.grid(row=4, column=0, columnspan=2, pady=20)

            messages_listbox = tk.Listbox(messages_window, bg=background_color, fg=text_color, width=20)
            messages_listbox.grid(row=1, column=0, columnspan=2, rowspan=3, padx=20, sticky='news')

            # Extra configurations
            for m in alarm_messages:
                messages_listbox.insert(tk.END, m)

            for x in range(3):
                messages_window.grid_columnconfigure(x, weight=1)

            for x in range(5):
                messages_window.grid_rowconfigure(x, weight=1)

            messages_window.protocol("WM_DELETE_WINDOW", close_messages)

        def start_timer():
            """Starts and counts down the set time from the numbers
            selected from the list boxes"""
            global timer_active, default_alarm
            timer_active = True
            hour = int(hours_var.get())
            minute = int(minutes_var.get())
            second = int(seconds_var.get())
            total_seconds = hour * 3600 + minute * 60 + second

            while total_seconds >= 0 and timer_active:
                hours_remaining = total_seconds // 3600
                minutes_remaining = (total_seconds % 3600) // 60
                seconds_remaining = total_seconds % 60

                time_str = f"{hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}"
                timer_var.set(time_str)
                alarm_window.update()
                time.sleep(1)
                total_seconds -= 1
            if timer_active:
                if alarm_messages:
                    rn = random.randint(0, len(alarm_messages) - 1)
                    default_alarm = alarm_messages[rn]
                tk.messagebox.showinfo("ALARM!!!", default_alarm)

        def reset_timer():
            """This will stop the current timer and set it back to zero"""
            global timer_active
            timer_active = False
            timer_var.set("00:00:00")
            hour_listbox.selection_clear(0, tk.END)
            minute_listbox.selection_clear(0, tk.END)
            second_listbox.selection_clear(0, tk.END)
            hours_var.set("0")
            minutes_var.set("0")
            seconds_var.set("0")

        # Labels and variables
        hours_var = tk.StringVar(value="0")
        minutes_var = tk.StringVar(value="0")
        seconds_var = tk.StringVar(value="0")
        timer_var = tk.StringVar(value="00:00:00")

        # Getting the set timer on screen
        time_label = tk.Label(alarm_window, textvariable=timer_var, bg=background_color, fg=text_color,
                              font=default_font)
        time_label.grid(column=0, row=0, columnspan=9, pady=20)

        # Setting up the 'Hours' list and scroll
        hour_label = tk.Label(alarm_window, text="Hours", background=background_color, foreground=text_color,
                              font=default_font)
        hour_label.grid(column=1, row=1, columnspan=1, padx=5, pady=5, sticky='ew')
        hour_listbox = tk.Listbox(alarm_window, selectmode="single", exportselection=0, height=10, width=5,
                                  bg=background_color, fg=text_color, font=default_font)
        hour_listbox.grid(column=1, row=2, columnspan=1, padx=5, pady=5, sticky='news')

        for i in range(24):
            hour_listbox.insert(tk.END, str(i))

        hour_listbox.bind("<<ListboxSelect>>",
                          lambda event, v=hours_var: v.set(event.widget.get(event.widget.curselection())))
        hour_scrollbar = tk.Scrollbar(alarm_window, orient="vertical", command=hour_listbox.yview)
        hour_scrollbar.grid(row=2, column=2, pady=5, sticky='wns')
        hour_listbox.config(yscrollcommand=hour_scrollbar.set)

        # Setting up the 'Minutes' list and scroll
        minutes_label = tk.Label(alarm_window, text="Minutes", background=background_color, foreground=text_color,
                                 font=default_font)
        minutes_label.grid(column=4, row=1, columnspan=1, padx=5, pady=5, sticky='ew')
        minute_listbox = tk.Listbox(alarm_window, selectmode="single", exportselection=0, height=10, width=5,
                                    bg=background_color, fg=text_color, font=default_font)
        minute_listbox.grid(column=4, row=2, columnspan=1, padx=5, pady=5, sticky='news')

        for i in range(60):
            minute_listbox.insert(tk.END, str(i))

        minute_listbox.bind("<<ListboxSelect>>",
                            lambda event, v=minutes_var: v.set(event.widget.get(event.widget.curselection())))
        minute_scrollbar = tk.Scrollbar(alarm_window, orient="vertical", command=minute_listbox.yview)
        minute_scrollbar.grid(row=2, column=5, pady=5, sticky='wns')
        minute_listbox.config(yscrollcommand=minute_scrollbar.set)

        # Setting up the 'Seconds' list and scroll
        second_label = tk.Label(alarm_window, text="Seconds", background=background_color, foreground=text_color,
                                font=default_font)
        second_label.grid(column=7, row=1, columnspan=1, padx=5, pady=5, sticky='ew')
        second_listbox = tk.Listbox(alarm_window, selectmode="single", exportselection=0, height=10, width=5,
                                    bg=background_color, fg=text_color, font=default_font)
        second_listbox.grid(column=7, row=2, columnspan=1, padx=5, pady=5, sticky='news')

        for i in range(1, 60):
            second_listbox.insert(tk.END, str(i))

        second_listbox.bind("<<ListboxSelect>>",
                            lambda event, v=seconds_var: v.set(event.widget.get(event.widget.curselection())))
        second_scrollbar = tk.Scrollbar(alarm_window, orient="vertical", command=second_listbox.yview)
        second_scrollbar.grid(row=2, column=8, pady=5, sticky='wns')
        second_listbox.config(yscrollcommand=second_scrollbar.set)

        # Buttons for alarm page
        start_button = tk.Button(alarm_window, text="Start", command=start_timer, bg=background_color,
                                 fg=text_color, font=default_font)
        start_button.grid(column=1, row=4, columnspan=1, padx=20, pady=20)

        reset_button = tk.Button(alarm_window, text="Reset", command=reset_timer, bg=background_color,
                                 fg=text_color, font=default_font)
        reset_button.grid(column=4, row=4, columnspan=1, padx=20, pady=20)

        back2 = tk.Button(alarm_window, text="Back", command=back_alarm, background=background_color,
                          fg=text_color, font=default_font)
        back2.grid(column=7, row=4, columnspan=1, padx=20, pady=20)

        messages_button = tk.Button(alarm_window, text="Manage Messages", command=messages_page,
                                    bg=background_color, fg=text_color, font=default_font)
        messages_button.grid(column=0, row=6, columnspan=9, pady=20)

        # Extra window configurations
        for i in range(9):
            alarm_window.grid_columnconfigure(i, weight=1)

        for i in range(5):
            alarm_window.grid_rowconfigure(i, weight=1)

        alarm_window.protocol("WM_DELETE_WINDOW", close_alarm)

    # Create the buttons for the settings page
    change_colors = tk.Button(settings_window, text="Appearance", bg=background_color, fg=text_color,
                              font=default_font, command=appearance_page)
    change_colors.grid(row=0, column=0, pady=10)

    setting_alarm = tk.Button(settings_window, text="Set Alarm", bg=background_color, fg=text_color,
                              font=default_font, command=alarm_page)
    setting_alarm.grid(row=1, column=0, pady=10)

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
