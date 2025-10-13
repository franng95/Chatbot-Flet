import flet as ft

# Define the sample data for schedules, deadlines, and contacts
schedules = {
    "monday": "No classes",
    "tuesday": "ENGL-1147: 9-11am, RESE-1160: 11-1pm",
    "wednesday": "Personal Tutorial: 11-12pm",
    "thursday": "COMP-1795: 9-11am, COMP-1793: 2-4pm",
    "friday": "COMP-1793: 9-11am, ENGL-1147: 2-4pm"
}

deadlines = {
    "web design and development": {
        "assignment": "9th August: Develop a responsive website in groups of 2 and present it in class explaining the process of developing and the HTML, CSS, JavaScript, and functionalities of the web.",
        "presentation": "9th August"
    },
    "computer research and technology": {
        "portfolio2": "29th July: 500 words essay about the impacts of AI on privacy and personal autonomy.",
        "portfolio3": "9th August: PowerPoint presentation about something each individual alumn thinks AI could help to solve."
    },
    "english for academic purposes": {
        "writing assessment": "2nd August: Essay about the question selected by each alumn.",
        "presentation": "29th August: PowerPoint presentation about the same question developed in the essay assessment.",
        "exam": "13th August: Listening and writing exam."
    },
    "project study": {
        "final report": "5th August: 1500-2000 words research paper explaining the research process and deployment of the selected group project.",
        "presentation": "9th August: Individual 5 minutes video presentation about what you have done on the project and your feelings about it."
    }
}

contacts = {
    "web design and development": "Lorna Leslie: l.m.leslie@greenwich.ac.uk",
    "computer research and technology": "Carol Kennedy: c.m.kennedysmith@greenwich.ac.uk",
    "english for academic purposes": "Laura Laubacher: l.k.laubacher@greenwich.ac.uk",
    "project study": "Alheri Garba: a.f.garba@greenwich.ac.uk",
    "personal tutorial": "Jenny Rogers: jenny.rogers@greenwich.ac.uk"
}

def main(page: ft.Page):

    def add_message(message, from_user=True):
        bubble = ft.Container(
            content=ft.Text(message),
            bgcolor=ft.colors.BLUE_GREY_100 if from_user else ft.colors.GREEN_100,
            padding=10,
            border_radius=ft.border_radius.all(10),
            margin=ft.margin.symmetric(vertical=5, horizontal=10),
        )
        messages.controls.append(bubble)
        messages.update()
        page.scroll_to_control(messages)

    def option_selected(e):
        selected_option = e.control.data
        user_message = f"User: {selected_option}"
        add_message(user_message)
        bot_response = ""

        if selected_option == "Schedule":
            bot_response = f"Bot: Here is your schedule: {schedules}"
        elif selected_option == "Deadlines":
            bot_response = f"Bot: Here are your deadlines: {deadlines}"
        elif selected_option == "Contacts":
            bot_response = f"Bot: Here are your contacts: {contacts}"
        else:
            bot_response = "Bot: I'm not sure how to help with that. Here are some options you might find useful."
        
        add_message(bot_response, from_user=False)
        add_main_options()

    def add_main_options():
        options_row = ft.Row([
            ft.ElevatedButton("Schedule", data="Schedule", on_click=option_selected),
            ft.ElevatedButton("Deadlines", data="Deadlines", on_click=option_selected),
            ft.ElevatedButton("Contacts", data="Contacts", on_click=option_selected)
        ])
        messages.controls.append(options_row)
        messages.update()

    def send_message(e):
        user_input = input_text.value
        if user_input:
            add_message(f"User: {user_input}")
            input_text.value = ""
            page.update()

    messages = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    input_text = ft.TextField(hint_text="Enter your message", expand=True, on_submit=send_message)
    send_button = ft.ElevatedButton("Send", on_click=send_message)

    page.add(
        messages,
        ft.Row([input_text, send_button], alignment=ft.MainAxisAlignment.CENTER),
    )

    add_message("Bot: Hello! How can I assist you today?", from_user=False)
    add_main_options()

ft.app(target=main)
