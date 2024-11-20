# PostMan
### Advanced Email Automation CLI Tool
![CertiMailer Logo](https://github.com/Dev-0618/PostMan/blob/main/postman.png)

## Description
PostMan is a powerful and customizable command-line tool designed for efficient email automation. Whether you're managing bulk email campaigns, sending personalized messages, or notifying users with specific templates, PostMan simplifies the entire process. With a sleek CLI interface and fully customizable options, it ensures ease of use for all levels of users.

## Features
- **Customizable Email Sending**: Send emails to a single recipient or a bulk list.
- **Pre-made and Custom Templates**: Select from predefined subject templates or create your own.
- **Attachment Support**: Optionally attach files to your emails.
- **Interactive CLI Prompts**: User-friendly prompts for all configurations.
- **Secure Communication**: Emails are sent securely using SSL.
- **Personalized Messages**: Match names with emails for tailored communication.
- **High Priority Marking**: Optionally mark your emails as high-priority.
- **Loading Animations**: A polished user experience with animations and color-coded prompts.

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Dev-0618/PostMan.git
   cd PostMan
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the program by running:

   ```bash
   python3 intro.py
   ```

2. Follow the interactive CLI prompts to:
   - Choose single or bulk email mode.
   - Enter recipient details (bulk mode supports a file with emails and names).
   - Select a subject from templates or create a custom one.
   - Optionally attach files or mark emails as high-priority.

3. Sit back and watch PostMan handle your emails!

## Example Workflow
```bash
└──╼ $python3 intro.py
Welcome to PostMan!
Creator: https://github.com/Dev-0618/
Loading...

Transitioning to the main program...

Do you want to mark this email as high priority? (y/n): y
Do you want to send this email to a single person or bulk? (single/bulk): bulk
Enter the file path containing the email list (one email per line): /path/to/emails.txt
Enter the file path containing names (one name per line): /path/to/names.txt
Choose subject option (1 for pre-made templates, 2 for custom): 1
Choose a subject template:
1. Important Account Update
2. Bulletin Alert
3. LinkedIn Invitation Reminder
Enter your choice: 1
Do you want to attach a file? (y/n): n
Email sent successfully to example1@gmail.com!
...
```

## Dependencies
The following Python modules are used in the project:
- **smtplib**: For email transmission.
- **ssl**: To secure communication.
- **email**: To format and handle email messages.
- **os**: For file and system operations.
- **sys**: To handle animations and user prompts.
- **time**: For smooth transitions and animations.

Install these modules using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. For major changes, open an issue to discuss what you’d like to improve.

## Creator
PostMan was developed by [Dev@127.4.7.8](https://github.com/Dev-0618/).
