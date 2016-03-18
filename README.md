component-kafka
===============

Version 1.1-41p
---------------

<img src="https://s3.amazonaws.com/qubell-images/kafka.png">

Installs and configures Apache Kafka

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-kafka/1.1-41p/meta.yml)

Features
--------

- Install and configure Apache Kafka on multiple compute
- Install and configure Kafka Manager web UI

Configurations
--------------
- Apache Kafka 0.8.2.1, Amazon Linux (us-east-1/ami-1ba18d72), AWS EC2 m1.small, ec2-user
- Apache Kafka 0.8.2.1, CentOS 6.5 (us-east-1/ami-bc8131d4), AWS EC2 m1.small, root

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
   - Apache Kafka and Kafka Manager distribution
   - S3 bucket with Chef recipes: qubell-starter-kit-artifacts
   - If Chef is not installed: please install Chef 10.16.2 using http://www.opscode.com/chef/install.sh ```bash <($WGET -O - http://www.opscode.com/chef/install.sh) -v $CHEF_VERSION```

Implementation notes
--------------------
 - Installation is based on Chef recipes from https://github.com/qubell-bazaar/cookbook-qubell-kafka_component

Configuration parameters
------------------------
- input.recipe-url: URL to Apache Kafka chef recipe repo
- input.kafka-port: Listen port for Apache Kafka service
- input.manager-port: Listen port for Kafka Manager web UI
- input.manager-url: URL to Kafka Manger archive repo
