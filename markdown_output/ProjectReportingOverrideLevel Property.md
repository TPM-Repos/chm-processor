Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectReportingOverrideLevel Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : ProjectReportingOverrideLevel Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the Group's [DriveWorks.Reporting.ReportingLevel](topic10362.md) which will actively override the [DriveWorks.Reporting.ReportingLevel](topic10362.md) set on individual Projects within the Group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ProjectReportingOverrideLevel As [ReportingLevel](topic10362.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim value As [ReportingLevel](topic10362.md)
     
    instance.ProjectReportingOverrideLevel = value
     
    value = instance.ProjectReportingOverrideLevel  
  
C#|   
---|---  
      
    
    public [ReportingLevel](topic10362.md) ProjectReportingOverrideLevel {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


