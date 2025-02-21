# Use an official Node runtime as a parent image
FROM node:lts-alpine
# Set the working directory in the container
WORKDIR /app
# Copy package.json and package-lock.json (if available)
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy the rest of your app's code
COPY . .
# Build the React app for production
RUN npm run build
# Install a lightweight web server to serve the static files
RUN npm install -g serve
# Expose the port the app runs on
EXPOSE 3000
# Start the app
CMD ["serve", "-s", "build"]
