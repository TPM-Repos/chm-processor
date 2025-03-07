Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsNameValidCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTable Class](topic4282.md) : IsNameValidCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newName_
    The proposed name of the document.

Glossary Item Box

When overridden in a derived class, checks to see if the specified new name is a valid name for the given type of document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function IsNameValidCore( _
       ByVal _newName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTable](topic4282.md)
    Dim newName As String
    Dim value As Boolean
     
    value = instance.IsNameValidCore(newName)  
  
C#|   
---|---  
      
    
    protected virtual bool IsNameValidCore( 
       string _newName_
    )  
  
#### Parameters

 _newName_
    The proposed name of the document.

#### Return Value

True if the name is valid, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[ProjectDataTable Members](topic4283.md)


