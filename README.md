## ZMQ介绍
>ZMQ (以下 ZeroMQ 简称 ZMQ)是一个简单好用的传输层，像框架一样的一个 socket library，
他使得 Socket 编程更加简单、简洁和性能更高。是一个消息处理队列库，可在多个线程、内核和主机盒之间弹性伸缩。
ZMQ 的明确目标是“成为标准网络协议栈的一部分，之后进入 Linux 内核”。现在还未看到它们的成功。
但是，它无疑是极具前景的、并且是人们更加需要的“传统”BSD 套接字之上的一层封装。
ZMQ 让编写高性能网络应用程序极为简单和有趣。


## RabbitMQ
>RabbitMQ是一个AMQP实现，传统的messaging queue系统实现，基于Erlang。
AMQP协议更多用在企业系统内，对数据一致性、稳定性和可靠性要求很高的场景，对性能和吞吐量还在其次

## Kafka
>Kafka是linkedin开源的MQ系统，
主要特点是基于Pull的模式来处理消息消费，追求高吞吐量，
一开始的目的就是用于日志收集和传输，0.8开始支持复制，不支持事务，适合产生大量数据的互联网服务的数据收集业务

