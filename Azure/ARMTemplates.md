# Azure Resource Manager (ARM) Templates Info

## Tips

"Resources with the condition element set to false are automatically removed from the dependency order, Set the dependencies as if the resource is always deployed"

## Best Practices

### Setting Location

- Use a parameter to specify the location for resources, and set the default value to `resourceGroup().location`
- Don't specify `allowedValues` the locations you specify might not be available in all clouds

### Allowed Values

- Restrict values that can be passed as a parameter
- Use sparringly

## Links

- [Template Best Practices](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/best-practices)