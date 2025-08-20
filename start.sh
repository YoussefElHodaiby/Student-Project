#!/bin/bash

# Start the Spring Boot backend
echo "Starting Spring Boot backend..."
cd /Users/youssefelhodaiby/restapi/restassurd
mvn spring-boot:run &

# Wait for backend to start
sleep 10

# Start the React frontend
echo "Starting React frontend..."
cd /Users/youssefelhodaiby/restapi/frontend
npm install && npm start
