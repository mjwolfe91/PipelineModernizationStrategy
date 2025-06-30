# Rollout Strategy

To effectively roll out the modernized data pipelines, we will need to ensure little to no downtime in the realtime dashboards. To accomplish this, we need to first identify critical data sources to focus on first, create effective consumption and monitoring, then begin cutting over to the new pipelines.

## Step 1: Kafka Integration

We first would need to roll out Kafka and integrate it with the web applications. The first step would be to deploy Kubernetes clusters supporting Kafka, then have the web applications start pushing data to these instances. Rudimentary PySpark pipelines can begin pushing the data from Kafka onto Iceberg data stores, so that analysis and monitoring can begin.

## Step 2: Analyze data and monitor SLAs and KPIs

Now that some data is available and SLAs can be monitored, start analyzing both to determine if they will suit the business needs. Determine what kind of refinements are required to make the data useful for the dashboards, and start ingesting additional data sources if needed.

## Step 3: Refine data and begin UAT

Implement the requirements defined in step 2. Create some dashboards based off the requirements and begin UAT with their respective users. If the users are happy with the results, move on to deployment.

## Step 4: Large scale rollout

Begin moving users onto dashboards supported by new pipelines. Have SRE and Ops teams begin monitoring the Grafana dashboards and create alerts for OCR, if needed.

## Step 5: Decommission Old Pipelines and Dashboards

Once users are fully onboarded, begin decommissioning old infrastructure and dashboards.
