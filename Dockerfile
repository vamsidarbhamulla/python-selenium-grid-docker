# Create a selenium pytest image without any browsers and browser drivers
FROM ubuntu
LABEL maintainer="Vamsi Darbhamulla"
LABEL email="vamsi.krishna0207@gmail.com"

ARG T_THREAD_COUNT=5
ENV THREAD_COUNT=$T_THREAD_COUNT
ARG T_ENABLE_PYTEST_CACHE=False
ENV ENABLE_PYTEST_CACHE=$T_ENABLE_PYTEST_CACHE
ARG T_ENABLE_ALLURE_REPORT=True
ENV ENABLE_ALLURE_REPORT=$T_ENABLE_ALLURE_REPORT
ARG T_ENABLE_MULTITHEAD=True
ENV ENABLE_MULTITHEAD=$T_ENABLE_MULTITHEAD

RUN mkdir /src && \
    apt-get update && \
    apt-get install -y \
    python3.7 \
    python3-pip && \
    pip3 install selenium \
	pytest-xdist \
	allure-pytest \
	webdriver_manager

WORKDIR /src
COPY . /src/

RUN chmod +x /src/entrypoint.sh

ENTRYPOINT ["/src/entrypoint.sh"]
CMD ["--help"]
