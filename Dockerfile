FROM caddy:alpine
WORKDIR /app
COPY dist ./dist
COPY Caddyfile .
CMD ["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"]
