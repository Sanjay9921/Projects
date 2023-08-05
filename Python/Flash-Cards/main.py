# Libraries
from import_modules import *
from import_constants import *

# Dictionaries
current_card = {}
to_learn = {}
to_learn_backup = {}
is_flipped = False

# Words from the excel/csv file
df = pd.read_csv("data/deutsch_words.csv", encoding = "ISO-8859-1")
to_learn = df.to_dict(orient="records")
to_learn_backup = to_learn.copy()

# Functions

## Get Next Card
def get_next_card():
    global current_card, is_flipped

    is_empty = len(to_learn) == 0

    if not is_empty:
        # Randomly selects a Deutsch word and removes it from the remaining loop
        current_card = random.choice(to_learn)
        to_learn.remove(current_card)

        canvas.itemconfig(card_title, text="Deutsch", fill="black")
        canvas.itemconfig(card_word, text=current_card["German"], fill="black")
        canvas.itemconfig(card_bg, image=card_front_img)
    else:
        canvas.itemconfig(card_title, text="The End", fill="black")
        canvas.itemconfig(card_word, text="Restart ?", fill="black")
        canvas.itemconfig(card_bg, image=card_front_img)

        restart_btn["state"] = "normal"
        flip_btn["state"] = "disabled"
        next_btn["state"] = "disabled"

    is_flipped = False

## Flip the card (displays English translated word)
def flip_card():
    global is_flipped

    if is_flipped:
        canvas.itemconfig(card_title, text="Deutsch", fill="black")
        canvas.itemconfig(card_word, text=current_card["German"], fill="black")
        canvas.itemconfig(card_bg, image=card_front_img)

        is_flipped = False
    else:
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas.itemconfig(card_bg, image=card_back_img)

        is_flipped = True

## Restart the game
def restart_card():
    global to_learn
    to_learn = to_learn_backup.copy()

    flip_btn["state"] = "normal"
    next_btn["state"] = "normal"
    restart_btn["state"] = "disable"

    get_next_card()

# Main UI File

## Window
window = Tk()
window.title("Flashen Karten - Deutsch to Englisch")
window.config(padx=50, pady=50, bg=BG_COLOR)

## Image Widget

### Front of the card
card_front_img = Image.open("images/card_front.png")
card_front_img = card_front_img.resize((400, 225))
card_front_img = ImageTk.PhotoImage(card_front_img)

### Back of the card
card_back_img = Image.open("images/card_back.png")
card_back_img = card_back_img.resize((400, 225))
card_back_img = ImageTk.PhotoImage(card_back_img)

### Next Button Image
next_img = Image.open("images/next.png")
next_img = next_img.resize((100, 100))
next_img = ImageTk.PhotoImage(next_img)

### Flip Button Image
flip_img = Image.open("images/flip.png")
flip_img = flip_img.resize((100, 100))
flip_img = ImageTk.PhotoImage(flip_img)

### Restart Button Image
restart_img = Image.open("images/restart.png")
restart_img = restart_img.resize((100, 100))
restart_img = ImageTk.PhotoImage(restart_img)

## Button Widget

### Next Button
next_btn = Button(image=next_img, highlightthickness=0, command=get_next_card)
next_btn.config(bg=BG_COLOR)

### Flip Button
flip_btn = Button(image=flip_img, highlightthickness=0, command=flip_card)
flip_btn.config(bg=BG_COLOR)

### Flip Button
restart_btn = Button(image=restart_img, highlightthickness=0, command=restart_card)
restart_btn.config(bg=BG_COLOR)
restart_btn["state"] = "disable"

## Canvas Widget
canvas = Canvas(width=800, height=450, highlightthickness=0)

card_bg = canvas.create_image(400, 225, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=SET_FONT1)
card_word = canvas.create_text(400, 200, text="Word", font=SET_FONT2)

canvas.config(bg=BG_COLOR)

## Grid
canvas.grid(row=0, column=0, columnspan=3)
flip_btn.grid(row=1, column=0)
next_btn.grid(row=1, column=1)
restart_btn.grid(row=1, column=2)

## Run the appl
get_next_card()
window.mainloop()