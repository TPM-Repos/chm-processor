Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : AddItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_typeDef_
    The type of item to create.

_values_
    The values to set for this item.

Glossary Item Box

Adds a new item to this item list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddItem( _
       ByVal _typeDef_ As [ProjectItemListTypeDef](topic4533.md), _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim typeDef As [ProjectItemListTypeDef](topic4533.md)
    Dim values() As Object
     
    instance.AddItem(typeDef, values)  
  
C#|   
---|---  
      
    
    public void AddItem( 
       [ProjectItemListTypeDef](topic4533.md) _typeDef_ ,
       object[] _values_
    )  
  
#### Parameters

 _typeDef_
    The type of item to create.
_values_
    The values to set for this item.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


