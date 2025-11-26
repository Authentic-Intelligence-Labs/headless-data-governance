import json
import os
import sys

def validate_metric(metric):
    required_fields = ["metric_id", "name", "domain", "calculation_logic", "owner"]
    issues = []
    for field in required_fields:
        if field not in metric:
            issues.append(f"Missing required field: {field}")
    return issues

def main():
    print("🔍 Running Open Governance Schema Validator...")
    has_error = False
    
    # Load Standard Metrics
    try:
        with open('standard_metrics.json', 'r') as f:
            metrics = json.load(f)
            
        print(f"✅ Loaded {len(metrics)} metrics.")
        
        for m in metrics:
            issues = validate_metric(m)
            if issues:
                print(f"❌ Error in {m.get('name', 'Unknown')}: {', '.join(issues)}")
                has_error = True
                
    except Exception as e:
        print(f"❌ critical Error: {str(e)}")
        has_error = True

    if has_error:
        sys.exit(1)
    else:
        print("🎉 All Governance Checks Passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
