![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsUserInteractionDisabled Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic333.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IInteraction Interface](topic321.md) : IsUserInteractionDisabled Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the application is allowed to show modal UI elements. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property IsUserInteractionDisabled As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IInteraction](topic321.md)
    Dim value As Boolean
     
    instance.IsUserInteractionDisabled = value
     
    value = instance.IsUserInteractionDisabled  
  
C#|   
---|---  
      
    
    bool IsUserInteractionDisabled {get; set;}  
  
# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The application does not support enabling/disabling interaction.  
System.InvalidOperationException| Thrown when the property is set to true, but the application is not interactive (see [IsInteractive](topic332.md) for more information).  
  
# ![](dotnetimages/collapse.gif)Remarks

This property is used to suppress user interactive behaviour in an application which is capable of user interaction. This property can only be changed if the value if [IsInteractive](topic332.md) is true because, when [IsInteractive](topic332.md) is false, the application can never be made interactive.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IInteraction Interface](topic321.md)   
[IInteraction Members](topic322.md)

©2024 DriveWorks Ltd. All Rights Reserved.
