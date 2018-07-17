#!/bin/bash
mkdir -p ~/chatbot_ner_elasticsearch
cd /tmp/
curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.3.0.tar.gz
tar -xzf elasticsearch-5.3.0.tar.gz -C ~/chatbot_ner_elasticsearch/
