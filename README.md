# Scikit Learn

|           |                                                                                 |
| --------- | ------------------------------------------------------------------------------- |
| Name      | Scikit-Learn                                                                    |
| Version   | v1.0.0                                                                          |
| DockerHub | [weevenetwork/scikit-learn](https://hub.docker.com/r/weevenetwork/scikit-learn) |
| Authors   | Jakub Grzelak                                                                   |

- [Scikit Learn](#scikit-learn)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Use your pre-trained scikit-learn model with weeve modules. The model should be available to the module via a downloadable URL or it should be stored in the edge device local filesystem. The module will take input data and the compose a numpy array with data in the order assigned to the Ordered Labels environment variable. Later, the module will input that array into the model.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name               | Environment Variables | type   | Description                                                                                                                                                                                       |
| ------------------ | --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model Download URL | MODEL_DOWNLOAD_URL    | string | If model is stored online, then provide a download URL to parse the model. Leave empty field to search for the model in the local filesystem (see Model Filepath configuration field).                                                     |
| Model Filepath     | MODEL_FILEPATH        | string | If model is stored in the local filesystem of the edge device or node (above field for the URL was left empty), then provide a path to the model file. |
| Ordered Labels     | ORDERED_LABELS        | string | Input data labels in the order of feeding into the model. Later a numpy array will be created to feed that data into the model in the given order.                                                |
| Output Label       | OUTPUT_LABEL          | string | The output label at which data is dispatched.                                                                                                                                                     |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoints for the next module        |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
scikit-learn
```

## Input

Input to this module is:

-   JSON body single object, example:

```json
{
    "temperature": 12,
    "volume": 1.3,
    "pressure": 0.32
}
```

-   array of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "volume": 1.3,
        "pressure": 0.32
    },
    {
        "temperature": 13,
        "volume": 2.1,
        "pressure": 0.34
    }
]
```

## Output

Output of this module is

-   JSON body single object, example:

```json
{
    "prediction": 14.323
}
```

-   array of JSON body objects, example:

```json
[
    {
        "prediction": 14.323
    },
    {
        "prediction": 13.45
    }
]
```
