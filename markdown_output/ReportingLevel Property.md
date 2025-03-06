       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReportingLevel Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11372.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationEnvironment Class](topic11355.md) : ReportingLevel Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the reporting level to use for specification reporting. Setting this value will automatically change the [OverrideProjectReportingLevel](topic11369.md) to true. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ReportingLevel As [ReportingLevel](topic10362.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationEnvironment](topic11355.md)
    Dim value As [ReportingLevel](topic10362.md)
     
    instance.ReportingLevel = value
     
    value = instance.ReportingLevel  
  
C#|   
---|---  
      
    
    public [ReportingLevel](topic10362.md) ReportingLevel {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[SpecificationEnvironment Members](topic11356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
