![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateReportWriter Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3244.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : CreateReportWriter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The identifier of the component for which to write the report.

_title_
    The title of the report.

_level_
    The maximum entry level to write to the report.

Glossary Item Box

Creates a new report writer which will write a report for the given component. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateReportWriter( _
       ByVal _componentId_ As Guid, _
       ByVal _title_ As String, _
       ByVal _level_ As [ReportingLevel](topic10362.md) _
    ) As [IGroupReportWriter](topic2207.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim title As String
    Dim level As [ReportingLevel](topic10362.md)
    Dim value As [IGroupReportWriter](topic2207.md)
     
    value = instance.CreateReportWriter(componentId, title, level)  
  
C#|   
---|---  
      
    
    public [IGroupReportWriter](topic2207.md) CreateReportWriter( 
       Guid _componentId_ ,
       string _title_ ,
       [ReportingLevel](topic10362.md) _level_
    )  
  
#### Parameters

 _componentId_
    The identifier of the component for which to write the report.
_title_
    The title of the report.
_level_
    The maximum entry level to write to the report.

#### Return Value

A report writer.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
