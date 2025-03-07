Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ParentProcessID Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IReportProcessItem Interface](topic2285.md) : ParentProcessID Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Unique ID of the parent process 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property ParentProcessID As Nullable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReportProcessItem](topic2285.md)
    Dim value As Nullable(Of Guid)
     
    instance.ParentProcessID = value
     
    value = instance.ParentProcessID  
  
C#|   
---|---  
      
    
    Nullable<Guid> ParentProcessID {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReportProcessItem Interface](topic2285.md)   
[IReportProcessItem Members](topic2286.md)


