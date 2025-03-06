![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EditItem Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4520.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : EditItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemIndex_
    The row index of the item to edit.

_itemType_
    

_values_
    New values for the item.

Glossary Item Box

Edits an existing item in this item list. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub EditItem( _
       ByVal _itemIndex_ As Integer, _
       ByVal _itemType_ As [ProjectItemListTypeDef](topic4533.md), _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim itemIndex As Integer
    Dim itemType As [ProjectItemListTypeDef](topic4533.md)
    Dim values() As Object
     
    instance.EditItem(itemIndex, itemType, values)  
  
C#|   
---|---  
      
    
    public void EditItem( 
       int _itemIndex_ ,
       [ProjectItemListTypeDef](topic4533.md) _itemType_ ,
       object[] _values_
    )  
  
#### Parameters

 _itemIndex_
    The row index of the item to edit.
_itemType_
    
_values_
    New values for the item.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)

©2024 DriveWorks Ltd. All Rights Reserved.
