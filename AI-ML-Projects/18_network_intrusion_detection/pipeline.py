def analyze_packet(src_bytes: int, dst_bytes: int, connection_count: int) -> dict:
    if connection_count > 100 and dst_bytes == 0:
        return {"threat": "DoS Flood", "action": "BLOCK_IP"}
    elif src_bytes == 0 and connection_count > 30:
        return {"threat": "Port Scan", "action": "FLAG_SUSPICIOUS"}
    return {"threat": "Benign", "action": "ALLOW"}

if __name__ == "__main__":
    print(analyze_packet(10, 0, 150))
    print(analyze_packet(450, 600, 4))
