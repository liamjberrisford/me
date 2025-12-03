# Publications

## Datasets 

### Machine Learning for Hourly Air Pollution Prediction - Global (ML-HAPPG)

![ML-HAPPG Visulisation](_static/images/ml_happg.png)

[Publication](https://catalogue.ceda.ac.uk/uuid/7f91b1326a324caa9e436b8fdef4a0d8/)

This dataset contains estimates of air pollution levels across the globe for every hour of the year 2022. It covers five major air pollutants that can affect human health and the environment. The data cover major air pollutants, including:

- Nitrogen Dioxide (**NO₂**)
- Ozone (**O₃**)
- Particulate Matter smaller than 10 micrometres (**PM₁₀**)
- Particulate Matter smaller than 2.5 micrometres (**PM₂.₅**)
- Sulphur Dioxide (**SO₂**)

Each air pollutant's concentrations are predicted not only as average (mean) values but also include estimates at lower (5th percentile), median (50th percentile), and upper (95th percentile) levels to highlight typical and potential extreme pollution scenarios. The spatial coverage of the dataset includes the entire globe, structured as an evenly spaced grid, with each grid square covering an area of 0.25 degrees (0.25 degrees × 0.25 degrees). Data points correspond to the centre of these grid squares. There is also training data used for the model from real-world monitoring stations.

### Machine Learning for Hourly Air Pollution Prediction in England (ML-HAPPE)

![ML-HAPPE Visulisation](_static/images/ml_happe.png)

[Publication](https://catalogue.ceda.ac.uk/uuid/fc735f9878ed43e293b85f85e40df24d)

This dataset contains estimates of air pollution levels across England for every hour of the year 2018. It covers seven major air pollutants that can affect human health and the environment. The data cover major air pollutants, including:

- Nitrogen Dioxide (**NO₂**)
- Nitric Oxide (**NO**)
- Nitrogen Oxides (**NOₓ**)
- Ozone (**O₃**)
- Particulate Matter smaller than 10 micrometres (**PM₁₀**)
- Particulate Matter smaller than 2.5 micrometres (**PM₂.₅**)
- Sulphur Dioxide (**SO₂**)

Each air pollutant’s concentrations are predicted not only as average (mean) values but also include estimates at lower (5th percentile), median (50th percentile), and upper (95th percentile) levels to highlight typical and potential extreme pollution scenarios. The spatial coverage of the dataset includes the entire area of England, structured as an evenly spaced grid, with each grid square covering an area of 1 square kilometre (1 km × 1 km); data points correspond to the centre of these grid squares. The underlying model was trained using real-world ambient air pollution measurements from monitoring stations over the period 2014–2018, enabling predictions even in areas without nearby monitoring sites.



### Synthetic Hourly Air Pollution Prediction Averages for England (SynthHAPPE)

![SynthHAPPE Visulisation](_static/images/synth_happe.png)

[Publication](https://catalogue.ceda.ac.uk/uuid/fe877f3035c042478fd67de21f5f445a/)

This dataset contains synthetic estimates of ambient air pollution concentrations across England, provided as hourly averages representing typical conditions. The data cover major air pollutants, including:

- Nitrogen Dioxide (**NO₂**)
- Nitric Oxide (**NO**)
- Nitrogen Oxides (**NOₓ**)
- Ozone (**O₃**)
- Particulate Matter smaller than 10 micrometres (**PM₁₀**)
- Particulate Matter smaller than 2.5 micrometres (**PM₂.₅**)
- Sulphur Dioxide (**SO₂**)

Each pollutant’s concentrations are predicted not only as average (mean) values but also include estimates at lower (5th percentile), median (50th percentile), and upper (95th percentile) levels to highlight typical and potential extreme pollution scenarios. The spatial coverage of the dataset includes the entire area of England, structured as an evenly spaced grid, with each grid square covering an area of 1 square kilometre (1 km²); data points correspond to the centre of these grid squares. Temporally, the dataset provides “typical day” profiles constructed by averaging observations from 2014–2018 for each month, weekday, and hour, offering representative pollution patterns rather than exact historical measurements. The underlying supervised machine learning model was trained using real-world monitoring data and a range of environmental predictors (weather, traffic, satellite data, land use, and emission inventories), and the percentile-based estimates provide uncertainty information to support evidence-based use.



## Papers 

### A data-driven supervised machine learning approach to estimating global ambient air pollution concentrations with associated prediction intervals

![Visulisation](_static/images/paper_3.png)

[Publication](https://royalsocietypublishing.org/doi/full/10.1098/rsos.241288)

Global ambient air pollution, a transboundary challenge, is typically addressed through interventions relying on data from spatially sparse and heterogeneously placed monitoring stations. These stations often encounter temporal data gaps due to issues such as power outages. In response, we have developed a scalable, data-driven, supervised machine learning framework. The models produced by the framework are designed to impute missing temporal and spatial measurements, thereby generating a comprehensive dataset for air pollutants including:

- Nitrogen Dioxide (**NO₂**)
- Ozone (**O₃**)
- Particulate Matter smaller than 10 micrometres (**PM₁₀**)
- Particulate Matter smaller than 2.5 micrometres (**PM₂.₅**)
- Sulphur Dioxide (**SO₂**)

In this work, we produce models providing concentration estimations at 261,377 locations across the globe. The dataset, with a fine granularity of 0.25° spatial resolution at hourly time intervals and accompanied by prediction intervals for each estimate, caters to a wide range of stakeholders relying on outdoor air pollution data for downstream assessments. This enables more detailed studies.

Additionally, the model’s performance across various geographical locations is examined, providing insights and recommendations for strategic placement of future monitoring stations to further enhance the model’s accuracy.

### Environmental Insights: Democratizing access to ambient air pollution data and predictive analytics with an open-source Python package

![Visulisation](_static/images/paper_4.png)

[Publication](https://www.sciencedirect.com/science/article/pii/S1364815224001920)

Ambient air pollution is a pervasive issue with wide-ranging effects on human health, ecosystem vitality, and economic structures. Utilizing data on ambient air pollution concentrations, researchers can perform comprehensive analyses to uncover the multifaceted impacts of air pollution across society. To this end, we introduce Environmental Insights, an open-source Python package designed to democratize access to air pollution concentration data. This tool enables users to easily retrieve historical air pollution data and employ a machine learning model for forecasting potential future conditions. Moreover, Environmental Insights includes a suite of tools aimed at facilitating the dissemination of analytical findings and enhancing user engagement through dynamic visualizations. This comprehensive approach ensures that the package caters to the diverse needs of individuals looking to explore and understand air pollution trends and their implications.

### A framework for scalable ambient air pollution concentration estimation

![Visulisation](_static/images/paper_2.png)

[Publication](https://www.cambridge.org/core/journals/environmental-data-science/article/framework-for-scalable-ambient-air-pollution-concentration-estimation/A6CA26BE98A5C4DD21F096DE0F608BB5)

Ambient air pollution remains a global challenge, with adverse impacts on health and the environment. Addressing air pollution requires reliable data on pollutant concentrations, which form the foundation for interventions aimed at improving air quality. However, in many regions, including the United Kingdom, air pollution monitoring networks are characterized by spatial sparsity, heterogeneous placement, and frequent temporal data gaps, often due to issues such as power outages We introduce a scalable, data-driven, supervised machine learning model framework designed to address temporal and spatial data gaps by filling missing measurements within the United Kingdom. The machine learning framework used is LightGBM, a gradient boosting algorithm based on decision trees, for efficient and scalable modeling. This approach provides a comprehensive dataset for England throughout 2018 at a 1 km² hourly resolution.

Leveraging machine learning techniques and real-world data from the sparsely distributed monitoring stations, we generate 355,827 synthetic monitoring stations across the study area. Validation was conducted to assess the model’s performance in forecasting, estimating missing locations, and capturing peak concentrations.

The resulting dataset is of particular interest to a diverse range of stakeholders engaged in downstream assessments supported by outdoor air pollution concentration data for:

- Nitrogen Dioxide (**NO₂**)
- Ozone (**O₃**)
- Particulate matter with a diameter of 10 μm or less (**PM₁₀**)
- Particulate matter with a diameter of 2.5 μm or less (**PM₂.₅**)
- Sulphur Dioxide (**SO₂**)

at a higher resolution than was previously possible.

### Estimating annual ambient air pollution using structural properties of road networks

![Visulisation](_static/images/paper_1.png)

[Publication](https://journals.sagepub.com/doi/full/10.1177/23998083241230707)

In recent years, the world has become increasingly concerned about air pollution. Particularly, High-Income Countries (HIC) and Upper Middle-Income Countries (UMIC) are implementing systems to monitor air pollution on a large scale to aid decision-making. Such efforts are essential, but they have at least three shortcomings, they are costly, they are slow to deploy and they focus on urban areas, which leads to urban–rural inequalities. Here, we show that we can estimate annual air pollution using open-source information about the structural properties of roads. We focus on England and Wales in the United Kingdom (UK) in this paper, although we argue that our methods are independent of specific country features.

Our approach is an inexpensive methods of estimating annual air pollution concentrations to an accuracy level that can underpin policymakers’ decisions while providing an estimate in all districts, not just urban areas. Furthermore, we contend that our process is interpretable and explainable.

## Thesis (PhD)

### Operationalising Ambient Air Pollution Estimation

![Operationalising Ambient Air Pollution Estimation ](_static/images/oaape.png)

[Publication](https://ore.exeter.ac.uk/articles/thesis/Operationalising_Ambient_Air_Pollution_Estimation/29811452?file=56857673)

Air pollution presents a significant health risk to individuals worldwide, with the estimation of ambient air pollution levels being an essential step in tackling the global health burden of air pollution due to the high cost of individual monitoring stations. This thesis outlines research done in fulfilment of a Ph.D. in Environmental Intelligence that looks at the use of machine learning to provide an alternative to traditional methods that fills a need for a scalable method of estimating ambient air pollution with varying spatial and temporal resolution to meet the demands of various stakeholders. Machine learning allows for estimations to be made at speed, allowing for deployment in an operational capacity to improve decision velocity and pivot interventions from reactive to proactive. The thesis presents how machine learning can estimate air pollution in the UK at the annual level, with a subsequent approach presented to estimate air pollution concentrations at the hourly and 1km2 temporal and spatial resolution in England. The merit of the approach is further explored with a global air pollution concentration model presented to address global inequality of air pollution intelligence, ensuring that no one is left behind when tackling the air pollution crisis. Finally, an open-source Python package and companion analysis of how the intelligence provided can help decision-making concerning decisions such as outdoor school activities timing, and clean air zones are presented, ensuring dissemination of the work to various stakeholders.

## Dissertation (BSc)

### Initial Underwater Structure Exploration Planning

![IUSEP](_static/images/IUSEP.png)

[Dissertation (BSc) Publication](https://doi.org/10.6084/m9.figshare.30745208)

When an Autonomous Underwater Vehicle (AUV) is exploring an underwater structure, the video / image feed gives a snapshot of the current detail of the structure that is being observed. Underwater structures such as shipwrecks and caves are routinely monitored and explored for varies reasons. The set of all images that an AUV gathered during a deployment is currently unused and discarded after it surfaces. The aim of this project is to improve the understanding of the structure by using this redundant data. During the project, a program was developed to create a single persistent comprehensive model of the structure being photographed. Implementing a range of functionality such as image manipulation, a 3D viewer, and an overview Graphical User Interface, alongside integrating external libraries and software into the program such as software to complete the point cloud reconstruction of the geometry of the structure. During the project, a simulation for an underwater environment was created, allowing for an example data set to be easily created.

The simulation has the ability to swap out the structure being photographed while also allowing for the details of the simulation to be changed, such as the lighting, turbidity or occluders of the underwater environment being simulated. The contribution of this project can be seen as the solving of six key problems identified during the initial investigation into the problem. The first was to create a pipeline to allow the creation of a model to inform the user of the geometry of the structure (1), while also allowing these models to be stored and indexed so that the structure can be monitored over time (2). An investigation into image manipulation techniques to compensate for the effects of underwater photography was also needed (3), and the development of a set of best practices for the pipeline complemented (4). The program also implemented features to make use of all available information from the initial data set to create supporting information, such as the path the AUV took while collecting the images for the data set (5). Finally, all these seemingly disconnected stages of the pipeline were collected together with an overarching graphical user interface, achieving task centralization (6).





