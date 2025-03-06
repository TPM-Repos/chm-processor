![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowContextDialog(UIElement) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic122.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButton Interface](topic115.md) > [ShowContextDialog Method](topic120.md) : ShowContextDialog(UIElement) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The WPF control to show in the contextual dialog.

Glossary Item Box

Shows a contextual dialog next to the button that can be used to take input from the user. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub ShowContextDialog( _
       ByVal _control_ As UIElement _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandButton](topic115.md)
    Dim control As UIElement
     
    instance.ShowContextDialog(control)  
  
C#|   
---|---  
      
    
    void ShowContextDialog( 
       UIElement _control_
    )  
  
#### Parameters

 _control_
    The WPF control to show in the contextual dialog.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandButton Interface](topic115.md)   
[ICommandButton Members](topic116.md)   
[Overload List](topic120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
