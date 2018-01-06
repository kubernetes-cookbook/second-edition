FROM nginx

RUN ["service", "nginx", "stop"]

COPY nginx_8800.conf /etc/nginx/conf.d/default.conf

EXPOSE 8800

CMD ["nginx", "-g", "daemon off;"]

