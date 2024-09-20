# Blog Project

This is a blog application built with Django, TailwindCSS, and DaisyUI. It allows users to create, read, update, and delete blog posts.

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Responsive design using TailwindCSS and DaisyUI

## Technologies Used

- **Django**: Backend framework
- **TailwindCSS**: Utility-first CSS framework
- **DaisyUI**: TailwindCSS component library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ashmil114/blog.git
    cd core
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Home Page:** Displays a list of all blog posts.
- **Post Detail Page:** View details of a single post.
- **Create Post:** Authenticated users can create new blog posts.
- **Edit Post:** Authenticated users can edit their own posts.
- **Delete Post:** Authenticated users can delete their own posts.


## TailwindCSS and DaisyUI Setup with Django

1. **Install TailwindCSS and DaisyUI:**

    ```bash
    npm install tailwindcss daisyui
    ```

2. **Configure TailwindCSS:**

    Create a `tailwind.config.js` file in the root of your project:

    ```javascript
    module.exports = {
      content: [
        './templates/**/*.html',
        './static/src/**/*.js',
      ],
      theme: {
        extend: {},
      },
      plugins: [
        require('daisyui'),
      ],
    }
    ```

3. **Include TailwindCSS in your CSS:**

    In your main CSS file (e.g., `static/src/styles.css`), add the following:

    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

4. **Build TailwindCSS:**

    ```bash
    npx tailwindcss -i ./static/src/styles.css -o ./static/css/styles.css --watch
    ```
Note : Also You can use misc/tailwind.txt documentation link for tailwind css configuration with django

## Acknowledgements

- Django
- TailwindCSS
- [DaisyUI](https://daisyui.com/)
