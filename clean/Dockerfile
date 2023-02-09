# Use same version as defined in .python-version.
FROM python:3.11.0-slim-bullseye

# Update Ubuntu Software repository.
RUN apt update -y \
    && apt upgrade -y \
    && apt install -y --no-install-recommends git build-essential procps curl file nano sudo ncdu gcc postgresql libpq-dev \
    # Cleanup.
    && rm -rf /var/lib/apt/lists/*

RUN echo 'alias la="ls -la"' >> ~/.bashrc

WORKDIR /app

# Upgrade pip.
# Install pipenv.
RUN python -m pip install --upgrade pip \
    && python -m pip install pipenv

# Copy dependency files into workdir (optimise docker cache layers).
COPY Pipfile Pipfile.lock ./

# Install virtual environment.
RUN python -m pipenv install --dev --deploy

# Copy rest of the project into image.
COPY . .


CMD ["bash"]