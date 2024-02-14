# MongoDB Instructions

## Here's a step-by-step guide on how to create a MongoDB Atlas cluster (online MongoDB database):

Sign in to MongoDB Atlas: Go to the MongoDB Atlas website and sign in with your account.

Create a new project: Click on the "Projects" dropdown on the top left of the screen, then click "New Project". Give your project a name and click "Next". Add members if you want, then click "Create Project".

Build a new cluster: Click the "Build a Cluster" button. Choose the free plan for now by clicking "Create a Cluster" under the "Free" tier.

Configure your cluster: Choose a Cloud Provider and Region (you can leave the default selection). Scroll down and give your cluster a name, or leave the default name. Click "Create Cluster" at the bottom.

Wait for your cluster to be created: It can take a few minutes for your cluster to be ready. Once it's ready, you'll be able to access it from your dashboard.

Set up database access: Click on the "Database Access" under the "Security" section in the left-hand menu. Click "Add New Database User". Choose a username and password. Under "Database User Privileges", select "Read and write to any database". Click "Add User".

Set up network access: Click on "Network Access" under the "Security" section in the left-hand menu. Click "Add IP Address". Click "Allow Access from Anywhere" and then click "Confirm".

Get your connection string:
Go back to your clusters overview by clicking "Clusters" in the left-hand menu.
Click "CONNECT" on your cluster.
Click "Connect your application". Choose "Python" as your driver and choose the version that matches your Python version.
Copy the connection string, but remember to replace `<password>` with the password you chose when setting up database access.

# Extra Help
