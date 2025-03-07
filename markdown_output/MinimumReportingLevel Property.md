Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MinimumReportingLevel Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationSettings Class](topic15238.md) : MinimumReportingLevel Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets minimum reporting level that will be used during generation. Anything below this level will not be stored in the group report. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property MinimumReportingLevel As [ReportingLevel](topic10362.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationSettings](topic15238.md)
    Dim value As [ReportingLevel](topic10362.md)
     
    instance.MinimumReportingLevel = value
     
    value = instance.MinimumReportingLevel  
  
C#|   
---|---  
      
    
    public [ReportingLevel](topic10362.md) MinimumReportingLevel {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[GenerationSettings Members](topic15239.md)


