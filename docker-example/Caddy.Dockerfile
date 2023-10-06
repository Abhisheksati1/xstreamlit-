FROM library/caddy

COPY --from=local/dotserve-app /app/.web/_static /srv
ADD Caddyfile /etc/caddy/Caddyfile