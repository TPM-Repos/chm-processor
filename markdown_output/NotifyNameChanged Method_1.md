Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyNameChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutputCollection Class](topic7087.md) : NotifyNameChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_endpoint_
    

_oldName_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub NotifyNameChanged( _
       ByVal _endpoint_ As [ConnectionEndpoint](topic6918.md), _
       ByVal _oldName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeOutputCollection](topic7087.md)
    Dim endpoint As [ConnectionEndpoint](topic6918.md)
    Dim oldName As String
     
    instance.NotifyNameChanged(endpoint, oldName)  
  
C#|   
---|---  
      
    
    public void NotifyNameChanged( 
       [ConnectionEndpoint](topic6918.md) _endpoint_ ,
       string _oldName_
    )  
  
#### Parameters

 _endpoint_
    
_oldName_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeOutputCollection Class](topic7087.md)   
[NodeOutputCollection Members](topic7088.md)


