FROM library/caddy

COPY --from=local/extpy-app /app/.web/_static /srv
ADD Caddyfile /etc/caddy/Caddyfile