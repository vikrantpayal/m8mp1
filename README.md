# m7_mp01_surv_predict

Step 1: Run your application on Cloud9 OR Hugging Face Spaces [2 point]
        1.1 Take the testing dataset from Colab and save into a csv file
        1.2 Update your application files to include prometheus-client 
        library and methods to send prometheus supported metrics whenever 
        a request is made to/metrics endpoint
        1.3 Create a Dockerfile to dockerize the application
        1.4 Run your application either on Cloud9 OR using Hugging Face Spaces
        1.5 Access your application and check its /metrics endpoint (Debug if 
        error persists)

Step 2: Setup Prometheus & Grafana using Cloud9 [2 point]
        2.1 Create prometheus.yml configuration file and include your
         application as a target
        2.2 Start Prometheus using docker on Cloud9
        2.3 Start Grafana Open Source using docker on Cloud9

Step 3: Access the application’s metrics in Prometheus [1 point]
        3.1 Access your Prometheus service on the PublicIP
        3.2 Go to the Targets page and check the State of the target application
        3.3 On Graph tab, query your application metric

Step 4: Create Real-time Dashboard in Grafana [2 points]
        4.1 Create a New Dashboard in Grafana
        4.2 Add visualization panels to it to monitor the metrics 
        coming fromPrometheus service
        4.3 Update panel settings such as title, description, 
        min & max values, threshold,etc
        4.4 Save your Dashboard

Step 5: Add an Alert in Grafana [2 points]
        5.1 Add a new Alert rule in Grafana (Make sure to link it with 
        a panel in your dashboard)
        5.2 Add a new Contact point such as Email
        5.3 Add a new Notification policy
        5.4 Check if the notification is being sent to the contact point 
        when the alert rule is in breach (You can alter the threshold to let alert rule in breach)

Step 6: CAUTION ! Clean up [ 1 point ]
        6.1 Delete/Terminate/Release the resources created on AWS
         for this mini-project
            ● Cloud9
            ○ Environment
            ○ EC2 instance associated
            ○ Security Group associated

            