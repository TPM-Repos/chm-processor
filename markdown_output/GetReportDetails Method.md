![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetReportDetails Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3280.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReports Class](topic3272.md) : GetReportDetails Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The identifier of the report to get the details of.

Glossary Item Box

Gets matching report details based on the specified report identifier. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetReportDetails( _
       ByVal _reportId_ As Guid _
    ) As [ReportDetails](topic5221.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReports](topic3272.md)
    Dim reportId As Guid
    Dim value As [ReportDetails](topic5221.md)
     
    value = instance.GetReportDetails(reportId)  
  
C#|   
---|---  
      
    
    public [ReportDetails](topic5221.md) GetReportDetails( 
       Guid _reportId_
    )  
  
#### Parameters

 _reportId_
    The identifier of the report to get the details of.

#### Return Value

The matching details or null if nothing is found.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReports Class](topic3272.md)   
[GroupReports Members](topic3273.md)

©2024 DriveWorks Ltd. All Rights Reserved.
