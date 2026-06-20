# Components

Components for which the kernel would provide support based on models are to be defined in this folder using a standard structure.

```bash
.
└── components
    └── type_name
        └── brand
            ├── model1.json
            ├── model2.json
            └── model3.json
```

## Model definition

Each model file should have the following structure:

```json
{
    "brand": "string",
    "name": "string",
    "key": "string",
    "kernel_added": "", // Version of the kernel adding support
    "kernel_works_confirmed": [], // Kernel versions with confirmed working support, as list of strings which can include ranges via - (e.g. "6.0-7.0") or any ("6.0+"), to be used if kernel_added is not possible to be used
    "kernel_removed": "", // Version of the kernel removing support
}
```

We do not aim to track all models as separate - we should group in a way which makes sense based on the support provided by the kernel.

As an example: for Intel/AMD CPUs, due to the pattern of yearly generations which are generally introduced together to the kernel, we can ignore specific variants and aggregate a whole generation in a single definition.

Optimization and further improvements on the security level are to be ignored for the scope of this project - we aim to track when suppor was added and eventually removed.