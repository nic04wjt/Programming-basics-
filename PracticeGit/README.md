# HOW TO START A VIRTUAL ENVIRONMENT & INSTALL LIBRARIES (In your Terminal):
 
1. Create the environment:  python -m venv env
2. Activate it:
   - Windows:               env\Scripts\activate
   - Mac/Linux:             source env/bin/activate
 3. Install libraries:       pip install pandas numpy matplotlib

## Creating a .gitignore File

1. Create a new file in your project root:  `touch .gitignore`
2. Add the virtual environment folder:
  ```
  env/
  ```
3. Add other common Python files to ignore:
  ```
  __pycache__/
  *.pyc
  .DS_Store
  ```
4. Save the file and commit it to your repository