#### 由三部分组成，push进行数据推送，work进行数据缓存，pull进行数据竞争获取处理。

>区别于Publish-Subscribe存在一个数据缓存和处理负载。当连接被断开，数据不会丢失，重连后数据继续发送到对端。
