![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetSelection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1140.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : SetSelection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newSelection_
    The new selection.

_clone_
    Dictates whether the array is cloned, if you make any changes to the array after calling this method, you should opt to clone the array, otherwise it is safe to pass false for this parameter's argument.

Glossary Item Box

Sets the current selection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub SetSelection( _
       ByVal _newSelection_() As Object, _
       ByVal _clone_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim newSelection() As Object
    Dim clone As Boolean
     
    instance.SetSelection(newSelection, clone)  
  
C#|   
---|---  
      
    
    protected void SetSelection( 
       object[] _newSelection_ ,
       bool _clone_
    )  
  
#### Parameters

 _newSelection_
    The new selection.
_clone_
    Dictates whether the array is cloned, if you make any changes to the array after calling this method, you should opt to clone the array, otherwise it is safe to pass false for this parameter's argument.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
