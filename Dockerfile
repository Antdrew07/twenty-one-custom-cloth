# Static site: no build step. Caddy serves index.html + assets on Railway's $PORT.
FROM caddy:2-alpine
WORKDIR /srv
COPY index.html ./
COPY assets ./assets
COPY Caddyfile /etc/caddy/Caddyfile
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
