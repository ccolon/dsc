import logging

# TODO make it a dictionary
# Indicate the subfolder of the input folder that contains the input files
input_folder = "Tanzania"

export = {
    # Save a log file in the output folder, called "exp.log"
    "log": True,

    # Transport nodes and edges as geojson
    "transport": False,

    # Save the main result in a "criticality.csv" file in the output folder
    # Each line is a simulation, it saves what is disrupted and for how long, and aggregate observables
    "criticality": True,

    # Save the amount of good flowing on each transport segment
    # It saves a flows.json file in the output folder
    # The structure is a dic {"timestep: {"transport_link_id: {"sector_id: flow_quantity}}
    # Can be True or False
    "flows": False,

    # Export information on aggregate supply chain flow at initial conditions
    # Used only if "disruption_analysis: None"
    # See analyzeSupplyChainFlows function for details
    "sc_flow_analysis": False,

    # Whether or not to export data for each agent for each time steps
    # See exportAgentData function for details.
    "agent_data": False,

    # Save firm-level impact results
    # It creates an "extra_spending.csv" file and an "extra_consumption.csv" file in the output folder
    # Each line is a simulation, it saves what was disrupted and the corresponding impact for each firm
    "impact_per_firm": False,

    # Save aggregated time series
    # It creates an "aggregate_ts.csv" file in the output folder
    # Each columns is a time series
    # Exports:
    # - aggregate production
    # - total profit, 
    # - household consumption, 
    # - household expenditure, 
    # - total transport costs, 
    # - average inventories.
    "time_series": False,

    # Save the firm table
    # It creates a "firm_table.xlsx" file in the output folder
    # It gives the properties of each firm, along with production, sales to households, to other firms, exports
    "firm_table": True,


    # Save the OD point table
    # It creates a "odpoint_table.xlsx" file in the output folder
    # It gives the properties of each OD point, along with production, sales to households, to other firms, exports
    "odpoint_table": True,

    # Save the country table
    # It creates a "country_table.xlsx" file in the output folder
    # It gives the trade profile of each country
    "country_table": True,

    # Save the edgelist table
    # It creates a "edgelist_table.xlsx" file in the output folder
    # It gives, for each supplier-buyer link, the distance and amounts of good that flows
    "edgelist_table": True,

    # Save inventories per sector
    # It creates an "inventories.xlsx" file in the output folder
    "inventories": False,

    # Save the combination of district and sector that are over the cutoffs value
    # It creates an "filtered_district_sector.xlsx" file in the output folder
    "district_sector_table": False,

    # Whether or not to export a csv summarizing some topological caracteristics of the supply chain network
    "sc_network_summary": True
}

# Specify edges on the transport network for which we want to observe the flows
specific_edges_to_monitor = {
    'multimodal': [],
    'special': []
}

# Logging level
logging_level = logging.INFO

# List of transport modes to include
transport_modes = ['roads']

# Monetary units to use in model. 'USD', 'kUSD', 'mUSD'
monetary_units_in_model = "mUSD"

# Monetary units in input files. 'USD', 'kUSD', 'mUSD'
monetary_units_inputed = "USD"

# Define the type of input data to calibrate the model
# - 'disaggregating IO' uses national input-table (tech_coef) with business census (district_economic_data)
# - 'supplier buyer network' uses supplier buyer network data
firm_data_type = "disaggregating IO"

# Whether or not to model congestion
congestion = True

# Whether or not firms should readjust their price to changes in input prices
propagate_input_price_change = True

# Which sectors to include. Possible values:
# - 'all': all the sectors are kept
# - list of sectors
sectors_to_include = "all"

# Which sectors to specifically exclude.
# - None
# - list of sectors
sectors_to_exclude = None

# The products from those sectors do not need transport network to be transported
sectors_no_transport_network = ['utility', 'transport', 'trade', 'service']

# Filter out sectors whose output is below that cutoff value
# - if 'type' is 'percentage', test cutoff againt the sector's relative output
# - if 'type' is 'absolute', test cutoff againt the sector's absolute output
# - if 'type' is 'relative_to_average', the cutoff is (cutoff value) * (country's total output) / (nb sectors)
cutoff_sector_output = {
    'type': 'relative_to_average',
    'value': 0.1
}

# Filter out sectors whose final demand is below that cutoff value
# - if 'type' is 'percentage', test cutoff againt the sector's relative output
# - if 'type' is 'absolute', test cutoff againt the sector's absolute output
# - if 'type' is 'relative_to_average', the cutoff is is set to (cutoff value) * (country's total demand) / (nb sectors)
cutoff_sector_demand = {
    'type': 'relative_to_average',
    'value': 0.1
}

