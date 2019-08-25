FROM python:3.7.2-stretch as python

# ENV PYTHONPATH="/src/disco/:${PYTHONPATH}"

WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

# Leaving this here for now. We may want to run a local notebook server with our code
# for the model prototyping portion. However, to reduce build time lets ignore this for
# now
# jupyter notebook settings
#COPY config/notebook/jupyter_notebook_config.py /root/.jupyter/
#COPY notebooks /analytics/notebooks

# add modules to the image - based on the pythonpath above this will now be importable
COPY src /src
