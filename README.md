# HMS - Hospitals Management System

This project is an Odoo module that provides a Hospitals Management System (HMS) to manage patient data, departments and doctors. The module includes a model for the patient entity, which contains basic information such as first name, last name and birth date, as well as more specific data such as medical history, blood type, and PCR status.

## Installation

1. Clone the repository to your local machine.
2. Add the "hms" folder to your Odoo addons directory.
3. Restart your Odoo server.
4. Install the "hms" module from the Odoo Apps menu.

## Features

The "hms" module includes the following features:

- **Patient Model:** A model for the patient entity that includes fields for first name, last name, birth date, medical history, blood type, PCR status, image, address, age, and department.
- **Department Model:** A model for the department entity that includes fields for name, capacity, is_opened, and patients.
- **Doctor Model:** A model for the doctor entity that includes fields for first name, last name, and image.
- **Patient-Department and Patient-Doctor Link:** The patient model is linked to the department and doctor models so that the selected department capacity is shown from the patient view.
- **Log History:** A log record is created for each patient that shows the date, creator, and description of the change. The patient also hasa state that can be changed between undetermined, good, fair, and serious, and each change of state creates a new log record with a description of the change.
- **Email Field:** An email field is added to the patient model that ensures a valid and unique email address.
- **Link with CRM Module:** The patient model is linked with the customers model from the CRM module by adding a new field called "related_patient_id" in the customers model, which is shown inside the Misc group within the sales and purchase tab.

## Usage

After installing the "hms" module, you can access the patient data by navigating to the Patients menu. From here, you can view and create new patient records, as well as edit existing ones. The department and doctor data can be accessed from their respective menus.

To link a patient to a department or doctor, simply select the desired department or doctor from the drop-down menu in the patient's form view. The patient's state can be changed by selecting the appropriate option from the state field.

To view a patient's log history, navigate to the Logs tab in the patient's form view. Here, you can see a record of all changes made to the patient's data, including the date, creator, and description of the change.

To link a customer to a patient, navigate to the Customers menu in the CRM module. From here, edit the desired customer record and select the corresponding patient from the "Related Patient" field in the Miscgroup within the sales and purchase tab.

