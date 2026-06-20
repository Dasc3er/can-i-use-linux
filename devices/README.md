# Devices & Features

This folder contains the device information, divided by brand.
Each device should have a folder with name matching the general device series.

Below is an example:
```bash
.
└── device
    └── fake_brand
        ├── fake_series
        │   ├── fake_model1.json
        │   ├── fake_model1.png
        │   ├── fake_model2.json
        │   ├── fake_model2.jpg
        │   └── fake_model3.json
        └── fake_series2
            ├── fake_model1.json
            ├── fake_model1.jpg
            ├── fake_model2.json
            └── fake_model3.json
```


The file `features.json` provides the generally known groups of features with some basic information.
More features can be added for specific devices, and more features can be added as needed to the generic features.

Please note that for the scope of this project we consider general storage and memory requirements for the kernel as satisfied, as it would be difficult for a device in the scope to produce a non-compatible component.

## Device definition

Each device should have a JSON definition following the standard below, and optionally an image.

```json
{
    "brand": "string",
    "name": "string",
    "image": "local_file.jpg",
    "model": ["string"], // All related model codes for the device and extremely similar variants
    "not_working": true, // Optional to set not-working status
    "experimental": true, // Optional to set experimental status
    "features": [
        // Only features of the device should be added
        // The additional_fields should be added as needed
        {
            "key": "key_from_features",
        },
        {
            "key": "cpu", // Required fields for CPU below
            "brand": "intel",
            "model": "i-13gen",
        },
        ...,
    ],
    "extra_features": [ // Optional
        // Non-standard features may be added separately without key providing name and description and any additional fields
        {
            "name": "",
            "description": "", //
            "status": "working"|"not_working"|"unknown",
            "statusReference": "reference to justify the status",
            // Any additional fields which could make sense
        },
    ],
    "notes": "" // Optional, to be used for known OS which provide support for specific devices in advance like Ashai Linux for Mac
}
```
