![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AfterInvoke Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic93.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommand Interface](topic77.md) : AfterInvoke Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised after the command has been invoked. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event AfterInvoke As [CommandInvokeEventHandler](topic1267.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommand](topic77.md)
    Dim handler As [CommandInvokeEventHandler](topic1267.md)
     
    AddHandler instance.AfterInvoke, handler  
  
C#|   
---|---  
      
    
    event [CommandInvokeEventHandler](topic1267.md) AfterInvoke  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [CommandInvokeEventArgs](topic691.md) containing data related to this event. The following **CommandInvokeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[CommandContext](topic698.md)| Gets the context passed to the command's [ICommand.Invoke](topic84.md) method.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommand Interface](topic77.md)   
[ICommand Members](topic78.md)

©2024 DriveWorks Ltd. All Rights Reserved.
