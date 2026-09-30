# VirtualOps Assist - Combined health checks

vdi_name = "vdi-04"
power_state = "running"
is_registered = False
maintenance_mode = False
cpu_usage = 90
response_time = 3

print(f"Checking desktop: {vdi_name}")

if power_state == "running" and is_registered and not maintenance_mode:
    print("Basic availability checks passed.")
else:
    print("Desktop needs availability investigation.")


if cpu_usage >= 80 or response_time >= 3:
    print("Performance needs investigation.")
else:
    print("Performance checks passed.")