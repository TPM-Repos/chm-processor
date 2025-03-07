Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseNameChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : RaiseNameChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldName_
    The name before it was changed.

_newName_
    The new name.

Glossary Item Box

Raises the [NameChanged](topic6979.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseNameChanged( _
       ByVal _oldName_ As String, _
       ByVal _newName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim oldName As String
    Dim newName As String
     
    instance.RaiseNameChanged(oldName, newName)  
  
C#|   
---|---  
      
    
    protected void RaiseNameChanged( 
       string _oldName_ ,
       string _newName_
    )  
  
#### Parameters

 _oldName_
    The name before it was changed.
_newName_
    The new name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


