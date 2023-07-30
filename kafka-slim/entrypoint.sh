#!/bin/bash -e
RUN_TYPE=$1

if [ "$RUN_TYPE" == "zookeeper" ]; then
  exec "$KAFKA_HOME/bin/zookeeper-server-start.sh" "$KAFKA_HOME/config/zookeeper.properties"
fi

if [ "$RUN_TYPE" == "kafka" ]; then
  /create-topics.sh &
  echo "zookeeper.connect=$KAFKA_ZOOKEEPER_CONNECT" > "$KAFKA_HOME/config/server.properties"
  exec "$KAFKA_HOME/bin/kafka-server-start.sh" "$KAFKA_HOME/config/server.properties"
fi




