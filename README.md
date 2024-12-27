# Project: Cafeteria Management Using Video Analytics!

[Project Demo](https://dhairyakhania-cafeteria-management-using-video-analytics.hf.space/)

The main goal of Cafeteria Management Using Video Analytics is to improve the efficiency, safety, and overall experience in cafeteria settings through the use of video surveillance and advanced data analytics. By leveraging video analytics technologies, such as computer vision and machine learning, cafeteria management systems can achieve a variety of objectives.

<img src="Picture_1_va.png">

<img src="Picture_3_va.png">

## Importance of the Project
- **Enhanced Operational Efficiency**: Video analytics helps optimize customer flow, seating arrangements, and staff productivity, improving overall cafeteria efficiency.
- **Improved Safety and Security**: It enables real-time monitoring for detecting suspicious behavior, safety hazards, and ensuring compliance with safety protocols.
- **Customer Experience Optimization**: Analyzing customer behavior and preferences allows for tailored services, reducing wait times and enhancing satisfaction.
- **Data-Driven Decision Making**: Provides valuable insights through data analytics, helping managers make informed decisions about staffing, inventory, and menu offerings.
- **Inventory and Resource Management**: Helps track stock levels and ensures efficient resource use, minimizing wastage and ensuring timely restocking.
- **Compliance Monitoring**: Assists in monitoring hygiene, food safety practices, and regulatory compliance, ensuring a safe and healthy environment for both staff and customers.

## Technical Overview
- **Deep Learning Frameworks**: Utilizes popular frameworks like TensorFlow or PyTorch for building and training the classification models.
- **Git Integration**: For source code management and version control, making the project easily maintainable and scalable.
- **MLOps Practices**: Incorporates best practices in machine learning operations to automate workflows, from data preparation to model deployment.
- **DagsHub Integration**: Facilitates collaboration, data and model versioning, experiment tracking, and more in a user-friendly platform.

## Features Consider:

1. TEMP.csv - Data from temperature sensor expressed degrees on the Celsius (°C) scale.

2. EDA.csv - Data from the electrodermal activity sensor expressed as microsiemens (μS).

3. BVP.csv - Data from photoplethysmograph.
4. HR.csv- Average heart rate extracted from the BVP signal.The first row is the initial time of the session expressed as unix timestamp in UTC.

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Dhairyakhania/Cafeteria_Management.git
```

### STEP 01- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 02- Model Training
```bash
#run this file to generate the models

Run the FinalVideoAnalytics.ipynb file present in Code branch
```

<img src="Picture_2_va.png">

Now run,
```bash
python app.py for frontend
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
