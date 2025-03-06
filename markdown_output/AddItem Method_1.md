![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddItem Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4517.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddItem( _
       ByVal _typeDef_ As [ProjectItemListTypeDef](topic4533.md), _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)

©2024 DriveWorks Ltd. All Rights Reserved.
