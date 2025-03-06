![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SearchedItem Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13209.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [NameSearchProcess Class](topic13195.md) : SearchedItem Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when starting search of a specific item. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SearchedItem As EventHandler(Of SearchEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NameSearchProcess](topic13195.md)
    Dim handler As EventHandler(Of SearchEventArgs)
     
    AddHandler instance.SearchedItem, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SearchEventArgs> SearchedItem  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [SearchEventArgs](topic13263.md) containing data related to this event. The following **SearchEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic13269.md)| The found item from the search.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NameSearchProcess Class](topic13195.md)   
[NameSearchProcess Members](topic13196.md)

©2024 DriveWorks Ltd. All Rights Reserved.
