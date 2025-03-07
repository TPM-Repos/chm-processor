Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : GetItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemIndex_
    The index of the item to retrieve.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetItem( _
       ByVal _itemIndex_ As Integer _
    ) As [ProjectListItemData](topic4555.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim itemIndex As Integer
    Dim value As [ProjectListItemData](topic4555.md)
     
    value = instance.GetItem(itemIndex)  
  
C#|   
---|---  
      
    
    public [ProjectListItemData](topic4555.md) GetItem( 
       int _itemIndex_
    )  
  
#### Parameters

 _itemIndex_
    The index of the item to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


