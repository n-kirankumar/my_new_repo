# Use OpenJDK 17 Alpine
FROM openjdk:17-alpine

# Set working directory
WORKDIR /app

# Copy Java file
COPY App.java .

# Compile Java file
RUN javac App.java

# Expose port
EXPOSE 8080

# Run the app
CMD ["java", "App"]
