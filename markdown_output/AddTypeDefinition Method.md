Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddTypeDefinition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : AddTypeDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dialogName_
    The name of the dialog that this definition will represent.

Glossary Item Box

Creates a new [ProjectItemListTypeDef](topic4533.md) instance and adds it to this [ProjectItemListDef](topic4511.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddTypeDefinition( _
       ByVal _dialogName_ As String _
    ) As [ProjectItemListTypeDef](topic4533.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim dialogName As String
    Dim value As [ProjectItemListTypeDef](topic4533.md)
     
    value = instance.AddTypeDefinition(dialogName)  
  
C#|   
---|---  
      
    
    public [ProjectItemListTypeDef](topic4533.md) AddTypeDefinition( 
       string _dialogName_
    )  
  
#### Parameters

 _dialogName_
    The name of the dialog that this definition will represent.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


