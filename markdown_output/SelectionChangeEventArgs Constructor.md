![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SelectionChangeEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic932.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SelectionChangeEventArgs Class](topic926.md) : SelectionChangeEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldSelectedItems_
    The selection before the change took place.

_newSelectedItems_
    The new selection.

Glossary Item Box

Initializes a new instance of the [SelectionChangeEventArgs](topic926.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _oldSelectedItems_() As Object, _
       ByVal _newSelectedItems_() As Object _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim oldSelectedItems() As Object
    Dim newSelectedItems() As Object
     
    Dim instance As New [SelectionChangeEventArgs](topic926.md)(oldSelectedItems, newSelectedItems)  
  
C#|   
---|---  
      
    
    public SelectionChangeEventArgs( 
       object[] _oldSelectedItems_ ,
       object[] _newSelectedItems_
    )  
  
#### Parameters

 _oldSelectedItems_
    The selection before the change took place.
_newSelectedItems_
    The new selection.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SelectionChangeEventArgs Class](topic926.md)   
[SelectionChangeEventArgs Members](topic927.md)

©2024 DriveWorks Ltd. All Rights Reserved.
