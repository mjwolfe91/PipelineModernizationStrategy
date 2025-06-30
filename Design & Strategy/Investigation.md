The first step is to **holistically investigate the current state and identify strategic opportunities**. This will drive the design and implementation of the modernization strategy. This boils down to a few key questions:

1. Getting a basic idea of the inventory of data pipelines.
    -We should identify the current workloads that are providing key data, and determine the provenance of the data they provide into key assets. This will help us determine the criticality and priority of the pipelines (how much downtime can be tolerated, etc).

2. Identify commonalities between each pipeline, such as functional overlap and repeated pain points.
    -Look for functional overlap (such as connectivity to external data sources, common transformatiom/cleansing steps, etc) and any repeated code. This will help us identify common components that can be shared across all pipelines, and what capabilities need to be enabled in individual implementations. Also identify common pain points, such as frequent downtime, data quality issues, etc.

3. Break down findings into design.
    -The findings from the above should drive the design. Turn the pain points into SLAs backed by elasticity and redundancy, the common findings into base definitions of classes and infrastructure, and the priorities into a plan to migrate with minimal impact.