![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RenameFinished Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10298.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : RenameFinished Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the renaming phase of the rename process has finished. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event RenameFinished As EventHandler(Of RenameFinishedEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of RenameFinishedEventArgs)
     
    AddHandler instance.RenameFinished, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RenameFinishedEventArgs> RenameFinished  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [RenameFinishedEventArgs](topic10277.md) containing data related to this event. The following **RenameFinishedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[TotalReplacements](topic10283.md)| Gets the total number of references that were replaced.   
[TotalRules](topic10284.md)| Gets the total number of actual rules that were scanned.   
[TotalScans](topic10285.md)| Gets the total number of potential rules that were scanned.   
[TotalUnparsedRules](topic10286.md)| Gets the total number of rules which couldn't be scanned because they were unparseable.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)

©2024 DriveWorks Ltd. All Rights Reserved.
