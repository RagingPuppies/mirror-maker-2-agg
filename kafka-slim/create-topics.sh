#!/bin/bash

if [[ -z "$KAFKA_CREATE_TOPICS" ]]; then
    echo "no KAFKA_CREATE_TOPICS env provided, will not create topics"
    exit 0
fi

sleep 20

IFS="${KAFKA_CREATE_TOPICS_SEPARATOR-,}"; for topicToCreate in $KAFKA_CREATE_TOPICS; do
    echo "creating topics: $topicToCreate"
    IFS=':' read -r -a topicConfig <<< $topicToCreate
    COMMAND="${KAFKA_HOME}/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions ${topicConfig[1]} --replication-factor ${topicConfig[2]} --topic ${topicConfig[0]}"
    echo "executing $COMMAND"
    eval "${COMMAND}"
done

wait