# How to combine the output and demand sector cutoffs
combine_sector_cutoff = "and"

# Which districts to include. Possible values:
# - 'all': all the districts are kept
# - list of districts
districts_to_include = "all"

# Population density cutoff, in capita / km2
# Adminunit below this cutoff are eliminated for demand odpoint
# If set to 0, deactivate this filter
pop_density_cutoff = 0

# Population cutoff
# Adminunit below this cutoff are eliminated for demand odpoint
# If set to 0, deactivate this filter
pop_cutoff = 0

# Local demand cutoff
# When generating the households, if, at an OD point, an household has a demand below this value for one sector
# then this demand is ignored
# unit is that of monetary_units_inputed
# If set to 0, deactivate this filter
local_demand_cutoff = 0

# Which countries to include. Possible values:
# - 'all': all the districts are kept
# - list of countries
countries_to_include = "all"

# Defines the different parts of the transport network that a commercial link can use
# "accepted_modes": list of "roads", "railways", "waterways", "maritime", "multimodal"
# "accepted_multimodal_links": list of string that should correspond to the attribute "multimodes" of the multimodal_edges input file
logistics_modes = {
    'domestic': {
        "accepted_modes": ['roads'],
        "accepted_multimodal_links": []
    },
    'international': {
        "accepted_modes": ['roads', 'maritime', 'multimodal'],
        "accepted_multimodal_links": ['roads-maritime']
    }
}

# Any sector in a district that have an importance lower than this value is discarded
# 2 exceptions apply:
# - for each sector, the most important district is kept, even if its importance is lower.
# It avoids having no firm at all from a sector
# - for agriculture, the cutoff value is twice lower. If we apply the same cutoff value as the other sector
# all districts are filtered out. This is because, agriculture is generally spread over 
# the country, such that importance values are low and rather uniformly distributed.
district_sector_cutoff = 0.003

# For each sector, how many of the most important districts will be kept, whatever the 'district_sector_cutoff' value
# Possible values:
# - None: no extra district will be kept using this method
# - Integer > 0: nb of top district to keep
nb_top_district_per_sector = 1

# If True, the service firms (utility, transport, service) are modeled as the nonservice firms
# Their output will not use the transport network, but their inputs, if it comes from nonservice firms, will.
# If False, then two firms per service sector will be modeled for the whole country
# Neither their input nor output will use the transport network.
explicit_service_firm = True

# Duration target for the firm inventory
# When firm holds the inventories meeting this target, then the firms can keep meeting their pre-disruption
# production targets without ordering more inputs for the specified number of time steps.
# Two types of value are possible:
# - an integer value: all firms have the same inventory duration target for all inputs
# - 'inputed': values are provided in an external file, which a specific duration target to each input-sector, buying-firm-sector combination 
inventory_duration_target = 2

# Extend the inventory duration targets of all firms, uniformly
# Possible values:
# - integer, which represents the number of time steps to add
# - None, no extra inventory
# The type of inputs for which the inventory is to be extended is determined by the inputs_with_extra_inventories parameter
extra_inventory_target = None

# List of inputs, identified by their producing sector, for which an extra inventory duration target is given
# Possible values:
# - 'all': all types of inputs
# - list of sector id, e.g., ['AGR','FOR','TRD','IMP']
inputs_with_extra_inventories = "all"

# List of sectors for which an extra inventory duration target is given
# Possible values:
# - 'all': all sectors
# - list of sector id, e.g., ['AGR','FOR','TRD','IMP']
buying_sectors_with_extra_inventories = "all"

# Determines the speed at which firms try to reach their inventory duration target
# See Henriet, Hallegatte, and Tabourier 2011 for the formulas
# A too large value leads to dynamic instabilities, called Bullwhip effect
reactivity_rate = 0.1

# Determines the initial utilization rate of firms
# It is used to determine, based on the production of the input-output equilibrium, the production capacity of the firms
# E.g., if a firm produces 80 and has a 0.8 utilization rate, then its production capacity is set to 100.
# It applies uniformly to all firms.
utilization_rate = 0.8

