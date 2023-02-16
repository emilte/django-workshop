# Use same version as defined in .python-version.
FROM python:3.11.0-slim-bullseye

SHELL ["/bin/bash", "-c"]

ARG INSTALL=1

# Update Ubuntu Software repository.
RUN apt update -y \
    && apt upgrade -y \
    && apt install -y --no-install-recommends git build-essential procps curl file git nano sudo ncdu gcc postgresql libpq-dev \
    # Cleanup.
    && rm -rf /var/lib/apt/lists/*

### Environment variables. ###
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1
# Docker should configure env vars in '.docker.env'.
ENV PIPENV_DONT_LOAD_ENV=1

# Set working directory.
WORKDIR /app

RUN echo 'alias la="ls -la"' >> ~/.bashrc

# Upgrade pip.
# Install pipenv.
RUN python -m pip install --upgrade pip \
  && python -m pip install pipenv

# Copy dependency files into workdir (optimise docker cache layers).
COPY Pipfile Pipfile.lock ./

# Install virtual environment.
RUN if [ "$INSTALL" == "1" ]; then python -m pipenv install --dev --deploy; fi

# Copy rest of the project into image.
COPY . .

# Expose port for django and debugpy.
EXPOSE 8000
EXPOSE 5678

CMD [ "pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
