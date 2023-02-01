"""
This file was auto-generated by an ObjectFactory of aTLAS
"""


SCENARIO_NAME = '10x10'


SUPERVISOR_AMOUNT = 10


TRUST_LOG_DICT = [{'agent': 'J',
  'date_time': '2023-01-07 23:24:41:888616',
  'exec_time': '0.09824275970458984',
  'other_agent': 'H',
  'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
  'trust_value': '0.2986209592743997'},
 {'agent': 'E',
  'date_time': '2023-01-07 23:24:42:041244',
  'exec_time': '0.13165783882141113',
  'other_agent': 'J',
  'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
  'trust_value': '0.1653985222305728'},
 {'agent': 'B',
  'date_time': '2023-01-07 23:24:42:199654',
  'exec_time': '0.0884392261505127',
  'other_agent': 'C',
  'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
  'trust_value': '0.19708815232985258'},
 {'agent': 'F',
  'date_time': '2023-01-07 23:24:42:362616',
  'exec_time': '0.09034061431884766',
  'other_agent': 'G',
  'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
  'trust_value': '0.020810517253287603'},
 {'agent': 'A',
  'date_time': '2023-01-07 23:24:42:476087',
  'exec_time': '0.041980743408203125',
  'other_agent': 'E',
  'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
  'trust_value': '-0.11227504288995252'},
 {'agent': 'B',
  'date_time': '2023-01-07 23:24:42:599978',
  'exec_time': '0.05032515525817871',
  'other_agent': 'E',
  'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
  'trust_value': '0.045159475275330596'},
 {'agent': 'A',
  'date_time': '2023-01-07 23:24:42:671538',
  'exec_time': '0.05627298355102539',
  'other_agent': 'B',
  'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
  'trust_value': '0.08740429520452783'},
 {'agent': 'G',
  'date_time': '2023-01-07 23:24:42:778940',
  'exec_time': '0.054414987564086914',
  'other_agent': 'F',
  'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
  'trust_value': '-0.08910996259382134'},
 {'agent': 'I',
  'date_time': '2023-01-07 23:24:42:830426',
  'exec_time': '0.0019426345825195312',
  'other_agent': 'B',
  'resource_id': 'befcda34-8561-4580-ad99-463510518ef7',
  'trust_value': '-1.0'},
 {'agent': 'C',
  'date_time': '2023-01-07 23:24:42:869134',
  'exec_time': '0.0013356208801269531',
  'other_agent': 'D',
  'resource_id': '95a883a4-bbe5-4084-a086-9020eab9169e',
  'trust_value': '-1.0'}]


