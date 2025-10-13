import flet as ft

# Define the static data sets
schedules = {
    "Monday": "No classes",
    "Tuesday": [
        {"subject": "English for Academic Purposes", "time": "9-12pm", "room": "Room 105 (18)"},
        {"subject": "Project Study", "time": "12-2pm", "room": "Room 205 (Lab L23)"}
    ],
    "Wednesday": [
        {"subject": "Personal Tutorial", "time": "11-12pm", "room": "Room 207 (Lab L21)"},
        {"subject": "Computer Research and Technology", "time": "12-4pm", "room": "Room 601 (Lab L12)"}
    ],
    "Thursday": [
        {"subject": "Computer Research and Technology", "time": "9-11am", "room": "Room 601 (Lab L12)"},
        {"subject": "Web Design and Development", "time": "2-4pm", "room": "Room 601 (Lab L12)"}
    ],
    "Friday": [
        {"subject": "Web Design and Development", "time": "9-11am", "room": "Room 601 (Lab L12)"},
        {"subject": "English for Academic Purposes", "time": "2-4pm", "room": "Room 105 (18)"}
    ]
}

contacts = {
    "Web Design and Development": "Lorna Leslie - l.m.leslie@greenwich.ac.uk",
    "Computer Research and Technology": "Carol Kennedy - c.m.kennedysmith@greenwich.ac.uk",
    "English for Academic Purposes": "Laura Laubacher - l.k.laubacher@greenwich.ac.uk",
    "Project Study": "Alheri Garba - a.f.garba@greenwich.ac.uk",
    "Personal Tutorial": "Andy Yianni - a.yianni@greenwich.ac.uk"
}

deadlines = {
    "Web Design and Development": [
        {"type": "Assignment", "date": "9th August", "details": "Develop a responsive website in groups of 2 and present it in class explaining the process of developing and the HTML, CSS, JavaScript, and functionalities of the web."},
        {"type": "Presentation", "date": "9th August", "details": "Present the developed website in class."}
    ],
    "Computer Research and Technology": [
        {"type": "Portfolio 2", "date": "29th July", "details": "500 words essay about the impacts of AI on privacy and personal autonomy."},
        {"type": "Portfolio 3", "date": "9th August", "details": "PowerPoint presentation about something each individual alumnus thinks AI could help to solve."}
    ],
    "English for Academic Purposes": [
        {"type": "Writing Assessment", "date": "2nd August", "details": "Essay about the question selected by each alumnus."},
        {"type": "Presentation", "date": "29th August", "details": "PowerPoint presentation about the same question developed in the essay assessment."},
        {"type": "Exam", "date": "13th August", "details": "Listening and writing exam."}
    ],
    "Project Study": [
        {"type": "Final Report", "date": "5th August", "details": "1500-2000 words research paper explaining the research process and deployment of the selected group project."},
        {"type": "Presentation", "date": "9th August", "details": "Individual 5 minutes video presentation about what you have done on the project and your feelings about it."}
    ]
}

# Keyword mappings
keyword_mappings = {
    "english": "English for Academic Purposes",
    "eap": "English for Academic Purposes",
    "crt": "Computer Research and Technology",
    "computer research": "Computer Research and Technology",
    "web design": "Web Design and Development",
    "web dev": "Web Design and Development",
    "project": "Project Study",
    "tutorial": "Personal Tutorial"
}

# Function to map keywords to full subject names
def map_keyword_to_subject(keyword):
    for key, subject in keyword_mappings.items():
        if key in keyword:
            return subject
    return None

# Function to handle user queries
def handle_query(query):
    query = query.lower()
    response = ""
    
    if any(greeting in query for greeting in ["hello", "hi", "hey"]):
        response = "Hello! How can I assist you today?"
    elif "timetable" in query or "schedule" in query:
        response = get_weekly_schedule()
    elif "class" in query:
        response = get_schedule_response(query)
    elif "contact" in query or "email" in query:
        response = get_contact_response(query)
    elif "deadline" in query or "due date" in query:
        response = get_deadline_response(query)
    else:
        response = "I'm sorry, I'm not very sure of that info. Were you looking for something like this?"
        # Suggest related information
        related_info = suggest_related_info(query)
        response += f"\n{related_info}"
    
    return response

def get_weekly_schedule():
    response = "Weekly Schedule:\n"
    for day, classes in schedules.items():
        response += f"\n{day}:\n"
        if classes == "No classes":
            response += "No classes\n"
        else:
            for cls in classes:
                response += f"  - {cls['subject']} from {cls['time']} at {cls['room']}\n"
    return response

def get_schedule_response(query):
    for day in schedules.keys():
        if day.lower() in query:
            classes = schedules[day]
            if classes == "No classes":
                return f"{day}: No classes"
            else:
                response = f"{day} Schedule:\n"
                for cls in classes:
                    response += f"{cls['subject']} from {cls['time']} at {cls['room']}\n"
                return response
    return "Schedule not found."

def get_contact_response(query):
    subject = map_keyword_to_subject(query)
    if subject:
        contact = contacts.get(subject, "Contact information not found.")
        return f"Contact for {subject}: {contact}"
    return "Contact information not found."

def get_deadline_response(query):
    subject = map_keyword_to_subject(query)
    if subject:
        deadlines_list = deadlines.get(subject, [])
        if deadlines_list:
            response = f"Deadlines for {subject}:\n"
            for deadline in deadlines_list:
                response += f"{deadline['type']} due on {deadline['date']}: {deadline['details']}\n"
            return response
    return "No deadlines found for the specified subject."

def suggest_related_info(query):
    if "schedule" in query or "class" in query:
        return "Try asking about a specific day, like 'What's the schedule for Tuesday?'"
    if "contact" in query or "email" in query:
        return "Try asking for a specific subject, like 'Who is the contact for Web Design and Development?'"
    if "deadline" in query or "due date" in query:
        return "Try asking for a specific subject, like 'What are the deadlines for English?'"
    return "Please provide more details."

def main(page: ft.Page):
    page.title = "University Chatbot"
    
    # Create a container for the chat messages
    chat_display = ft.Column(scroll=True, expand=True, controls=[])
    
    # Function to handle sending messages
    def send_message(e):
        user_message = input_field.value
        if not user_message.strip():
            return
        bot_response = handle_query(user_message)
        
        chat_display.controls.append(
            ft.Container(
                content=ft.Text(f"User: {user_message}", weight=ft.FontWeight.BOLD),
                padding=10,
                bgcolor=ft.colors.BLUE_100,
                border_radius=10,
                margin=ft.margin.only(bottom=10)
            )
        )
        chat_display.controls.append(
            ft.Container(
                content=ft.Text(f"Bot: {bot_response}", weight=ft.FontWeight.BOLD),
                padding=10,
                bgcolor=ft.colors.GREEN_100,
                border_radius=10,
                margin=ft.margin.only(bottom=10)
            )
        )
        
        input_field.value = ""
        page.update()
    
    # Create the input field and send button
    input_field = ft.TextField(hint_text="Type your message here...", expand=True)
    send_button = ft.ElevatedButton(text="Send", on_click=send_message)
    
    # Add components to the page
    page.add(
        ft.Column(
            expand=True,
            controls=[
                chat_display,
                ft.Row(
                    [input_field, send_button],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ]
        )
    )

# Run the Flet app
ft.app(target=main)
