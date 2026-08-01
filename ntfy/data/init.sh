#!/bin/sh
set -eu

if [ ! -s "${NTFY_AUTH_FILE}" ]; then
  ntfy serve >/tmp/ntfy-init.log 2>&1 &
  server_pid=$!
  tries=0
  while [ ! -s "${NTFY_AUTH_FILE}" ] && [ "${tries}" -lt 20 ]; do
    sleep 0.25
    tries=$((tries + 1))
  done
  kill "${server_pid}" 2>/dev/null || true
  wait "${server_pid}" 2>/dev/null || true
fi

test -s "${NTFY_AUTH_FILE}"
ntfy user add --role=admin --ignore-exists admin