AGENT_TRUST_LOGS_DICT = {'A': [{'date_time': '2023-01-07 23:24:42:433579',
        'metric_str': 'content_trust.bias',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '-0.707820906802209'},
       {'date_time': '2023-01-07 23:24:42:434218',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '-0.552599485545487'},
       {'date_time': '2023-01-07 23:24:42:434789',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '-0.028623607915303495'},
       {'date_time': '2023-01-07 23:24:42:435333',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '-0.9842468504050286'},
       {'date_time': '2023-01-07 23:24:42:435902',
        'metric_str': 'content_trust.deception',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '-0.030793016348472868'},
       {'date_time': '2023-01-07 23:24:42:436481',
        'metric_str': 'content_trust.age',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:437043',
        'metric_str': 'content_trust.authority',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:437990',
        'metric_str': 'content_trust.topic',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:438581',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '0.19999999999999996'},
       {'date_time': '2023-01-07 23:24:42:440914',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '0.2451353070250173'},
       {'date_time': '2023-01-07 23:24:42:460489',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:465844',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '0.09097513155189385'},
       {'date_time': '2023-01-07 23:24:42:466980',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:472295',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'E',
        'resource_id': '753115e2-c1a2-4678-9784-43bd38377280',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:614503',
        'metric_str': 'content_trust.bias',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '0.03309896848442939'},
       {'date_time': '2023-01-07 23:24:42:615088',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '0.3701313430414004'},
       {'date_time': '2023-01-07 23:24:42:615615',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '-0.8082873259332894'},
       {'date_time': '2023-01-07 23:24:42:616167',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '-0.007644935461602165'},
       {'date_time': '2023-01-07 23:24:42:616728',
        'metric_str': 'content_trust.deception',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '0.20528628227230694'},
       {'date_time': '2023-01-07 23:24:42:617303',
        'metric_str': 'content_trust.age',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:617867',
        'metric_str': 'content_trust.authority',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:620339',
        'metric_str': 'content_trust.topic',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:620913',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '-1.0'},
       {'date_time': '2023-01-07 23:24:42:623416',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '-0.21833524314560204'},
       {'date_time': '2023-01-07 23:24:42:664475',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '-0.13408748753170033'},
       {'date_time': '2023-01-07 23:24:42:665180',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:667665',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:668460',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'B',
        'resource_id': 'ae7188a0-493f-4f75-94f9-4eca82d71390',
        'trust_value': '0.0'}],
 'B': [{'date_time': '2023-01-07 23:24:42:110622',
        'metric_str': 'content_trust.bias',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '-0.7614461960466483'},
       {'date_time': '2023-01-07 23:24:42:113169',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '0.7568967319213662'},
       {'date_time': '2023-01-07 23:24:42:115880',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '0.3555705052664331'},
       {'date_time': '2023-01-07 23:24:42:118530',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '0.03446359658236209'},
       {'date_time': '2023-01-07 23:24:42:119108',
        'metric_str': 'content_trust.deception',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '0.21684617651712923'},
       {'date_time': '2023-01-07 23:24:42:119721',
        'metric_str': 'content_trust.age',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:120316',
        'metric_str': 'content_trust.authority',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:121245',
        'metric_str': 'content_trust.topic',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '-0.27008695036587527'},
       {'date_time': '2023-01-07 23:24:42:121559',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:123578',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '-0.8158165341958741'},
       {'date_time': '2023-01-07 23:24:42:161027',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:172283',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '-0.29479275673434807'},
       {'date_time': '2023-01-07 23:24:42:173976',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:195134',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'C',
        'resource_id': '5b0a489e-3a43-4426-864f-3b9c084dc715',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:549147',
        'metric_str': 'content_trust.bias',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '-0.03173205653296951'},
       {'date_time': '2023-01-07 23:24:42:550671',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '-0.6074908343256029'},
       {'date_time': '2023-01-07 23:24:42:551107',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '-0.651386176956436'},
       {'date_time': '2023-01-07 23:24:42:551512',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '-0.6916765731170922'},
       {'date_time': '2023-01-07 23:24:42:551876',
        'metric_str': 'content_trust.deception',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '0.21637013996734433'},
       {'date_time': '2023-01-07 23:24:42:552273',
        'metric_str': 'content_trust.age',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:552641',
        'metric_str': 'content_trust.authority',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:555036',
        'metric_str': 'content_trust.topic',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:555468',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '0.33333333333333326'},
       {'date_time': '2023-01-07 23:24:42:557492',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '0.21801478571551725'},
       {'date_time': '2023-01-07 23:24:42:580769',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '-0.28383315428058775'},
       {'date_time': '2023-01-07 23:24:42:581611',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:584064',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:598430',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'E',
        'resource_id': 'dfbc7e78-0d8d-45da-a48c-ea788de8ea95',
        'trust_value': '0.6666666666666665'}],
 'C': [{'date_time': '2023-01-07 23:24:42:867533',
        'metric_str': 'content_trust.bias',
        'other_agent': 'D',
        'resource_id': '95a883a4-bbe5-4084-a086-9020eab9169e',
        'trust_value': '-0.684296796199446'},
       {'date_time': '2023-01-07 23:24:42:867864',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'D',
        'resource_id': '95a883a4-bbe5-4084-a086-9020eab9169e',
        'trust_value': '-0.8771749042732477'},
       {'date_time': '2023-01-07 23:24:42:868202',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'D',
        'resource_id': '95a883a4-bbe5-4084-a086-9020eab9169e',
        'trust_value': '-0.4206870197200947'},
       {'date_time': '2023-01-07 23:24:42:868521',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'D',
        'resource_id': '95a883a4-bbe5-4084-a086-9020eab9169e',
        'trust_value': '0.5437725084019822'}],
 'D': [],
 'E': [{'date_time': '2023-01-07 23:24:41:908753',
        'metric_str': 'content_trust.bias',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '0.8961016043719563'},
       {'date_time': '2023-01-07 23:24:41:909592',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '0.29176488230136144'},
       {'date_time': '2023-01-07 23:24:41:910559',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '-0.13028923671245463'},
       {'date_time': '2023-01-07 23:24:41:911383',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '-0.20744435572316067'},
       {'date_time': '2023-01-07 23:24:41:912214',
        'metric_str': 'content_trust.deception',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '0.10545618634549081'},
       {'date_time': '2023-01-07 23:24:41:913017',
        'metric_str': 'content_trust.age',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:41:913636',
        'metric_str': 'content_trust.authority',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:41:914785',
        'metric_str': 'content_trust.topic',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:41:915409',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '0.0'},
       {'date_time': '2023-01-07 23:24:41:923544',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '-0.24925123684122463'},
       {'date_time': '2023-01-07 23:24:42:002172',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '0.5472971394245425'},
       {'date_time': '2023-01-07 23:24:42:028491',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '-0.043492780311680176'},
       {'date_time': '2023-01-07 23:24:42:030196',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:038700',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'J',
        'resource_id': '5580be08-3f90-4f61-afda-60159b720de3',
        'trust_value': '1.0'}],
 'F': [{'date_time': '2023-01-07 23:24:42:271597',
        'metric_str': 'content_trust.bias',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '-0.09115861785680912'},
       {'date_time': '2023-01-07 23:24:42:272576',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '0.12049602982067542'},
       {'date_time': '2023-01-07 23:24:42:273226',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '0.45804554264236774'},
       {'date_time': '2023-01-07 23:24:42:273998',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '-0.5799840355132677'},
       {'date_time': '2023-01-07 23:24:42:274780',
        'metric_str': 'content_trust.deception',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '0.07839908159476305'},
       {'date_time': '2023-01-07 23:24:42:275600',
        'metric_str': 'content_trust.age',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:276472',
        'metric_str': 'content_trust.authority',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:277817',
        'metric_str': 'content_trust.topic',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:278610',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '-1.0'},
       {'date_time': '2023-01-07 23:24:42:282158',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:304505',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:318608',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '-0.22809372571296113'},
       {'date_time': '2023-01-07 23:24:42:320223',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:360285',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'G',
        'resource_id': '2d01e9a7-770e-4d33-b9d1-388f02393660',
        'trust_value': '0.8571428571428572'}],
 'G': [{'date_time': '2023-01-07 23:24:42:724048',
        'metric_str': 'content_trust.bias',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '0.06276444418594895'},
       {'date_time': '2023-01-07 23:24:42:725222',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '0.27552598467610645'},
       {'date_time': '2023-01-07 23:24:42:726380',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '0.28405255597695667'},
       {'date_time': '2023-01-07 23:24:42:727068',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '-0.4480206823452728'},
       {'date_time': '2023-01-07 23:24:42:727753',
        'metric_str': 'content_trust.deception',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '-0.4570228147942379'},
       {'date_time': '2023-01-07 23:24:42:728456',
        'metric_str': 'content_trust.age',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:42:729279',
        'metric_str': 'content_trust.authority',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:730553',
        'metric_str': 'content_trust.topic',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:731249',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '-1.0'},
       {'date_time': '2023-01-07 23:24:42:734835',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '-0.22675417569991296'},
       {'date_time': '2023-01-07 23:24:42:763146',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '-0.10855742234046291'},
       {'date_time': '2023-01-07 23:24:42:769755',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:771414',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:42:775665',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'F',
        'resource_id': '93b9771a-9afa-4fcc-82c2-5465057097d4',
        'trust_value': '0.5'}],
 'H': [],
 'I': [{'date_time': '2023-01-07 23:24:42:828003',
        'metric_str': 'content_trust.bias',
        'other_agent': 'B',
        'resource_id': 'befcda34-8561-4580-ad99-463510518ef7',
        'trust_value': '0.8634560937314013'},
       {'date_time': '2023-01-07 23:24:42:828479',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'B',
        'resource_id': 'befcda34-8561-4580-ad99-463510518ef7',
        'trust_value': '0.7071814621387973'},
       {'date_time': '2023-01-07 23:24:42:828934',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'B',
        'resource_id': 'befcda34-8561-4580-ad99-463510518ef7',
        'trust_value': '-0.26126071948825325'},
       {'date_time': '2023-01-07 23:24:42:829433',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'B',
        'resource_id': 'befcda34-8561-4580-ad99-463510518ef7',
        'trust_value': '-0.5479615345698774'}],
 'J': [{'date_time': '2023-01-07 23:24:41:789795',
        'metric_str': 'content_trust.bias',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '-0.3942799868599005'},
       {'date_time': '2023-01-07 23:24:41:790591',
        'metric_str': 'content_trust.specificity',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.32510351855394637'},
       {'date_time': '2023-01-07 23:24:41:791258',
        'metric_str': 'content_trust.likelihood',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.9918488885810015'},
       {'date_time': '2023-01-07 23:24:41:791920',
        'metric_str': 'content_trust.incentive',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.9418530174215094'},
       {'date_time': '2023-01-07 23:24:41:792606',
        'metric_str': 'content_trust.deception',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.023216837071337926'},
       {'date_time': '2023-01-07 23:24:41:793268',
        'metric_str': 'content_trust.age',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:41:793917',
        'metric_str': 'content_trust.authority',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '1.0'},
       {'date_time': '2023-01-07 23:24:41:795034',
        'metric_str': 'content_trust.topic',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.5038930308369243'},
       {'date_time': '2023-01-07 23:24:41:795722',
        'metric_str': 'content_trust.provenance',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.19999999999999996'},
       {'date_time': '2023-01-07 23:24:41:800025',
        'metric_str': 'content_trust.direct_experience',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:41:824335',
        'metric_str': 'content_trust.recommendation',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:41:827335',
        'metric_str': 'content_trust.related_resources',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:41:828286',
        'metric_str': 'content_trust.user_expertise',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': 'None'},
       {'date_time': '2023-01-07 23:24:41:886159',
        'metric_str': 'content_trust.popularity',
        'other_agent': 'H',
        'resource_id': 'a3858573-e72e-4bb4-b875-0286518086ef',
        'trust_value': '0.8'}]}


ATLAS_TIMES = {'cleanup_time': 3.8728420734405518,
 'execution_time': 1.1615862846374512,
 'preparation_time': 3.438303232192993}


RAM_USAGES = {'caliban.informatik.tu-chemnitz.de': [36016128,
                                       36016128,
                                       36016128,
                                       36016128,
                                       37126144],
 'debussy.informatik.tu-chemnitz.de': [36274176,
                                       37396480,
                                       37400576,
                                       37400576,
                                       37400576],
 'gosler3.informatik.tu-chemnitz.de': [36225024,
                                       36794368,
                                       36818944,
                                       36818944,
                                       36818944],
 'mahler.informatik.tu-chemnitz.de': [36229120,
                                      36229120,
                                      36421632,
                                      37371904,
                                      37371904],
 'mendelssohn.informatik.tu-chemnitz.de': [36155392,
                                           36155392,
                                           37244928,
                                           37261312,
                                           37261312],
 'minsky.informatik.tu-chemnitz.de': [36036608,
                                      36036608,
                                      36036608,
                                      36474880,
                                      37199872],
 'mozart.informatik.tu-chemnitz.de': [36315136,
                                      36315136,
                                      36966400,
                                      37597184,
                                      37597184],
 'rachmaninov.informatik.tu-chemnitz.de': [36270080,
                                           37367808,
                                           37367808,
                                           37367808,
                                           37367808],
 'schumann.informatik.tu-chemnitz.de': [36171776,
                                        36171776,
                                        36171776,
                                        36765696,
                                        37253120],
 'vsr-dem0.informatik.tu-chemnitz.de': [21553152,
                                        21942272,
                                        21942272,
                                        21942272,
                                        23035904]}

