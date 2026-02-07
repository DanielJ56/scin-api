
# SCIN Dataset PowerBI and API


The SCIN Dataset is a collection of user submitted, anonymized dermatology images, labeled with skin condition by dermatologists for academic and research purposes. 

SCIN Dataset: (Ward et al 2024 available at https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2826506) 

To enable convenient access to these images, a REST Flask API was create in python as a convenient way to directly access the images themselves for development purposes. 

To demonstrate this, a PowerBI report was created allowing users to filter and search cases by conditions and display the corresponding images. 
# API Development


This API leverages google cloud's storage library in python, allowing direct access to the SCIN google cloud bucket. The user is required to provide a "path" query parameter in the request, which returns the image file itself. 

#### Endpoint: 
`GET /image?path=<ImageFileName`
#### Parameters: 
`?path=<"ImageFileName">`

#### Example using Local Deployment:
`http://localhost:PORTNUMBER/image?path=<"ImageFileName">`

# SCIN PowerBI Report and Look Up tool


![[Screenshot2.png]]


![[Screenshot1.png]]
