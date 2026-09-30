# VirtualOps Assist - Check simulated desktop CPU usage

vdi_name = "vdi-03"
cpu_usage = 85

print(f"Checking desktop: {vdi_name}")

if cpu_usage >= 90:
    print("Critical: CPU usage is very high.")
elif cpu_usage >= 70:
    print("Warning: CPU usage is elevated.")
else:
    print("CPU usage is normal.")


print(cpu_usage >= 70)