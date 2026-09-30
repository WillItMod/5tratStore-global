"""Exercise the actual Tailscale initializer without mounting any host data."""
import subprocess
from pathlib import Path

import yaml

recipe = yaml.safe_load(
    (Path(__file__).resolve().parents[1] / "tailscale/docker-compose.yml").read_text()
)
initializer = recipe["services"]["init"]
initialize = initializer["command"][2]

fresh = initialize + "\ntest -d /data/state; test -d /data/run"
legacy_setup = """
mkdir -p /data/tailscale
printf legacy-identity > /data/tailscale/tailscaled.state
printf retained-file > /data/tailscale/received.txt
"""
legacy_checks = """
test "$(cat /data/state/tailscaled.state)" = legacy-identity
test "$(cat /data/tailscale/tailscaled.state)" = legacy-identity
test "$(cat /data/state/received.txt)" = retained-file
test "$(stat -c %a /data/state)" = 700
printf current-identity > /data/state/tailscaled.state
touch /data/run/tailscaled.sock
"""
repeat_checks = """
# Re-running init during an update must not unlink the live socket path.
test -e /data/run/tailscaled.sock
test "$(cat /data/state/tailscaled.state)" = current-identity
test "$(cat /data/tailscale/tailscaled.state)" = legacy-identity
"""
cases = {
    "fresh": fresh,
    "legacy-and-idempotency": "\n".join(
        [legacy_setup, initialize, legacy_checks, initialize, repeat_checks]
    ),
}
for name, script in cases.items():
    subprocess.run(
        ["docker", "run", "--rm", "--network", "none", initializer["image"], "sh", "-ec", script],
        check=True,
    )
    print(f"{name}: passed")
