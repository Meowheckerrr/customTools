#!/usr/bin/python3 
import subprocess

def run_assetfinder(domain):
    try:
        print(f"[+] Finding Assets: {domain}")
        result = subprocess.run(
            f"assetfinder {domain}",
            shell=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            for line in result.stdout.strip().split('\n'):
                subprocess.run(
                    f'echo "{line}" | anew assets.txt',
                    shell=True
                )
        else:
            print(f"[-] No Assets for {domain}")

    except Exception as e:
        print(f"[!] Error：{e}")


def main():
    with open("domain.txt", "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    for domain in domains:
        run_assetfinder(domain)


if __name__ == "__main__":
    main()
