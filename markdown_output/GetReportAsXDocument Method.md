Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetReportAsXDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportReader Class](topic10462.md) : GetReportAsXDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetReportAsXDocument( _
       ByVal _reportId_ As Guid _
    ) As XDocument  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReportReader](topic10462.md)
    Dim reportId As Guid
    Dim value As XDocument
     
    value = instance.GetReportAsXDocument(reportId)  
  
C#|   
---|---  
      
    
    public XDocument GetReportAsXDocument( 
       Guid _reportId_
    )  
  
#### Parameters

 _reportId_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportReader Class](topic10462.md)   
[ReportReader Members](topic10463.md)


