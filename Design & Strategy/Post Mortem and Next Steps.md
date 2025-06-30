# Post Mortem

## What works well

 - Kubernetes should scale to meet high traffic periods, as well as provide redundancy in the event of failures to prevent data loss. It can also natively provide metrics to Prometheus and Grafana to monitor the cluster's health, and provide alerts if needed.

 - The solution is cloud agnostic and open source, which should prevent vendor lock and keep costs manageable.

 - Configurations of Kubernetes and PySpark framework provide abstract, reusable components managed by implementation and configuration, keeping many consistencies across use cases while allowing individual products to maintain their own logic.

## Potential issues and how to address

 - Kubernetes clusters can take some time to deploy if changes to the config are needed. Backup and rollout strategies are needed in the event of upgrades 

 - Kubernetes can become expensive if more and more clusters are added. If necessary, integrate with native cloud solutions if rollouts are more provider specific, or integrate partially or wholly with data platform providers (such as Databricks) if cost becomes a factor.

 - Kuberentes configurations can proliferate depending on the types of clusters needed. Enforce cluster management at the lowest level to ensure standard images and libraries are used.

 ## Next steps

 - Clean up Kubernetes config, it should be configured once at the lowest level, and implemented by Helm charts.

 - Add unit testing. Unit tests will enforce code quality in all layers of the PySpark framework to ensure consistent and stable reusable components, and should be included with each implementation to guarantee logic and code coverage.
 