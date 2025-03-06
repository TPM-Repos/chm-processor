![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IViewCommandBarManager Interface   
[Members](topic544.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : IViewCommandBarManager Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for an object which manages an application's command bar for a single view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface IViewCommandBarManager 
       Inherits [IUpdateable](topic519.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IViewCommandBarManager](topic543.md)  
  
C#|   
---|---  
      
    
    public interface IViewCommandBarManager : [IUpdateable](topic519.md)    
  
# ![](dotnetimages/collapse.gif)Remarks

A view has the ability to add any number of command button groups to the command bar while the view is visible by using the [ViewControl.CommandBarManager](topic1142.md) property, which returns an object which implements [IViewCommandBarManager](topic543.md).

Unlike the application-level [ICommandBarManager](topic109.md) interface, command button groups created by implementations of the the view-level [IViewCommandBarManager](topic543.md) interface are implicitly locked to the view that created them.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IViewCommandBarManager Members](topic544.md)   
[DriveWorks.Applications Namespace](topic16.md)


