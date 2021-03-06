#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Real estate.
"""

__version__ = '4.0'


content = {
        'real-estate_headline': ['<#realestate_shortheadline#>'],
        'realestate_headline': ['<#realestate_shortheadline#>'],

        'realestate_section': ['<#realestate_type#>'],
        'realestate_shortheadline': [
            '<#realestate_type#>',
            '<#city#> <#realestate_types#>',
            '<#country#> <#realestate_types#>',
            '<#realestate_type#> <#realestate_verb#> <#realestate_subject#>',
            '<#realestate_types#> <#realestate_verbplural#> <#realestate_subject#>',
            '<#realestate_types#> <#time_thisyear#>',
            '<#realestate_subject#>',
            '<#realestate_subject#>',
            '<#realestate_subject#> <#time_thisyear#>',
        ],
        'realestate_type': [
            'Your Home', 'Your House', 'Your Accommodation', 'Your Apartment', 'The Flat',
            'Your Condo', 'Your Office', 'Your Site', 'Your Estate', 'Your area', 'Your Land',
        ],
        'realestate_types': [
            'Homes', 'Houses', 'Accommodations', 'Apartments', 'Flats', 'Condo’s',    'Offices',
            'Sites', 'Estates', 'Areas', 'Investments',
        ],
        'realestate_verb': [
            '', '', '', 'for', 'needs', 'has', 'requires', 'takes', 'invokes', 'does', 'gets',
        ],
        'realestate_verbplural': [
            '', '', '', 'for', 'need', 'have', 'require', 'take', 'invoke',    'do', 'get',
        ],
        'realestate_subject':[
    'Advance Fee',
    'Advertising',
    'Aesthetic Value',
    'Affirmative Lending',
    'Affordability State',
    'A-Frame',
    'Agency Disclosure',
    'Agent',
    'Agreement',
    'Annexation',
    'Annual Cap',
    'Annuity',
    'Antitrust Laws',
    'Appraiser',
    'Appreciation',
    'Appropriation',
    'Attorney',
    'Architecture',
    'Asbestos',
    'Asking Price',
    'Assemblage',
    'Assessment',
    'Audit',
    'Authentication',
    'Bailiff',
    'Bailment',
    'Balance',
    'Balustrade',
    'Bankruptcy',
    'Binder',
    'Blight',
    'Blighted Area',
    'Blueprint',
    'Blue-Sky Laws',
    'Boiler Plate',
    'Broker',
    'Brokerage',
    'Brownfields',
    'Brownstone',
    'Budget',
    'Budget Mortgage',
    'Builder',
    'Warranty',
    'Bulk Sales',
    'Bulk Transfer',
    'Bungalow',
    'Buy-Down',
    'Buyer’s Agent',
    'Buyer’s Broker',
    'Buyer’s Market',
    'Buyout',
    'By-Laws',
    'Caisson',
    'Cap',
    'Cap Sheet',
    'Capacity',
    'Cash Equivalent',
    'Cash Flow',
    'Cash Method',
    'Cash Out',
    'Cash Rent',
    'Casing',
    'Caulk',
    'Caulking',
    'Cavity',
    'Cavity Wall',
    'Ceiling joist',
    'Cement',
    'Census',
    'Chalk line',
    'Chancellor',
    'Chancery',
    'Change Order',
    'Channeling',
    'Chase',
    'Chattel',
    'Checking',
    'Chip Board',
    'Chose',
    'Clean out',
    'Cleaning Fee',
    'Closing',
    'Closing Costs',
    'Closing Date',
    'Cold Applied',
    'Cold Joint',
    'Collar',
    'Collar Beam',
    'Collateral',
    'Concession',
    'Consent',
    'Convey',
    'Cooperative',
    'Coping',
    'Corbel',
    'Cornerite',
    'Cornice',
    'Credit',
    'Cubic Yard',
    'Cupping',
    'Curb',
    'Cure',
    'Curtesy',
    'Custodian',
    'Custom Builder',
    'Decree',
    'Dedication',
    'Deductions',
    'Deed',
    'Depression',
    'Depth',
    'Deregulation',
    'Dereliction',
    'Descent',
    'Devise',
    'Devisee',
    'Devisor',
    'Economics',
    'Elevation',
    'Employee',
    'Encroachment',
    'Equity',
    'Examination',
    'Exception',
    'Exchange',
    'Exchangor',
    'Exclusion',
    'Execution',
    'Executor',
    'Fishmouth',
    'Fishplate',
    'Forbearance',
    'Forced Sale',
    'Forecasting',
    'Foreclosure',
    'Forgery',
    'Form',
    'Fuse',
    'Gain',
    'Gap',
    'Gap Loan',
    'Glazing',
    'Goodwill',
    'Gradient',
    'Grading',
    'Grain',
    'Grant',
    'Grant Deed',
    'Grantee',
    'Grantor',
    'Grounds',
    'Groundwater',
    'Gutter',
    'Hardware',
    'Haunch',
    'Header',
    'Hearth',
    'Heir',
    'Highlights',
    'Highrise',
    'Hip',
    'Implied',
    'Impounds',
    'Incentive',
    'Incline',
    'Income',
    'Indemnify',
    'Indenture',
    'Infant',
    'Infiltration',
    'Inflation',
    'Infrastructure',
    'Ingress',
    'Inheritance',
    'Input',
    'Joint',
    'Joist',
    'Judgment',
    'Jumpers',
    'Land Lease',
    'Lattice',
    'Law',
    'Layout',
    'Lead',
    'Lease',
    'Leaseback ',
    'Listing',
    'Loan',
    'Location',
    'Male',
    'Mall',
    'Mall Stores',
    'Mandatory',
    'Masonry',
    'Mile',
    'Mill',
    'Molding',
    'Monument',
    'Mortar',
    'Mortgage',
    'Negotiable',
    'Offeree',
    'Offeror',
    'Organic',
    'Orientation',
    'Parties',
    'Patent',
    'Permeability',
    'Permit',
    'Plat',
    'Pledge',
    'Plough',
    'Plumb',
    'Premises',
    'Premium',
    'Price',
    'Probate',
    'Promisee',
    'Property',
    'Quasi',
    'Radius',
    'Rafter',
    'Redeem',
    'Redemption',
    'Reformation',
    'Refrigerant',
    'Regime',
    'Regulations',
    'Rehabilitate',
    'Reinforcing',
    'Reinstate',
    'Reinstatement ',
    'Residence',
    'Reversion',
    'Scarcity',
    'Secured',
    'Security',
    'Solvent',
    'Span',
    'Split',
    'Stakeholder',
    'Status',
    'Sublease',
    'Subletting',
    'Subordinate',
    'Summation',
    'Summons',
    'Sump',
    'Tee',
    'Tempered',
    'Trade',
    'Tread',
    'Treads',
    'TREC',
    'Visqueen',
    'Waive',
    'Waste',
    'Zone',
    ],
        }
