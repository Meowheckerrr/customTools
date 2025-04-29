import subprocess

def run_dnsrecon(domain):
    try:
        print(f"[+] DNS Query: {domain}")
        result = subprocess.run(
            f"dnsrecon -d {domain}",
            shell=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            with open("dnsquery.txt", "a") as out:
                out.write(f"\n### Results for {domain} ###\n")
                out.write(result.stdout)
        else:
            print(f"[-] No records: {domain}")

    except Exception as e:
        print(f"[!] Error: {e}")


def main():
    with open("domains.txt", "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    for domain in domains:
        run_dnsrecon(domain)


if __name__ == "__main__":
    main()
