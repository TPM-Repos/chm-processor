![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddGroup Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewCommandBarManager Interface](topic543.md) : AddGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The localized title of the group.

Glossary Item Box

Creates a new group which will contain related command buttons. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AddGroup( _
       ByVal _title_ As String _
    ) As [ICommandBarGroup](topic99.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IViewCommandBarManager](topic543.md)
    Dim title As String
    Dim value As [ICommandBarGroup](topic99.md)
     
    value = instance.AddGroup(title)  
  
C#|   
---|---  
      
    
    [ICommandBarGroup](topic99.md) AddGroup( 
       string _title_
    )  
  
#### Parameters

 _title_
    The localized title of the group.

# ![](dotnetimages/collapse.gif)Remarks

Groups created by this method are implicitly locked to the view to which the command bar manager belongs.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IViewCommandBarManager Interface](topic543.md)   
[IViewCommandBarManager Members](topic544.md)


