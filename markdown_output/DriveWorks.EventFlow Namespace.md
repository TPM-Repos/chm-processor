Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.EventFlow Namespace   
See Also [Inheritance Hierarchy](topic6872.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6871.md)  
[DriveWorks.Engine Assembly](topic2156.md) : DriveWorks.EventFlow Namespace  
---  
  
Glossary Item Box

# Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [ConditionOutput](topic6901.md) | Represents the base class for all logical condition outputs within a [IFlowNode](topic6873.md).  
![Class](dotnetimages/Class.gif)| [Connection](topic6909.md) | Represents a connection between one node's input and another node's output.  
![Class](dotnetimages/Class.gif)| [ConnectionEndpoint](topic6918.md) | Represents the common base class for inputs and outputs.  
![Class](dotnetimages/Class.gif)| [ConnectionEventArgs](topic6930.md) | Provides data for events relating to [Connection](topic6909.md).  
![Class](dotnetimages/Class.gif)| [ExecutableNodeBase](topic6938.md) | Represents a [IFlowNode](topic6873.md) that is executable.  
![Class](dotnetimages/Class.gif)| [ExecutableNodeEventArgs](topic6983.md) | Represents event data for events involving [ExecutableNodeBase](topic6938.md) objects.  
![Class](dotnetimages/Class.gif)| [ExecutableNodeWithStatus](topic6990.md) |   
![Class](dotnetimages/Class.gif)| [FlowBase](topic6999.md) | Provides the base for all flows that allow nodes to be connected.  
![Class](dotnetimages/Class.gif)| [FlowNodeCollection](topic7011.md) | Represents a collection of [ExecutableNodeBase](topic6938.md) objects.  
![Class](dotnetimages/Class.gif)| [FlowPropertyEventArgs](topic7026.md) | Represents event data for events pertaining to [DriveWorks.Specification.FlowProperty](topic10946.md) objects.  
![Class](dotnetimages/Class.gif)| [InputConnectionEndpoint](topic7033.md) | Represents the common base class for all input connection endpoints on nodes.  
![Class](dotnetimages/Class.gif)| [InvalidFlowException](topic7044.md) | The exception thrown when an invalid / corrupt [FlowBase](topic6999.md) is encountered.  
![Class](dotnetimages/Class.gif)| [MacroStartNode](topic7050.md) | Represents the very first task to execute in a [DriveWorks.Specification.SpecificationMacro](topic11429.md).  
![Class](dotnetimages/Class.gif)| [NodeNavigationInput](topic7058.md) | Represents a logical flow input endpoint for a [IFlowNode](topic6873.md).  
![Class](dotnetimages/Class.gif)| [NodeNavigationOutput](topic7067.md) | Represents a logical endpoint on a [IFlowNode](topic6873.md) that allows logical connections to be made between the node this output belongs to and the node a [NodeNavigationInput](topic7058.md) belongs to.  
![Class](dotnetimages/Class.gif)| [NodeOutput](topic7074.md) | Represents a data output of a [IFlowNode](topic6873.md).  
![Class](dotnetimages/Class.gif)| [NodeOutputCollection](topic7087.md) | Represents a collection of [NodeOutput](topic7074.md).  
![Class](dotnetimages/Class.gif)| [NodeOutputEventArgs](topic7113.md) | Provides event data for events pertaining to [NodeOutput](topic7074.md) objects.  
![Class](dotnetimages/Class.gif)| [StartNode](topic7120.md) | Represents the very first node in a [FlowBase](topic6999.md) where execution will begin.  
![Class](dotnetimages/Class.gif)| [SubFlowInputsNode](topic7136.md) | This node represents the inputs to a SubFlow.  
![Class](dotnetimages/Class.gif)| [SubFlowOutputsNode](topic7143.md) | Represents the outputs of a **SubFlow**.  
  
# Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [IFlowNode](topic6873.md) | Represents a common interface for all nodes in a flow.  
![Interface](dotnetimages/Interface.gif)| [INodeEditor](topic6888.md) | Represents a visual editor for a [IFlowNode](topic6873.md).  
![Interface](dotnetimages/Interface.gif)| [INodeEndpointCollection](topic6894.md) | Represents the owner of a [DriveWorks.Specification.FlowProperty](topic10946.md) or [NodeOutput](topic7074.md).  
  
# Enumerations

| Enumeration| Description  
---|---|---  
![Enumeration](dotnetimages/Enumeration.gif)| [NodeExecutionState](topic6900.md) | Represents the state of a [ExecutableNodeBase](topic6938.md).  
  
# See Also

#### Reference

[DriveWorks.Engine Assembly](topic2156.md)


