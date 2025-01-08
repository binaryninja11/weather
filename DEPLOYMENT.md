# **Deployment Guide**

This document explains the steps required to deploy the Weather App project to a live server using GitHub Pages or any other cloud platform, such as Azure.

---

### **Prerequisites**

Before you deploy the application, make sure you have the following:

1. **GitHub Account** – For storing and deploying the code.
2. **Python (for backend)** – Flask must be installed, and backend APIs should be functional.
3. **Hosting Platform (GitHub Pages, Azure, etc.)** – Ensure you have access to the platform you want to deploy on.

---

### **Step 1: Set Up the Local Development Environment**

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/weather.git
   ```
2. Navigate to the project directory:
   ```bash
   cd src
   ```

3. **Set up Python virtual environment** (for backend):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask server locally**:
   ```bash
   flask run
   ```

   Your backend should now be running locally on `http://127.0.0.1:5000`.

---

### **Step 2: Deploying to GitHub Pages (Frontend)**

1. **Push the frontend to GitHub Pages:**
   - Go to your repository settings.
   - Under the "Pages" section, select the branch you want to deploy (usually `main` or `gh-pages`).
   - Select the root directory (or `/docs` if you have it).
   - GitHub will automatically deploy the frontend.
   
2. **Access your live site:**
   After deployment, GitHub Pages will provide a live link, usually:
   ```plaintext
   https://your-username.github.io/weather
   ```

---

### **Step 3: Deploying Backend (Azure)**

To deploy your Flask backend to **Azure**, follow these steps:

1. **Create a new Web App** in the Azure portal:
   - Go to the Azure portal.
   - Navigate to "Create a resource" and select "Web App."
   - Choose a unique name for your web app and select Python as the runtime.
   - Select the region closest to your users.

2. **Deploy using GitHub Actions** (Automatic Deployment from GitHub):
   - In your repository, go to "Actions" and set up a new workflow.
   - Follow the prompts to link your GitHub repo to the Azure Web App.
   - Azure will automatically set up CI/CD pipelines for you.

3. **Configure Environment Variables:**
   - In the Azure portal, navigate to the "Configuration" section of your Web App.
   - Add any environment variables (like API keys or Flask settings).

4. **Test your deployed backend:**
   - Your backend should now be live on a unique Azure URL.

---

### **Step 4: Testing the Deployment**

Once the frontend and backend are deployed, make sure everything is working by:

1. Accessing the frontend via the GitHub Pages URL.
2. Testing the interaction with the backend APIs.
   - Make sure the frontend correctly fetches and displays weather data.
   - Test the POST and GET methods using real-time data.

---

### **Step 5: Troubleshooting**

If you run into issues, here are some things to check:

- **Backend not starting**: Ensure all environment variables are correctly set.
- **Frontend not showing data**: Verify that your frontend is correctly making API calls to the deployed backend.

For more help, refer to the respective platform’s documentation (GitHub Pages, Azure).

---

### **Step 6: Additional Notes**

- You can also set up Continuous Deployment using GitHub Actions to automate deployments whenever changes are made to the repository.

