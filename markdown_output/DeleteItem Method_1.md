Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : DeleteItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemIndex_
    Index of the row to remove.

Glossary Item Box

Removes a item from the item list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub DeleteItem( _
       ByVal _itemIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim itemIndex As Integer
     
    instance.DeleteItem(itemIndex)  
  
C#|   
---|---  
      
    
    public void DeleteItem( 
       int _itemIndex_
    )  
  
#### Parameters

 _itemIndex_
    Index of the row to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


