![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EntryWritten Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [EventProxyReportWriter Class](topic10392.md) : EntryWritten Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an entry is written. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event EntryWritten As [EntryEventHandler](topic10508.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [EventProxyReportWriter](topic10392.md)
    Dim handler As [EntryEventHandler](topic10508.md)
     
    AddHandler instance.EntryWritten, handler  
  
C#|   
---|---  
      
    
    public event [EntryEventHandler](topic10508.md) EntryWritten  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [EntryEventArgs](topic10379.md) containing data related to this event. The following **EntryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[EntryClass](topic10386.md)| Gets the entry class.   
[EntryDescription](topic10387.md)| Gets the entry description.   
[EntryDetail](topic10388.md)| Gets optional extra detail about the entry.   
[EntryLevel](topic10389.md)| Gets the reporting level of the entry.   
[EntryTarget](topic10390.md)| Gets the target of the entry.   
[EntryType](topic10391.md)| Gets the type of entry.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[EventProxyReportWriter Class](topic10392.md)   
[EventProxyReportWriter Members](topic10393.md)


