Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyNameChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [INodeEndpointCollection Interface](topic6894.md) : NotifyNameChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_endpoint_
    The end point whose name has changed.

_oldName_
    The old name of the end point before the name was changed.

Glossary Item Box

Called by [DriveWorks.Specification.FlowProperty](topic10946.md)s and [NodeOutput](topic7074.md)s to let the owner know its name has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyNameChanged( _
       ByVal _endpoint_ As [ConnectionEndpoint](topic6918.md), _
       ByVal _oldName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [INodeEndpointCollection](topic6894.md)
    Dim endpoint As [ConnectionEndpoint](topic6918.md)
    Dim oldName As String
     
    instance.NotifyNameChanged(endpoint, oldName)  
  
C#|   
---|---  
      
    
    void NotifyNameChanged( 
       [ConnectionEndpoint](topic6918.md) _endpoint_ ,
       string _oldName_
    )  
  
#### Parameters

 _endpoint_
    The end point whose name has changed.
_oldName_
    The old name of the end point before the name was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[INodeEndpointCollection Interface](topic6894.md)   
[INodeEndpointCollection Members](topic6895.md)


