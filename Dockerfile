FROM python:3.11 AS build_py

COPY script.py .
RUN chmod +x ./script.py && ./script.py
RUN cat artifact.txt

FROM scratch AS export-stage
COPY --from=build_py /artifact.txt .
