const standardMetrics = require('./protocol/lib/standard_metrics.json');
const standardDqDimensions = require('./protocol/lib/standard_dq_dimensions.json');
const standardDataRules = require('./protocol/lib/standard_data_rules.json');
const rootCauseFactors = require('./protocol/lib/root_cause_factors.json');
const businessProcessMaps = require('./protocol/lib/business_process_maps.json');
const physicalDataMap = require('./protocol/lib/physical_data_map.json');
const ontologyGraph = require('./protocol/lib/ontology_graph.json');

module.exports = {
  standardMetrics,
  standardDataRules,
  standardDqDimensions,
  rootCauseFactors,
  businessProcessMaps,
  physicalDataMap,
  ontologyGraph
};
