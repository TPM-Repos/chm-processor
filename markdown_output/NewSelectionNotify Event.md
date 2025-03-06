![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NewSelectionNotify Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13439.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : NewSelectionNotify Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Post-notifies the user program when the selection list has changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event NewSelectionNotify As EventHandler(Of NewSelectionNotifyEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim handler As EventHandler(Of NewSelectionNotifyEventArgs)
     
    AddHandler instance.NewSelectionNotify, handler  
  
C#|   
---|---  
      
    
    event EventHandler<NewSelectionNotifyEventArgs> NewSelectionNotify  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [NewSelectionNotifyEventArgs](topic13867.md) containing data related to this event. The following **NewSelectionNotifyEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[IsDrawing](topic13874.md)| Gets whether a drawing is selection.   
[Success](topic13916.md)| Gets/sets the result of the event (default is True). (Inherited from [DriveWorks.SolidWorks.ResultEventArgs](topic13909.md))  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)

©2024 DriveWorks Ltd. All Rights Reserved.
