FROM alpine:3.16

ENV KAFKA_VERSION 3.4.1
ENV SCALA_VERSION 2.13
ENV KAFKA_HOME /opt/kafka
LABEL name="kafka" version=${KAFKA_VERSION}

RUN apk add --no-cache openjdk17-jre bash coreutils su-exec
RUN apk add --no-cache -t .build-deps curl ca-certificates tar \
  && mkdir -p /opt \
  && curl -s https://dlcdn.apache.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \
  | tar -xzf - -C /opt \
  && mv ${KAFKA_HOME}_${SCALA_VERSION}-${KAFKA_VERSION} ${KAFKA_HOME} \
  && adduser -DH -s /sbin/nologin kafka \
  && chown -R kafka: ${KAFKA_HOME} \
  && rm -rf /tmp/* \
  && apk del --purge .build-deps

ENV PATH /sbin:${KAFKA_HOME}/bin/:$PATH

WORKDIR ${KAFKA_HOME}

EXPOSE 9092 2181

COPY entrypoint.sh  /entrypoint.sh
COPY create-topics.sh /create-topics.sh
RUN chmod +x /entrypoint.sh && chmod +x /create-topics.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["zookeeper"]