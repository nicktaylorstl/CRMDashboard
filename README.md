# CRMDashboard2
The purpose of this project is to create a data pipeline to stream live data from Capsule CRM to a dashboard where the data can be seen clearly in real time. 

1- business opportunities are put into Capsule CRM
2- Using rest hook subscriptions the data is produced to a Kafka cluster
3- The data is then consumed to a BigQuery dataset
4- The data is transformed through DBT and a mart layer is created in BigQuery
5- Using PowerBI the data is visualized into a meaningful dashboard
