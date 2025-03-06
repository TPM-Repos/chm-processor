![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddGroup Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandBarManager Interface](topic109.md) : AddGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The localized title of the group.

_linkedViewName_
    The name of a view to which the group is linked, or a null reference (Nothing in Visual Basic), if the group is always visible.

Glossary Item Box

Creates a new group which will contain related command buttons. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AddGroup( _
       ByVal _title_ As String, _
       ByVal _linkedViewName_ As String _
    ) As [ICommandBarGroup](topic99.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandBarManager](topic109.md)
    Dim title As String
    Dim linkedViewName As String
    Dim value As [ICommandBarGroup](topic99.md)
     
    value = instance.AddGroup(title, linkedViewName)  
  
C#|   
---|---  
      
    
    [ICommandBarGroup](topic99.md) AddGroup( 
       string _title_ ,
       string _linkedViewName_
    )  
  
#### Parameters

 _title_
    The localized title of the group.
_linkedViewName_
    The name of a view to which the group is linked, or a null reference (Nothing in Visual Basic), if the group is always visible.

# ![](dotnetimages/collapse.gif)Remarks

Command bar groups can be linked to views, which means they will only be visible if the linked view is the active view.

If a view wishes to create a command button group, it should use the [ViewControl.CommandBarManager](topic1142.md) property to access a [IViewCommandBarManager](topic543.md) rather than using this interface.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandBarManager Interface](topic109.md)   
[ICommandBarManager Members](topic110.md)


