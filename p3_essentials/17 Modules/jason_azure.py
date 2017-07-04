__author__ = 'rafael'

import json

# 1. Decode JSON (from text to dict)
the_dict = json.loads('''{
    "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
    "contentVersion": "",
    "parameters": {
        "<parameter-name>" : {
            "type" : "<type-of-parameter-value>",
            "defaultValue": "<default-value-of-parameter>",
            "allowedValues": [ "<array-of-allowed-values>" ],
            "minValue": 10,
            "maxValue": 20,
            "minLength": 1,
            "maxLength": 2,
            "metadata": {
                "description": "<description-of-the parameter>"
            }
        }
    },
    "variables": {
        "<variable-name>": "myname"
    },
    "resources": [
      {
          "apiVersion": "<api-version-of-resource>",
          "type": "<resource-provider-namespace/resource-type-name>",
          "name": "<name-of-the-resource>",
          "location": "<location-of-resource>",
          "tags": "<name-value-pairs-for-resource-tagging>",
          "comments": "<your-reference-notes>",
          "dependsOn": [
              "<array-of-related-resource-names>"
          ],
          "properties": "<settings-for-the-resource>",
          "copy": {
              "name": "<name-of-copy-loop>",
              "count": "<number-of-iterations>"
          },
          "resources": [
              "<array-of-child-resources>"
          ]
      }
    ],
    "outputs": {
        "<outputName>" : {
            "type" : "<type-of-output-value>",
            "value": "<output-value-expression>"
        }
    }
}''')


# 2. Create variables for each value of the five major keys ($schema,
# contentVersion, parameters, variables, resources, and outputs)
# At this point all your variables are Python data types strings, list, and dictionary objects.
schema = 'http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#'
content_version = ''
parameters = {
         '<parameter-name>': {
             'minValue': 10,
             'minLength': 1,
             'metadata': {
                 'description': '<description-of-the parameter>'},
             'allowedValues': ['<array-of-allowed-values>'],
             'maxLength': 2,
             'type': '<type-of-parameter-value>',
             'defaultValue': '<default-value-of-parameter>',
             'maxValue': 20}}

variables = {
         '<variable-name>': 'myname'}

resources = [
         {
             'name': '<name-of-the-resource>',
             'location': '<location-of-resource>',
             'resources': [
                 '<array-of-child-resources>'],
             'apiVersion': '<api-version-of-resource>',
             'properties': '<settings-for-the-resource>',
             'tags': '<name-value-pairs-for-resource-tagging>',
             'dependsOn': [
                 '<array-of-related-resource-names>'],
             'comments': '<your-reference-notes>',
             'type': '<resource-provider-namespace/resource-type-name>',
             'copy': {
                 'name': '<name-of-copy-loop>',
                 'count': '<number-of-iterations>'
             }
         }
     ]

outputs = {
         '<outputName>': {
             'type': '<type-of-output-value>',
             'value': '<output-value-expression>'
         }
     }
print(parameters['<parameter-name>']['minValue'])
main_keys = {'$schema': schema,
     'contentVersion': content_version,
     'parameters': parameters,
     'variables': variables,
     'resources': resources,
     'outputs': outputs
     }

# Encoding JSON (str)
the_json = json.dumps(main_keys, sort_keys=True, indent=4)
print(the_json)

