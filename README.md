#Code-Refactoring-Bug-Fixing

Scenario -

A team of enthusiastic data scientists embarked on a mission to develop a Note Taking Application using Python, Flask, and HTML. However, their lack of experience in backend development has led to challenges in making the application fully functional. Recognizing your proficiency in backend development, you have been tasked with fixing the broken code and ensuring the application works seamlessly.


Task-

Refactor the existing codebase and ensure the proper functioning of the Note Taking Application. Document all identified bugs during the debugging process. Remember, the task is not about recreating the app from scratch. Your goal is to fix the already existing codebase and make the application work as intended.

#Identifying and Correcting Bugs in the Python Code.
•	Added a methods=["GET", "POST"] argument to the @app.route('/') decorator to allow both GET and POST requests to the home page.
•	Changed request.args.get("note") to request.form.get("note") to get the note from the form data instead of the query parameters.

•	 Added a check for if note: before appending it to the notes list to avoid adding empty strings.

•	Moved the render_template call outside of the, if block to always render the template, even if the request method is GET.

#Identifying and correcting the Bugs in the HTML Code.
•	Added <style> tags in the second HTML code to include CSS styles for better presentation.
•	Added CSS styles for the <body> and <form> elements to align content vertically and horizontally.
•	Added <body> tags to enclose the content of the page.
•	Moved the <title> tag to be properly nested within the <head> section.	
•	Moved the <h1> tag to be directly within the <body> section for the main heading of the page.
•	Corrected the indentation and spacing within the <form> tag.
•	Updated the <form> tag to include an action attribute set to "/" to specify the URL where the form data should be submitted.
