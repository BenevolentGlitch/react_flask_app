## Starting Docker Images

API

From the main directory first navigate to api/
From that directory run the following commands:
  * docker build -t flask-app .
  * docker run --rm -p 5000:5000 flask-app

The Flask app is now running the development mode.\
Open [http://localhost:5000](http://localhost:5000) to view it in your browser.
If you navigate to localhost:5000/ you should see 'hello world'

From the main directory first navigate to react-app/
From that directory run the following commands:
  * docker build -t react-app .
  * docker run --rm -p 3000:3000 -t react-app
  
The react app in now running the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.
if you navigate to localhost:3000 you should see the UI
  
The services/related pages will reload when you make changes.\
You may also see any lint errors in the console.
