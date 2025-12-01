import argparse
import sys
import os

# Add project root to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.validate_schema import validate_all
from adapters.dbt.generate_seeds import generate_seeds
from adapters.dbt.generate_tests import generate_tests
from adapters.dbt.generate_semantic_models import generate_dbt_semantic_models
from adapters.powerbi.generate_tmsl import generate_powerbi_tmsl
from adapters.tableau.generate_tds import generate_tableau_tds

def main():
    parser = argparse.ArgumentParser(description="ODGS: The Protocol for Algorithmic Accountability")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Validate Command
    validate_parser = subparsers.add_parser("validate", help="Verify schema integrity and AI safety compliance")

    # Build Command
    build_parser = subparsers.add_parser("build", help="Generate downstream adapters (dbt, PowerBI, Tableau)")

    args = parser.parse_args()

    if args.command == "validate":
        print("🛡️  Running ODGS AI Safety Checks...")
        try:
            validate_all()
            print("✅ All systems go. Schema is mathematically consistent.")
        except Exception as e:
            print(f"❌ Validation Failed: {e}")
            sys.exit(1)

    elif args.command == "build":
        print("🏗️  Building Governance Artifacts...")
        
        print("\n--- dbt Adapter ---")
        generate_seeds()
        generate_tests()
        generate_dbt_semantic_models()
        
        print("\n--- Power BI Adapter ---")
        generate_powerbi_tmsl()
        
        print("\n--- Tableau Adapter ---")
        generate_tableau_tds()
        
        print("\n✨ Build Complete. Your data ecosystem is now synchronized.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
