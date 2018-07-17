#!/bin/bash
~/chatbot_ner_elasticsearch/elasticsearch-5.2.2/bin/elasticsearch -Ees.insecure.allow.root=true -d
/usr/sbin/nginx -g 'daemon off;'
