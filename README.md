## Description
Project for get urls of instagram pictures. Really only get the post covers, just wanted to 
demonstrate how it's done, I think that's the most important thing. 
Links are obtained by sending requests directly to instagram api with the data of the authorized account in the header.
In settings.py offered an alternative to update authorization data.


Endpoints:

1. GET /pictures/ - Get urls of pictures


## Running the app

```bash
$ docker compose up
```

## Send requests to endpoints

To test the endpoints, please import the **InstagramPhotos.json** file into Postman.

or

```bash
$ curl --location 'http://localhost:8000/pictures/?username=icecube&count=10'
```
