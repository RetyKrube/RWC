import datetime
import tkinter as tk


def timing():
    t_now = datetime.datetime.now().strftime('%I:%M:%S:%p')
    t_label.config(text=t_now, background=background_color, foreground=text_color)
    t_label.after(1000, timing)


def settings_page():
    main_window.withdraw()
    settings_window = tk.Toplevel()
    settings_window.title("RWC Settings")
    settings_window.geometry("")
    settings_window.configure(background=background_color)

    def close_window():
        settings_window.destroy()
        main_window.destroy()

    def close_settings():
        settings_window.destroy()
        main_window.deiconify()

    change_colors = tk.Button(settings_window, text="Appearance", bg=background_color, fg=text_color, font=default_font)
    change_colors.grid(padx=10, pady=10)

    setting_alarm = tk.Button(settings_window, text="Set Alarm", bg=background_color, fg=text_color, font=default_font)
    setting_alarm.grid(padx=10, pady=10)

    change_sound = tk.Button(settings_window, text="Alarm Sound", bg=background_color, fg=text_color, font=default_font)
    change_sound.grid(padx=10, pady=10)

    font_settings = tk.Button(settings_window, text="Fonts", bg=background_color, fg=text_color, font=default_font)
    font_settings.grid(padx=10, pady=10)

    close_settings = tk.Button(settings_window, text="Close", command=close_settings,
                               bg=background_color, fg=text_color, font=default_font)
    close_settings.grid(padx=10, pady=10)

    settings_window.protocol("WM_DELETE_WINDOW", close_window)

    settings_window.mainloop()


background_color = "black"
text_color = "lime"
default_font = ("Arial", 15)

main_window = tk.Tk()
main_window.title("RWC(Remote Work Clock)")
main_window.geometry(f'350x100')
main_window.configure(background=background_color)

t_label = tk.Label(main_window, font=("ds-digital", 50))
t_label.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='news')

settings_button = tk.Button(main_window, text="Settings", command=settings_page, bg=background_color, fg=text_color)
settings_button.grid(row=2, column=0, columnspan=2)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.rowconfigure(2, weight=1)

timing()

main_window.mainloop()
