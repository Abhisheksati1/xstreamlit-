FROM library/caddy

COPY --from=local/dotreact-app /app/.web/_static /srv
ADD Caddyfile /etc/caddy/Caddyfile