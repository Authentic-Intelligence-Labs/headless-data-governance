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

def validate_data_rule(rule):
    required_fields = ["rule_id", "name", "domain", "calculation_logic", "owner"]
    issues = []
    for field in required_fields:
        if field not in rule:
            issues.append(f"Missing required field: {field}")
    return issues

def main():
    print("🔍 Running Open Governance Schema Validator...")
    has_error = False
    
    # Validate Standard Metrics
    try:
        with open('standard_metrics.json', 'r') as f:
            metrics = json.load(f)
            
        print(f"✅ Loaded {len(metrics)} metrics.")
        
        for m in metrics:
            issues = validate_metric(m)
            if issues:
                print(f"❌ Error in metric '{m.get('name', 'Unknown')}': {', '.join(issues)}")
                has_error = True
                
    except Exception as e:
        print(f"❌ Critical Error loading metrics: {str(e)}")
        has_error = True

    # Validate Standard Data Rules
    try:
        with open('standard_data_rules.json', 'r') as f:
            rules = json.load(f)
            
        print(f"✅ Loaded {len(rules)} data rules.")
        
        for r in rules:
            issues = validate_data_rule(r)
            if issues:
                print(f"❌ Error in rule '{r.get('name', 'Unknown')}': {', '.join(issues)}")
                has_error = True
                
    except Exception as e:
        print(f"❌ Critical Error loading data rules: {str(e)}")
        has_error = True

    if has_error:
        sys.exit(1)
    else:
        print("🎉 All Governance Checks Passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()

