       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetInputEndpoint Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : TryGetInputEndpoint Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the input to find.

_isNavigation_
    True if the requested input is expected to be a navigation end point.

_endpoint_
    The end point (if found), otherwise a null reference.

Glossary Item Box

Attempts to find an input with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetInputEndpoint( _
       ByVal _name_ As String, _
       ByVal _isNavigation_ As Boolean, _
       ByRef _endpoint_ As [InputConnectionEndpoint](topic7033.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim name As String
    Dim isNavigation As Boolean
    Dim endpoint As [InputConnectionEndpoint](topic7033.md)
    Dim value As Boolean
     
    value = instance.TryGetInputEndpoint(name, isNavigation, endpoint)  
  
C#|   
---|---  
      
    
    public bool TryGetInputEndpoint( 
       string _name_ ,
       bool _isNavigation_ ,
       ref [InputConnectionEndpoint](topic7033.md) _endpoint_
    )  
  
#### Parameters

 _name_
    The name of the input to find.
_isNavigation_
    True if the requested input is expected to be a navigation end point.
_endpoint_
    The end point (if found), otherwise a null reference.

#### Return Value

True if the end point was found, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


