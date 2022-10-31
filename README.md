<p align="center">
  <img src="static/images/my-logo.png">
</p>

# Customer Relationship Management (CRM)

CRM stands for Customer Relationship Management. It's a technology used to manage interactions with customers
and potential customers.

This app stores customer information in a database kind of like a CRM.
It has two types of users: admin and customers. Depending on the role the users will be able to create, edit and delete orders and products. The search of specific information is also available. Users will be able to edit their account settings and upload a photo to their profile.

This project is based on Dennis Ivy (@divanov11) crash course *Customer Management App*, but several changes has been made:
- Functionalities to manage products and tags added
- Graph added using *Chart.js*
- Icons added using *Font Awesome*
- Styles changed

## Areas involved

- API
- Data storage
- Data parsing
- Data visualization

## Steps to run this project

In order to be able to see the output of this project, it is required to follow the next steps:

1. Clone the project
2. Install the requirements.txt
3. Create superuser
4. Create two groups in django admin panel: *admin* and *customer*
5. Asign admin user the group admin
4. Execute `python manage.py runserver`
