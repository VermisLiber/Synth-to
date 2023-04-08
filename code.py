#importing required libraries
import random
import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter import filedialog
import nltk
from nltk.corpus import wordnet
from textblob import TextBlob
import gensim
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from transformers import pipeline
from transformers import AutoModelForSequenceClassification
import sqlite3
y=""
width, height = 900,600


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Post:
    def __init__(self, author, content, is_public):
        self.author = author
        self.content = content
        self.is_public = is_public

class UserInterface:

    def splash_screen(self):
        # Create a lavender canvas
        canvas = Canvas(self.master, bg="#F9A754", width=900, height=600)
        canvas.pack(expand=YES, fill=BOTH)

        # Create a white 'σ' in the center of the canvas
        canvas.create_text(450, 300, text="σ", font=("Helvetica", 100), fill="white")

        # Update the canvas and wait for 5 seconds
        self.master.update()
        self.master.after(5000)

        # Destroy the canvas and continue with the UI initialization
        canvas.destroy()
    def __init__(self, master):
        self.master = master
        master.title("Synth-to")
        self.splash_screen()
        master.geometry("900x600")
        master.configure(bg="#F9A754")
        master.option_add("*Font", "Times 14")
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                               (author TEXT, content TEXT, is_public INTEGER)''')
        self.cursor.execute("SELECT * FROM posts WHERE is_public=1")
        posts = self.cursor.fetchall()
        canvas1= Canvas(self.master, width=width, height=height, bd=0, highlightthickness=0)
        self.background_image1=Image.open("Resources/Images/cng.jpg")
        self.img1 = ImageTk.PhotoImage(self.background_image1)
        canvas1.pack(fill=BOTH, expand=True)
        canvas1.create_image(0, 0, image=self.img1, anchor='nw')
        x, y, r = 30, 30, 13
        canvas1.create_oval(x-r, y-r, x+r, y+r, fill='#F9A754')
        canvas1.create_text(x, y, text='σ', fill='white', font=("Helvetica", 17))
        self.login_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Login',font=("Times New Roman",15),command=self.show_login_screen)
        self.login_button.place(relx=1.0, x=-10, y=20, anchor='ne')
        self.post_textbox = tk.Text(self.master, height=28, width=90,font=("Times New Roman",11))
        self.post_textbox.place(relx=0.48, rely=0.5, anchor='center')
        for post in posts:
          self.post_textbox.insert(END, f"{post[0]}:\n{post[1]}\n\n")
        self.master.update()

    def show_login_screen(self):
        self.login_button.destroy()
        self.post_textbox.destroy()
        self.labelFrame =Frame(self.master,bg='#F9A754')
        self.labelFrame.place(relx=0.05,rely=0.2,relwidth=0.9,relheight=0.7)
        self.lb1 = Label(self.labelFrame,text="Username: ",font=("Times New Roman",15), bg='#F9A754', fg='white')
        self.lb1.place(relx=0.05,rely=0.1, relheight=0.09)
        self.lb2 = Label(self.labelFrame,text="Password: ",font=("Times New Roman",15), bg='#F9A754', fg='white')
        self.lb2.place(relx=0.05,rely=0.2, relheight=0.09)
        self.user_entry = Entry(self.labelFrame, font=("Times New Roman", 15))
        self.user_entry.place(relx=0.3, rely=0.1, relwidth=0.6, relheight=0.08)
        y=self.user_entry.get()
        self.password_entry = Entry(self.labelFrame, font=("Times New Roman", 15), show="*")
        self.password_entry.place(relx=0.3, rely=0.2, relwidth=0.6, relheight=0.08)
        self.login_button1 = tk.Button(self.master,bg='#F9A754', fg="white", text='Login',font=("Times New Roman",15),command=self.log_in)
        self.login_button1.place(relx=0.5, rely=0.5, anchor="center")
        self.create_account = tk.Button(self.master,bg='#F9A754', fg="white", text='Create Account',font=("Times New Roman",15),command=self.create_account)
        self.create_account.place(relx=0.5, rely=0.6, anchor="center")
        self.returnback = tk.Button(self.master,bg='#F9A754', fg="white", text='Return',font=("Times New Roman",15),command=self.return_to_init_screen)
        self.returnback.place(relx=0.5, rely=0.7, anchor="center")
        self.master.update()
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                  (username TEXT, password TEXT)''')
    def return_to_init_screen(self):
        # destroy the login screen
        self.labelFrame.destroy()
        self.lb1.destroy()
        self.lb2.destroy()
        self.user_entry.destroy()
        self.password_entry.destroy()
        self.returnback.destroy()
        self.login_button1.destroy()
        self.create_account.destroy()
        self.master.update()

        # display the initial screen
        self.login_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Login',font=("Times New Roman",15),command=self.show_login_screen)
        self.login_button.place(relx=1.0, x=-10, y=20, anchor='ne')
        self.cursor.execute("SELECT * FROM posts WHERE is_public=1")
        posts = self.cursor.fetchall()
        self.post_textbox = tk.Text(self.master, height=28, width=90,font=("Times New Roman",11))
        self.post_textbox.place(relx=0.48, rely=0.5, anchor='center')
        for post in posts:
          self.post_textbox.insert(END, f"{post[0]}:\n{post[1]}\n\n")
        # other initial screen elements...
        self.master.update()
    def returntwo(self):
        # destroy the login screen
        self.input_text.destroy()
        self.output_text.destroy()
        self.spell_check_button.destroy()
        self.grammer_check_button.destroy()
        self.synonyms_button.destroy()
        self.writing_prompts_button.destroy()
        self.vocabulary_button.destroy()
        self.summarize_para__button.destroy()
        self.summarize_bullet_button.destroy()
        self.return2.destroy()
        self.post_button.destroy()
        self.public_checkbutton.destroy()
        self.menubar.destroy()
        self.master.update()

        # display the initial screen
        self.login_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Login',font=("Times New Roman",15),command=self.show_login_screen)
        self.login_button.place(relx=1.0, x=-10, y=20, anchor='ne')
        self.cursor.execute("SELECT * FROM posts WHERE is_public=1")
        posts = self.cursor.fetchall()
        self.post_textbox = tk.Text(self.master, height=28, width=90,font=("Times New Roman",11))
        self.post_textbox.place(relx=0.48, rely=0.5, anchor='center')
        for post in posts:
          self.post_textbox.insert(END, f"{post[0]}:\n{post[1]}\n\n")
        # other initial screen elements...
        self.master.update()
    def create_account(self):
        username = self.user_entry.get()
        password = self.password_entry.get()

        # Check if the username is already taken
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        result = self.cursor.fetchone()

        if result:
            # Display an error message
            messagebox.showerror("Error", "Username already taken.")
        else:
            # Save the user's account to the database
            account = Account(username, password)
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (account.username, account.password))
            self.conn.commit()

            # Display a success message
            messagebox.showinfo("Success", "Account created successfully.")
    def log_in(self):
       username = self.user_entry.get()
       password = self.password_entry.get()

      # Check if the username and password match a record in the database
       self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
       result = self.cursor.fetchone()

       if result:
          self.labelFrame.destroy()
          self.lb1.destroy()
          self.lb2.destroy()
          self.user_entry.destroy()
          self.password_entry.destroy()
          self.returnback.destroy()
          self.login_button1.destroy()
          self.create_account.destroy()
          # Create a text box for input
          self.input_text = tk.Text(self.master, height=20, width=50,font=("Times New Roman",11))
          self.input_text.place(relx=0.01, rely=0.5, anchor="w")

          # Create a text box for output
          self.output_text = tk.Text(self.master, height=20, width=50,font=("Times New Roman",11))
          self.output_text.place(relx=0.99, rely=0.5, anchor="e")

          self.spell_check_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Spell Check',font=("Times New Roman",13),command=self.spell_check)
          self.spell_check_button.place(relx=0.5, rely=0.15, anchor="center")

          self.grammer_check_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Grammar Check',font=("Times New Roman",13),command=self.grammar_check)
          self.grammer_check_button.place(relx=0.5, rely=0.25, anchor="center")

          self.synonyms_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Synonyms',font=("Times New Roman",13),command=self.synonyms)
          self.synonyms_button.place(relx=0.5, rely=0.35, anchor="center")

          self.writing_prompts_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Writing Prompts',font=("Times New Roman",13),command=self.writing_prompts)
          self.writing_prompts_button.place(relx=0.5, rely=0.45, anchor="center")

          self.vocabulary_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Vocabulary',font=("Times New Roman",13),command=self.vocabulary)
          self.vocabulary_button.place(relx=0.5, rely=0.55, anchor="center")

          self.summarize_para__button = tk.Button(self.master,bg='#F9A754', fg="white", text='Summarize Para',font=("Times New Roman",13),command=self.summarizepara)
          self.summarize_para__button.place(relx=0.5, rely=0.65, anchor="center")

          self.summarize_bullet_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Summarize Bullet',font=("Times New Roman",13),command=self.summarizebullet)
          self.summarize_bullet_button.place(relx=0.5, rely=0.75, anchor="center")

          self.return2 = tk.Button(self.master,bg='#F9A754', fg="white", text='Return',font=("Times New Roman",13),command=self.returntwo)
          self.return2.place(relx=0.5, rely=0.85, anchor="center")

          self.post_button = tk.Button(self.master,bg='#F9A754', fg="white", text='Post',font=("Times New Roman",13),command=self.post)
          self.post_button.place(relx=0.5, rely=0.95, anchor="center")

          self.is_public = tk.BooleanVar()
          self.public_checkbutton = tk.Checkbutton(self.master, text="Public",font=("Times New Roman",13), variable=self.is_public)
          self.public_checkbutton.place(relx=0.7, rely=0.92)

          # Create a menu bar
          self.menubar = tk.Menu(self.master)
          filemenu = tk.Menu(self.menubar, tearoff=0)
          filemenu.add_command(label="Open", command=self.open_file)
          filemenu.add_command(label="Save", command=self.save_file)
          filemenu.add_separator()
          filemenu.add_command(label="Exit", command=self.master.quit)
          self.menubar.add_cascade(label="File", menu=filemenu)
          self.master.config(menu=self.menubar)
          self.master.update()

          # Load the pre-trained models and data files
          nltk.download('punkt')
          nltk.download('wordnet')
          nltk.download('words')
          nltk.download('stopwords')
          self.spellchecker = nltk.corpus.words.words('en')

          self.tokenizer = AutoTokenizer.from_pretrained("sshleifer/tiny-ctrl")
          model_name = "distilbert-base-uncased-finetuned-sst-2-english"
          self.model = model_name

       else:
          # Display an error message
          messagebox.showerror("Error", "Incorrect username or password.")
    def spell_check(self):
     text = self.input_text.get("1.0", "end-1c")  # get the text from the input_text widget
    # perform spell check on the text here
     blob = TextBlob(text)
     corrected_text = str(blob.correct())
    # update the output_text widget with the corrected text
     self.output_text.delete("1.0", tk.END)  # clear the output_text widget
     self.output_text.insert(tk.END, corrected_text)  # insert the corrected text into the output_text widget
    def grammar_check(self):
     text = self.input_text.get("1.0", "end-1c")  # get the text from the input_text widget

     matches = TextBlob(text).correct()
     self.output_text.delete("1.0", tk.END)  # clear the output_text widget
     self.output_text.insert(tk.END, matches)  # insert the matches into the output_text widget
    def synonyms(self):
     text = self.input_text.get("1.0", "end-1c")  # get the text from the input_text widget
     words = nltk.word_tokenize(text)  # tokenize the text into words
     synonyms = []  # initialize an empty list to store synonyms
     for word in words:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.name() != word:  # exclude the original word from the list of synonyms
                    synonyms.append(lemma.name())
    # update the output_text widget with the list of synonyms
     self.output_text.delete("1.0", tk.END)  # clear the output_text widget
     self.output_text.insert(tk.END, ", ".join(set(synonyms)))  # insert the synonyms into the output_text widget, removing duplicates
    def writing_prompts(self):
        prompts = [
            "Write about a childhood memory that you cherish.",
            "Describe your dream vacation destination and what you would do there.",
            "Write a short story about a character who discovers a hidden talent.",
            "Write about a time when you had to overcome a challenge.",
            "Describe a place that you find peaceful or inspiring.",
            "Write about a historical figure that you admire and explain why.",
            "Create a dialogue between two characters who have just met.",
            "Write a letter to your future self.",
            "Describe a typical day in your life.",
            "Write about a decision that you regret making and what you learned from it."
        ]
        prompt = random.choice(prompts)
        self.output_text.delete("1.0", tk.END)  # clear the output_text widget
        self.output_text.insert(tk.END, prompt)  # insert the matches into the output_text widget
    def vocabulary(self):
        # Load the text from the text widget
        text = self.input_text.get("1.0", "end-1c")

        # Tokenize the text
        tokens = nltk.word_tokenize(text)

        # Get synonyms and antonyms for each token
        synonyms = []
        antonyms = []
        for token in tokens:
            for syn in wordnet.synsets(token):
                for lemma in syn.lemmas():
                    if lemma.name() != token:
                        synonyms.append(lemma.name())
                        if lemma.antonyms():
                            antonyms.append(lemma.antonyms()[0].name())

        # Create a set of unique synonyms and antonyms
        unique_synonyms = set(synonyms)
        unique_antonyms = set(antonyms)

        # Display the vocabulary and phrases in a new window
        vocabulary_window = tk.Toplevel(self.master, width=50, height=50)
        vocabulary_window.title("Vocabulary and Phrases")
        vocabulary_text = "Synonyms:\n\n" + "\n".join(unique_synonyms) + "\n\nAntonyms:\n\n" + "\n".join(unique_antonyms)
        vocabulary_label = tk.Label(vocabulary_window, text=vocabulary_text,font=("Times New Roman",11))
        vocabulary_label.pack()
    def summarizepara(self):
        # Load the summarization pipeline
        summarizer = pipeline("summarization")
        # Get the text to summarize
        text = self.input_text.get("1.0", "end-1c")
        summary = summarizer(text, max_length=512, min_length=128, do_sample=False)[0]["summary_text"]
        self.output_text.delete("1.0", tk.END)  # clear the output_text widget
        self.output_text.insert(tk.END, summary)
    def summarizebullet(self):
        summarizer = pipeline("summarization")
        # Get the text to summarize
        text = self.input_text.get("1.0", "end-1c")
        summary = summarizer(text, max_length=256, min_length=64, do_sample=False, num_beams=4, length_penalty=2.0, no_repeat_ngram_size=2)
        bullets = [f"- {s['generated_text'].strip()}" for s in summary]
        summary_text = "\n".join(bullets)
        self.output_text.delete("1.0", tk.END)  # clear the output_text widget
        self.output_text.insert(tk.END, summary_text)
    def post(self):
        author = y
        content = self.output_text.get("1.0", "end-1c")
        is_public = self.is_public.get()

        # Save the post to the database
        post = Post(author, content, is_public)
        self.cursor.execute("INSERT INTO posts VALUES (?, ?, ?)", (post.author, post.content, post.is_public))
        self.conn.commit()

        # Display a success message
        messagebox.showinfo("Success", "Post created successfully.")
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                file_content = f.read()
                self.input_field.delete('1.0', tk.END)
                self.input_field.insert(tk.END, file_content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as f:
                file_content = self.output_field.get('1.0', tk.END)
                f.write(file_content)



root = tk.Tk()
interface = UserInterface(root)
root.mainloop()
