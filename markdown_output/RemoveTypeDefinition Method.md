       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveTypeDefinition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : RemoveTypeDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_typeDefinition_
    The type definition to remove from the item list.

Glossary Item Box

Removes a type definition from the item list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveTypeDefinition( _
       ByVal _typeDefinition_ As [ProjectItemListTypeDef](topic4533.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim typeDefinition As [ProjectItemListTypeDef](topic4533.md)
     
    instance.RemoveTypeDefinition(typeDefinition)  
  
C#|   
---|---  
      
    
    public void RemoveTypeDefinition( 
       [ProjectItemListTypeDef](topic4533.md) _typeDefinition_
    )  
  
#### Parameters

 _typeDefinition_
    The type definition to remove from the item list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


