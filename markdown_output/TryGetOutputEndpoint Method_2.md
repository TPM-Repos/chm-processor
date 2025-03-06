TryGetOutputEndpoint Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [IFlowNode Interface](topic6873.md) : TryGetOutputEndpoint Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the end point to find.

_isNavigation_
    True if the requested end point is expected to be a navigation end point.

_endpoint_
    The end point (if found), otherwise a null reference.

Glossary Item Box

Attempts to retrieve the output end point with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryGetOutputEndpoint( _
       ByVal _name_ As String, _
       ByVal _isNavigation_ As Boolean, _
       ByRef _endpoint_ As [NodeOutput](topic7074.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IFlowNode](topic6873.md)
    Dim name As String
    Dim isNavigation As Boolean
    Dim endpoint As [NodeOutput](topic7074.md)
    Dim value As Boolean
     
    value = instance.TryGetOutputEndpoint(name, isNavigation, endpoint)  
  
C#|   
---|---  
      
    
    bool TryGetOutputEndpoint( 
       string _name_ ,
       bool _isNavigation_ ,
       ref [NodeOutput](topic7074.md) _endpoint_
    )  
  
#### Parameters

 _name_
    The name of the end point to find.
_isNavigation_
    True if the requested end point is expected to be a navigation end point.
_endpoint_
    The end point (if found), otherwise a null reference.

#### Return Value

True if the end point was found, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IFlowNode Interface](topic6873.md)   
[IFlowNode Members](topic6874.md)


