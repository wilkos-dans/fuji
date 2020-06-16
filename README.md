# F-UJI (FAIRsFAIR Data Assessment Service)
Developers: Anusuriya Devaraju, Robert Huber

## Overview
F-UJI is a web service to programatically assess FAIRness of research data objects based on [metrics](https://doi.org/10.5281/zenodo.3775793) developed by the [FAIRsFAIR](https://www.fairsfair.eu/) project. 
The service will be applied to demostrate the evaluation of objects in repositories selected for in-depth collaboration with the project.  
The service was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  
The service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server (default port 1071), please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m fuji_server
```

and open your browser to here:

```
http://localhost:1071/fuji/api/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:1071/uji/api/v1/swagger.json
```
## License
This project is licensed under the MIT License; for more details, see the [LICENSE](https://github.com/pangaea-data-publisher/fuji/blob/master/LICENSE) file.
