FROM python:3.8

RUN ["mkdir","-p","/root/.jupyter"]
RUN ["mkdir","-p","/example/example_code"]
RUN ["mkdir","-p","/example/sample_data"]

ARG BUILD_PATH
ADD $BUILD_PATH/requirements.txt /var/requirements.txt

ADD $BUILD_PATH/sample_data /example/sample_data
ADD $BUILD_PATH/example_code /example/example_code

USER root
RUN pip install jupyter notebook 
RUN pip install -r /var/requirements.txt
RUN jupyter notebook --generate-config -y

ADD $BUILD_PATH/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

WORKDIR /example

ENTRYPOINT jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root


