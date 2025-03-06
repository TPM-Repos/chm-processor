![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EntryRemoved Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11535.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationTaskList Class](topic11525.md) : EntryRemoved Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an entry is removed from the list. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event EntryRemoved As [SpecificationTaskListEntryEventHandler](topic11823.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SpecificationTaskList](topic11525.md)
    Dim handler As [SpecificationTaskListEntryEventHandler](topic11823.md)
     
    AddHandler instance.EntryRemoved, handler  
  
C#|   
---|---  
      
    
    public event [SpecificationTaskListEntryEventHandler](topic11823.md) EntryRemoved  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [SpecificationTaskListEntryEventArgs](topic11548.md) containing data related to this event. The following **SpecificationTaskListEntryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Entry](topic11558.md)| Gets the entry that is the target of the event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationTaskList Class](topic11525.md)   
[SpecificationTaskList Members](topic11526.md)

©2024 DriveWorks Ltd. All Rights Reserved.
