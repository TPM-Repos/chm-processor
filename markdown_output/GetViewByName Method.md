![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetViewByName Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewManager Interface](topic564.md) : GetViewByName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_viewName_
    The name of the view to get.

_create_
    True to create the view if it has not been activated at least once, otherwise false to return a null reference (Nothing in Visual Basic) if the view has not been activated at least once.

Glossary Item Box

Gets the named view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetViewByName( _
       ByVal _viewName_ As String, _
       ByVal _create_ As Boolean _
    ) As [IView](topic534.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IViewManager](topic564.md)
    Dim viewName As String
    Dim create As Boolean
    Dim value As [IView](topic534.md)
     
    value = instance.GetViewByName(viewName, create)  
  
C#|   
---|---  
      
    
    [IView](topic534.md) GetViewByName( 
       string _viewName_ ,
       bool _create_
    )  
  
#### Parameters

 _viewName_
    The name of the view to get.
_create_
    True to create the view if it has not been activated at least once, otherwise false to return a null reference (Nothing in Visual Basic) if the view has not been activated at least once.

#### Return Value

The named view, or a null reference (Nothing in Visual Basic) if the view is not registered, or hasn't been activated at least once.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IViewManager Interface](topic564.md)   
[IViewManager Members](topic565.md)


