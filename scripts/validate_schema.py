import json
import os
import sys

# Get project root (parent of scripts dir)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(filename):
    path = os.path.join(PROJECT_ROOT, filename)
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Could not find {filename} at {path}")
        raise

def validate_metric(metric):
    required_fields = ["metric_id", "name", "domain", "calculation_logic", "owner"]
    issues = []
    for field in required_fields:
        if field not in metric:
            issues.append(f"Missing required field: {field}")
            
    # Validate calculation_logic structure
    if "calculation_logic" in metric:
        logic = metric["calculation_logic"]
        if not isinstance(logic, dict):
             issues.append("calculation_logic must be an object")
        else:
            if "abstract" not in logic:
                issues.append("calculation_logic missing 'abstract' field")
                
    return issues

def validate_data_rule(rule):
    required_fields = ["rule_id", "name", "domain", "calculation_logic", "owner"]
    issues = []
    for field in required_fields:
        if field not in rule:
            issues.append(f"Missing required field: {field}")
    return issues

def validate_all():
    print("🔍 Running Open Governance Schema Validator...")
    has_error = False
    
    # Validate Standard Metrics
    try:
        metrics = load_json('standard_metrics.json')
            
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
        rules = load_json('standard_data_rules.json')
            
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
        raise Exception("Validation failed. See logs for details.")
    else:
        print("🎉 All Governance Checks Passed!")

if __name__ == "__main__":
    try:
        validate_all()
        sys.exit(0)
    except Exception:
        sys.exit(1)
