## 网站访问TCP MSS检查

正常的链路MTU=1500，如果是IPv4协议，MSS是1460，如果是IPv6协议，MSS是1440。

但是Linux默认会启用TIME_STAMP选项，占用12字节的TCP头，如果是IPv协议，MSS是1448，如果是IPv6协议，MSS是1428。

checkmss.py通过建立TCP连接，然后获取内核中的TCP状态，显示 对方接收 和 我方接收的MSS。

ipv4.txt/ipv6.txt分别是一些网站的IPv4/IPv6结果（按照对方接收MSS排序）
