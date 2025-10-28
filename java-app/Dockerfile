# Étape 1 : build de l'application
FROM maven:3.9.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Étape 2 : image d'exécution minimale
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/java-app-1.0-SNAPSHOT.jar app.jar
CMD ["java", "-jar", "app.jar"]
