🚀--Multilingual FAQ Management System--🚀

👉Overview:

This project is a Django-based multilingual FAQ management system that allows users to manage FAQs in multiple languages. 
It supports:

✅WYSIWYG editor for rich text formatting
✅REST API for managing FAQs
✅Language selection via query parameters (?lang=hi, ?lang=bn, etc.)
✅Caching with Redis for better performance
✅Automated translations using Google Translate API (googletrans)


👉Installation Guide:

1. Clone the Repository:
git clone <repo-url>
cd faq_project

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Setup the Database
python manage.py migrate
python manage.py createsuperuser  # Create an admin user

5. Run the Development Server
python manage.py runserver

🚀Access the admin panel at: http://127.0.0.1:8000/admin

👉API Endpoints
        
[
    {
        "id": 3,
        "question": "What is Django?",
        "question_en": "What is Django?",
        "question_hi": "Django क्या है?",
        "question_bn": "জ্যাঙ্গো কী?",
        "answer": "A web framework.",
        "answer_en": "A web framework.",
        "answer_hi": "एक वेब फ्रेमवर्क।",
        "answer_bn": "একটি ওয়েব কাঠামো।",
        "created_at": "2025-02-02T09:06:59.850132Z"
    },


Request Body:
{
    "question": "What is Django?",
    "answer": "Django is a Python web framework."
}


👉Features Implemented:
    
✅Django Model for FAQs
✅ CKEditor Integration for Rich Text Editing
✅ REST API with Django REST Framework
✅ Multilingual Support with googletrans
✅ Redis Caching
✅ Unit Tests with pytest
✅ PEP8 Compliance with flake8
✅ Admin Panel for Managing FAQs  

![1](https://github.com/user-attachments/assets/f5459e42-0f55-4a52-8edd-40d5a56886a7)


![image](https://github.com/user-attachments/assets/1efd4acc-7815-4a48-b025-907ff1398fbf)

![image](https://github.com/user-attachments/assets/e4226673-829a-4b04-9009-ca79203ffe20)

![image](https://github.com/user-attachments/assets/dbab10cc-3f6d-4c1f-9b4b-27d03715df52)

![image](https://github.com/user-attachments/assets/76c09d9f-f7fa-4ee4-addb-f52dedb5ff6a)

![image](https://github.com/user-attachments/assets/13db5691-f3c4-4444-9015-88f9e6570e4d)





