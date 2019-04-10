# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
"""Creates the App Engine."""

d_type = {
    'deployment.file': 'F',
    'deployment.container': 'CT',
    'deployment.zip': 'Z'
}

def GenerateConfig(context):
    """Creates the App Engine with single templates."""
    resources = []
    files_str_value = context.properties['fileinfo'] 

    fileinfo = FillintheFilesObject(files_str_value)
    AppendResourceOb(context, resources, fileinfo)

    return {'resources': resources}

def FillintheFilesObject(strval):
    Object = {}

    files_ary = strval.split('&')

    for content in files_ary:
        content_to_ary = content.split('=')
        file_name = content_to_ary[0]
        file_url_ob = {}
        file_url_ob['source_url'] = content_to_ary[1]
        Object[file_name] = file_url_ob
    
    return Object

def AppendResourceOb(context, resources, fileinfo):
    """Add Json objectd to Resource List."""
    deployment_type = context.properties['deployment_type']
    
    if deployment_type == d_type['deployment.file']:
            resources.append({
                'name': context.properties['version'],
                'type': 'appengine.v1.version',
                'properties': {
                    'deployment': {
                        'files': fileinfo
                    },
                    'servicesId': 'default',
                    'appsId': context.properties['project'],
                    'handlers': [{
                        'script': {
                           'scriptPath': context.properties['scriptpath']
                        },
                        'securityLevel': context.properties['securitylevel'],
                        'urlRegex': context.properties['urlregex']
                    }],
                    'runtime': context.properties['runtime'],
                    'threadsafe': True,
                    'zones': [
                         context.properties['zone']
                    ],
                    'env': context.properties['environment']
                }
            })
    elif deployment_type == d_type['deployment.container']:
            resources.append({
                'name': context.properties['version'],
                'type': 'appengine.v1.version',
                'properties': {
                    'deployment': {
                        'container': {
                            'image': context.properties['path']
                        }
                    },
                    'servicesId': 'default',
                    'appsId': context.properties['project'],
                    'handlers': [{
                        'script': {
                           'scriptPath': context.properties['scriptpath']
                        },
                        'securityLevel': context.properties['securitylevel'],
                        'urlRegex': context.properties['urlregex']
                    }],
                    'runtime': context.properties['runtime'],
                    'threadsafe': True,
                    'zones': [
                         context.properties['zone']
                    ],
                    'env': context.properties['environment']
                }
            })
    elif deployment_type == d_type['deployment.zip']:
            resources.append({
                'name': context.properties['version'],
                'type': 'appengine.v1.version',
                'properties': {
                    'deployment': {
                        'zip': {
                            'source_url': context.properties['path']
                        }
                    },
                    'servicesId': 'default',
                    'appsId': context.properties['project'],
                    'handlers': [{
                        'script': {
                           'scriptPath': context.properties['scriptpath']
                        },
                        'securityLevel': context.properties['securitylevel'],
                        'urlRegex': context.properties['urlregex']
                    }],
                    'runtime': context.properties['runtime'],
                    'threadsafe': True,
                    'zones': [
                         context.properties['zone']
                    ],
                    'env': context.properties['environment']
                }
            })
    else:
        logging.log(50, 'deployment_type error')
        exit()
