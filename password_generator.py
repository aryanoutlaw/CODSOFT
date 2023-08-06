import PySimpleGUI as sg
import random
import string
import pyperclip

def generate_password(length, characters):
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():

    default_password_length = 12
    max_password_length = 64

    sg.theme('DarkBlue14')
    

    layout = [
        [sg.Text("Password Generator")],
        [sg.Text("Enter the desired length of the password:")],
        [sg.Input(key="-LENGTH-", size=(10, 1), default_text=default_password_length)],
        [sg.Checkbox("Uppercase", key="-UPPERCASE-")],
        [sg.Checkbox("Lowercase", key="-LOWERCASE-")],
        [sg.Checkbox("Numbers", key="-NUMBERS-")],
        [sg.Checkbox("Symbols", key="-SYMBOLS-")],
        [sg.Button("Generate Password"), sg.Button("Exit")],
        [sg.Text(size=(40, 1), key="-ERROR-", text_color="red")],
        [sg.Output(size=(40, 10), key="-OUTPUT-")]
    ]

    window = sg.Window("Password Generator", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Generate Password":
            try:
                password_length = int(values["-LENGTH-"])
                if password_length <= 0:
                    raise ValueError("Password length must be a positive integer.")
                if password_length > max_password_length:
                    raise ValueError(f"Password length cannot exceed {max_password_length}.")

                characters = ""

                if values["-UPPERCASE-"]:
                    characters += string.ascii_uppercase
                if values["-LOWERCASE-"]:
                    characters += string.ascii_lowercase
                if values["-NUMBERS-"]:
                    characters += string.digits
                if values["-SYMBOLS-"]:
                    characters += string.punctuation

                # If no checkboxes are selected, include only uppercase letters by default
                if not any(values.values()):
                    characters = string.ascii_uppercase

                password = generate_password(password_length, characters)
                window["-OUTPUT-"].update("Generated Password: " + password)
                pyperclip.copy(password)
                window["-ERROR-"].update("Password copied to clipboard!", text_color="red")
            except ValueError as e:
                window["-ERROR-"].update(str(e))
                window["-OUTPUT-"].update("")

    window.close()

if __name__ == "__main__":
    main()
