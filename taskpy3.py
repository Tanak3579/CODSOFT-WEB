import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    def on_choice(user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)
        user_score, comp_score = int(lbl_user_score.cget("text")), int(lbl_comp_score.cget("text"))

        lbl_user_choice.config(text=f"Your choice: {user_choice}")
        lbl_comp_choice.config(text=f"Computer's choice: {computer_choice}")
        lbl_result.config(text=f"Result: {result}")

        if result == "You win!":
            lbl_user_score.config(text=str(user_score + 1))
        elif result == "You lose!":
            lbl_comp_score.config(text=str(comp_score + 1))

    window = tk.Tk()
    window.title("Rock-Paper-Scissors Game")

    # Fonts and Colors
    title_font = ('Helvetica', 18, 'bold')
    button_font = ('Helvetica', 12)
    label_font = ('Helvetica', 12)
    window.configure(background='#333333')



    lbl_title = tk.Label(window, text="Rock-Paper-Scissors Game", font=title_font, bg='#333333', fg='white')
    lbl_title.pack(pady=10)

    lbl_user_choice = tk.Label(window, text="Your choice: ", font=label_font, bg='#333333', fg='white')
    lbl_user_choice.pack()

    lbl_comp_choice = tk.Label(window, text="Computer's choice: ", font=label_font, bg='#333333', fg='white')
    lbl_comp_choice.pack()

    lbl_result = tk.Label(window, text="Result: ", font=label_font, bg='#333333', fg='white')
    lbl_result.pack()

    lbl_user_score = tk.Label(window, text="0", font=label_font, bg='#333333', fg='white')
    lbl_user_score.pack()

    lbl_comp_score = tk.Label(window, text="0", font=label_font, bg='#333333', fg='white')
    lbl_comp_score.pack()

    btn_frame = tk.Frame(window, bg='#333333')
    btn_frame.pack(pady=10)

    choices = ['rock', 'paper', 'scissors']
    for choice in choices:
        btn = tk.Button(btn_frame, text=choice.capitalize(), font=button_font, bg='#222222', fg='white',
                        activebackground='#444444', activeforeground='white', 
                        command=lambda ch=choice: on_choice(ch))
        btn.pack(side=tk.LEFT, padx=10)

    window.mainloop()

play_game()
