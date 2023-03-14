import tkinter as tk
import openai

API= "YOUR_API_KEY"
openai.api_key = API # Replace with your own API key

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        engine="text-davinci-00e",  # Use the GPT-3.5 Turbo engine
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def show_dialog():
    dialog = tk.Toplevel()
    dialog.geometry("400x300")
    dialog.title("OpenAI Chatbot")

    prompt_label = tk.Label(dialog, text="User: ")
    prompt_label.pack(side="left")

    prompt_entry = tk.Entry(dialog)
    prompt_entry.pack(side="left", fill="x", expand=True)

    response_text = tk.Text(dialog)
    response_text.pack(side="bottom", fill="both", expand=True)

    def generate_and_display_response():
        prompt = prompt_entry.get()
        response = generate_response(prompt)
        response_text.insert("end", "Chatbot: " + response + "\n")
        prompt_entry.delete(0, "end")

    submit_button = tk.Button(dialog, text="Submit", command=generate_and_display_response)
    submit_button.pack(side="right")

    dialog.mainloop()

root = tk.Tk()
root.geometry("200x100")
root.title("OpenAI Chatbot")

openai_button = tk.Button(root, text="OpenAI Chatbot", command=show_dialog)
openai_button.pack(fill="both", expand=True)

root.mainloop()
