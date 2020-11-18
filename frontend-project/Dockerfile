FROM node:14.15.1-slim@sha256:48619db9da7dfd7f22a13aee46e2c1336b56fadf6eb53fa17a50b341befc9b63

RUN apt update && apt install -y g++ git make python3

WORKDIR /code

EXPOSE 8000

CMD ["bash", "-c", "yarn && yarn start"]
