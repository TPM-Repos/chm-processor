![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Added Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6491.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskCollection Class](topic6466.md) : Added Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised when a task has been added to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Added As EventHandler(Of ComponentTaskEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskCollection](topic6466.md)
    Dim handler As EventHandler(Of ComponentTaskEventArgs)
     
    AddHandler instance.Added, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ComponentTaskEventArgs> Added  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ComponentTaskEventArgs](topic6596.md) containing data related to this event. The following **ComponentTaskEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Task](topic6602.md)| Gets the task associated with this event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskCollection Class](topic6466.md)   
[ComponentTaskCollection Members](topic6467.md)

©2024 DriveWorks Ltd. All Rights Reserved.
