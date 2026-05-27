# 📌 Project Overview

This project provides technical articles retrieved through semantic search using LLaMA model, with content generation powered 
by the OpenAI. 

Additionally, it integrates a third-party WeatherAPI to provide weather data, which is used to generate non-technical 
articles related to current weather conditions.

# Architecture

## System-level Architecture

Frontend Technologies: JavaScript, jQuery, React, HTML, Tailwind CSS

Backend-for-Frontend (BFF)
- auth, rate limiting, request shaping
- validation, caching, and aggregation
- manages API keys, and hides service internals

Semantic search service
- performs calls to OpenAI if needed, and do the semantic search in text
- Open-source models (for example, LLaMA)
- Serves as LLM API

## Backend-for-Frontend (BFF) Service

- Code-level Architecture: Layered architecture

  - Controller / API / Presentation Layer
  - Service / Business Logic / Application / Domain Layer
  - Infrastructure Layer & Repository / Data Access Layer
- Handler pattern (gRPC)

API design

|                    |                                          |
|--------------------|------------------------------------------|
| **API**            | REST                                     |
| **Framework**      | FastAPI                                  |
| **Data validation** | Pydantic                                 |
| **Security**       | CORS, User's credentials + JWT, API keys |

DB design
- PostgreSQL (database for web application), MongoDB
- Pydantic Settings

## Semantic search microservice
- Code-level Architecture: Layered architecture

API design

|                         |          |
|-------------------------|----------|
| **API**                 | gRPC     |
| **Framework**           | FastAPI  |
| **Data validation**     | Protobuf |

## Infrastructure and Deployment Architecture

|                   |                     |
|-------------------|---------------------|
| **Deployment / Runtime:**    | Docker, Kubernetes  |
| **Infrastructure** | Terraform           |

- Frontend talks to BFF using internal DNS, e.g. http://bff-svc.default.svc.cluster.local.
- Backend (BFF) is deployed as a ClusterIP service meaning it’s internal only.

# 🏛️ System architecture pillars

## Reliable architecture

TBD

# 🛠 Development

|                       |                                                            |
|-----------------------|------------------------------------------------------------|
| **IDE & Environment** | PyCharm with Python virtual environment                    |
| **Testing**           | Pytest, Unittest frameworks                                |
| **Local Kubernetes**  | Minikube (lightweight local cluster) managed via Terraform |  
| **CI/CD**             | GitHub Actions workflow simulation for local testing       |  
| **Terraform**         | OpenTofu                                                   |  

PostgreSQL DB

[docker-compose.yml](docker-compose.yml)

```docker-compose up```
