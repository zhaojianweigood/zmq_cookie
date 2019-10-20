
####请求回复模式，Request请求然后等待响应。Reply监听然后回复。
> Request方先发后收，send-recv
Reply方先收后发，recv-send
Request和Reply不停的重复它们的操作循环。
Reply类似于http服务器，
Request类似于客户端。
一个Reply可以连接多个Request端，顺序处理Request的请求。
