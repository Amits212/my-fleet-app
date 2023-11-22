# My Fleet App

This is a FastAPI-based application that provides endpoints for retrieving information about ships based on their country and distance from a specified point.

## Getting Started

These instructions will guide you on how to set up and run the application locally.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/my-fleet-app.git
   cd my-fleet-app

2. Build the Docker image:

   ```bash
   docker build -t my-fleet-app .
   
3. Running the Application, Run the Docker container:
   
   ```bash
   docker run -p 8001:80 my-fleet-app

4. API Documentation
   Get Ships by Country:

Endpoint: /ships/by-country/{country}
Example: http://127.0.0.1:8001/ships/by-country/Cyprus
Get Ships by Distance:

Endpoint: /ships/by-distance
Parameters:
lat: Latitude of the point
lon: Longitude of the point
radius_km: Radius in kilometers
Example: http://127.0.0.1:8001/ships/by-distance?lat=39.1617&lon=21.4767&radius_km=5
