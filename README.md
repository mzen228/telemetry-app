# Secure Distributed Telemetry System

A containerized distributed telemetry system built using a microservice-style
architecture and modern DevSecOps practices.

The system consists of two independenly containerized services communicating over
a user-defined Docket network.

- `telemetry_receiver.py` listens for telemetry 
- `telemetry_sender.py` sends telemetry.

## Architecture 

The application follows microservice design principles:
- Separate containers for sender and receiver
- UDP-based communication
- Independent runtime processes
- Docker Compose orchestration

## Container Runtime Hardening

The containers are hardened using multiple security controls:
- Dropped Linux capabilities
- Read-only root filesystem
- No-new-privilege enforcement
- CPU, memory, and PID limits 
- Non-root user execution

These controls reduce attack surface and limit container breakout risk.

## CI/CD & Supply Chain Security

The CI/CD pipeline integrates security controls at build time:
- Static linting
- Vulnerability scanning with Trivy (fail on critical)
- SBOM generation (CycloneDX format)
- Publication to GitHub Container Registery (GHCR)
- Keyless container signing using Sigstore Cosign
- SBOM attestation attached to image digest
- Transparency log itegration (Rekor)

Images are signed using GitHub OIDC-based keyless signing, cryptographically bindig container artifacts to the GitHub workflow identity.

## How to run

To run the both containers, clone the repository and run,

`docker compose up`

## Purpose and learning goals

The purpose of this project is to gain experience using Docker containers
and gain experience incorporating security checks into a CI/CD workflow (DevSecOps).

