# VirtualOps Assist - Simulated desktop triage

vdi_name = "vdi-03"
power_state = "running"
maintenance_mode = False
is_registered = True
cpu_usage = 25

print(f"Checking desktop: {vdi_name}")

if maintenance_mode:
    print("Desktop is in maintenance mode.")

elif power_state != "running":
    print("Desktop is not running. Check power state.")

elif not is_registered:
    print("Desktop is running but not registered")

elif cpu_usage >= 80:
    print("Desktop is registered, but CPU usage is high.")

else:
    print("Basic desktop checks passed")