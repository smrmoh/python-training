# VirtualOps Assist - Basic VDI health check
vdi_name = "vdi-01"
power_state = "running"
logged_on_user = "monty"
cpu_usage = 25
registration_state = "registered"

print(f"Checking VDI: {vdi_name}")
print(f"Current Power State: {power_state}")
print(f"Logged-on User: {logged_on_user}")
print(f"CPU Usage: {cpu_usage}%")
print(f"Registration State: {registration_state}")
