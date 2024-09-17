# GeoLocator-India

FrontEnd UI
![indiamap](https://github.com/TGouriSankar/GeoLocator-India/blob/main/indiamap.png)

**GeoLocator-India** is an offline map application built using OpenStreetMap data and Docker.\
It allows users to input latitude and longitude coordinates to retrieve location information, such as state, district, city, and pin code, using Leaflet.\
js for rendering the map. \
The application is designed to work in offline mode, running a Flask backend to serve the map and perform geolocation queries. 

**Features**

-  **Offline Mapping:** Leverages OpenStreetMap data and Docker to provide an offline geolocation service.
-  **Location Details:** Given latitude and longitude, the application displays the state name, district name, city, and pin code.
-  **Interactive Map:** Uses Leaflet.js for displaying and interacting with the map.
-  **Dockerized:** Easily deployable using Docker, ensuring consistency across environments.
-  **Flask Backend:** Powered by Flask, enabling simple and efficient server-side handling of geolocation requests.

**Technologies Used**

- **OpenStreetMap:** Source for map data.
-  **Leaflet.js:** JavaScript library for interactive maps.
-  **Flask:** Python micro-framework for backend API.
-  **Docker:** Containerization for easy deployment and offline capabilities.

  **Getting Started**

**Prerequisites**

Make sure you have Docker and Docker Compose installed on your machine:

-  **Docker:** Install Docker
-  **Docker Compose:** Install Docker Compose

**Installation**

1:  Clone the repository:
  
    git clone https://github.com/yourusername/GeoLocator-India.git
    cd GeoLocator-India
    
2:  run the flask:

    python3 app.py

3:  Build and run the Docker container:

    docker pull overv/openstreetmap-tile-server

    sudo docker run \
    -v /media/player/karna1/india-map/india-latest.osm.pbf:/data/region.osm.pbf \
    -v /media/player/karna1/map:/data/database/ \
    overv/openstreetmap-tile-server \
    import

    
    sudo docker run \
    -p 8082:80 \
    -v /media/player/karna1/map:/data/database/ \
    -p 5432:5432 \
    -e ALLOW_CORS=enabled \
    -d overv/openstreetmap-tile-server \
    run
    
    
4:  Access the application: \
  Once the container is running, open your browser and go to: 

    http://localhost:5000

5: Using the application:

  Enter latitude and longitude values in the input fields. \
  Click "Locate" to fetch and display the location details (state, district, city, pin code) on the card.

**Usage**
- **User Interface**

    - **Map Display:** The interactive map (powered by Leaflet.js) allows users to explore regions.
    - **Location Search:** Input latitude and longitude values in the provided form.
   -  **Card Information:** The location details (state, district, city, pin code) are shown on a card once retrieved.

**Sample Coordinates**

- Try these coordinates for testing:

    - Latitude: 28.6139, Longitude: 77.2090 (Delhi)
    - Latitude: 19.0760, Longitude: 72.8777 (Mumbai)

  
**Contributing**

- Contributions are welcome! Please follow the standard fork and pull request workflow.

    - Fork the repo.
    - Create your feature branch (git checkout -b feature/AmazingFeature).
    - Commit your changes (git commit -m 'Add some AmazingFeature').
    - Push to the branch (git push origin feature/AmazingFeature).
    - Open a pull request.

**License**

This project is licensed under the MIT License.



