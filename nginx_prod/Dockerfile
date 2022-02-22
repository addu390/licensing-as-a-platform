FROM nginx:stable-alpine

COPY default.conf /etc/nginx
COPY default.conf /etc/nginx/conf.d

EXPOSE 80

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]