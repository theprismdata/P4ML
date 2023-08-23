FROM python:3.8

RUN ["mkdir","-p","/root/.jupyter"]
RUN ["mkdir","-p","/example/workdir"]
RUN ["mkdir","-p","/example/sample_data"]

ARG BUILD_PATH
ADD $BUILD_PATH/requirements.txt /var/requirements.txt
ADD $BUILD_PATH/sample_data /example/sample_data

ADD $BUILD_PATH/mongo_ex.ipynb /example/mongo_ex.ipynb
ADD $BUILD_PATH/PostgreSQL_ex.ipynb /example/PostgreSQL_ex.ipynb
ADD $BUILD_PATH/LabelEncoder_1d_array.ipynb /example/LabelEncoder_1d_array.ipynb
ADD $BUILD_PATH/object_storage.ipynb /example/object_storage.ipynb
ADD $BUILD_PATH/pearson_correlation.ipynb /example/pearson_correlation.ipynb
ADD $BUILD_PATH/scikit-decision-tree.ipynb /example/scikit-decision-tree.ipynb


USER root
RUN pip install jupyter notebook 
RUN pip install -r /var/requirements.txt
RUN jupyter notebook --generate-config -y

ADD $BUILD_PATH/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

WORKDIR /example

ENTRYPOINT jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root


