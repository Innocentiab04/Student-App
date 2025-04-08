## Setup (For Running the Wireframe Locally)

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_link>
    cd student_app_wireframe
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate   # On Windows
    ```
3.  **Install Django:**
    ```bash
    pip install django
    ```
4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser (optional, for accessing the admin panel):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
7.  **Access the wireframe in your web browser:** Navigate to `http://127.0.0.1:8000/`.

## Screenshots

[**Replace this section with a brief explanation of each screenshot and embed the image files.**]

Here are a few screenshots showcasing the key screens of the Assignment Tracking feature:

### Assignment List

![Assignment List Screenshot](path/to/assignment_list_screenshot.png)
*A list displaying upcoming and past assignments for the student.*

### Create Assignment Form

![Create Assignment Form Screenshot](path/to/create_assignment_screenshot.png)
*The form used to add new assignments with details like title, due date, and description.*

### Assignment Detail View

![Assignment Detail View Screenshot](path/to/assignment_detail_screenshot.png)
*Detailed information for a specific assignment.*

## Interaction Design Process

This wireframe is a result of applying the interaction design process, which included:

* **Understanding User Needs:** [Briefly mention the problem space and user research methods used (interviews).]
* **Designing Alternatives:** [Mention if any alternative designs were explored.]
* **Developing a Conceptual Model:** [Briefly describe the core functionalities, interaction types, and interface metaphor.]
* **Sketching Prototypes:** [Mention that interface sketches were created before the Django wireframe.]
* **Evaluation Planning:** [State that an evaluation plan was developed (see the final report).]

## Deliverables

This repository includes the Django project files for the wireframe. The full assignment deliverables, including user research summaries, personas, scenarios, conceptual model diagram and explanation, annotated sketches, and the evaluation plan, are available in the final PDF report submitted separately.

## Future Considerations

This wireframe provides a basic visual representation. Future development would involve:

* Implementing full backend logic for data persistence and manipulation.
* Integrating context-awareness features.
* Developing other core functionalities (e.g., class schedules, study reminders, wellness check-ins).
* Conducting usability testing and iterating on the design.

