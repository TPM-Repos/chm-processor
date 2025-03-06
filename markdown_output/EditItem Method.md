![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EditItem Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4029.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : EditItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_itemIndex_
    The row index of the item to edit.

_specificationName_
    The new name of the specification that was edited.

_values_
    New values for the item.

Glossary Item Box

Edits an existing item in this item list. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub EditItem( _
       ByVal _itemIndex_ As Integer, _
       ByVal _specificationName_ As String, _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim itemIndex As Integer
    Dim specificationName As String
    Dim values() As Object
     
    instance.EditItem(itemIndex, specificationName, values)  
  
C#|   
---|---  
      
    
    public void EditItem( 
       int _itemIndex_ ,
       string _specificationName_ ,
       object[] _values_
    )  
  
#### Parameters

 _itemIndex_
    The row index of the item to edit.
_specificationName_
    The new name of the specification that was edited.
_values_
    New values for the item.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)

©2024 DriveWorks Ltd. All Rights Reserved.
