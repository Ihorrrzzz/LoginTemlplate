import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk  # Import to handle image assets

# Function to create a rounded rectangle on the canvas
def create_rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

# Function to manage placeholder text
def on_entry_focus_in(entry, default_text, color):
    if entry.get() == default_text:
        entry.delete(0, "end")
        entry.config(fg=color)

def on_entry_focus_out(entry, default_text, color):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg=color)

def toggle_password():
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        toggle_btn.config(image=hidden_icon)
    else:
        entry_password.config(show='')
        toggle_btn.config(image=visible_icon)

# Create the main window
root = tk.Tk()
root.title("Login Window")
root.geometry("540x400")
root.configure(bg='#2c2c2c')  # Dark background

# Load the images for the toggle button
hidden_icon = ImageTk.PhotoImage(Image.open("hidden.png").resize((16, 16)))
visible_icon = ImageTk.PhotoImage(Image.open("visible.png").resize((16, 16)))

# Styling variables
entry_default_bg = '#FFFFFF'  # White background for both label and canvas
entry_hover_bg = '#FFFFFF'    # White background
entry_default_fg = '#BDC1CA'  # Neutral-400 for placeholder text
entry_typing_fg = '#171A1F'   # Neutral-900 for typed text
label_bg = entry_default_bg   # Make label background the same as the canvas
label_fg = '#171A1F'          # Neutral-900 for label text
font = ('Manrope', 14)
radius = 4                    # Radius for rounded corners

# Canvas dimensions
canvas_width = 469
canvas_height = 71

# Create Canvas for Email
canvas_email = Canvas(root, width=canvas_width, height=canvas_height, bg='#2c2c2c', highlightthickness=0)
canvas_email.pack(pady=(40, 10))

# Draw the rounded rectangle
create_rounded_rect(canvas_email, 0, 0, canvas_width, canvas_height, radius, fill=entry_default_bg)

# Place Email label
label_email = tk.Label(canvas_email, text="Email", fg=label_fg, bg=label_bg, font=(font[0], 14, 'bold'))
canvas_email.create_window(12, 13.5, anchor='nw', window=label_email)  # Positioning Email label

# Create and place Email entry
entry_email = tk.Entry(canvas_email, fg=entry_default_fg, bg=entry_default_bg, font=font,
                       bd=0, highlightthickness=0, width=38)
entry_email.insert(0, 'example.email@gmail.com')
canvas_email.create_window(12.5, canvas_height - 12.5 - 22, anchor='nw', window=entry_email)  # Positioning Email entry

entry_email.bind("<FocusIn>", lambda event: on_entry_focus_in(entry_email, 'example.email@gmail.com', entry_typing_fg))
entry_email.bind("<FocusOut>", lambda event: on_entry_focus_out(entry_email, 'example.email@gmail.com', entry_default_fg))

# Create Canvas for Password
canvas_password = Canvas(root, width=canvas_width, height=canvas_height, bg='#2c2c2c', highlightthickness=0)
canvas_password.pack(pady=(20, 10))

# Draw the rounded rectangle
create_rounded_rect(canvas_password, 0, 0, canvas_width, canvas_height, radius, fill=entry_default_bg)

# Place Password label
label_password = tk.Label(canvas_password, text="Password", fg=label_fg, bg=label_bg, font=(font[0], 14, 'bold'))
canvas_password.create_window(12, 13.5, anchor='nw', window=label_password)  # Positioning Password label

# Create and place Password entry
entry_password = tk.Entry(canvas_password, fg=entry_default_fg, bg=entry_default_bg, font=font,
                          bd=0, highlightthickness=0, width=34, show='*')
entry_password.insert(0, 'Enter at least 8+ characters')
canvas_password.create_window(12.5, canvas_height - 10 - 22, anchor='nw', window=entry_password)  # Positioning Password entry

entry_password.bind("<FocusIn>", lambda event: on_entry_focus_in(entry_password, 'Enter at least 8+ characters', entry_typing_fg))
entry_password.bind("<FocusOut>", lambda event: on_entry_focus_out(entry_password, 'Enter at least 8+ characters', entry_default_fg))

# Password Toggle Button with Image
toggle_btn = tk.Label(canvas_password, image=hidden_icon, bg=entry_default_bg)
toggle_btn.bind("<Button-1>", lambda event: toggle_password())
canvas_password.create_window(canvas_width - 12 - 16, canvas_height - 18 - 16, anchor='nw', window=toggle_btn)  # Aligning the button

# Run the main loop
root.mainloop()
