upstream tensorflow_backend {
	server 127.0.0.1:3014;
	keepalive 1;
}

server {
    listen       443;
    server_name  tensorflow.vi123456.com;

    ssl                  on;
    ssl_certificate      /etc/nginx/ssl/tensorflow.vi123456.com/server.crt;
    ssl_certificate_key  /etc/nginx/ssl/tensorflow.vi123456.com/server.key;

    access_log  /var/log/nginx/tensorflow.vi123456.com.access.log timed_combined;
    error_log   /var/log/nginx/tensorflow.vi123456.com.error.log;

    keepalive_timeout 99999999;

    location / {
        proxy_read_timeout 400s;
        proxy_pass http://tensorflow_backend;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
