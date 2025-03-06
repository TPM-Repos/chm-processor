![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActivateView Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewManager Interface](topic564.md) : ActivateView Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_viewName_
    The name of the view to activate.

Glossary Item Box

Sets the currently active view control 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ActivateView( _
       ByVal _viewName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IViewManager](topic564.md)
    Dim viewName As String
    Dim value As Boolean
     
    value = instance.ActivateView(viewName)  
  
C#|   
---|---  
      
    
    bool ActivateView( 
       string _viewName_
    )  
  
#### Parameters

 _viewName_
    The name of the view to activate.

#### Return Value

True if the view was successfully activated, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IViewManager Interface](topic564.md)   
[IViewManager Members](topic565.md)


