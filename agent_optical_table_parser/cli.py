"""CLI for agent-optical-table-parser."""
import sys
import argparse
from .parser import OpticalTableParser, TextCell

def main():
    parser = argparse.ArgumentParser(description="Agent Optical Table Parser CLI")
    parser.add_argument("--demo", action="store_true", help="Run optical table parser demo")
    args = parser.parse_args()

    if args.demo:
        parser_obj = OpticalTableParser()
        cells = [
            TextCell("Metric", 10, 10), TextCell("Value", 120, 10),
            TextCell("Accuracy", 10, 40), TextCell("99.2%", 120, 40),
            TextCell("Latency", 10, 70), TextCell("12ms", 120, 70)
        ]
        md = parser_obj.to_markdown(cells)
        print("[+] Generated Markdown Table:")
        print(md)
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
