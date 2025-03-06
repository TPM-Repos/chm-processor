TryGetNode Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowBase Class](topic6999.md) : TryGetNode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the [IFlowNode](topic6873.md) to retrieve.

_node_
    The node if found, or a null reference (Nothing in Visual Basic) if a node with that name could not be found.

Glossary Item Box

Attempt to retrieve a [IFlowNode](topic6873.md) from this flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Function TryGetNode( _
       ByVal _name_ As String, _
       ByRef _node_ As [IFlowNode](topic6873.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowBase](topic6999.md)
    Dim name As String
    Dim node As [IFlowNode](topic6873.md)
    Dim value As Boolean
     
    value = instance.TryGetNode(name, node)  
  
C#|   
---|---  
      
    
    public virtual bool TryGetNode( 
       string _name_ ,
       ref [IFlowNode](topic6873.md) _node_
    )  
  
#### Parameters

 _name_
    The name of the [IFlowNode](topic6873.md) to retrieve.
_node_
    The node if found, or a null reference (Nothing in Visual Basic) if a node with that name could not be found.

#### Return Value

True if a node was found, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowBase Class](topic6999.md)   
[FlowBase Members](topic7000.md)


