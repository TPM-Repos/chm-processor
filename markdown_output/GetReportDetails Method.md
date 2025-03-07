Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetReportDetails Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReports Class](topic3272.md) : GetReportDetails Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The identifier of the report to get the details of.

Glossary Item Box

Gets matching report details based on the specified report identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetReportDetails( _
       ByVal _reportId_ As Guid _
    ) As [ReportDetails](topic5221.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReports Class](topic3272.md)   
[GroupReports Members](topic3273.md)


