![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InsertControlViewAfter(String,String,String,String,ImageSource,StateFilter,Type) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewRegistrationService Interface](topic578.md) > [InsertControlViewAfter Method](topic584.md) : InsertControlViewAfter(String,String,String,String,ImageSource,StateFilter,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_afterViewName_
    The name of the view after which to insert the view, or a null reference (Nothing in Visual Basic) to place the view at the end of the views at the current level.

_name_
    The culture-invariant name of the view.

_title_
    The localized title of the view.

_parent_
    The culture-invariant name of the parent view (see remarks).

_imageSource_
    The source of the image shown in the view manager UI.

_stateFilter_
    A filter which describes which application states the view is included in and/or excluded from.

_viewControlType_
    The CLR type of a WinForms control or WPF UI element that provides the UI for the view.

Glossary Item Box

Inserts a new view after an existing view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub InsertControlViewAfter( _
       ByVal _afterViewName_ As String, _
       ByVal _name_ As String, _
       ByVal _title_ As String, _
       ByVal _parent_ As String, _
       ByVal _imageSource_ As ImageSource, _
       ByVal _stateFilter_ As [StateFilter](topic1077.md), _
       ByVal _viewControlType_ As Type _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IViewRegistrationService](topic578.md)
    Dim afterViewName As String
    Dim name As String
    Dim title As String
    Dim parent As String
    Dim imageSource As ImageSource
    Dim stateFilter As [StateFilter](topic1077.md)
    Dim viewControlType As Type
     
    instance.InsertControlViewAfter(afterViewName, name, title, parent, imageSource, stateFilter, viewControlType)  
  
C#|   
---|---  
      
    
    void InsertControlViewAfter( 
       string _afterViewName_ ,
       string _name_ ,
       string _title_ ,
       string _parent_ ,
       ImageSource _imageSource_ ,
       [StateFilter](topic1077.md) _stateFilter_ ,
       Type _viewControlType_
    )  
  
#### Parameters

 _afterViewName_
    The name of the view after which to insert the view, or a null reference (Nothing in Visual Basic) to place the view at the end of the views at the current level.
_name_
    The culture-invariant name of the view.
_title_
    The localized title of the view.
_parent_
    The culture-invariant name of the parent view (see remarks).
_imageSource_
    The source of the image shown in the view manager UI.
_stateFilter_
    A filter which describes which application states the view is included in and/or excluded from.
_viewControlType_
    The CLR type of a WinForms control or WPF UI element that provides the UI for the view.

# ![](dotnetimages/collapse.gif)Remarks

Views are organized into two levels, a parent view generally categorizes and describes its children (this view is usually an HTML view), and the children provide access to capabilities related to the parent (these are usually control views).

Views may not be nested deeper than two levels.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IViewRegistrationService Interface](topic578.md)   
[IViewRegistrationService Members](topic579.md)   
[Overload List](topic584.md)