# Determines which inputs will be kept in the firms' Leontief production function
# It sets to 0 the elements of the technical coefficient IO matrix that are below this cutoff
# E.g., if sector A uses 0.3 input of sector B and 0.005 input of sector C to produce 1 unit of output (data from
# the technical coefficient matrix), then, with a io_cutoff of 0.01, firms for sector A will only source inputs from 
# sector B firms.
io_cutoff = 0.01

# Determines the way firms ration their clients if they cannot meet all demand
# Possible values are:
# - 'equal': all clients are equally rationned in proportion of their order
# - 'household_first': if the firm sells to both households and other firms, then households are served first 
rationing_mode = "household_first"

# Set the number of supplier that firms have for each type of input
# Possible values are:
# - 1: each firms select one supplier per input
# - 2: each firms select two suppliers per input
# - a decimal number between 1 and 2: firms choose either one or two suppliers per input, such that, in average
# the average number of supplier per sector is equal to the specified number.
nb_suppliers_per_input = 1

# Determines how important it is for firms to choose suppliers close to them
# The chance of choosing a firm as a supplier for an input, depends on its importance score and on its distance
# It is (importance) / (distance)^w where w is the weight_localization parameter
weight_localization_firm = 1

# Determines how important it is for households to choose suppliers close to them
# The chance of choosing a firm as a supplier for an input, depends on its distance
# It is 1 / (distance)^w where w is the weight_localization parameter
weight_localization_household = 4

# Determines the type of disruption analysis to be done
# Possible values are:
# - None: no disruption is made. The model is only initialized at t=0, and stops.
# Metrics describing the initial state are exported.
# - a dic: {
#       "disrupt_nodes_or_edges": "nodes" or "edges", 
#        "nodeedge_tested": object
#   }
#   - "disrupt_nodes_or_edges" determines whether nodes or edges are to be dirupted.
#   - "nodeedge_tested" determines" what is disrupted. Possible values are:
#       - integer: a single node or edge ID. The time series are exported.
#       - a list of node/edge ids. Criticality exports.
#       - "all": test all nodes or edges, ordered by their ID. Criticality exports.
#       - a path to a list of node or edges. Criticality exports.
#   - "duration" determines" the duration of a disruption
disruption_analysis = None

# What time interval does a time step represents
# Possible values are: 'day', 'week', 'month', 'year'
time_resolution = 'week'

# Number of nodeedge to test
# It will take only the first N in the list of nodes or edges of the criticality loop
# Possible values are:
# - None: all elements are tested
# - an integer N: the N first are tested
nodeedge_tested_topn = None

# Skip the first elements in the list of nodes or edges to disrupt in the criticality loop
# Possible values are None or integer values. It should be lower than nodeedge_tested_topn, if such value is given.
# If nodeedge_tested_topn is N and nodeedge_tested_skipn is M, the we test list[M,N]
nodeedge_tested_skipn = None

# Run the model in the "Aggregate IO mode"
# Instead of disrupting the transport network, we evaluate how much production would be blocked if all the firms 
# located in the disrupted nodes were unable to produce. Then we uniformly distribute this drop of production on
# all the firm of the corresponding sector.
model_IO = False

# Provides default simulation duration Tfinal for different disruption duration
duration_dic = {
    1:4, 
    2:8, 
    3:11, 
    4:14
}

# Whether or not to load extra roads in the model
extra_roads = False

# Value of the household extra spending and consumption loss under which we stop the simulation
# Units is the monetary_units_in_model
# If None, then we use the default simulation duration Tfinal, see duration_dic
epsilon_stop_condition = 1e-3

# Characteristic of the transport edges that the path chosen by firms to 
# deliver to their to clients should minimized
# Possible values are:
# - time_cost
# - cost_per_ton
route_optimization_weight = "cost_per_ton" 

# How to translate an increase in transport cost into increase in prices
cost_repercussion_mode = "type1"

# Whether or not to account for transport network capacity
# If True, then each shipment adds a "load" on transport edges 
# it the load exceed the capacity, then the edges cannot be used anymore
account_capacity = True

# How to create firms from economic data
# - "economic_adminunit_data" is a new method developped for Cambodia
#   We have econmic data for each sector at the commune level
#   We use a cutoff value per sector, over which we create a firm
#   That way we select the commune, hence the od points
# - "district_sector_importance" is the method used for Tanzania
#   We have preselected OD points, hence district in which we want to have firms
#   There may be multiple OD points per district
#   We have precalculated the relative importance of each district for each sector
#   We use a single cutoff values (in fact one for agriculture, and another for the other sectors)
#   that is applied to these relative importance
firm_sampling_mode = "economic_adminunit_data"