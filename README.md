# fullstack-task-manager
Project Structure
fullstack_project/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
├── frontend/
│   ├── package.json
│   ├── src/
├── README.md


# Frontend: React (JavaScript)
Backend: Python (Flask)
Use case: A "Task Manager" app (add, delete, complete tasks)

🔧 Backend (Flask) backend/app.py backend/requirements.txt

# CMD for run the code on host

pip install -r requirements.txt

python app.py

# Frontend (React)

From the frontend/ folder:

frontend/src/App.js (Write the code in App.js)

frontend/src/components/TaskManager.js (write the code in TaskManager.js)

frontend/package.json 

(create with npx create-react-app frontend) - 

Create react app using this CMD

$ npm install axios

$ npm start

After running those cmd your react app are running on localhost default port 3000

# Run It All
# Start the Flask backend: 

cd backend

$ python app.py

Start the React frontend:

cd frontend

$ npm start

Now your app is running mode. you can add and delete your task.
