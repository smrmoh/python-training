# VirtualOps Assist - Simulated desktop triage

vdi_name = "vdi-03"
maintenance_mode = False
power_state = "stopped"
is_registered = False
cpu_usage = 95

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