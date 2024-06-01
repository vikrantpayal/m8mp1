# m7_mp01_surv_predict

Step 1: Run your application on Cloud9 OR Hugging Face Spaces [2 point]

        1.1 Take the testing dataset from Colab and save into a csv file
            -> Run the step "Download the dataset" from this collab notebook
            -> https://colab.research.google.com/drive/14kVhXNx4D-DMppR9_tCE3Pc_iNnNltqG#scrollTo=W-M_jM840AMp



        1.2 Update your application files to include prometheus-client 
        library and methods to send prometheus supported metrics whenever 
        a request is made to/metrics endpoint
            -> Update app.py with these lines
            -> import prometheus_client as prom
            -> r2_metric = 
                prom.Gauge('predict_death__r2_score', 
                            'R2 score for random 100 test samples')
                            # Function for updating metrics
            -> def update_metrics():
            ->  test = test_data.sample(100)
            ->  test_feat = test.drop('cnt', axis=1)
            ->  test_cnt = test['cnt'].values
            ->  test_pred = make_prediction(input_data=test_feat)['predictions']
            ->  r2 = r2_score(test_cnt, test_pred).round(3)
            ->  r2_metric.set(r2)
            ->
            -> @app.get("/metrics")
            ->
            -> async def get_metrics():
            ->  update_metrics()
            ->  return Response(media_type="text/plain",
            ->      content = prom.generate_latest())



        1.3 Create a Dockerfile to dockerize the application 
            -> Add these lines in the existing Dockerfile
            -> ADD *.whl .
            -> WORKDIR .
            -> RUN rm *.whl 
            -> COPY app/. app/.
            -> EXPOSE 8080 
            

        1.4 Run your application either on Cloud9 OR using Hugging Face Spaces
            -> ??? 
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

